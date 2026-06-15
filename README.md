# Country Guess

Country Guess ist ein kleines Länder-Quiz mit grafischer Oberfläche auf Basis von
[Flet](https://flet.dev/). Die App zeigt eine zufällige Flagge an und der
passende Ländername muss erraten werden. Bei falschen Antworten gibt es nach und
nach Hinweise, zum Beispiel Kontinent, Hauptstadt, Sprache und Anfangsbuchstabe.

## Features

- Zufällige Länderabfrage aus lokalen REST-Countries-Daten
- Anzeige der passenden Flagge aus `src/assets`
- Deutsche Ländernamen aus `src/countries.json`
- Hinweis-System mit vier Stufen
- Punktewertung: richtige Antworten bringen mehr Punkte, wenn weniger Hinweise
  gebraucht wurden
- Eingaben werden mit `unidecode` normalisiert, damit Umlaute und Akzente weniger
  Probleme machen
- Hintergrundmusik über `src/assets/sounds/Background_music.mp3`

## Projektstruktur

```text
country_guess/
├── src/
│   ├── main.py                 # Einstiegspunkt der Flet-App
│   ├── country.py              # Country-Datenklasse
│   ├── logic_handler.py        # Laden und Umwandeln der Länderdaten
│   ├── countries.json          # Lokale Länderdaten
│   └── assets/
│       ├── *.png               # Flaggenbilder nach CCA3-Code
│       └── sounds/
│           └── Background_music.mp3
├── country_api.py              # Lädt Länderdaten von restcountries.com
├── flag_loader.py              # Lädt Flaggenbilder aus den Länderdaten
├── pyproject.toml              # Projekt- und Flet-Konfiguration
├── requriements.txt            # Eingefrorene Paketliste
└── README.md
```

## Voraussetzungen

- Python 3.10 oder neuer
- Eine virtuelle Python-Umgebung wird empfohlen
- Flet für die grafische Oberfläche

Zusätzlich benötigt die App das Paket `Unidecode`, weil `src/main.py` es für die
Normalisierung der Eingaben importiert.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install flet Unidecode requests
```

Alternativ kann die vorhandene Paketliste installiert werden:

```bash
python -m pip install -r requriements.txt
python -m pip install Unidecode
```

Hinweis: Die Datei heißt im Projekt aktuell `requriements.txt`.

## App Starten

Desktop-App starten:

```bash
python src/main.py
```

Oder über Flet:

```bash
flet run src
```

Web-App starten:

```bash
flet run src --web
```

## Spielablauf

1. Beim Start wird automatisch ein zufälliges Land geladen.
2. Die App zeigt die Flagge und ein verdecktes Muster des Ländernamens.
3. Gib deinen Tipp in das Eingabefeld ein.
4. Mit `check guess` wird die Antwort geprüft.
5. Bei falscher Antwort erscheint ein Hinweis.
6. Bei richtiger Antwort steigt der Score und das nächste Land wird geladen.

Die Punkte pro richtigem Land berechnen sich aktuell aus:

```text
1 + verbleibende Hinweise
```

## Daten und Assets

Die Datei `src/countries.json` enthält die verwendeten Länderdaten. Sie kann mit
`country_api.py` neu aus der REST Countries API geladen werden:

```bash
python country_api.py
```

Die Flaggenbilder können anschließend mit `flag_loader.py` neu erzeugt werden:

```bash
python flag_loader.py
```

Dabei werden die Bilder nach dem dreistelligen `cca3`-Ländercode benannt und in
`src/assets` gespeichert, zum Beispiel `DEU.png`, `FRA.png` oder `JPN.png`.

## Wichtige Dateien

- `src/main.py`: Erstellt die Flet-Oberfläche, verwaltet Score, Hinweise,
  Eingaben und Länderwechsel.
- `src/logic_handler.py`: Lädt `countries.json` und baut daraus `Country`-
  Objekte.
- `src/country.py`: Enthält das einfache `Country`-Modell.
- `country_api.py`: Hilfsskript zum Aktualisieren der Länderdaten.
- `flag_loader.py`: Hilfsskript zum Herunterladen der Flaggen.

## Bekannte Hinweise

- In `src/main.py` gibt es bereits einen TODO-Kommentar für Länder ohne
  vorhandenes Flaggenbild.
- Das Projekt enthält aktuell 250 Länder-Datensätze und 249 lokale PNG-Flaggen.
- Die Paketliste ist als `requriements.txt` abgelegt. Falls du daraus eine
  Standarddatei machen willst, sollte sie in `requirements.txt` umbenannt werden.

## Verbesserungsvorschläge

- Eine Start- und Endansicht ergänzen, damit das Spiel einen klaren Einstieg,
  eine finale Auswertung und eine Möglichkeit zum Neustart bekommt.
- Fehlende Flaggen automatisch erkennen und entweder nachladen oder Länder ohne
  Flaggenbild beim Spielen überspringen.
- Schwierigkeitsgrade einbauen, zum Beispiel mit weniger Hinweisen, Zeitlimit
  oder einer Auswahl nach Kontinenten.
