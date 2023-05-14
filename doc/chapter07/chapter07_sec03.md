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

# 7.3 Zufallszahlen

In diesem Kapitel werden wir uns mit der Erzeugung und Anwendung von
Zufallszahlen in Python beschäftigen. Wir nutzen dazu das Modul `numpy.random`
aus der Bibliothek NumPy. 

## Lernziele

```{admonition} Lernziele
:class: important
* Sie kennen den Unterscheid zwischen **gleichverteilten** und
  **normalverteilten** Zufallszahlen.
* Sie können gleichverteilte Integer und Floats erzeugen lassen.
* Sie können normalverteilte Floats zu einem vorgegebenen Mittelwert und einer
  vorgegebenen Standabweichung erzeugen lassen.
```

## Gleichverteilte Zufallszahlen

Eine gleichverteilte Zufallszahl ist eine Zufallszahl, bei der jedes mögliche
Ergebnis die gleiche Wahrscheinlichkeit hat. Das ist ähnlich wie beim Würfeln:
Jede der sechs Zahlen hat die gleiche Wahrscheinlichkeit aufzutauchen.

In Python können wir mit der Funktion `.uniform()` aus dem Modul `numpy.random`
gleichverteilte Zufallszahlen erzeugen. Hier ist ein Beispiel:

```{code-cell} ipython3
import numpy as np

zufallszahl = np.random.uniform()
print(zufallszahl)
```

Wir können auch mehrere Zahlen gleichzeitig erzeugen und dabei den Bereich der
Zahlen bestimmen:

```{code-cell} ipython3
zufallszahlen = np.random.uniform(10, 20, 5)
print(zufallszahlen)
```

Damit werden fünf gleichverteilte Zufallszahlen zwischen 10 und 20 generiert.

Neben den Funktionen für kontinuierliche Zufallszahlen stellt `numpy.random`
auch eine Funktion bereit, um zufällige Integer zu erzeugen. Die Funktion
`randint()` erzeugt zufällige ganze Zahlen innerhalb eines angegebenen Intervalls.

Dabei benötigt die Funktion `randint()` zwei Parameter: den Start des Intervalls
 und das Ende des Intervalls. Dabei gehört der Start des Intervalls dazu, aber
das Ende des Intervalls nicht. Optional kann ein dritter Parameter hinzugefügt
werden, um anzugeben, wie viele Zahlen erzeugt werden sollen.

Hier ist ein Beispiel:

```{code-cell} ipython
zufallszahl = np.random.randint(37, 99)
print(zufallszahl)
```

Der Code generiert eine zufällige ganze Zahl (Integer) zwischen 37 und 98. Die
99 kann jedoch nicht zufällig gezogen werden, da das Ende des Intervalls nicht
inkludiert ist.

Und hier ist ein Beispiel für die Erzeugung mehrerer Zahlen:

```{code-cell} ipython3
zufallszahlen = np.random.randint(0, 10, 5)
print(zufallszahlen)
```

Der Code generiert fünf ganzzahlige Zufallszahlen zwischen 0 und 9 und speichert
sie in der Liste `zufallszahlen`.

Es ist wichtig zu beachten, dass der obere Grenzwert bei `randint()` exklusiv
ist, d.h. er wird selbst nicht als möglicher Ausgang berücksichtigt. Wenn also
z.B. Zahlen von 1 bis 10 benötigt werden, sollte der obere Grenzwert als 11
angegeben werden:

```{code-cell} ipython3
zufallszahl = np.random.randint(1, 11)
print(zufallszahl)
```

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie sechs Lottozahlen erzeugen, d.h. sechs Integer, die zwischen 1 und 49
gleichmäßig verteilt sind. Die Lottozahlen sollen auch ausgegeben werden.
```
```{code-cell} ipython3
# Hier Ihr Code
```
````{admonition} Lösung
:class: minisolution, toggle
```python
import numpy as np
lottozahlen = np.random.randint(1, 50, 6)
print(lottozahlen)
```
````


## Normalverteilte Zufallszahlen

Eine normalverteilte Zufallszahl folgt der sogenannten Normalverteilung oder
Gaußschen Verteilung. Das ist eine Wahrscheinlichkeitsverteilung, die durch ihr
Glockenkurven-Diagramm bekannt ist.

Die Normalverteilung ist durch zwei Parameter definiert: Den Mittelwert (oder
Erwartungswert) und die Standardabweichung. Der Mittelwert ist der Wert, um den
die Werte im Durchschnitt zentriert sind. Die Standardabweichung ist ein Maß für
die Streuung der Werte.

In Python können wir mit der Funktion `numpy.random.normal()` normalverteilte
Zufallszahlen erzeugen:

```{code-cell} ipython3
zufallszahl = np.random.normal(0, 1)
print(zufallszahl)
```

Das erste Argument `0` steht für einen Mittelwert von 0. Das zweite Argument `1`
bedeutet, dass die Normalverteiung eine Standardabweichung von 1 hat.

Wir können auch mehrere Zahlen gleichzeitig erzeugen:

```{code-cell} ipython3
zufallszahlen = np.random.normal(0, 1, 5)
print(zufallszahlen)
```

Jetzt wurden fünf normalverteilte Zufallszahlen erzeugt.

```{admonition} Mini-Übung
:class: miniexercise
Bei einer Schulklasse wird die Körpergröße der Jugendlichen (Alter: 14 bis 18
Jahre) gemessen. Der Mittelwert bei den Mädchen ist 166.3 cm (Standardabweichung
6.39 cm) und bei den Jungen 176.8 cm (Standardabweichung 7.46 cm) (Quelle:
[Wikipedia ](https://de.wikipedia.org/wiki/Normalverteilung)).

Lassen Sie die Körpergrößen einer durchschnittlichen Schulklasse (= 13 Mädchen und 13 Jungen)erzeugen und ausgeben.
```
```{code-cell} ipython3
# Hier Ihr Code
```
````{admonition} Lösung
:class: minisolution, toggle
```python
import numpy as np

# Erzeugung der Körpergrößen
maedchen = np.random.normal(166.3, 6.39, 13)
jungen = np.random.normal(176.8, 7.46, 13)

# Ausgabe
print(maedchen)
print(jungen)
```
````
