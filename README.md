# Geodätische Berechnungen

Eine programmatische Implementierung der Übungsaufgaben im Studiengang „Vermessungswesen“

Holz/Dresden 2025

## Get started

Die Programme sind in Python und/oder in TypeScript implementiert.
Aufgaben die auch in TypeScript implementiert sind, kann man online probieren:
[https://felixfuchsff.github.io/gberweb/](https://felixfuchsff.github.io/gberweb/)

## Entwicklung

### Python

#### Einmalige Arbeit

Bibliotheken können via `pip` installiert werden. 
Zu empfehlen ist eine Nutzung von einer virtuellen Umgebung:

```shell
# Einmalig auszuführen
cd src
python -m venv .venv
source .venv/bin/active
pip install --requirement requirement.txt
```

#### Skript ausführen

Jeweilige Aufgaben sind in einem eigenen Ordner unter `src` implementiert.
Es gibt ein gemeinsames Pythonmodul `geodesy.py` in  `src`, wo gängige Funktionen implementiert sind.
Dieses Modul ist dann soft-linked in jeweiligen Aufgabe-Ordner, dadurch wird Verwaltungsarbeit reduziert. 

Eine Python-Aufgabe lässt sich etwa durch 

```bash
python 01-dreieckbrechnungen.py
```

#### Unittest

```shell
pytest -s
#                   -s   disable all capture → show print in console
# --log-cli-level=INFO   set log-level to INFO 
```

### Typescript

Nicht jede Aufgabe hat eine TypeScript-Version.
Wenn ich Spaß daran habe, mache ich es, oder wenn es gewünscht wird. (=in WA-Gruppe 2025 schreiben)


