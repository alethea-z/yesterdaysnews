# Input Log

| Datum | Input | Auswirkung |
| --- | --- | --- |
| 2026-05-05 | Ziel: relevante und handlungsorientierte Informationen aus der Nachrichtenflut filtern und als kuratierte Übersicht mit Originalquellen und Hintergrundinformationen bereitstellen. Das Relevanzkriterium ist: Das auslösende Ereignis ist mehr als einen Tag her, aber immer noch für die heutigen Nachrichten interessant. | Projektziel, Scope und Relevanzkriterium in `requirements.md` präzisiert. |
| 2026-05-05 | MVP-Workflow: statische Website mit Hugo/GitHub Pages, täglicher Recherche-Job um 03:00 Uhr für 10 Beiträge, Relevanzkriterien als Markdown-Sammlung in separatem Ordner. | Architektur, Workflow, Kriterienstruktur und Automatisierung in `requirements.md`, `criteria/`, `automation/` und Cron-Job abgebildet. |
| 2026-05-05 | GitHub-Repo für `yesterdaysnews` erstellt, initiale Hello-World-Seite gepusht und GitHub Pages aktiviert. | Öffentliche Veröffentlichung ist jetzt unter `https://alethea-z.github.io/yesterdaysnews/` erreichbar. |
| 2026-05-05 | Hugo-Struktur mit `site/`, Journal-Section, Tags und Startseite für nur neue Einträge angelegt. | Der Blog-/Journal-MVP hat jetzt eine saubere Quellstruktur für tägliche Beiträge. |
| 2026-05-05 | Build auf GitHub Actions umgestellt; Pages-Quelle steht jetzt auf `workflow`. | Der HTML-Build passiert nicht mehr lokal, sondern im GitHub-Workflow. |
| 2026-05-05 | Theme `hugo-theme-stack` als Git-Submodule eingebunden und Hugo-Konfiguration darauf ausgerichtet. | Das Projekt nutzt jetzt Stack als visuelles und strukturelles Blog-Theme. |
| 2026-05-05 | GitHub Actions auf `hugo-version: latest` umgestellt, weil Stack eine neuere Hugo-API erwartet. | Der Build läuft jetzt erfolgreich auf GitHub mit kompatibler Hugo-Version. |
| 2026-05-05 | Logo oben links angelegt und Stack-Widgets für Archives, Categories und Tags auf der rechten Seite aktiviert. | Die Seite hat jetzt ein visuelles Markenzeichen und die gewünschte Sidebar-Struktur. |
| 2026-05-05 | Relevanzkriterien in drei Achsen aufgeteilt: zeitliche Relevanz, örtliche Nähe und fachliche Themen. | Die Recherche bekommt eine klarere Bewertungs- und Priorisierungslogik. |
