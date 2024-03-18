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
wird. In diesem Kapitel geht es nun darum, dass das Python-Programm auf das
Ergebnis eines Vergleichs reagiert, indem Code-Abschnitte nur dann ausgeführt
werden, wenn eine Bedingung erfüllt ist.


## Lernziele

```{admonition} Lernziele
:class: admonition-goals
* Sie können mit **if** eine Programmverzweigung implementieren.
```

## Syntax der if-Verzweigung

Bei einer Programmverzweigung wird Code abhängig von einer Bedingung ausgeführt.
Im einfachsten Fall liegt ein if-Block vor. Die Syntax lautet wie folgt:

```python
if bedingung:
    anweisungsblock
```

Ist die Bedingung erfüllt, also "True", so wird der eingerückte Anweisungsblock
ausgeführt, ansonsten übersprungen. Damit ist gemeint, dass der
Python-Interpreter nach dem Ende des if-Blocks weiter macht, falls die Bedingung
nicht erfüllt (= False) wird.

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
weiter.

Dieser Code könnte beispielsweise mit einer Benutzerabfrage kombiniert werden:
```python
alter = int(input('Wie alt sind Sie?'))
if (alter >= 18):
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
temperatur = int(input('Welche Temperatur haben wir aktuell?'))

# Verarbeitung und Ausgabe
if temperatur <= 10:
    print('Heute ist es aber kalt!')
```
````

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

Der Code erfordert drei if-Blöcke.
````

<iframe width="560" height="315" src="https://www.youtube.com/embed/b6KzYbM-Hvg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>