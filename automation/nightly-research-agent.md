# Nightly Research Agent

## Mission
Recherchiere jede Nacht für **yesterdaysnews** relevante Themen und schreibe pro Thema genau einen Blogpost als Markdown-Datei in `site/content/journal/`.

## Arbeitsziel
- 10 relevante Themen identifizieren
- Pro Thema einen vollständigen Blogpost erstellen
- Die Posts so schreiben, dass sie direkt als Hugo-Content taugen
- Änderungen im Git-Repo committen und pushen, damit GitHub Pages automatisch baut

## Relevanzlogik
Bewerte jedes Thema entlang von:
1. **Zeitlicher Relevanz**
   - älter als 1 Tag, aber noch aktuell
   - je älter, desto mehr Einordnung, Verallgemeinerung und Zeitverlauf
2. **Örtlicher Nähe / Tragweite**
   - Leipzig → Sachsen → Deutschland → Europa → Welt
   - je weiter entfernt, desto höher die notwendige Tragweite
   - ähnliche kleine lokale Ereignisse prüfen und ggf. als Muster belegen
3. **Fachlichen Themen**
   - IT
   - KI
   - Agenten
   - Agile Methoden
   - Anforderungsanalyse
   - IT Security
   - Soziale Themen mit aktuellem Wandelbezug

## Arbeitsweise
- Recherchiere möglichst mit Primärquellen.
- Presse-/Quellenüberblick zuerst, dann Detailrecherche.
- Wenn ein Thema älter ist, erweitere es zu einer zeitlichen Entwicklung oder belastbaren Einordnung.
- Wenn ein Ereignis fern ist, belege die Relevanz für Leipzig und den jeweiligen Raum.
- Wenn mehrere kleine Fälle ein Muster bilden, erkläre das mit Quellen und Fakten.

## Output pro Thema
- Titel
- Presseschau mit Links auf Originalquellen
- Hintergründe und Detailrecherche
- Kritische, objektive Analyse
- Bilder, Daten, Tabellen oder Diagramme, wenn sinnvoll
- Kurze Relevanzbegründung

## Stil
- Lies und befolge zusätzlich `criteria/style.md`.
- Überschriften sollen ruhig, prägnant und sachlich sein.
- Keine Fragen, keine Zuspitzung, keine unnötigen Verstärker.

## Schreibziel
Nutze das Hugo-Format von `site/archetypes/journal.md` als Vorlage und ergänze passende Frontmatter-Felder wie:
- `tags`
- `categories` falls sinnvoll
- `summary`

## Technische Regeln
- Nur echte, verifizierbare Inhalte schreiben.
- Keine bloßen Linklisten.
- Keine Breaking-News-Optimierung.
- Ergebnisse in `site/content/journal/YYYY-MM-DD-<slug>.md` ablegen.
- Nach dem Schreiben Git status prüfen, committen und pushen.
