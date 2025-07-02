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

# 12.3 Polynomiale Regression

Die in den vorangegangenen Regressionstechniken erweitern wir nun von linearen
Regressiongeraden auf Regressionspolynome wie beispielsweise
Regressionsparabeln.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können mit **polyfit** zu gegebenen Messdaten die Koeffizienten eines
  Regressionspolynoms bestimmen.
* Sie können mit **polyval** aus den Koeffizienten ein Regressionspolynom
  auswerten.
* Sie wissen, was die Begriffe **Underfitting** und **Overfitting** bedeuten.
* Sie können mit dem Bestimmtheitsmaß R² abschätzen, welcher Polynomgrad $n$ zu
  den Daten passt.
```

## Regressionspolynome

Ein Regressionspolynom ist eine Möglichkeit der Regressionsanalyse, bei der die
Beziehung zwischen einer unabhängigen/erklärenden Variablen $x$ und einer
abhängigen Variablen $y$ durch ein Polynom modelliert wird. Damit erweitert die
polynomiale Regression die einfache lineare Regression, indem sie einen
quadratischen oder kubischen Anteil berücksichtigt. Theoretisch sind noch höhere
Polynomgrade möglich.

Ein Polynom 2. Grades hat die Form

$$y = ax^2 + bx + c,$$

ein Polynom 3. Grades

$$y = ax^3 + bx^2 + cx + d.$$

Die reellen Zahlen $a, b, c, d$ werden Koeffizienten des Polynoms genannt.

## Beispiel Regressionsparabel

Wir betrachten als Beispiel die folgenden künstlichen Messwerte.

```{code-cell}
import matplotlib.pyplot as plt

x = [-1, 0, 1, 2, 3, 4, 5]
y = [5.4384, 14.3252, 19.2451, 23.3703, 18.2885, 13.8978, 3.7586]

plt.figure()
plt.scatter(x,y)
plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten')
plt.show()
```

Sieht nicht nach einer linearen Funktion, also einer Geraden aus. Wir probieren
es mit einer quadratischen Funktion. Die Modellfunktion lautet

$$f(x)=ax^2 + bx + c$$

mit den Parametern $a$, $b$  und $c$. Wir setzen in der `polyfit()`-Funktion den
Polynomgrad auf `grad=2`.

```{code-cell}
import numpy as np

p = np.polyfit(x, y, 2)
print(p)
```

Bei der Zuordnung der Koeffizienten müssen wir sorgsam auf die Sortierung
achten. Unsere Modellfunktion beginnt beim quadratischen Anteil $ax^2$, dann
kommt der lineare Anteil $bx$ und zuletzt der konstante Part $c$.

```{code-cell}
a = p[0]
b = p[1]
c = p[2]

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
```

Wir erhalten also als Regressionsfunktion

$$r(x)=-1.9 x^2 + 7.4 x + 14.5.$$

Visualisieren wir die Modellfunktion zusammen mit den Messpunkten.

```{code-cell}
plt.figure();
plt.scatter(x,y);

x_plot = np.linspace(-1, 5, 100);
y_plot = a * x_plot**2 + b * x_plot + c
plt.plot(x_plot, y_plot, color='red')

plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten')
plt.show()
```

Alternativ kann die Funktion `polyval` dazu genutzt werden, um die Parabel auszuwerten.

```{code-cell}
plt.figure();
plt.scatter(x,y);

x_plot = np.linspace(-1, 5, 100);
y_plot = np.polyval(p, x_plot)
plt.plot(x_plot, y_plot, color='red')

plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten')
plt.show()
```

## Zu viel des Guten, höhere Polynomgrade sind nicht besser

Regressionspolynome scheinen zunächst besser zu sein als Regressionsgeraden.
Durch die zusätzlichen Terme können auch nichtlineare Beziehungen und komplexere
Muster in den Daten erklärt werden. Allerdings birgt die Verwendung höherer
Polynomgrade auch das Risiko des Overfittings. Der Begriff **Overfitting**
bedeutet, dass das Regressionspolynom zu genau an die Daten angepasst wurde und
neue Daten schlechter prognostiziert. Das Gegenteil davon ist **Underfitting**.
Das Regressionspolynom hat einen zu kleinen/niedrigen Polynomgrad und kann daher
die Daten kaum bis gar nicht erklären. Die Wahl des Polynomgrades ist daher sehr
wichtig.

```{admonition} Was ist Overfitting und Underfitting?
:class: note
Ist ein Modell zu stark an die Trainingsdaten angepasst und lässt es sich daher
nicht mehr verallgemeinern, liegt **Overfitting** (Überanpassung) vor. Fehlen
dahingegen erklärende Variablen, so dass die Komplexität der Daten nicht
abgebildet werden kann, sprechen wir von **Underfitting** (Unteranpassung).
```

Wir betrachten dazu das Beispiel von oben und verändern den Polynomgrad.

```{code-cell}
# künstliche Messdaten
x = [-1, 0, 1, 2, 3, 4, 5]
y = [5.4384, 14.3252, 19.2451, 23.3703, 18.2885, 13.8978, 3.7586]

plt.figure()
plt.scatter(x,y, color='black')
plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten')

x_plot = np.linspace(-1,5)

for grad in [1, 2, 3, 4]:
  # berechne Regressionspolynom
  p = np.polyfit(x, y, grad)
  y_plot = np.polyval(p, x_plot)
  # visualisiere zusätzlich das Regressionspolynon
  plt.plot(x_plot, y_plot, label=f'Grad {grad}')
plt.legend()
plt.show()
```

Eine Regressionsgerade kann die Messdaten nicht gut erklären, aber die
Regressionspolynome Grad 2 bis 4 passen sehr gut zu den künstlichen Messdaten
des Beispiels. Probieren wir noch höhere Polynomgrade aus.

```{code-cell}
# künstliche Messdaten
x = [-1, 0, 1, 2, 3, 4, 5]
y = [5.4384, 14.3252, 19.2451, 23.3703, 18.2885, 13.8978, 3.7586]

plt.figure()
plt.scatter(x,y, color='black')
plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten')

x_plot = np.linspace(-1,5, 200)

for grad in [5, 6, 7, 8]:
  # berechne Regressionspolynom
  p = np.polyfit(x, y, grad)
  y_plot = np.polyval(p, x_plot)
  # visualisiere zusätzlich das Regressionspolynon
  plt.plot(x_plot, y_plot, label=f'Grad {grad}')
plt.legend()
plt.show()
```

Grad 5 ist schon gut, aber die Regressionspolynome Grad 6 bis 8 scheinen perfekt
zu sein. Allerdings gibt es auch eine Warnung, denn wenn mehr
Polynomkoeffizienten da sind als Messpunkte, ist die Bestimmung der
Polynomkoeffizienten nicht mehr eindeutig. Bei $n$ Datenpunkten ist ein Polynom
vom Grad $n-1$ bereits eindeutig bestimmt und interpoliert alle Punkte exakt.

Dennoch, jeder Messpunkt wird exakt von dem Regressionspolynom getroffen.
Demnach müssten alle Residuen 0 sein und damit für das Bestimmtheitsmaß $R^2 =
1$ gelten. Am besten lassen wir eine Tabelle für den Polynomgrad und das
jeweilige Residuum ausgeben.

```{code-cell}
from sklearn.metrics import r2_score

for grad in range(1,9):
    p = np.polyfit(x, y, grad)
    y_modell = np.polyval(p, x)
    r2 = r2_score(y, y_modell)
    print(f'Polynomgrad {grad}: R2 = {r2:.4f}')
```

Die mathematische Theorie wird in der Praxis bestätigt. Der $R^2$-Score hat ab
dem Polynomgrad 6 den Wert 1. Wenn wir den Polynomgrad noch höher treiben,
passiert etwas Seltsames, was aber nicht im $R^2$-Score zu entdecken ist,
sondern in der Visualisierung der Regressionspolynome.

```{code-cell}
# künstliche Messdaten
x = [-1, 0, 1, 2, 3, 4, 5]
y = [5.4384, 14.3252, 19.2451, 23.3703, 18.2885, 13.8978, 3.7586]

plt.figure()
plt.scatter(x,y, color='black')
plt.xlabel('Ursache')
plt.ylabel('Wirkung')
plt.title('Künstliche Messdaten')

x_plot = np.linspace(-1,5, 200)

for grad in [9, 10, 15, 25]:
  # berechne Regressionspolynom
  p = np.polyfit(x, y, grad)
  y_plot = np.polyval(p, x_plot)
  # visualisiere zusätzlich das Regressionspolynon
  plt.plot(x_plot, y_plot, label=f'Grad {grad}')
plt.legend()
plt.show()
```

Die Polynome beginnen zwischen $x=4$ und $x=5$ immer höher zu schwingen. Es ist
unplausibel, dass diese Polynome die Messdaten gut erklären. Daher empfiehlt es
sich, möglichst den kleinsten Polynomgrad zu nehmen, der sehr gut, aber nicht
perfekt ist. Bei der Tabelle der R2-Werte haben wir gesehen, dass der R2-Wert
von 0.0054 (Grad 1) auf 0.9834 (Grad 2) springt. Danach sind aber keine
wesentlichen Verbesserungen mehr erkennbar. Daher wählen wir Grad 2 als
Regressionspolynom.

```{admonition} Tipp
:class: note
In der Ingenieurspraxis sollte immer das einfachste Modell gewählt werden, das
die Daten ausreichend gut beschreibt. Dies folgt dem Prinzip »Ockhams
Rasiermesser« (siehe [Wikipedia →  Ockhams
Rasiermesser](https://de.wikipedia.org/wiki/Ockhams_Rasiermesser)).
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, Messdaten durch Regressionspolynome zu modellieren. Dabei ist die sorgsame Wahl des Polynomgrads sehr wichtig, um Overfitting und Underfitting zu vermeiden. Es gibt außer den Regressionsmodellen noch viele weitere Möglichkeiten, für Messdaten Modelle zu erstellen. Damit beschäftigt sich das maschinelle Lernen, das ein Teilgebiet der Künstlichen Intelligenz ist.
