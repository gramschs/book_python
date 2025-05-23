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

# 7.1 Digitale Logik: und, oder, nicht

In früheren Kapiteln haben wir den booleschen Datentyp kennengelernt: wahr
(`True`) oder falsch (`False`). Man kann solche Ausdrücke auch kombinieren, z.B.
wenn zwei Bedingungen gleichzeitig erfüllt sein sollen. Beispielsweise soll eine
Maschine nur dann gestartet werden, wenn der Sicherheitsschalter aktiviert ist
UND die Temperatur unter einem kritischen Wert liegt. Beide Bedingungen müssen
erfüllt sein.

Die Grundlage solcher Verknüpfungen bildet die **boolesche Algebra**, benannt
nach dem Mathematiker [George
Boole](https://de.wikipedia.org/wiki/George_Boole). In dieser Vorlesung
konzentrieren wir uns auf die drei wichtigsten logischen Operatoren:

* UND (`and`): beide Bedingungen müssen erfüllt sein
* ODER (`or`): mindestens eine Bedingung muss erfüllt sein
* NICHT (`not`): kehrt den Wahrheitswert einer Bedingung um

Diese Operatoren sind grundlegend für technische Systeme und werden häufig für
Steuerungen, Regelungen und Sicherheitssysteme eingesetzt.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie kennen die logischen Operatoren und können diese in Python einsetzen:
    * logisches UND: `and`
    * logisches ODER: `or`
    * logisches NICHT: `not`
* Sie verstehen die Priorität der logischen Operatoren und können komplexe
  Bedingungen korrekt formulieren.
```

## Das logische UND

Beim logischen UND müssen beide Bedingungen erfüllt sein, damit insgesamt die
kombinierte Bedingung erfüllt ist. Vergleichbar ist dies mit einer
Reihenschaltung in der Elektrotechnik: Nur wenn beide Schalter eingeschaltet
sind, kann der Strom fließen.

Hier finden Sie ein erläuterndes Video (ca. 3:14 min) zur UND-Schaltung:

<https://www.youtube.com/watch?v=79WVEr2BVZI>

Die Ergebnisse der UND-Verknüpfung lassen sich in einer Wahrheitstabelle
darstellen:

Bedingung 1 | Bedingung 2 | Ergebnis mit ```and```
------------|-------------|--------------------------
True | True | True
False | True | False
True | False | False
False | False | False

Beispiel aus der Industrie: Ein automatisches Werkzeug darf nur dann betätigt
werden, wenn das Werkstück korrekt eingespannt ist UND der Sicherheitsbereich
frei ist:

```{code-cell} ipython3
werkstueck_eingespannt = True
sicherheitsbereich_frei = True

if werkstueck_eingespannt and sicherheitsbereich_frei:
    print('Werkzeug kann betätigt werden.')
else:
    print('Sicherheitsvoraussetzungen nicht erfüllt.')
```

Bei komplexeren Bedingungen kann die Verwendung von Klammern die Lesbarkeit
verbessern, auch wenn dies syntaktisch nicht immer erforderlich ist:

```{code-cell} ipython3
temperatur = 75
druck = 3.5

if (temperatur < 80) and (druck < 4.0):
    print('System arbeitet im normalen Betriebszustand.')
else:
    print('System außerhalb der normalen Parameter.')
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm für die Steuerung einer Hydraulikpresse. Die Presse
darf nur betätigt werden, wenn

1. die Betriebstemperatur zwischen 60°C und 85°C liegt und
2. der Druck zwischen 2.5 und 5.0 bar beträgt.

Lassen Sie die Werte vom Benutzer eingeben und geben Sie eine entsprechende
Meldung aus.
```

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe
temperatur = float(input('Aktuelle Betriebstemperatur (°C): '))
druck = float(input('Aktueller Druck (bar): '))

# Verarbeitung und Ausgabe
if (60 <= temperatur <= 85) and (2.5 <= druck <= 5.0):
    print('Hydraulikpresse kann betätigt werden.')
else:
    print('Betriebsparameter außerhalb des sicheren Bereichs!')
```
````

## Das logische ODER

Beim logischen ODER muss nur eine der Bedingungen erfüllt sein, damit insgesamt
die kombinierte Bedingung erfüllt ist. Die Bedingung ist auch erfüllt, wenn
beide Teilbedingungen wahr sind. Vergleichbar ist dies mit einer
Parallelschaltung in der Elektrotechnik: Es reicht, wenn einer der beiden
Schalter eingeschaltet ist, damit der Strom fließen kann.

Hier finden Sie ein erläuterndes Video (ca. 2:42 min) zur ODER-Schaltung:

<https://www.youtube.com/watch?v=UNkXbvSN9w8>

Die Wahrheitstabelle für das logische ODER:

Bedingung 1 | Bedingung 2 | Ergebnis mit ```or```
------------|-------------|--------------------------
True | True | True
False | True | True
True | False | True
False | False | False

Beispiel aus der Produktion: Ein Notaus-System muss aktiviert werden, wenn
entweder der Temperaturwert zu hoch ist ODER der Druckwert einen kritischen Wert
überschreitet:

```{code-cell} ipython3
temperatur = 95  # in Grad Celsius
druck = 4.8      # in bar

if (temperatur > 90) or (druck > 5.0):
    print('WARNUNG: Notabschaltung wird eingeleitet!')
else:
    print('System arbeitet im normalen Betriebsbereich.')
```

Python verwendet eine sogenannte **Kurzschlussauswertung** für logische
Operatoren. Dies bedeutet:

* Bei einem `and`-Ausdruck: Wenn der erste Teil `False` ist, wird der zweite
  Teil nicht mehr ausgewertet.
* Bei einem `or`-Ausdruck: Wenn der erste Teil `True` ist, wird der zweite Teil
  nicht mehr ausgewertet.

Dies kann man sich zur Verbesserung der Performance zunutze machen, indem man
bei `and`-Verknüpfungen die Bedingung mit der höheren Wahrscheinlichkeit für
`False` zuerst platziert.

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm für ein Alarmsystem einer CNC-Fräse. Das System soll
einen Alarm auslösen, wenn:

1. Die Drehzahl unter 500 U/min fällt oder über 2000 U/min steigt
2. Die Kühlmitteltemperatur über 60°C steigt

Lassen Sie die Werte vom Benutzer eingeben und geben Sie eine entsprechende
Meldung aus.
```

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe
drehzahl = float(input('Aktuelle Drehzahl (U/min): '))
kuehlmitteltemperatur = float(input('Aktuelle Kühlmitteltemperatur (°C): '))

# Verarbeitung und Ausgabe
if (drehzahl < 500) or (drehzahl > 2000) or (kuehlmitteltemperatur > 60):
    print('ALARM: Betriebsparameter außerhalb des sicheren Bereichs!')
else:
    print('System arbeitet im normalen Betriebsbereich.')
```
````

## Das logische NICHT

Das logische NICHT kehrt eine Aussage um. Wenn eine Bedingung wahr ist, wird sie
falsch und umgekehrt. In Python verwenden wir den Operator `not` für diese
Umkehrung.

Die Wahrheitstabelle für das logische NICHT:

Bedingung | Ergebnis mit ```not```
----------|--------------------------
True | False
False | True

Beispiel aus dem Maschinenbau: Eine Maschine darf nicht gestartet werden, wenn
der Wartungsmodus aktiviert ist:

```{code-cell} ipython3
wartungsmodus_aktiv = True

if not wartungsmodus_aktiv:
    print('Maschine kann gestartet werden.')
else:
    print('Maschine im Wartungsmodus: Start nicht möglich.')
```

Die Verwendung von `not` kann oft komplexe Bedingungen vereinfachen. Statt zu
prüfen, ob ein Wert außerhalb eines Bereichs liegt, kann man prüfen, ob er nicht
innerhalb des Bereichs liegt:

```{code-cell} ipython3
temperatur = 78

# Diese beiden Bedingungen sind äquivalent
if (temperatur < 60) or (temperatur > 85):
    print('Temperatur außerhalb des Betriebsbereichs.')
    
if not (60 <= temperatur <= 85):
    print('Temperatur außerhalb des Betriebsbereichs.')
```

## Priorität der logischen Operatoren

Bei mehreren logischen Operatoren in einem Ausdruck ist die Reihenfolge der
Auswertung wichtig. In Python gilt folgende Priorität:

1. Klammern `()`
2. Nicht `not`
3. Und `and`
4. Oder `or`

Zur Verdeutlichung einige Beispiele:

```{code-cell} ipython3
# Priorität der logischen Operatoren
a = True
b = False
c = True

# not hat Vorrang vor and
ergebnis1 = not a and b  # entspricht (not a) and b
print(f"not a and b = {ergebnis1}")

# and hat Vorrang vor or
ergebnis2 = a and b or c  # entspricht (a and b) or c
print(f"a and b or c = {ergebnis2}")

# Klammern ändern die Priorität
ergebnis3 = a and (b or c)  # erst b or c, dann and
print(f"a and (b or c) = {ergebnis3}")
```

Um Missverständnisse zu vermeiden, ist es oft ratsam, Klammern zu setzen, auch
wenn sie aufgrund der Prioritätsregeln nicht unbedingt nötig wären. Dies
verbessert die Lesbarkeit des Codes.

```{admonition} Mini-Übung
:class: miniexercise
Überlegen Sie zunächst, was das Ergebnis der folgenden logischen Verknüpfungen
ist (wahr oder falsch):

1. True and True
2. True or False
3. not True
4. False or True
5. True or (not False)
6. (not True) and False
7. not (True or False)
8. (not False) or (False and False)

Prüfen Sie Ihre Antworten anschließend im Python-Interpreter.
```

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# 1. True and True
print("True and True =", True and True)  # True

# 2. True or False
print("True or False =", True or False)  # True

# 3. not True
print("not True =", not True)  # False

# 4. False or True
print("False or True =", False or True)  # True

# 5. True or (not False)
print("True or (not False) =", True or (not False))  # True

# 6. (not True) and False
print("(not True) and False =", (not True) and False)  # False

# 7. not (True or False)
print("not (True or False) =", not (True or False))  # False

# 8. (not False) or (False and False)
print("(not False) or (False and False) =", (not False) or (False and False))  # True
```
````

```{dropdown} Video zu "Logische Operatoren" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/075l6R42tkQ"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Die booleschen Operatoren `and`, `or` und `not` sind fundamentale Werkzeuge für
die Programmierung von Bedingungen in Python. Sie ermöglichen die Formulierung
komplexer Entscheidungslogik und sind besonders für Steuerungs- und
Regelungsanwendungen von großer Bedeutung. Im nächsten Kapitel beschäftigen wir
uns mit Schleifen.
