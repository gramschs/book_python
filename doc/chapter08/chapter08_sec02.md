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

# 8.2 GUI



Bevor wir einen Ausflug in die GUI-Programmierung unternehmen, müssen einige
Module geladen werden. 

<font color='red'> Bitte installieren Sie mit dem Anaconda-Navigator -->
Environments das Modul jupyterlab-widgets nach, falls es fehlen sollte.
</font></br>


Bitte führen Sie mindestens einmal den folgenden Code aus, um die Funktionen für
die GUI-Programmierung in den Speicher zu laden. Mehr Details zu grafischen
Benutzeroberflächen in Jupyter Notebooks finden Sie auf der Internetseite
https://ipywidgets.readthedocs.io/en/stable/.


```python
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from numpy import *
from matplotlib.pylab import *
```

## Sliders

Danach programmieren wir zum Einstieg eine sehr simple Funktion.

```python
def f(x):
    print('Die Quadratzahl von {} ist {}.'.format(x, x**2)) 
```

Ich kann diese Funktion nun wie gewohnt aufrufen:

```python
f(2)
```

Oder beispielsweise alle Werte von -3 bis 3 durchlaufen:

```python
for x in range(-3,4):
    f(x)
```

Komfortabler für Benutzerinnen und Benutzer sind grafische Benutzeroberflächen.
Wir führen als erstes **Slider** ein. Ein Slider ist ein grafisches
Kontrollelement, mit dem die Benutzerin einen Wert setzen kann, indem ein
Indikator bewegt wird.

Dazu nutzen wir die Funktion `interact()` aus dem Modul `ipywidgets`. Die
Funktion `interact()` erzeugt zuerst einen Slider mit Variable und bennent
diesen Slider als `x` (siehe 2. Argument von interact) und verbindet dann die
Variable x mit der Funktion im 1. Argument. 

Klingt alles komplizierter als der entsprechende Code ist:

```python
interact(f, x=10);
```

Schauen wir uns ein zweites Beispiel an. Wir visualisieren eine Parabel mit
einem Vorfaktor, also $f(x)=a\cdot x^2$. Dazu schreiben wir eine Funktion, die
den Vorfaktor als Input-Argument entgegen nimmt und dann die Parabel mit dem
Definitionsgebiet $[-10, 10]$ zeichnet:

```python
def zeichne_parabel(a):
    x = linspace(-10, 10, 200)
    y = a * x**2
    plot(x,y)
```

```python
interact(zeichne_parabel, a=1);
```

Wie Sie sehen, wird bei der Initialisierung des Sliders ein Startwert gesetzt.
Das vertiefen wir gleich. Zunächst eine Aufgabe:

## Aufgabe 

Schreiben Sie eine Funktion, die die Funktion $f(x) = \sin(k \cdot x)$ im
Intervall $[-2\pi, 2\pi]$ zeichnet. Definieren Sie anschließend für `k` einen
Slider mit Startwert $k=2$. Bewegen Sie anschließend den Slider.

```python

```

Es ist auch möglich, zwei Slider zu definieren. Die folgende Funktion zeichnet
einen Punkt an den Koordinaten $(x,y)$:

```python
def zeichne_punkt(x,y):
    plot(x,y, 'o')
    xlim([-5,5])
    ylim([-5,5])
```

```python
zeichne_punkt(1,2)
```

Als nächstes definieren wir zwei Slider und verbinden die beiden Slider mit der
Funktion.

```python
interact(zeichne_punkt, x = 1, y = 2);
```

Es ist schade, dass wir nicht ganz nach links oder unten kommen, weil die Slider
Grenzen haben. Diese Grenzen und auch die Schrittweite zwischen den einzelnen
Werten des Sliders können wir direkt bei der Initialisierung der Slider
kontrollieren. Dann ist der Aufruf allerdings etwas komplizierter:

```python
interact(zeichne_punkt, 
         x = widgets.IntSlider(min=-5, max=5, step=1, value=1), 
         y = widgets.IntSlider(min=-5, max=5, step=1, value=2));
```

Der `IntSlider` kann auch durch einen `FloatSlider` ersetzt werden, bei dem dann
auch Fließkommazahlen und kleinere Zwischenschritte erlaubt sind.

```python
interact(zeichne_punkt, 
         x = widgets.FloatSlider(min=-5, max=5, step=0.2, value=1), 
         y = widgets.FloatSlider(min=-5, max=5, step=0.5, value=2));
```

## Aufgabe 

Eine Gerade wird durch die Funktionsgleichung

$y=m\cdot x + b$

mit der Steigung $m$ und dem y-Achsenabschnitt $b$ beschrieben. Schreiben Sie
eine Funktion, die eine Gerade im Intervall $[-5,5]$ zeichnet und bei der die
y-Achse stets zwischen $-10$ und $10$ anzeigt. Eine Benutzerin oder ein Benutzer
soll die Steigung im Bereich $m\in[-3,3]$ mit der Schrittweite $0.1$ und den
y-Achsenabschnitt $b\in[-7.5, 7.5]$ mit der Schrittweite $0.5$ wählen können. 

```python

```

## Edit Field

Bei einem Slider wird indirekt eine Variable mit einem Wert gefüllt, indem der
Benutzer oder die Benutzerin der Applikation einen Indikator regelt. Im Gegenzug
dazu erfolgt die direkte Eingabe über dein sogenanntes **Edit Field**. 

Wir konstruieren ein Eingabefeld für eine Altersabfrage. Der erste Wert, der
angezeigt werden soll, bevor der Benutzer seine Eingabe tätigt, wird mit `value`
definiert. `description` ist die Beschreibung, die vor dem Edit Field steht:

```python
widgets.IntText(
    value=18,
    description='Alter:'
)
```

Wir können nun zwar das Edit Field direkt mit ganzzahligen Werten befüllen, doch
werden diese nicht gespeichert. Daher wird im Folgenden das Edit Field mit einer
Funktion verbunden. Dazu verwenden wir erneut die Funktion `interact()`:

```python
def drucke(a):
    print('Das eingegebene Alter ist: ', a)

interact(drucke, a = widgets.IntText(value=18, description='Alter:' ));
```

## Aufgabe 

Schreiben Sie eine Funktion, die das Geburtsjahr eines Benutzers über ein Edit
Field abfragt und danch das Alter berechnet und ausgibt.

```python

```

## Drop-Down-Liste

Eine **Drop-Down-Liste**, manchmal auch **Pulldown-Menü** genannt, ermöglicht
eine Auswahl aus einer Liste von Objekten. Die einzelnen Auswahlmöglichkeiten
werden als Optionen gelistet. Wieder wird die Beschreibung vor dem GUI-Element
über den Wert von `description` gesetzt. Ein Startwert wird über `value`
vorausgewählt.

```python
widgets.Dropdown(
    options = [1, 2, 3],
    value = 2,
    description = 'Zahl:'
)
```

Die Verwendung dieses GUI-Elements erfolgt analog zu den vorherigen. Allerdings
packen wir der Übersichtlichkeit halber zunächst die Drop-Down-Liste in eine
Variable `dropdown` und verbinden per `interact()` die Funktion `f` und ihre
Variable `x`:

```python
def f(x):
    print('Die Quadratzahl von {} ist {}.'.format(x, x**2)) 
    
dropdown = widgets.Dropdown(
    options = [1, 2, 3],
    value = 2,
    description = 'Zahl:')
interact(f, x=dropdown);
```

## Aufgabe 

Schreiben Sie ein Programm, bei dem der Benutzer über zwei Drop-Down-Listen den
Tag und den Monat seines Geburtstages auswählt. Lassen Sie den Computer danach
feststellen, ob der Benutzer dieses Jahr schon Geburtstag hatte, heute gerade
Gebutstag hat (Gratulation) oder noch Geburtstag haben wird. Geben Sie eine
entsprechende Meldung aus.

```python

```

## Checkbox

Checkboxen sind explizit für die Abfrage von booleschen Werte, d.h. wahr oder
falsch, gemacht. Hier direkt ein Beispiel:

```python
widgets.Checkbox(
    value = False,
    description = 'Ja oder nein? ',
    indent = False
)
```

Falls Sie sich über die neue Option `indent` (zu deutsch Einzug) gewundert
haben, probieren Sie mal aus, was passiert, wenn Sie diese Option weglassen oder
auf `True` setzen.

```python
widgets.Checkbox(
    value = False,
    description = 'Ja oder nein? ',
    indent = True
)
```

Wir erweitern unseren Plot der Sinus-Funktion um eine Legende.

```python
def plotte_sinus(mit_legende):
    x = linspace(-2*pi, +2*pi)
    y = sin(x)
    plot(x, y, label='Sinus')
    if mit_legende == True:
        legend()
        

legende_checkbox = widgets.Checkbox(
    value = False,
    description = 'Legende ein ',
    indent = True
)      

interact(plotte_sinus, mit_legende = legende_checkbox);
```

## Aufgabe 

Schreiben Sie ein Programm, bei dem der Benutzer über eine Drop-Down-Liste
zwischen den Funktionen Sinus und Kosinus wählen darf. Anschließend wird die
ausgewählte Funktion im Intervall $[-2\pi, 2\pi]$ gezeichnet. Über eine Checkbox
darf der Benutzer entscheiden, ob die Gitterlinien eingeblendet werden sollen
oder nicht. 

```python

```
