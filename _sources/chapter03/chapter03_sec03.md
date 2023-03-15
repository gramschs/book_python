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

# 3.3 Das Modul Turtle

In der Informatik nennt man Grafiken, die dadurch entstehen, dass ein Roboter
Linien auf eine Leinwand zeichnet, Turtle-Grafiken. Der Roboter wird dabei mit
einfachen Kommandos gesteuert. Beschrieben wird er durch seine Position (x- und
y-Koordinaten in einem kartesischen Koordinatensystem) und seine Ausrichtung.
Der "Stift" des Roboters kann von seinen Eigenschaften her ebenfalls variieren.
So können beispielsweise verschiedenfarbige Stifte verwendet werden oder die
Linienstärke kann verändert werden.

Der Kern von Python enthält bereits ein Modul namens `turtle`, um eine solche
Turtle-Grafik zu erzeugen. Da wir in dieser Vorlesung mit Jupyter Notebooks
arbeiten, verwenden wir jedoch das Modul `ipyturtle3`, das das Turtle-Modul mit
Funktionalitäten für Jupyter Notebooks erweitert.

**Achtung: Bitte verwenden Sie kein JupyterLab, sondern die klassische Software
Jupyter Notebook.**

## Lernziele 

```{admonition} Lernziele
:class: hint
* Sie wissen, was eine **Turtle-Grafik** ist.
* Sie können das Modul **ipyturtle3** importieren.
* Sie können ein Roboterfeld initalisieren und den Roboter mit einfachen Kommandos über das Roboterfeld steuern.
```

+++

## Die Leinwand vorbereiten

Als erstes importieren wir aus dem `ipyturtle3`-Modul die Kommandos Canvas, TurtleScreen und Turtle. Wir erzeugen mit dem Befehl

```python3
Canvas(width=500, height=250)
``` 

eine leere Leinwand, die 500 Bildpunkte breit ist und 250 Bildpunkte hoch ist. Bildpunkte werden normalerweise als Pixel bezeichnet, was wiederum mit px abgekürzt wird. Damit wir mit der Leinwand weiter arbeiten können, speichern wir dieses Objekt in der Variablen `leinwand`. Zuletzt lassen wir uns die Leinwand mit dem Befehl `display()` anzeigen.

Zusammengesetzt lautet der Code zur Erzeugung einer Leinwand also wie folgt:

```python3
from ipyturtle3 import Canvas, TurtleScreen, Turtle

leinwand = Canvas(width=500, height=250)
display(leinwand)
```

Die folgende Animation zeigt, was passiert, wenn die obige Code-Zelle ausgeführt
wird. Da die weiße Leinwand auf dem weißen Hintergrund des Jupyter Notebooks
nicht zu sehen, wird sie rot umrahmt.

```{image} media/demo_turtle_initialization.gif
:name: demo_turtle_initialization
```


Damit der Computer weiß, dass auf dieser Leinwand eine Turtle-Grafik gezeichnet
werden soll, platzieren wir über die Leinwand ein Turtle-Feld. Dazu erzeugen wir
mit dem Befehl `TurtleScreen()` das Feld und speichern es zur weiteren
Verwendung in der Variablen `feld`. Damit das Turtle-Feld auf der Leinwand
platziert wird, müssen wir der Erzeugung des Turtle-Feldes die Leinwand als
Zusatzinformation hinzufügen.

```python3
feld = TurtleScreen(leinwand)
```

## Der Roboter bewegt sich

Nun können wir endlich einen Roboter erzeugen und in die Mitte des Feldes setzen
lassen.

```python3
robo = Turtle(feld)
```

Mit dem Befehl

```python3
robo.forward(schritte)
```

wird der Roboter vorwärts bewegt und legt insgesamt `schritte` (gemessen in Pixeln) zurück.

Mit den Befehlen 

```python3
robo.left(winkel)
```

und 

```python3
robo.right(winkel)
```

wird der Roboter nach links (gegen den Uhrzeigersinn) oder rechts (im
Uhrzeigersinn) gedreht. Der Drehwinkel wird durch die Variable `winkel`
bestimmt.

Um jetzt den kompletten Code zusammen zu haben, wiederholen wir die bisherigen
Code-Zeilen in der folgenden Code-Zelle und experimentieren dann in der
übernächsten Code-Zelle mit der Steuerung des Roboters. Wenn Sie das Turtle-Feld
wieder auf seinen Ausgangszustand zurücksetzen möchten, führen Sie erneut die
Code-Zelle mit der Erzeugung und Initialisierung aus.

```python3
# Import der benötigten Module
from ipyturtle3 import Canvas, TurtleScreen, Turtle

# Erzeugung und Anzeige der Leinwand
leinwand = Canvas(width=500, height=250)
display(leinwand)

# Initialisierung des Turtle-Feldes
feld = TurtleScreen(leinwand)

# Erzeugung eines Roboters mit Namen robo und Platzierung auf dem Feld
robo = Turtle(feld)
```

```python3
robo.forward(100)
robo.left(120)
robo.forward(50)
```

Wenn Sie den Code in Ihrem Jupyter Notebook ausführen, sollten Sie Folgendes
sehen:

```{image} media/demo_turtle_running.gif
:name: demo_turtle_running
```

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie den Roboter ein Rechteck der Länge 200 px und Höhe 100 px zeichnen. Am Ende soll der Roboter in die ursprüngliche Richtung hin ausgerichtet sein, also nach Osten bzw. rechts.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: minisolution, toggle
```python
robo.forward(200)
robo.left(90)
robo.forward(100)
robo.left(90)
robo.forward(200)
robo.left(90)
robo.forward(100)
robo.left(90)
```
Anmerkung: natürlich hätten wir den Roboter auch viermal nach rechts drehen lassen können.
````

## Robo kann noch mehr... 

Die folgenden Befehle an den Roboter dienen zur Steuerung der Bewegung:

* forward(schritte): Der Roboter bewegt sich vorwärts, die Streckenlänge wird in
  Schritten `schritte` angegeben.
* backward(schritte): Der Roboter bewegt sich rückwärts, die Streckenlänge wird
  in Schritten `schritte` angegeben.
* right(winkel): Der Roboter dreht sich nach rechts, der Winkel `winkel` wird in
  Grad angegeben. 
* left(winkel): Der Roboter dreht sich nach links, der Winkel `winkel` wird in
  Grad angegeben.  
* goto(x,y): Der Roboter läuft direkt zu der angegeben Position (x,y).

Der Stift wird mit folgenden Befehlen eingestellt:

* pendown(): Der Stift wird hochgehoben. Bewegt sich der Roboter, hinterlässt er
  keine Zeichnung. 
* penup(): Der Stift wird abgesetzt, ab jetzt zeichnet der Roboter wieder.
* pensize(breite): Die Breite der Striche wird eingestellt, z.B. ist
  `robo.pensize(10)` ein breiter Strich.  

Für die Farbe gibt es das folgende Kommando:

* pencolor(farbe): Ändert die Farbe der Striche, z.B. stellt der Befehl
  `robo.pencolor('red')` auf rote Farbe um. Die Farben werden als String
  übergeben und entsprechen den englischen Farben.

Mehr Details finden Sie in der
[Turtle-Dokumentation](https://docs.python.org/3/library/turtle.html).



