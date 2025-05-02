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

# Übungen

```{admonition} Übung 3.1
:class: miniexercise
1. Erstellen Sie eine Liste mit den ersten drei Fußballvereinen der aktuellen
   Bundesligatabelle.
2. Erstellen Sie eine Liste, die die folgenden aktuellen Daten von Eintracht
   Frankfurt enthält:
   * Anzahl Spieltage
   * Anzahl Siege
   * Anzahl Unentschieden
   * Anzahl Niederlagen
   * Torverhältnis (also z.B. 55:31)
   * Tordifferenz 
   * Punkte
3. Lassen Sie beide Listen ausgeben.
4. Lassen Sie die aktuellen Punkte von Eintracht Frankfurt ausgeben.
```

````{admonition} Lösung
:class: miniexercise, toggle
Die folgenden Daten variieren natürlich je nach Datum. Das ist der Stand vom 22.03.2023: 
```python
# Eingabe
bundesliga_top3 = ['Borussia Dortmund', 'FC Bayern München', '1. FC Union Berlin']
eintracht_frankfurt = [25, 11, 7, 7, '46:36', 10, 40]

# Ausgabe
print('TOP3 der Bundesliga:')
print(bundesliga_top3)

print('Spieldaten Eintracht Frankfurt:')
print(eintracht_frankfurt)

print('Aktuelle Punkte von Eintracht Frankfurt:')
print(eintracht_frankfurt[6])
```
````

```{admonition} Übung 3.2
:class: miniexercise
Schreiben Sie ein Programm, das den Benutzer zwei Seitenlängen für die beiden
Katheten $a$ und $b$ eines rechtwinkligen Dreiecks eingeben lässt. Anschließend
berechnet das Programm die Länge der Hypotenuse $c$ und gibt diese aus.

Bemerkung: Was passiert, wenn Sie eine negative Zahl eingeben?
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe der Seitenlängen
a = float(input('Gib die Länge von Seite a ein: '))
b = float(input('Gib die Länge von Seite b ein: '))

# Berechnung der Hypotenuse
c = (a**2 + b**2)**0.5

# Ausgabe des Ergebnisses
print('Die Länge der Hypotenuse c beträgt:')
print(c)
```
Alternativ könnte man auch die Wurzelfunktion aus dem NumPy-Modul importieren und benutzen:
```python
from numpy import sqrt
c = sqrt(a**2 + b**2)
```
Zur Bemerkung: Wenn der Benutzer eine negative Zahl eingibt, würde das Programm
das berechnen, was es soll. Aber im Kontext der Anwendung könnte das Ergebnis
sinnlos sein, da die Länge der Seiten eines Dreiecks immer positiv sein muss. Es
wäre daher sinnvoll, eine Überprüfung der Eingabe durchzuführen, um
sicherzustellen, dass a und b positive Zahlen sind. Wenn der Benutzer eine
negative Zahl eingibt, könnte das Programm eine Fehlermeldung ausgeben und den
Benutzer auffordern, eine gültige Eingabe zu machen. Dazu kommen wir in späteren
Vorlesungen.
````

```{admonition} Übung 3.3
:class: miniexercise
Schreiben Sie ein Programm, das den Benutzer nach seinem Gewicht in Kilogramm
und seiner Größe in Metern fragt. Danach soll das Programm Body-Mass-Index (BMI)
berechnen und ausgeben. Der BMI berechnet sich mit der Formel

$$\text{BMI} = \frac{m}{l^2},$$

wobei $m$ für das Körpergewicht in kg und $l$ für die Körpergröße in m steht.

Welchen BMI haben Sie?
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe von Gewicht und Größe
gewicht = float(input("Gib dein Gewicht in Kilogramm ein: "))
groesse = float(input("Gib deine Größe in Metern ein: "))

# Berechnung des BMI
bmi = gewicht / (groesse ** 2)

# Ausgabe des Ergebnisses
print("Dein BMI beträgt:")
print(bmi)
```
````

```{admonition} Übung 3.4
:class: miniexercise
Schreiben Sie ein Programm, das mit dem Turtle-Modul ein Quadrat zeichnet. Zuerst
soll vom Benutzer abgefragt werden, welche Seitenlänge in Pixel das Quadrat
haben soll. Dann soll abgefragt werden, welche Farbe die Seiten haben sollen.
Mit diesen Angaben soll dann das Quadrat gezeichnet werden.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Import notwendiger Module
import ColabTurtlePlus.Turtle as turtle

# Benutzereingabe für die Größe und Farbe des Quadrats
seitenlaenge = int(input("Gib die Seitenlänge des Quadrats ein: "))
farbe = input("Gib die Farbe des Quadrats auf Englisch ein (z.B. red, blue, green, yellow): ")

# Erstellen eines Turtle-Objekts
turtle.clearscreen()
quadrat = turtle.Turtle()

# Zeichnen des Quadrats
quadrat.pencolor(farbe)
quadrat.forward(seitenlaenge)
quadrat.left(90)
quadrat.forward(seitenlaenge)
quadrat.left(90)
quadrat.forward(seitenlaenge)
quadrat.left(90)
quadrat.forward(seitenlaenge)
quadrat.left(90)
```
````

```{admonition} Übung 3.5
:class: miniexercise
Lassen Sie Turtle das Haus vom Nikolaus zeichnen. Das Haus vom Nikolaus sieht folgendermaßen aus:
```{figure} media/haus_nikolaus.svg
---
height: 150px
name: haus_nikolaus
---
Das Haus vom Nikolaus
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Import notwendiger Module
import ColabTurtlePlus.Turtle as turtle
from numpy import sqrt

seite = 100
diagonale = sqrt(100**2 + 100**2)

# Erstellen eines Turtle-Objekts
turtle.clearscreen()
t = turtle.Turtle()

# Zeichne das Haus
t.forward(seite)
t.left(135)
t.forward(diagonale)
t.right(135)
t.forward(seite)
t.left(135)
t.forward(0.5 * diagonale)
t.left(90)
t.forward(0.5 * diagonale)
t.left(45)
t.forward(seite)
t.left(135)
t.forward(diagonale)
t.right(135)
t.forward(seite)
```
````
