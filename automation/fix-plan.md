# Fix Plan – Nightly Research Stabilisierung

## Ziel
Den Nightly-Lauf für `yesterdaysnews` so stabilisieren, dass er ohne Kontext-Overflow, ohne kaputte Quellen und mit nachvollziehbarer Fehlerdiagnose durchläuft.

## Prinzipien
- Immer nur **ein** technischer Fix pro Schritt.
- Nach jedem Fix: **Testen** und **Dokumentieren**.
- Erst nach bestandenem Check den nächsten Schritt angehen.
- Bei Rückschritt oder neuem Befund den Plan anpassen.

## Schritt 1 – Kontextdruck reduzieren
**Status:** erledigt

**Änderung:**
- Nightly-Agent auf `lightContext` umgestellt.
- Prompt auf Phasenbetrieb und Batch-Splitting verkürzt.
- Arbeitsanweisung ergänzt, dass bei zu großem Kontext in kleinere Batches aufgeteilt wird.

**Test:**
- JSON-Syntax von `~/.openclaw/cron/jobs.json` geprüft.
- Konfigurationsdiff auf `lightContext` und Phasenhinweis geprüft.
- `python3 scripts/source_lint.py` als Hygiene-Check laufen lassen.

**Dokumentation:**
- `projects/yesterdaysnews/decisions.md`
- `projects/yesterdaysnews/input-log.md`
- `projects/yesterdaysnews/automation/nightly-research-agent.md`

## Schritt 2 – Quellenhygiene härten
**Status:** teilweise erledigt

**Änderung:**
- Problematische oder wenig passende Quellen in vorhandenen Beiträgen identifizieren und ersetzen.
- Linter so angepasst, dass er bei kurzen Titeln weniger falsche Relevanzwarnungen produziert.
- Zwei vorhandene Beiträge wurden auf belastbarere bzw. thematisch deutlichere Quellenbezüge nachgeschärft.
- Weiterhin offene Post-Inhalte mit schwachen Quellen separat nacharbeiten.

**Test:**
- `python3 scripts/source_lint.py`
- betroffene Journal-Posts einzeln prüfen

**Dokumentation:**
- betroffene Journal-Posts
- `projects/yesterdaysnews/decisions.md`

## Schritt 3 – Fehlerdiagnose verbessern
**Status:** erledigt

**Änderung:**
- Pro Lauf präzisere Statusinfos schreiben: Phase, Ursache, Datei oder URL, nächster Schritt.
- Fehlersignale so strukturieren, dass sie im Log sofort grep-bar sind.
- Die Agenten-Anweisung verlangt jetzt feste Diagnosefelder: `PHASE`, `STATUS`, `CAUSE`, `URL`/`FILE`, `NEXT`, optional `JOB`/`COMMIT`.

**Test:**
- Konfigurationscheck auf die Diagnosefelder durchgeführt.
- Prompt und Cron-Job auf die neuen Vorgaben geprüft.

**Dokumentation:**
- `projects/yesterdaysnews/automation/nightly-research-agent.md`
- `projects/yesterdaysnews/decisions.md`
- `projects/yesterdaysnews/input-log.md`

## Schritt 4 – Benachrichtigungen und Job-Aufräumen
**Status:** erledigt

**Änderung:**
- Telegram-Zielkonfiguration für Fehler-/Statusmeldungen geprüft.
- Veraltete oder doppelte Cron-Jobs bereinigt.
- Aktive yesterdaysnews-Configs enthalten keinen `@heartbeat`-Zielpfad mehr.

**Test:**
- Cron-Jobliste geprüft.
- Aktive Configs auf `@heartbeat` durchsucht; nur historische Speicherstände fanden sich noch.

**Dokumentation:**
- `projects/yesterdaysnews/decisions.md`
- `projects/yesterdaysnews/input-log.md`
