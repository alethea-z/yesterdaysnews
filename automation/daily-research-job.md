# Daily Research Job

## Zweck
Tägliche Recherche um 03:00 Uhr für **yesterdaysnews**.

## Ziel
- 10 relevante Blogposts erarbeiten, je Thema genau ein Beitrag
- Relevanz gegen die Markdown-Kriterien prüfen
- Inhalte für die statische Website vorbereiten

## Relevanzprüfung
Jeder potenzielle Treffer wird gegen vier Hauptkriterien geprüft:

1. **Zeitliche Relevanz**
   - Ist das auslösende Ereignis älter als einen Tag?
   - Braucht das Thema eine breitere Einordnung oder einen Zeitverlauf?
   - Lassen sich langfristig gültige Erkenntnisse oder Entwicklungen ableiten?

2. **Örtliche Nähe / Tragweite**
   - Relevanzraum: Leipzig → Sachsen → Deutschland → Europa → Welt
   - Je weiter weg das Ereignis, desto höher muss die Tragweite sein.
   - Prüfe explizit, ob ähnliche kleine Ereignisse lokal an vielen Stellen auftreten.
   - Wenn ja, belege die Verallgemeinerung mit Quellen, Fakten oder mehreren Beispielen.
   - Vermeide allgemeine Ortsfloskeln; beschreibe den konkreten Wirkungspfad.

3. **Fachliche Themen**
   - IT
   - KI
   - Agenten
   - Agile Methoden
   - Anforderungsanalyse
   - IT Security
   - Soziale Themen mit Bezug zu aktuellen Veränderungen in der Welt

4. **Konkrete Wirkung auf Michaels Arbeitsfelder**
   - Berührt das Thema Softwareentwicklung, Projektleitung, KI-Nutzung, Security oder Governance?
   - Verändert es Toolauswahl, Kosten, Risiko, Compliance, Lieferfähigkeit oder Arbeitsweise?
   - Kann die Auswirkung mit Quelle, Zahl, Dokument oder direktem Mechanismus belegt werden?

## Arbeitsauftrag
1. Relevante Themen recherchieren.
2. Zu Beginn den aktuellen Wissensstand laden: `criteria/*.md`, `site/archetypes/journal.md`, `decisions.md`, `open-questions.md` und die zuletzt bearbeiteten Posts.
3. Die Recherche mit mehreren Startpunkten beginnen: Primärquelle, unabhängige Berichtsquelle, ggf. dritte Einordnung.
4. Bei Unternehmensquellen möglichst die konkrete News-, Event-, Filing- oder PDF-Seite verwenden; allgemeine IR-Startseiten nur als Fallback.
5. Aus der Initialmeldung eigene Folge-Suchanfragen ableiten, die Geschichte, Vergleichsfälle, Auswirkungen und regionale Unterschiede erschließen.
6. Pro Thema eine Presseschau mit Quellen aus unterschiedlichen Rollen erstellen.
7. Pro Thema eine **Recherchefrage** formulieren, die den Einzelfall zu einer überprüfbaren größeren Fragestellung verdichtet.
8. Zu jeder Recherchefrage eine **Prüfidee** festhalten: Welche Primärquelle, welche unabhängige Berichtsquelle und welche Kontextquelle tragen die Antwort?
9. Wenn die Frage mit „woran kann man erkennen …?“ beginnt, zuerst die allgemeinen Entscheidungskriterien notieren und danach den konkreten Fall bewerten.
10. Pro Thema zusätzliche, neu gesuchte Quellen für Hintergründe, Kontext und Detailrecherche sammeln.
11. Bei älteren Themen nach Trends, Chronologien und langfristigen Erkenntnissen suchen.
12. Für fernere Ereignisse die Tragweite klar belegen.
13. Wenn möglich, ähnliche lokale Kleinereignisse vergleichen.
14. Zahlen, Fristen, Vergleichswerte und Gegenbeispiele explizit prüfen und in die Argumentation einbauen.
15. Wenn eine Meldung Produktionsreife, Marktreife oder eine eindeutige Ursache behauptet, zusätzlich mit externen Kriterien, Gegenbeispielen und mindestens einer alternativen Erklärung validieren.
16. Pro Thema eine kritische und möglichst objektive Analyse schreiben.
17. Die Schlussfolgerung am Ende der Analyse klar mit der Ausgangsfrage verknüpfen und direkt beantworten, statt eine offene Frage stehen zu lassen.
18. Falls sinnvoll, Bilder, Daten, Tabellen oder Diagramme ergänzen — aber nur mit neuen Zahlen oder Auswertung, nicht als Textwiederholung.
19. Eine kurze Relevanzbegründung formulieren, die auf einen konkreten Mechanismus verweist.
20. 10 Beiträge auswählen, die das Kernkriterium erfüllen.
21. Die Ergebnisse als Markdown-Journal-Einträge mit der Standardgliederung vorbereiten.
22. Jeden Eintrag mit passenden Tags und ggf. Kategorien versehen.
23. Die Inhalte in `site/content/journal/` ablegen.

## Ausgaberegeln
- Ein Beitrag pro Thema / Blogpost
- Titel
- Presseschau mit 2 bis 4 Quellen aus unterschiedlichen Rollen, sinngemäß zusammengefasst und direkt verlinkt
- Hintergrund und Detailrecherche
- Kritische, objektive Analyse
- Bilder, Daten, Tabellen oder Diagramme, wenn sinnvoll und mit Zahlen/Auswertung
- Kurze Relevanzbegründung am Ende, mechanistisch statt allgemein
- Wenn das Thema älter ist: verallgemeinernde Zusammenfassung statt bloßer Meldung

## Status
- Platzhalter / initiale Definition
- Automatisierung wird separat über Cron betrieben
- Interaktive Zusammenarbeit ändert nicht direkt Posts, sondern passt nur die Laufanweisungen und Kriterien an; die eigentliche Ausführung läuft dann über denselben Batch- und Nightly-Mechanismus.
