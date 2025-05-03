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

# 3.2 Das Modul NumPy

Python kann auch auf schwachbrüstiger Hardware laufen wie beispielsweise auf
dem Raspberry Pi. Ein Grund für die Effizienz von Python ist, dass nicht alle
möglichen Datentypen, Funktionen und Methoden von Beginn an in den Speicher
geladen werden, sondern erst bei Bedarf. Python-Code ist in sogenannte Module
unterteilt.

In diesem Jupyter Notebook werden wir den Modul-Mechanismus anhand des
NumPy-Moduls kennenlernen.

+++

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können erklären, was ein **Modul** in Python ist.
* Sie können ein Modul komplett mit **import modul** importieren und auf die
  darin enthaltenen Funktionalitäten mit **modul.funktionalitaet** zugreifen.
* Sie können mit **from modul import funktionalitaet** einzelne Funktionalitäten
  eines Moduls importieren.
* Sie kennen das Modul **NumPy**.
```

## Importieren von Modulen

Es wäre schön, häufig gebrauchte Zahlen wie die Kreiszahl $\pi$ oder die
Eulersche Zahl $e$ zur Verfügung zu haben. Leider gehören beide nicht zum
Python-Kern. Geben Sie einmal den folgenden Code ein:

```python
print(pi)
```

+++

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
die direkte import-Anweisung und importieren das Mathematik-Modul `numpy`. Das
NumPy-Modul ist eine leistungsstarke Bibliothek für numerische Berechnungen in
Python, die häufig in wissenschaftlichen und technischen Anwendungen verwendet
wird.

```{code-cell} ipython3
import numpy
```

Wird die obige Anweisung `import numpy` ausgeführt, passiert scheinbar nichts.
Tatsächlich hat der Python-Interpreter jedoch das Modul geladen. Die Anweisung
`dir(numpy)` listet auf, was genau alles importiert wurde.

```{code-cell} ipython3
dir(numpy)
```

Offensichtlich gehören sehr viele mathematische Funktionen zum NumPy-Modul, aber
auch die beiden Zahlen `pi` und `e` finden wir in der Liste. Dann können wir ja
$\pi$ jetzt direkt ausgeben lassen:

```{code-cell} ipython3
print(pi)
```

Erstaunlich, dass in einem Standard-Modul von Python die Programmier:innen $\pi$
nur mit zwei Nachkommastellen angegeben haben... haben sie auch nicht. Die
Variable `pi` wurde von uns selbst mit `pi = 3.14` definiert und ist nicht
identisch mit `pi` aus dem NumPy-Modul. Die Kreiszahl aus dem NumPy-Modul heißt
nämlich `numpy.pi`.

```{code-cell} ipython3
print(numpy.pi)
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
:class: miniexercise, toggle
```python
x = numpy.pi
y = numpy.sin(x)

print(y)
```
````

+++

## Importieren von einzelnen Funktionen oder Klassen

Wenn nur die Kreiszahl $\pi$ gebraucht wird, ist der komplette Import des
NumPy-Modules eine Verschwendung von Ressourcen. Auch kann es lästig sein, immer
`numpy.` vor pi zu setzen. Eine zweite Möglichkeit, Funktionalitäten eines
Moduls zu importieren, ist die Alternative

```python
from modulname import etwas1, etwas2
```

$\pi$ und die Sinus-Funktion werden dann folgendermaßen importiert:

```{code-cell} ipython3
from numpy import pi, sin
```

Jetzt können `pi` und `sin` direkt benutzt werden, ohne `numpy.` davor zu
schreiben.

```{code-cell} ipython3
print(pi)
print(sin(0))
```

````{admonition} Mini-Übung
:class: miniexercise
Importieren Sie die Wurzel-Funktion sqrt() direkt aus NumPy. Berechnen Sie dann
$\sqrt{49}$ und $\sqrt{2}$ und lassen Sie das Ergebnis jeweils ausgeben.
````

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
from numpy import sqrt

print(sqrt(49))
print(sqrt(2))
```
````

## Importieren von Modulen mit Alias

Es ist üblich, Module mit einem kürzeren Alias zu importieren, um den Code
lesbarer zu gestalten und weniger tippen zu müssen. Im Fall von NumPy wird
häufig der Alias `np` verwendet:

```{code-cell} ipython3
import numpy as np
```

Nachdem wir das Modul mit einem Alias importiert haben, verwenden wir diesen
Alias, um auf die Funktionen und Klassen des Moduls zuzugreifen:

```{code-cell} ipython3
x = np.pi
print(x)
```

````{admonition} Mini-Übung
:class: miniexercise
Importieren Sie das `math`-Modul mit dem Alias `m` und lassen Sie die Kreiszahl
$\pi$ ausgeben. Bilden Sie dann die Differenz aus der Kreiszahl des math-Moduls
und der Kreiszahl des NumPy-Moduls.

Gibt es einen Unterschied zwischen den beiden Zahlen?
````

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
import math as m

print(m.pi)

differenz = m.pi - np.pi
print(differenz)
```
````

Das math-Modul stellt ebenfalls mathematische Konstanten und Funktionen zur
Verfügung, ist aber weniger umfangreich. Daher verwenden wir in dieser Vorlesung
NumPy.

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir den Modul-Mechanismus in Python untersucht und das
NumPy-Modul als Beispiel verwendet. Wir haben gelernt, wie man Module
importiert, spezifische Funktionen und Klassen aus einem Modul importiert und
Module mit einem Alias importiert. Durch das Verständnis dieser Konzepte können
Sie Ihren Python-Code besser organisieren und die Wiederverwendbarkeit von Code
verbessern. Im nächsten Kapitel werden wir ein weiteres Modul kennenlernen.
