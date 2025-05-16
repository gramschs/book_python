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

# 5.2 Programmverzweigungen: if

Im letzten Kapitel haben wir gelernt, wie ein Vergleich in Python durchgeführt
wird und mit welchem Datentyp das Ergebnis eines solchen Vergleichs gespeichert
wird. In diesem Kapitel geht es nun darum, dass ein Python-Programm auf das
Ergebnis eines Vergleichs reagiert, indem Code-Abschnitte nur dann ausgeführt
werden, wenn eine Bedingung erfüllt ist.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können mit **if** eine Programmverzweigung implementieren.
* Sie kennen den **modulo**-Operator `%`.
```

## Syntax der if-Verzweigung

Bei einer Programmverzweigung wird Code abhängig von einer Bedingung ausgeführt.
Im einfachsten Fall liegt ein if-Block vor. Die Syntax lautet wie folgt:

```python
if bedingung:
    anweisung 1 # gehört zum if-Block
    anweisung 2 # gehört zum if-Block
anweisung 3 # gehört NICHT zum if-Block, wird immer ausgeführt
```

Ist die Bedingung erfüllt, also "True", so wird der eingerückte Anweisungsblock
ausgeführt. Ist die Bedingung *nicht* erfüllt, wird dieser übersprungen. Damit
ist gemeint, dass der Python-Interpreter nach dem Ende des if-Blocks
weitermacht, falls die Bedingung nicht erfüllt ist (= False).

Das Ende eines if-Blocks wird in Python durch die Einrückung bestimmt. Alle
Anweisungen, die mit der gleichen Einrückung nach dem Doppelpunkt folgen,
gehören zum if-Block. Sobald eine Zeile mit geringerer Einrückung (oder ohne
Einrückung) erscheint, erkennt Python, dass der if-Block abgeschlossen ist.
Diese Anweisungen werden dann unabhängig vom Ergebnis der if-Bedingung
ausgeführt.

Wir betrachten nun ein Beispiel:

```{code-cell} ipython3
alter = 20
if alter >= 18:
    print('Sie dürfen Alkohol kaufen.')
print('Bananen dürfen Sie immer kaufen, egal wie alt Sie sind ...')
```

Da die Person volljährig ist (`alter = 20`), ist der Vergleich `alter >= 18`
wahr, die Bedingung also erfüllt. Daher wird der Anweisungsblock, der nur aus
einer einzigen Anweisung besteht, ausgeführt. Der Python-Interpreter gibt den
String `Sie dürfen Alkohol kaufen.` aus und macht dann mit dem normalen Programm
weiter. In unserem Beispiel mit dem Alkoholkauf ist die Zeile `print('Bananen
dürfen Sie immer kaufen...')` nicht eingerückt und wird daher unabhängig vom
Alter immer ausgeführt.

Dieser Code könnte beispielsweise mit einer Benutzerabfrage kombiniert werden:

```python
alter = int(input('Wie alt sind Sie?'))
if alter >= 18:
    print('Sie dürfen Alkohol kaufen.')
print('Bananen dürfen Sie immer kaufen, egal wie alt Sie sind...')
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Skript, das einen Benutzer oder eine Benutzerin nach der aktuellen Temperatur fragt. Wenn die Temperatur kleiner gleich 10 ˚C ist, soll ausgegeben werden: "Heute ist es aber kalt!"
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe
temperatur = float(input('Welche Temperatur haben wir aktuell?'))

# Verarbeitung und Ausgabe
if temperatur <= 10:
    print('Heute ist es aber kalt!')
```
````

Nach dieser kurzen Mini-Übung kommt in der nächsten Mini-Übung eine etwas
längere Aufgabenstellung.

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Skript, das eine Benutzerin oder einen Benutzer nach einer Zahl fragt. 
Wenn die Zahl kleiner als 0 ist, soll ausgegeben werden: "Die Zahl ist negativ."
Wenn die Zahl genau gleich 0 ist, soll ausgegeben werden: "Die Zahl ist Null."
Wenn die Zahl größer als 0 ist, soll ausgegeben werden: "Die Zahl ist positiv."

Wie viele if-Blöcke brauchen Sie für die Umsetzung dieser Mini-Übung?
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe
zahl = float(input('Geben Sie bitte eine Zahl ein: '))

# Verarbeitung und Ausgabe
if zahl < 0:
    print('Die Zahl ist negativ.')

if zahl == 0:
    print('Die Zahl ist Null.')

if zahl > 0:
    print('Die Zahl ist positiv.')
```

Der Code erfordert drei if-Blöcke. In einem späteren Kapitel werden wir lernen,
diese Aufgabe eleganter mit elif / else zu programmieren.
````

```{dropdown} Video "if-Anweisung" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/b6KzYbM-Hvg"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Der modulo-Operator

Ein nützlicher Operator für Verzweigungen ist der modulo-Operator `%`. Dieser
berechnet den Rest einer Division und wird häufig verwendet, um festzustellen,
ob eine Zahl durch eine andere teilbar ist oder um zyklische Muster zu erzeugen.

```{code-cell} ipython3
# Beispiele für den modulo-Operator
print(10 % 3)  # Ergebnis: 1 (Rest bei Division 10 durch 3)
print(8 % 4)   # Ergebnis: 0 (Rest bei Division 8 durch 4)
```

Der modulo-Operator ist besonders nützlich, um zu prüfen, ob eine Zahl gerade
oder ungerade ist:

```{code-cell} ipython3
zahl = 15
if zahl % 2 == 0:
    print(f"Die Zahl {zahl} ist gerade.")
```

Er wird auch häufig eingesetzt, um zu überprüfen, ob ein Wert ein Vielfaches
eines anderen ist. Zum Beispiel kann man prüfen, ob eine fortlaufende Zahl ein
Vielfaches von 10 ist:

```{code-cell} ipython3
for i in range(1, 31):
    if i % 10 == 0:
        print(f"Die Zahl {i} ist ein Vielfaches von 10.")
```

Dieses Konzept werden wir später bei Schleifen wiedersehen, wenn wir
beispielsweise nur jeden n-ten Wert verarbeiten oder anzeigen möchten.

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, das die Zahlen von 1 bis 30 durchläuft und nur jede
dritte Zahl ausgibt. Verwenden Sie den Modulo-Operator, um zu prüfen, ob eine
Zahl durch 3 teilbar ist.
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Ausgabe jeder dritten Zahl von 1 bis 30
for zahl in range(1, 31):
    if zahl % 3 == 0:
        print(zahl)
```
````

## Typische Fehlerquellen bei if-Anweisungen

Bei der Implementierung von if-Anweisungen in Python gibt es einige häufige
Fallstricke, die besonders Anfängern begegnen:

**Vergessener Doppelpunkt:** Nach der Bedingung muss immer ein Doppelpunkt
stehen.

```python
# Falsch
if alter >= 18
    print("Sie sind volljährig.")

# Richtig
if alter >= 18:
    print("Sie sind volljährig.")
```

**Falsche Einrückung:** Python verwendet Einrückungen, um Codeblöcke zu
definieren. Alle Anweisungen, die zum if-Block gehören, müssen gleich eingerückt
sein.

```python
# Falsch
if alter >= 18:
print("Sie sind volljährig.")  # Fehlende Einrückung!

# Richtig
if alter >= 18:
    print("Sie sind volljährig.")
```

**Verwechslung von Zuweisungs- und Vergleichsoperator:** Für Vergleiche wird
`==` verwendet, nicht `=`.

```python
# Falsch (führt zu unerwarteten Ergebnissen)
if alter = 18:  # Zuweisung statt Vergleich!
    print("Sie sind genau 18.")

# Richtig
if alter == 18:
    print("Sie sind genau 18.")
```

**Ungeeignete Datentypen für Vergleiche:** Achten Sie darauf, dass die
verglichenen Werte kompatible Datentypen haben.

```python
# Problematisch
alter = input("Wie alt sind Sie? ")  # alter ist ein String
if alter >= 18:  # Vergleich zwischen String und Zahl führt zu TypeError
    print("Sie sind volljährig.")

# Richtig
alter = int(input("Wie alt sind Sie? "))  # Umwandlung in Integer
if alter >= 18:
    print("Sie sind volljährig.")
```

Diese Fehler führen zu Syntax- oder Laufzeitfehlern, die den Programmablauf
unterbrechen. Achten Sie daher besonders auf die korrekte Syntax und Einrückung
bei if-Anweisungen.

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir uns mit einer einfachen Verzweigung beschäftigt. Im
nächsten Kapitel geht es um mehrfache Verzweigungen mit elif und else.
