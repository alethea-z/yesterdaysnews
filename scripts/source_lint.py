#!/usr/bin/env python3
"""Lint yesterdaysnews journal posts for source hygiene.

Checks:
- each post should have a Quellen section with at least one markdown link
- duplicate source URLs across posts are flagged when the posts look topically unrelated
- obvious broken URLs (HTTP 404/410) are flagged; 401/403 on gated sites are noted, not hard-failed
- source labels/URLs that look unrelated to the post topic are warned about, not blocked
"""

from __future__ import annotations

import re
import sys
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
JOURNAL = ROOT / "site" / "content" / "journal"

# Keep only truly generic function words here. Topic words are intentionally
# *not* stopwords because the linter uses short titles and slugs as a relevance hint.
STOPWORDS = {
    "der", "die", "das", "und", "oder", "ein", "eine", "einer", "eines", "einem", "einen",
    "the", "and", "for", "from", "with", "about", "what", "why", "wie", "warum", "wieso",
    "news", "rules", "warns", "warning", "zählt", "zählen", "kommt", "nicht", "mehr", "jetzt", "neu",
    "post",
}

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
TITLE_RE = re.compile(r'^title:\s*["\']?(.*?)["\']?\s*$', re.M)
DATE_RE = re.compile(r'^date:\s*(.*?)\s*$', re.M)


def normalize(text: str) -> set[str]:
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    return {t for t in tokens if len(t) > 2 and t not in STOPWORDS}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


@dataclass
class SourceIssue:
    file: str
    title: str
    kind: str
    detail: str
    url: str | None = None
    text: str | None = None


def parse_post(path: Path):
    raw = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(raw)
    if not m:
        return None
    fm, body = m.groups()
    title_m = TITLE_RE.search(fm)
    date_m = DATE_RE.search(fm)
    title = title_m.group(1).strip() if title_m else path.stem
    date = date_m.group(1).strip() if date_m else ""

    sections = list(SECTION_RE.finditer(body))
    sources_body = body
    if sections:
        source_idx = None
        for i, sec in enumerate(sections):
            if sec.group(1).strip().lower() in {"quellen", "sources"}:
                source_idx = i
                break
        if source_idx is not None:
            start = sections[source_idx].end()
            end = len(body)
            if source_idx + 1 < len(sections):
                end = sections[source_idx + 1].start()
            sources_body = body[start:end]
        else:
            sources_body = ""
    links = LINK_RE.findall(sources_body)
    return {
        "path": path,
        "title": title,
        "date": date,
        "body": body,
        "links": links,
        "topic_tokens": normalize(path.stem),
    }


def check_url(url: str) -> tuple[str, str]:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req, timeout=15) as r:
            code = getattr(r, "status", 200)
            return "ok" if code < 400 else "warn", f"HTTP {code}"
    except HTTPError as e:
        if e.code in (401, 403):
            return "warn", f"HTTP {e.code} (gated or blocked; manual check needed)"
        return "error", f"HTTP {e.code}"
    except URLError as e:
        return "error", f"URL error: {e.reason}"
    except Exception as e:
        return "error", f"{type(e).__name__}: {e}"


def main() -> int:
    issues: list[SourceIssue] = []
    url_to_posts = defaultdict(list)

    for path in sorted(JOURNAL.glob("*.md")):
        if path.name == "_index.md" or "hello-world" in path.stem:
            continue
        post = parse_post(path)
        if not post:
            continue

        if not post["links"]:
            issues.append(SourceIssue(str(path), post["title"], "missing_sources", "No Quellen section or no links found."))
            continue

        for text, url in post["links"]:
            url_to_posts[url].append((path, post["title"], post["topic_tokens"]))

            source_tokens = normalize(text + " " + urlparse(url).netloc + " " + urlparse(url).path)
            overlap = jaccard(post["topic_tokens"], source_tokens)
            if overlap < 0.10:
                issues.append(
                    SourceIssue(
                        str(path),
                        post["title"],
                        "weak_relevance",
                        f"Source looks only loosely related to the post topic (overlap={overlap:.2f}).",
                        url=url,
                        text=text,
                    )
                )

            status, detail = check_url(url)
            if status == "error":
                issues.append(
                    SourceIssue(
                        str(path),
                        post["title"],
                        "broken_url",
                        detail,
                        url=url,
                        text=text,
                    )
                )
            elif status == "warn":
                issues.append(
                    SourceIssue(
                        str(path),
                        post["title"],
                        "gated_url",
                        detail,
                        url=url,
                        text=text,
                    )
                )

    # Duplicate URL across posts
    for url, items in url_to_posts.items():
        if len(items) < 2:
            continue
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                p1, t1, tok1 = items[i]
                p2, t2, tok2 = items[j]
                sim = jaccard(tok1, tok2)
                if sim < 0.20:
                    issues.append(
                        SourceIssue(
                            str(p1),
                            t1,
                            "duplicate_url_cross_topic",
                            f"URL is reused in another post with low topic overlap (similarity={sim:.2f}) to '{t2}'.",
                            url=url,
                        )
                    )

    # Print report
    if not issues:
        print("OK: no source hygiene issues found.")
        return 0

    grouped = defaultdict(list)
    for issue in issues:
        grouped[issue.kind].append(issue)

    print(json.dumps({k: [asdict(i) for i in v] for k, v in grouped.items()}, indent=2, ensure_ascii=False))
    print(f"\nFound {len(issues)} issue(s) across {len(grouped)} category(ies).")

    fatal_kinds = {"broken_url", "duplicate_url_cross_topic", "missing_sources"}
    fatal_count = sum(1 for issue in issues if issue.kind in fatal_kinds)
    return 1 if fatal_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
