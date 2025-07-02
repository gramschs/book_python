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

# 12.2 Lineare Regression mit polyfit und polyval

Nachdem wir im letzten Kapitel uns mit der Theorie der linearen Regression
beschäftigt haben, möchten wir nun konkret eine Regressionsgerade an Messdaten
anpassen. Umgangssprachlich wird auch gesagt, dass wir einen Fit durchführen
bzw. eine Gerade an die Messdaten anfitten.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können mit **polyfit** die Koeffizienten einer Regressionsgerade zu
  gegebenen Messwerten bestimmen.
* Sie können mit **polyval** aus den berechneten Koeffizienten die
  Regressionsgerade bestimmen.
```

## Koeffizienten der Regressionsgerade berechnen mit polyfit

Python bzw. das Modul NumPy unterstützt die Suche nach Regressionspolynomen mit
der Funktion `polyfit()`. Eine detaillierte Beschreibung finden Sie in der
[NumPy-Dokumentation
(polyfit)](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy-polyfit).
Mittlerweile gibt es modernere Methoden im Modul `numpy.polynomial`, aber wir
bleiben in dieser Vorlesung dennoch beim klassischen `polyfit()`, um eine
möglichst große Ähnlichkeit zu MATLAB zu wahren.

Aufgerufen wird polyfit mit

`p = polyfit(x, y, grad)`

Dabei sind x und y die Messdaten und `grad` ist ein Integer mit dem Polynomgrad.
Für eine lineare Funktion setzen wir `grad = 1`. Das Ergebnis ist ein
sogenanntes NumPy-Array, das wir im Folgenden wie eine Liste benutzen. Das Array
`p` enthält die Koeffizienten des Polynoms in absteigender Reihenfolge. Damit
ist gemeint, dass die höchste Potenz zuerst kommt.

Ist der Polynomgrad 1, dann ist `p[0]` die Steigung der linearen
Regressionsgerade und der y-Achsenabschnitt ist in `p[1]` gespeichert:

$$f(x) = p[0] \cdot x + p[1].$$

Um die Anwendung von `polyfit()` zu zeigen, werden zunächst die folgenden sieben
Messpunkte visualisiert:

```{code-cell}
import matplotlib.pyplot as plt

x = [-1, 0, 1, 2,  3, 4, 5]
y = [-2.52,  0.85,   3.21,  7.19,  8.93, 12.89, 15.40]

plt.figure()
plt.scatter(x,y)
plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten mit linearem Zusammenhang')
plt.show()
```

Als nächstes verwenden wir `polyfit`, um die Koeffizienten einer
Regressionsgerade von Python berechnen zu lassen.

```{code-cell}
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

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Wertetabelle für Regressionsgerade mit 50 Punkten
x_modell = np.linspace(-1, 5)
y_modell = 2.98 * x_modell + 0.59

# Visualisierung Messwerte und Regressionsgerade
plt.figure()
plt.scatter(x,y)
plt.plot(x_modell, y_modell, color='red')
plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten mit linearem Zusammenhang')
plt.show()
```
````

## Regressionsgerade aus Koeffizienten mit polyval auswerten

Eine weitere Funktion aus dem NumPy-Modul ist die Funktion `polyval()`. Die
polyval-Funktion wird dazu benutzt, ein Polynom auszuwerten. Der Aufruf der
polyval-Funktion sieht prinzipiell so aus:

```python
y = np.polyval(koeffizienten, x)
```

Dabei ist `koeffizienten` die Liste mit den Koeffizienten des Polynoms, die z.B.
aus der Berechnung `polyfit()` stammen. Die Koeffizienten sind dabei wieder
absteigend sortiert. Zuerst kommt der Koeffizient der höchsten Potenz. `x` ist
eine Liste von Zahlen oder ein NumPy-Array, für die das Polynom ausgewertet
werden soll.

Wenn wir die Regressionsgerade des Beispiels an der Stelle $x = 2.5$ auswerten
wollen, so schreiben wir

```{code-cell}
y = np.polyval(koeffizienten, 2.5)
print(f'Die Regressionsgerade an der Stelle x = 2.5 ist {y:.2f}.')
```

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie die Regressionsgerade mit `polyval` aus den mit `polyfit` für das
Intervall $[-1, 5]$ auswerten und visualisieren Sie die Messwerte (in blau)
zusammen mit der Regressionsgeraden (in rot).
```

```{code-cell}
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
plt.title('Künstliche Messdaten mit linearem Zusammenhang')
plt.show()
```
````

## Anwendung auf CO2-Daten

Nachdem wir die NumPy-Funktionen `polyfit()` und `polyval()` kennengelernt
haben, können wir diese nun auf unser CO2-Beispiel aus Kapitel 12.1 anwenden und
dabei systematisch vorgehen. Anstatt die Parameter der Regressionsgeraden durch
Ausprobieren zu finden, berechnen wir sie direkt:

```{code-cell}
import pandas as pd
from sklearn.metrics import r2_score

# Daten
data = pd.read_csv('data/co2_emissionen_worldwide.csv', skiprows=1, index_col=0)
jahre = data.index
co2 = data['Metrische_Tonnen_pro_Einwohner']

# Berechnung der optimalen Regressionskoeffizienten
koeffizienten = np.polyfit(jahre, co2, 1)
print(f'Steigung m = {koeffizienten[0]:.4f}')
print(f'y-Achsenabschnitt b = {koeffizienten[1]:.4f}')

# Erstellung der Modellfunktion
co2_modell = np.polyval(koeffizienten, jahre)

# Berechnung des R2-Wertes zur Bewertung der Anpassungsqualität
r2 = r2_score(co2_modell, co2)
print(f'R2 = {r2:.4f}')
```

Mit `polyfit()` erhalten wir eine Steigung von etwa 0.0344 und einen
y-Achsenabschnitt von -64.75, was unseren durch Ausprobieren gefundenen Werten
sehr nahe kommt. Der R²-Wert von 0.77 bestätigt, dass die lineare Regression die
CO2-Emissionsdaten gut erklärt, aber nicht sehr gut. Dies macht die
Regressionsgerade zu einem brauchbaren Modell für Prognosen, auch wenn die
Abweichungen zeigen, dass andere Faktoren ebenfalls eine Rolle spielen.

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, eine lineare Funktion an Messdaten
anzupassen. Im nächsten Kapitel werden wir uns mit dem Fit von Polynomen
beschäftigen.
