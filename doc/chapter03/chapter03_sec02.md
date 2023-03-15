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

# 3.2 Das Modul Math

Python kann auch auf schwachbrüstiger Hardware laufen wie beispielsweise auf
dem Raspberry Pi. Ein Grund für die Effizienz von Python ist, dass nicht alle
möglichen Datentypen, Funktionen und Methoden von Beginn an in den Speicher
geladen werden, sondern erst bei Bedarf. Python-Code ist in sogenannte Module
unterteilt.

In diesem Jupyter Notebook werden wir den Modul-Mechanismus anhand des
Math-Moduls kennenlernen.

+++

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie können erklären, was ein **Modul** in Python ist.
* Sie können ein Modul komplett mit **import modul** importieren und auf die darin enthaltenen Funktionalitäten mit **modul.funktionalitaet** zugreifen.
* Sie können mit **from modul import funktionalitaet** einzelne Funktionalitäten eines Moduls importieren.
```

+++

## Import math

Es wäre schön, häufig gebrauchte Zahlen wie die Kreiszahl $\pi$ oder die
Eulersche Zahl $e$ zur Verfügung zu haben. Leider gehören beide nicht zum
Python-Kern, wie der folgende Versuch zeigt:

```{code-cell} ipython3
print(pi)
```

Python gibt eine Fehlermeldung aus. Der Fehler lautet "NameError". Der
Python-Interpreter meldet auch, bei welcher Variable der Namensfehler auftritt,
nämlich bei 'pi'. 

Die fehlende Kreiszahl Pi könnte natürlich zu Beginn eines Programmes eingeführt werden. 

```{code-cell} ipython3
pi = 3.14
print(pi)
```

Aber es gibt ja noch mehr Funktionalitäten, die im Python-Kern fehlen wie
beispielsweise die Sinus-Funktion oder die Wurzel-Funktion. 

Module sind Python-Programme, die Konstanten oder Anweisungen (Funktionen,
Klassen) zur Verfügung stellen und damit den eigentlichen Python-Kern erweitern.
Module müssen importiert werden, damit der Python-Interpreter diese erweiterten
Funktionalitäten benutzen kann.

Es gibt mehrere Anweisungen, ein Modul zu importieren. Als erstes betrachten wir
die direkte import-Anweisung und importieren das Mathematik-Modul `math`.

```{code-cell} ipython3
import math
```

Wird die obige Anweisung `import math` ausgeführt, passiert scheinbar nichts.
Tatsächlich hat der Python-Interpreter jedoch das Modul `math` geladen. Die
Anweisung `dir(math)` listet auf, was genau alles importiert wurde. 

```{code-cell} ipython3
dir(math)
```

Offensichtlich gehören sehr viele mathematische Funktionen zum math-Modul, aber auch die beiden Zahlen `pi` und `e` finden wir in der Liste. Dann können wir ja $\pi$ jetzt direkt ausgeben lassen:

```{code-cell} ipython3
print(pi)
```

Erstaunlich, dass in einem Standard-Modul von Python die Programmier:innen $\pi$
nur mit zwei Nachkommastellen angegeben haben... haben sie auch nicht. Die
Variable `pi` wurde von uns selbst mit `pi = 3.14` definiert und ist nicht
identisch mit `pi` aus dem math-Modul. Die Kreiszahl aus dem math-Modul heißt
nämlich `math.pi`.

```{code-cell} ipython3
print(math.pi)
```

Um Konstanten, Datentypen oder Funktionen eines Moduls zu nutzen, wird der
Modulname vorangestellt und erneut der Punkt benutzt. Probieren Sie es in der
nächsten Mini-Übung aus.

+++

````{admonition} Mini-Übung
:class: miniexercise
Weisen Sie der Variablen x den Wert $\pi$ zu. Lassen Sie dann $y = \sin(x)$
berechnen und ausgeben.
````

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: solution, toggle
```python
x = math.pi
y = math.sin(x)

print(y)
```
````

+++

## From math import

Wenn nur die Kreiszahl $\pi$ gebraucht wird, ist der komplette Import des
math-Modules zuviel des Guten. Auch kann es lästig sein, immer `math.` vor pi zu
setzen. Eine zweite Möglichkeit, Funktionalitäten eines Moduls zu importieren,
ist die Alternative

```python
from modulname import etwas1, etwas2
```

$\pi$ und die Sinus-Funktion werden dann folgendermaßen importiert:

```{code-cell} ipython3
from math import pi, sin
```

Jetzt können `pi` und `sin` direkt benutzt werden, ohne `math.` davor zu schreiben.

```{code-cell} ipython3
print(pi)
print(sin(0))
```

Tatsächlich gibt es noch weitere Möglichkeiten, etwas aus einem Modul zu importieren. Einen Überblick über diese Alternativen finden Sie im Internet unter [https://docs.python.org/3/tutorial/modules.html](https://docs.python.org/3/tutorial/modules.html).
