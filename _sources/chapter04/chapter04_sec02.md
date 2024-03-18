---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: turtle
  language: python
  name: python3
---

(ref04_sec02)=
# 4.2 for-Schleifen mit range

In diesem Kapitel werden wir uns erneut mit Schleifen beschäftigen. Schleifen
ermöglichen es uns, bestimmte Aufgaben wiederholt auszuführen, ohne den Code
mehrmals schreiben zu müssen. Im [Kapitel 4.1](ref04_sec01) haben wir ja bereits
die for-Schleife mit Listen kennengelernt. In diesem Kapitel konzentrieren wir
uns auf die for-Schleife mit der range()-Funktion in Python.

## Lernziele

```{admonition} Lernziele
:class: admonition-goals
Sie können Zahlenlisten mit der **range()**-Funktion erzeugen und diese mit der
for-Schleife kombinieren.
```

## Die range()-Funktion

In vielen Fällen möchten wir eine Schleife für eine bestimmte Anzahl von
Iterationen ausführen. In Python können wir dies mit Hilfe der
`range()`-Funktion erreichen. Die range()-Funktion generiert eine Liste von
Zahlen, die wir dann anschließend in einer for-Schleife verwenden können.
Natürlich kann die Liste von Zahlen auch für andere Dinge genutzt werden, aber
die Verwendung für for-Schleifen ist sicherlich der häufigste Einsatzzweck von
range().

Die Syntax der range()-Funktion ist:

```python
range(stop)               # erzeugt eine Liste von 0 bis (stop - 1)
range(start, stop)        # erzeugt eine Liste von start bis (stop - 1)
range(start, stop, step)  # erzeugt eine Liste von start bis (stop - 1) mit der Schrittweite step
```

Es ist schwierig, sich den Inhalt von `range()` direkt anzuschauen. Am
einfachsten ist es, die range()-Funktion direkt mit der for-Schleife zu
kombinieren wie im nächsten Abschnitt.

## range() mit for

Um eine for-Schleife mit der range()-Funktion zu verwenden, kombinieren wir
einfach die beiden Konzepte:

```python
for i in range(start, stop, step):
    Anweisungen
```

Hier ist `i` die Schleifenvarible, die nacheinander bei jedem Schleifendurchgang
die Werte in der von range() erzeugten Liste annimmt. Im Folgenden finden Sie
einige Beispiele für die Verwendung von for-Schleifen mit range():

```{code-cell} ipython3
for i in range(5):
    print(i)
```

`range(5)` erzeugt eine Liste mit den Zahlen 0, 1, 2, 3, 4, die dann durch die
`print()`-Funktion nacheinander ausgegeben werden.


```{code-cell} ipython3
for i in range(2, 6):      
    print(i)
```

`range(2,6)` erzeugt eine Liste mit den Zahlen 2, 3, 4, 5. Achtung, die 6 gehört
nicht dazu, da das letzte Element der Liste ja die stop-Zahl - 1 ist.


```{code-cell} ipython3
for i in range(1, 10, 2): 
    print(i)
```

`range(1, 10, 2)` erzeugt die Liste 1, 3, 5, 7, 9.

Um die Bedeutung der Schrittweite `step` zu zeigen, können wir einmal eine
negative Schrittweite ausprobieren.

```{code-cell} ipython3
for i in range(10, 0, -1):
    print(i)
```

Die negative Schrittweite `step = -1` führt dazu, dass der Python-Interpreter
rückwärts zählt.

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie die Dreier-Zahlen von 3 bis 99 ausgeben, also 3, 6, 9, 12, 15, ..., 96, 99.
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
for i in range(3, 100, 3):
    print(i)
```
````

## Anwendungsbeispiele für die for-Schleife

Insbesondere, wenn die Anzahl der Wiederholungen feststeht, kommt die
for-Schleife in Kombination mit range() zum Einsatz. Im Folgenden sehen wir uns
typische Beispiele an.

Beispiel 1: Berechnung der Summe der ersten 10 natürlichen Zahlen

```{code-cell} ipython3
summe = 0
for i in range(1, 11):
    summe += i

print("Die Summe der ersten 10 natürlichen Zahlen ist: ", summe)
```

Beispiel 2: Nur jedes zweite Mal wird eine Aktion ausgeführt

```{code-cell} ipython3
for i in range(2, 11, 2):
    print(i)
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, dass die Summe der ersten n Quadratzahlen berechnet.
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
n = 5  # Beispielwert
summe = 0

for i in range(1, n + 1):
    summe += i ** 2

print("Die Summe der ersten Quadratzahlen ist:", summe)
```

Hier ist die Variable `n` im Python-Code gesetzt worden. Schöner wäre eine interaktive Abfrage mit der input()-Funktion:
```python
n = int(input('Wie viele Quadratzahlen sollen summiert werden?))
```
Aber das war nicht gefragt.
````




