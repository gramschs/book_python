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

# 10.2 Lineare Regression mit polyfit und polyval

## Lernziele

```{admonition} Lernziele
:class: admonition-goals
* Sie können mit **polyfit** die Koeffizienten einer Regressionsgerade zu
  gegebenen Messwerten bestimmen.
* Sie können mit **polyval** aus den berechneten Koeffizienten die
  Regressionsgerade bestimmen.
```

## Koeffizienten der Regressionsgerade berechnen mit polyfit

Python bzw. das Modul NumPy unterstützt die Suche nach der Regressionspolynomen
mit der Funktion `polyfit()`. Eine detaillierte Bechreibung finden Sie ìn der
[NumPy-Dokumentation
(polyfit)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfit.html).
Aufgerufen wird polyfit mit

`p = polyfit(x, y, grad)`

Dabei sind x und y die die Messdaten und `grad` ist ein Integer mit dem
Polynomgrad. Für eine lineare Funktion setzen wir `grad = 1`. Das Ergebnis ist
eine Liste (genauer gesagt ein Tupel). Die Liste enthält die Koeffizienten des
Polynoms in absteigender Reihenfolge.

Ist der Polynomgrad 1, dann ist `p[0]` die Steigung der linearen
Regressionsgerade und der y-Achsenabschnitt ist in `p[1]` gespeichert:

$$f(x) = p[0] \cdot x + p[1].$$

Um die Anwendung von `polyfit()` zu zeigen, werden zunächst die folgenden sieben
Messpunkte visualisiert:

```{code-cell} ipython3
import matplotlib.pyplot as plt

x = [-1, 0, 1, 2,  3, 4, 5]
y = [-2.52,  0.85,   3.21,  7.19,  8.93, 12.89, 15.40]

plt.figure()
plt.scatter(x,y)
plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten mit linearem Zusammenhang');
```

Als nächstes verwenden wir `polyfit`, um die Koeffizienten einer
Regressionsgerade von Python berechnen zu lassen.

```{code-cell} ipython3
import numpy as np

koeffizienten = np.polyfit(x,y, 1)
print(koeffizienten)
```

Die gefundene Regressionsgerade lautet also

$$f(x) = 2.98\cdot x + 0.59.$$ 

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie zusätzlich zu den Messwerten die gefundene Regressionsgerade in der
Farbe rot visualisieren.
```
```{code-cell} ipython3
# Hier Ihr Code
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
# Wertetabelle für Regressionsgerade
x_modell = np.linspace(-1, 5)
y_modell = 2.98 * x_modell + 0.59

# Visualisierung Messwerte und Regressionsgerade
plt.figure()
plt.scatter(x,y)
plt.plot(x_modell, y_modell, color='red')
plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten mit linearem Zusammenhang');
```
````

## Regressionsgerade aus Koeffizienten mit polyval aufstellen

Eine weitere Funktion aus dem NumPy-Modul ist die Funktion `polyval()`. Die
polyval-Funktion wird dazu benutzt, ein Polynom aufzustellen. Der Aufruf der
polyval-Funktion sieht prinzipiell so aus:

```python
y = np.polyval(koeffizienten, x)
```

Dabei ist `koeffizienten` die Liste mit den Koeffizienten des Polynoms, die z.B.
aus der Berechnung `polyfit()`stammen. Die Koeffizienten sind dabei wieder
absteigend sortiert. Zuerst kommt der Koeffizient der höchsten Potenz. `x` ist
eine Liste von Zahlen oder ein NumPy-Array, für die das Polynom ausgewertet
werden soll.

Wenn wir beispielhaft die Regressionsgerade des Beispiels an der Stelle $x =
2.5$ auswerten wollen, so schreiben wir

```{code-cell} ipython3
y = np.polyval(koeffizienten, 2.5)
print(f'Die Regressionsgerade an der Stelle x = 2.5 ist {y:.2f}.')
```

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie die Regressionsgerade mit `polyval` aus den mit `polyfit` für das
Intervall $[-1,5]$ auswerten und visualisieren Sie die Messwerte (in blau)
zusammen mit der Regressionsgeraden (in rot).
```
```{code-cell} ipython3
# Hier Ihr Code
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
# Wertetabelle für Regressionsgerade
x_modell = np.linspace(-1, 5)
y_modell = np.polyval(koeffizienten, x_modell)

# Visualisierung Messwerte und Regressionsgerade
plt.figure()
plt.scatter(x,y)
plt.plot(x_modell, y_modell, color='red')
plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten mit linearem Zusammenhang');
```
````

