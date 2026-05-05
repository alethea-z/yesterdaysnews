# Decisions

| Datum | Entscheidung | Begründung | Quelle |
| --- | --- | --- | --- |
| 2026-05-05 | MVP als statische Website, bevorzugt mit Hugo und Veröffentlichung über GitHub Pages. | Minimaler, gut automatisierbarer Veröffentlichungsweg ohne komplexes Backend. | User-Input |
| 2026-05-05 | Relevanzkriterien werden als separate Markdown-Sammlung im Projektordner gepflegt. | Kriterien sollen einfach änderbar und erweiterbar bleiben. | User-Input |
| 2026-05-05 | Täglicher Recherche-Job um 03:00 Uhr ist angelegt und soll 10 relevante Beiträge vorbereiten. | Der Workflow wird dadurch planbar und wiederholbar. | OpenClaw Cron Job `yesterdaysnews daily research` |
| 2026-05-05 | GitHub-Repo `alethea-z/yesterdaysnews` erstellt und GitHub Pages als Veröffentlichungsziel aktiviert. | Der MVP kann jetzt tatsächlich öffentlich ausgeliefert werden. | GitHub Repo + Pages API |
| 2026-05-05 | Hugo-Quellstruktur liegt getrennt unter `site/`, mit `journal/` als Archiv und Tags für thematische Strukturierung. | Saubere Trennung von Quelle, Journal und künftiger Build-Ausgabe. | User-Input + lokale Projektstruktur |
| 2026-05-05 | Der eigentliche Hugo-Build läuft jetzt auf GitHub Actions; GitHub Pages wird über den Workflow veröffentlicht. | Kein lokaler Build im Repo nötig, klarer CI/CD-Pfad. | GitHub Actions Workflow `/.github/workflows/hugo-pages.yml` |
| 2026-05-05 | `hugo-theme-stack` ist das verwendete Theme und wird als Git-Submodule eingebunden. | Der MVP erhält direkt ein passendes Blog-Theme mit Tags und Journal-Charakter. | Git Submodule + Hugo-Konfiguration |
| 2026-05-05 | Der GitHub-Actions-Build nutzt die aktuelle Hugo-Version (`latest`). | Das Theme benötigt eine neuere Hugo-API als die zuvor gepinnten Versionen. | GitHub Actions Workflow `/.github/workflows/hugo-pages.yml` |
| 2026-05-05 | Das Projekt nutzt ein 150x150-Logo links oben sowie Standard-Widgets für Archives, Categories und Tags rechts. | Gewünschte Blog-Optik und schnelle thematische Navigation sind damit direkt vorhanden. | Hugo-Konfiguration + Theme-Widgets |
| 2026-05-05 | Relevanz wird künftig entlang der drei Achsen Zeit, Ort/Tragweite und Fachthema geprüft. | Dadurch wird die Recherche breiter, robuster und für Leipzig stärker fokussiert. | User-Input |
