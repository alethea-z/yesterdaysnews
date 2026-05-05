# Requirements

## Projektziel
- Relevante und handlungsorientierte Informationen aus der Nachrichtenflut filtern und als kuratierte Übersicht bereitstellen.
- Bewusst aus der hektischen, auf Aufmerksamkeit getrimmten Nachrichtenblase ausbrechen.
- Als MVP zunächst eine statische Website im Blog-/Journal-Stil veröffentlichen.

## Scope
- Kuratierte Nachrichtenübersicht mit Verweisen auf Originalquellen.
- Ergänzende Hintergrundinformationen, damit Meldungen besser eingeordnet werden können.
- Auswahl nach Relevanz statt nach Lautstärke, Tempo oder Klickanreiz.
- Veröffentlichung als statische Website, bevorzugt über GitHub Pages.
- Generierung der Website mit einem statischen Website-Generator, z. B. Hugo.
- Blog-/Journal-Struktur mit Tags, damit Themen auffindbar bleiben.
- Neue tägliche Einträge erscheinen zuerst auf der Startseite; ältere Inhalte bleiben im Journal archiviert.
- Relevanzkriterien als eigene Markdown-Sammlung in einem separaten Projektordner.
- Die Kriterien umfassen zeitliche Relevanz, örtliche Nähe und fachliche Themen.

## Workflow
0. Relevanzkriterien festlegen und im Projektordner pflegen.
1. Tägliche Recherche passender Inhalte.
2. Inhalte als neue Journal-Einträge für die Website aufbereiten.
3. Publizieren über die statische Website.

## Anforderungen
- Das wichtigste Relevanzkriterium ist: Das auslösende Ereignis ist älter als einen Tag, aber immer noch für die heutigen Nachrichten interessant.
- Nachrichten sollen nicht nur chronologisch gesammelt, sondern thematisch und inhaltlich verdichtet werden.
- Jede relevante Meldung soll einen Verweis auf die Originalquelle enthalten.
- Wo sinnvoll, sollen ergänzende Hintergrundinformationen mitgeliefert werden.
- Die Darstellung soll handlungsorientiert sein: Was ist passiert, warum ist es relevant, was sollte man wissen?
- Für den MVP soll ein täglicher Recherche-Job um 03:00 Uhr laufen und 10 relevante Beiträge vorbereiten.
- Neue Beiträge werden als Hugo-kompatible Journal-Einträge mit Tags angelegt.
- Die Startseite zeigt nur die neuesten Beiträge, das Journal enthält den vollständigen Verlauf.
- Relevanzprüfungen sollen die drei Hauptachsen explizit behandeln: Zeit, Ort/Tragweite und Fachthema.
- Bei älteren Themen sollen Verallgemeinerungen oder Zeitverläufe nur mit Quellen, Fakten oder mehreren Beispielen erfolgen.
- Die Recherche kann zunächst als Platzhalter oder Entwurf laufen; der Schwerpunkt liegt auf einem sauberen, automatisierbaren Ablauf.

## Nicht-Ziele
- Keine Live-Ticker- oder Breaking-News-Optimierung.
- Keine reine Aufmerksamkeits- oder Empörungslogik.
- Keine vollständige Abdeckung des gesamten Nachrichtengeschehens.
- Kein komplexes Backend, solange ein statischer MVP reicht.

## Randbedingungen
- Der Relevanzfokus liegt auf Nachrichten, deren auslösendes Ereignis nicht brandneu ist.
- Die Ausgabe soll strukturiert, kompakt und quellenbasiert bleiben.
- Der MVP soll mit einer statischen Website und einem statischen Generator wie Hugo umsetzbar sein.
- Relevanzkriterien werden als Markdown-Dateien in einem separaten Ordner gepflegt.
- Der Hugo-Quellcode liegt getrennt unter `site/`.
- Die Relevanz wird aus Zeitnähe, räumlicher Nähe und fachlicher Passung zusammengedacht.

## Akzeptanzkriterien
- Eine Übersicht enthält nur Meldungen, die dem Relevanzkriterium entsprechen oder es plausibel erfüllen.
- Jede Meldung hat mindestens einen Link zur Originalquelle.
- Die Übersicht enthält bei Bedarf kurze Hintergrundinfos und Einordnung.
- Die Ausgabe wirkt kuratiert statt reaktiv und hektisch.
- Es existiert ein täglicher Job um 03:00 Uhr, der 10 relevante Beiträge vorbereitet.

## Offene Punkte
- Wie genau die Veröffentlichung über GitHub Pages automatisiert wird.
- Welche Hugo-Struktur und welches Content-Modell verwendet werden.
- Wie die 10 Beiträge pro Nacht genau priorisiert und formatiert werden.
