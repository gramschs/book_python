---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 7.3 Dictionaries

Häufig müssen Daten strukturiert gespeichert werden. Beispielsweise sollen
Maschinenkonfigurationen effizient verwaltet werden. Für solche Fälle gibt es
eine Datenstruktur, die besser als eine Liste geeignet ist, das sogenannte
Dictionary.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können Dictionary-Objekte mit **Schlüssel** und **Wert** anlegen und
  verstehen die grundlegende Syntax **{key: value}**.
* Sie beherrschen den Zugriff auf Werte über ihre Schlüssel und können
  überprüfen, ob bestimmte Schlüssel in einem Dictionary vorhanden sind.
* Sie können neue Schlüssel-Wert-Paare hinzufügen, bestehende Werte
  aktualisieren und Einträge aus einem Dictionary entfernen.
* Sie kennen und nutzen die wichtigsten Methoden wie `.keys()`, `.values()`,
  `.items()` und `.get()` für effiziente Operationen.
* Sie können durch Schlüssel, Werte oder Schlüssel-Wert-Paare eines Dictionaries
  iterieren und diese in Schleifen verarbeiten.
```

## Grundlagen von Dictionaries

Dictionaries (deutsch: Wörterbücher) sind eine der wichtigsten Datenstrukturen
in Python. Sie speichern Daten in Form von Schlüssel-Wert-Paaren (key-value
pairs), wobei jeder Schlüssel eindeutig sein muss. Wir können uns ein Dictionary
wie ein technisches Handbuch vorstellen: Wir schlagen einen Begriff (Schlüssel)
nach und erhalten die zugehörige Information (Wert).

Ein Dictionary ist eine veränderbare, ungeordnete Sammlung von
Schlüssel-Wert-Paaren. Im Gegensatz zu Listen, die über einen numerischen Index
angesprochen werden, erfolgt der Zugriff bei Dictionaries über beliebige
unveränderliche Objekte als Schlüssel (meist Strings oder Zahlen).

```{code-cell}
stahl = {
    "Werkstoffnummer": "1.4301",
    "Dichte": 7900,  # kg/m³
    "E-Modul": 200000,  # MPa
    "Streckgrenze": 190  # MPa
}
print(stahl)
```

Dictionaries werden mit geschweiften Klammern `{}` erstellt. Die
Schlüssel-Wert-Paare werden durch Doppelpunkte `:` getrennt, mehrere Paare durch
Kommas `,`.

```{code-cell}
# Verschiedene Möglichkeiten der Dictionary-Erstellung
# 1. Direkte Erstellung
motor = {"Typ": "V6", "Leistung": 250, "Hubraum": 3.0}

# 2. Leeres Dictionary erstellen und befüllen
getriebe = {}
getriebe["Typ"] = "Automatik"
getriebe["Gänge"] = 8

# 3. Mit der dict()-Funktion
reifen = dict(Breite=225, Verhältnis=45, Durchmesser=17)

print("Motor:", motor)
print("Getriebe:", getriebe)
print("Reifen:", reifen)
```

Der Zugriff auf Werte erfolgt über die Angabe des Schlüssels in eckigen
Klammern:

```{code-cell}
# Zugriff auf einzelne Werte
print("Motorleistung:", motor["Leistung"], "kW")
print("Anzahl Gänge:", getriebe["Gänge"])
print("Reifenbreite:", reifen["Breite"], "mm")

# Ändern von Werten
motor["Leistung"] = 265
print("Neue Motorleistung:", motor["Leistung"], "kW")
```

Im Gegensatz zu Listen, die über numerische Indizes (0, 1, 2, ...) angesprochen
werden, verwenden Dictionaries aussagekräftige Schlüssel:

```{code-cell}
# Vergleich: Liste vs. Dictionary
# Als Liste (unübersichtlich)
werkstoff_liste = ["1.4301", 7900, 200000, 190]
print("Dichte (Liste):", werkstoff_liste[1])  # Was bedeutet Index 1?

# Als Dictionary (selbsterklärend)
werkstoff_dict = {
    "Werkstoffnummer": "1.4301",
    "Dichte": 7900,
    "E-Modul": 200000,
    "Streckgrenze": 190
}
print("Dichte (Dictionary):", werkstoff_dict["Dichte"])
```

```{admonition} Mini-Übung
:class: miniexercise
Erstellen Sie ein Dictionary für die Eigenschaften von Aluminium mit folgenden Daten:
- Werkstoffnummer: "3.1645"
- Dichte: 2700 kg/m³
- E-Modul: 70000 MPa
- Streckgrenze: 160 MPa
- Wärmeleitfähigkeit: 140 W/(m·K)

Greifen Sie dann auf die Dichte und die Wärmeleitfähigkeit zu und geben Sie diese mit passenden Einheiten aus.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Dictionary für Aluminium erstellen
aluminium = {
    "Werkstoffnummer": "3.1645",
    "Dichte": 2700,
    "E-Modul": 70000,
    "Streckgrenze": 160,
    "Wärmeleitfähigkeit": 140
}

# Zugriff auf spezifische Eigenschaften
print("Dichte von Aluminium:", aluminium["Dichte"], "kg/m³")
print("Wärmeleitfähigkeit:", aluminium["Wärmeleitfähigkeit"], "W/(m·K)")
```
````

## Arbeiten mit Dictionaries

In diesem Abschnitt betrachten wir, wie Dictionaries dynamisch verändert,
durchsucht und mit verschiedenen Methoden effizient bearbeitet werden können.

Dictionaries sind veränderbar. Wir können jederzeit neue Einträge hinzufügen
oder bestehende entfernen:

```{code-cell}
# Dictionary für eine Hydraulikpumpe
pumpe = {
    "Typ": "Axialkolbenpumpe",
    "Volumenstrom": 120,  # l/min
    "Druck": 250  # bar
}

# Neue Einträge hinzufügen
pumpe["Drehzahl"] = 1450  # U/min
pumpe["Wirkungsgrad"] = 0.92

print("Erweiterte Pumpendaten:", pumpe)

# Eintrag löschen mit del
del pumpe["Wirkungsgrad"]
print("Nach Löschen:", pumpe)

# Eintrag löschen mit pop() - gibt den Wert zurück
drehzahl = pumpe.pop("Drehzahl")
print("Entfernte Drehzahl:", drehzahl)
print("Finale Pumpendaten:", pumpe)
```

Bevor Sie auf einen Schlüssel zugreifen, sollten wir prüfen, ob er existiert:

```{code-cell}
# Maschinenkonfiguration
maschine = {
    "Modell": "DMG MORI DMU 50",
    "Achsen": 5,
    "Arbeitsraum_X": 500,
    "Arbeitsraum_Y": 450
}

# Prüfen, ob Schlüssel existiert
if "Arbeitsraum_Z" in maschine:
    print("Z-Achse:", maschine["Arbeitsraum_Z"])
else:
    print("Z-Achse nicht definiert")
    maschine["Arbeitsraum_Z"] = 400

# Negative Prüfung
if "Spindeldrehzahl" not in maschine:
    maschine["Spindeldrehzahl"] = 12000  # U/min
    
print("Vollständige Maschinendaten:", maschine)
```

Python bietet mehrere nützliche Methoden für die Arbeit mit Dictionaries:

```{code-cell}
# Werkzeugdaten für Fräswerkzeuge
werkzeuge = {
    "VHM_Schaftfraeser_6mm": {"Durchmesser": 6, "Zaehne": 4, "Material": "VHM"},
    "HSS_Bohrer_8mm": {"Durchmesser": 8, "Material": "HSS-E"},
    "Planfraeser_50mm": {"Durchmesser": 50, "Zaehne": 5, "Material": "HM"}
}

# keys() - alle Schlüssel abrufen
print("Verfügbare Werkzeuge:")
for werkzeug in werkzeuge.keys():
    print("-", werkzeug)

# values() - alle Werte abrufen
print("\nWerkzeugdetails:")
for details in werkzeuge.values():
    print(details)

# items() - Schlüssel-Wert-Paare abrufen
print("\nKomplette Werkzeugliste:")
for name, eigenschaften in werkzeuge.items():
    print(f"{name}: {eigenschaften}")
```

Es gibt verschiedene Möglichkeiten, über ein Dictionary zu iterieren:

```{code-cell}
# Materialdatenbank
materialien = {
    "Stahl": {"Dichte": 7850, "E_Modul": 210000, "Preis_kg": 1.50},
    "Aluminium": {"Dichte": 2700, "E_Modul": 70000, "Preis_kg": 3.20},
    "Titan": {"Dichte": 4500, "E_Modul": 110000, "Preis_kg": 45.00}
}

# Iteration über Schlüssel (Standard)
print("Materialien in der Datenbank:")
for material in materialien:  # äquivalent zu materialien.keys()
    print(material)

# Iteration über Werte
print("\nMaterialdichten (kg/m³):")
for eigenschaften in materialien.values():
    print(eigenschaften["Dichte"])

# Iteration über Schlüssel-Wert-Paare
print("\nMaterialpreise:")
for material, eigenschaften in materialien.items():
    print(f"{material}: {eigenschaften['Preis_kg']} €/kg")
```

Die Methode `.get()` ermöglicht sicheren Zugriff mit Standardwerten:

```{code-cell}
# Lagerdaten
lager = {
    "Schrauben_M8": 500,
    "Muttern_M8": 480,
    "Scheiben_M8": 520
}

# Unsicherer Zugriff (kann Fehler verursachen)
# anzahl = lager["Schrauben_M10"]  # KeyError!

# Sicherer Zugriff mit get()
anzahl_m10 = lager.get("Schrauben_M10", 0)  # Standardwert 0
print(f"Schrauben M10 im Lager: {anzahl_m10}")

# Mit get() auf vorhandene Werte zugreifen
anzahl_m8 = lager.get("Schrauben_M8", 0)
print(f"Schrauben M8 im Lager: {anzahl_m8}")
```

```{admonition} Mini-Übung
:class: miniexercise
Erstellen Sie ein Dictionary für verschiedene Stahlsorten mit ihren Preisen pro Kilogramm:
- S235: 1.20 €/kg
- S275: 1.35 €/kg
- S355: 1.50 €/kg

Fügen Sie dann S460 mit 1.80 €/kg hinzu. Gehen Sie anschließend mit einer for-Schleife durch alle Einträge und geben aus, welche Stahlsorten teurer als 1.40 €/kg sind.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Dictionary für Stahlsorten erstellen
stahlpreise = {
    "S235": 1.20,
    "S275": 1.35,
    "S355": 1.50
}

# Neue Stahlsorte hinzufügen
stahlpreise["S460"] = 1.80

# Teure Stahlsorten ausgeben
print("Stahlsorten über 1.40 €/kg:")
for stahl, preis in stahlpreise.items():
    if preis > 1.40:
        print(f"- {stahl}: {preis} €/kg")
```
````

## Fortgeschrittene Dictionary-Konzepte

In diesem Abschnitt vertiefen wir unser Wissen über Dictionaries durch
verschachtelte Strukturen und erweiterte Methoden für komplexe Anwendungen im
Maschinenbau.

Dictionaries können andere Dictionaries als Werte enthalten, was hierarchische
Datenstrukturen ermöglicht:

```{code-cell}
# CNC-Maschinenkonfiguration mit verschachtelten Dictionaries
cnc_maschine = {
    "Modell": "DMG MORI NLX 2500",
    "Achsen": {
        "X": {"Verfahrweg": 300, "Geschwindigkeit": 30, "Beschleunigung": 5},
        "Y": {"Verfahrweg": 200, "Geschwindigkeit": 30, "Beschleunigung": 5},
        "Z": {"Verfahrweg": 500, "Geschwindigkeit": 24, "Beschleunigung": 4}
    },
    "Spindel": {
        "Max_Drehzahl": 12000,
        "Leistung": 30,  # kW
        "Drehmoment": 250  # Nm
    },
    "Werkzeugwechsler": {
        "Plaetze": 24,
        "Wechselzeit": 1.5  # Sekunden
    }
}

# Zugriff auf verschachtelte Elemente
print("X-Achse Verfahrweg:", cnc_maschine["Achsen"]["X"]["Verfahrweg"], "mm")
print("Spindelleistung:", cnc_maschine["Spindel"]["Leistung"], "kW")

# Ändern eines verschachtelten Wertes
cnc_maschine["Achsen"]["Z"]["Geschwindigkeit"] = 28
print("Neue Z-Geschwindigkeit:", cnc_maschine["Achsen"]["Z"]["Geschwindigkeit"], "m/min")
```

Für sicheren Umgang mit möglicherweise fehlenden Schlüsseln bieten sich
erweiterte Methoden an:

```{code-cell}
# Maschinenwartungsdaten
wartung = {
    "Oelwechsel": "2024-03-15",
    "Inspektion": "2024-01-10",
    "Kalibrierung": "2024-02-20"
}

# get() mit Standardwert für nicht vorhandene Schlüssel
naechste_wartung = wartung.get("Hauptwartung", "nicht geplant")
print("Nächste Hauptwartung:", naechste_wartung)

# setdefault() - fügt Schlüssel nur hinzu, wenn er nicht existiert
wartung.setdefault("Schmierung", "2024-04-01")
wartung.setdefault("Inspektion", "2024-12-31")  # Ändert nichts, da bereits vorhanden

print("\nAktuelle Wartungsliste:")
for art, datum in wartung.items():
    print(f"- {art}: {datum}")
```

Ein praktisches Beispiel zeigt, wie verschachtelte Dictionaries zur Verwaltung
komplexer Maschinenkonfigurationen verwendet werden:

```{code-cell}
# Werkzeugmagazin einer Fräsmaschine
werkzeugmagazin = {
    "Platz_1": {
        "Typ": "Schaftfraeser",
        "Durchmesser": 10,
        "Material": "VHM",
        "Standzeit": 120  # Minuten
    },
    "Platz_2": {
        "Typ": "Bohrer",
        "Durchmesser": 8.5,
        "Material": "HSS",
        "Standzeit": 80
    },
    "Platz_3": {
        "Typ": "Gewindebohrer",
        "Durchmesser": 6,
        "Material": "HSSE",
        "Standzeit": 60
    }
}

# Übersicht über alle Werkzeuge
print("Werkzeugmagazin-Übersicht:")
for platz, werkzeug in werkzeugmagazin.items():
    print(f"\n{platz}:")
    print(f"  Typ: {werkzeug['Typ']}")
    print(f"  Durchmesser: {werkzeug['Durchmesser']} mm")
    print(f"  Reststandzeit: {werkzeug['Standzeit']} min")
```

```{admonition} Mini-Übung
:class: miniexercise
Erstellen Sie ein verschachteltes Dictionary für eine einfache Werkzeugmaschine mit:
- Name: "Drehbank DL-200"
- Zwei Achsen (X und Z) mit jeweils:
  - Verfahrweg in mm
  - Aktuelle Position in mm
- Spindeldaten mit:
  - Maximale Drehzahl
  - Aktuelle Drehzahl

Geben Sie dann die aktuelle Position beider Achsen aus.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Werkzeugmaschine als verschachteltes Dictionary
drehbank = {
    "Name": "Drehbank DL-200",
    "Achsen": {
        "X": {
            "Verfahrweg": 150,
            "Aktuelle_Position": 75.5
        },
        "Z": {
            "Verfahrweg": 500,
            "Aktuelle_Position": 250.0
        }
    },
    "Spindel": {
        "Max_Drehzahl": 3000,
        "Aktuelle_Drehzahl": 1500
    }
}

# Ausgabe der aktuellen Positionen
print(f"Aktuelle Positionen der {drehbank['Name']}:")
print(f"X-Achse: {drehbank['Achsen']['X']['Aktuelle_Position']} mm")
print(f"Z-Achse: {drehbank['Achsen']['Z']['Aktuelle_Position']} mm")
```
````

## Zusammenfassung

Dictionaries sind eine essenzielle Datenstruktur in Python für die Verwaltung
von Schlüssel-Wert-Paaren. Sie bieten schnellen Zugriff über aussagekräftige
Bezeichner statt numerischer Indizes.
