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

```{admonition} Übung 6.1
:class: miniexercise
Schreiben Sie eine Funktion, die als Argument einen Integer $n$ übergeben
bekommt und danach n-mal das Wort `Hallo` ausdruckt. Testen Sie anschließend
Ihre Funktion.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Funktion
def schreibe_hallo(n):
    for i in range(n):
        print('Hallo')

# Test der Funktion
schreibe_hallo(7)
```
````

```{admonition} Übung 6.2
:class: miniexercise
Der Body-Maß-Index BMI wird berechnet nach der Formel 

$$\text{bmi} = \frac{m}{l^2},$$

wobei $m$ das Gewicht (Masse) in kg ist und $l$ die Körpergröße in m.

1. Schreiben Sie eine Funktion, die als Argument Gewicht und Körpergröße
entgegennimmt und den BMI zurückgibt. 
2. Schreiben Sie anschließend ein Hauptprogramm, das eine Benutzerin oder einen
Benutzer nach Gewicht und Körpergröße fragt. Dann wird der BMI mittels der
Funktion aus Schritt 1 berechnet und zuletzt wird ausgeben: 
* bei einem BMI < 18.5: Sie haben Untergewicht. Ihr BMI lautet: xx.
* bei einem BMI im Intervall [18.5, 25.0]: Sie haben Normalgewicht. Ihr BMI
  lautet: xx.
* bei einem BMI im Intervall [25.0, 30.0]: Sie haben Übergewicht. Ihr BMI
  lautet: xx.
* bei einem BMI > 30.0: Sie haben Adipositas. Ihr BMI lautet: xx.

xx steht dabei für den ausgerechneten BMI.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Funktion zur Berechnung des BMI
def berechne_bmi(gewicht, koerpergroesse):
    bmi = gewicht / koerpergroesse**2
    return bmi

### HAUPTPROGRAMM ###

# Eingabe
m = float(input('Bitte geben Sie Ihr Gewicht in kg an: '))
l = float(input('Bitte geben Sie Ihre Körpergröße in m an: '))

# Verarbeitung
bmi = berechne_bmi(m,l)

# Ausgabe
if bmi <= 18.5:
    print(f'Sie haben Untergewicht. Ihr BMI lautet {bmi :.1f}.')
elif bmi <= 25:
    print(f'Sie haben Normalgewicht. Ihr BMI lautet {bmi :.1f}.')
elif bmi <= 30:
    print(f'Sie haben Übergewicht. Ihr BMI lautet {bmi :.1f}.')
else:
    print('Sie haben Adipositas, bitte suchen Sie einen Arzt auf. Ihr BMI lautet {bmi :.1f}.', bmi)
```
````

```{admonition} Übung 6.3
:class: miniexercise
:class: miniexercise
Im Maschinenbau müssen Sie oft mit geometrischen Formen arbeiten. Erstellen Sie eine kleine Funktionsbibliothek zur Berechnung von Flächen und Volumen.

1. Schreiben Sie eine Funktion `kreisflaeche(radius)`, die die Fläche eines
   Kreises berechnet.
2. Schreiben Sie eine Funktion `zylindervolumen(radius, hoehe)`, die das Volumen
   eines Zylinders berechnet. Nutzen Sie dabei die erste Funktion!
3. Testen Sie beide Funktionen mit unterschiedlichen Werten.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
from numpy import pi

def kreisflaeche(radius):
    flaeche = pi * radius**2
    return flaeche

def zylindervolumen(radius, hoehe):
    grundflaeche = kreisflaeche(radius)
    volumen = grundflaeche * hoehe
    return volumen

# Test der Funktionen
r1 = 5
print(f"Ein Kreis mit Radius {r1} hat die Fläche: {kreisflaeche(r1):.2f} Flächeneinheiten")

r2 = 3
h2 = 7
print(f"Ein Zylinder mit Radius {r2} und Höhe {h2} hat das Volumen: {zylindervolumen(r2, h2):.2f} Volumeneinheiten")
```
````

```{admonition} Übung 6.4
:class: miniexercise
Im Ingenieurwesen müssen oft Temperaturwerte zwischen verschiedenen Einheiten
umgerechnet werden. Die gebräuchlichsten Einheiten sind Celsius (°C), Fahrenheit
(°F) und Kelvin (K).

Schreiben Sie drei Funktionen:

1. `celsius_zu_fahrenheit(celsius)`: Diese Funktion soll einen Temperaturwert in
   Celsius als Parameter erhalten und den entsprechenden Wert in Fahrenheit
   zurückgeben. Die Formel lautet: F = C · 1.8 + 32

2. `fahrenheit_zu_celsius(fahrenheit)`: Diese Funktion soll einen Temperaturwert
   in Fahrenheit als Parameter erhalten und den entsprechenden Wert in Celsius
   zurückgeben. Die Formel lautet: C = (F - 32) / 1.8

3. `celsius_zu_kelvin(celsius)`: Diese Funktion soll einen Temperaturwert in
   Celsius als Parameter erhalten und den entsprechenden Wert in Kelvin
   zurückgeben. Die Formel lautet: K = C + 273.15

Schreiben Sie außerdem ein Hauptprogramm, das:

1. Den Benutzer nach einem Temperaturwert in Celsius fragt.
2. Diesen Wert in Fahrenheit und Kelvin umrechnet.
3. Die umgerechneten Werte ausgibt.
4. Den Wert in Fahrenheit wieder zurück in Celsius umrechnet, um die Richtigkeit
   der Umrechnung zu überprüfen.

Erweitern Sie Ihr Programm um eine Benutzerschnittstelle, die dem Benutzer
ermöglicht, die gewünschte Umrechnungsrichtung auszuwählen (z.B. von Celsius
nach Fahrenheit oder von Fahrenheit nach Celsius).
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
def celsius_zu_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


def fahrenheit_zu_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius


def celsius_zu_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


### HAUPTPROGRAMM ###

print("Temperaturumrechner")
print("===================")
print("1: Celsius → Fahrenheit und Kelvin")
print("2: Fahrenheit → Celsius")
print("3: Kelvin → Celsius")

auswahl = int(input("\nBitte wählen Sie die gewünschte Umrechnung (1-3): "))

if auswahl == 1:
    # Celsius → Fahrenheit und Kelvin
    celsius = float(input("Bitte geben Sie die Temperatur in Celsius ein: "))
    
    # Umrechnung
    fahrenheit = celsius_zu_fahrenheit(celsius)
    kelvin = celsius_zu_kelvin(celsius)
    
    # Überprüfung durch Rückumrechnung
    celsius_pruefung = fahrenheit_zu_celsius(fahrenheit)
    
    # Ausgabe
    print(f"\nTemperaturumrechnung für {celsius:.2f} °C:")
    print(f"Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Kelvin: {kelvin:.2f} K")
    print(f"\nÜberprüfung: {fahrenheit:.2f} °F = {celsius_pruefung:.2f} °C")
    
    # Genauigkeitsüberprüfung mit Rundungsfehlertoleranz
    if abs(celsius - celsius_pruefung) < 0.001:
        print("Die Umrechnung ist korrekt!")
    else:
        print("Hinweis: Es gibt eine kleine Abweichung aufgrund von Rundungsfehlern.")
        
elif auswahl == 2:
    # Fahrenheit → Celsius
    fahrenheit = float(input("Bitte geben Sie die Temperatur in Fahrenheit ein: "))
    
    # Umrechnung
    celsius = fahrenheit_zu_celsius(fahrenheit)
    
    # Ausgabe
    print(f"\n{fahrenheit:.2f} °F entspricht {celsius:.2f} °C")
    
elif auswahl == 3:
    # Kelvin → Celsius
    kelvin = float(input("Bitte geben Sie die Temperatur in Kelvin ein: "))
    
    # Umrechnung (Kelvin zu Celsius ist einfach K - 273.15)
    celsius = kelvin - 273.15
    
    # Ausgabe
    print(f"\n{kelvin:.2f} K entspricht {celsius:.2f} °C")
    
else:
    print("Fehler: Ungültige Auswahl. Bitte wählen Sie 1, 2 oder 3.")
```
````

````{admonition} Übung 6.5
:class: miniexercise
Lassen Sie einen Tannenbaum als sogenannte ASCII-Art zeichnen. Damit ist
gemeint, dass ein Bild durch Zeichen dargestellt wird. In diesem Fall sollen die
Blätter durch den Stern `*` dargestellt werden und der Stamm durch drei
vertikale Striche `|||`. Das Zeichnen des Tannenbaums soll als Funktion
implementiert werden, wobei die Höhe der Blätter und die Höhe des Stammes als
Argumente übergeben werden sollen. Die Funktion soll die Gesamthöhe des
Tannenbaums zurückgeben.

Testen Sie Ihre Funktion. Lassen Sie einen Tannenbaum mit Blätterhöhe 5 und
einer Stammhöhe von 3 zeichnen. Darüber hinaus soll ausgegeben werden, wie hoch
der Tannenbaum insgesamt ist. Beispielhaft könnte Ihr Test folgende Ausgabe
produzieren:
```
    *
   ***
  *****
 *******
*********
   |||
   |||
   |||

Der Tannenbaum ist insgesamt 8 Zeilen hoch.
```
````

````{admonition} Lösung
:class: miniexercise, toggle
```python
def zeichne_tannenbaum(blaetterhoehe, stammhoehe):
    # Blätter zeichnen
    for i in range(blaetterhoehe):
        print(' ' * (blaetterhoehe - i - 1) + '*' * (2 * i + 1))
    # Stamm zeichnen
    for i in range(stammhoehe):
        print(' ' * (blaetterhoehe - 2) + 3 * '|')

    # Gesamthöhe berechnen und zurückgeben
    gesamthoehe = blaetterhoehe + stammhoehe
    return gesamthoehe


# Test
L = zeichne_tannenbaum(5, 3)
print(f'Der Tannenbaum ist insgesamt {L} Zeilen hoch.')
```
````

```{admonition} Übung 6.6
:class: miniexercise
Schreiben Sie drei Funktionen. Die erste soll mit Hilfe des Turtle-Moduls den
Buchstaben `R` zeichnen, die zweite den Buchstaben `O` und die dritte den
Buchstaben `T`. 

Dabei sollen die Funktionen die folgenden Bedingungen erfüllen:

1. Jeder Buchstabe soll in einem rechteckigen Rahmen sein, bei dem die untere
   linke Ecke auf der Position $(start, 0)$ beginnt. Dabei wird `start` der
   Funktion als Argument übergeben. Der Rahmen muss aber nicht gezeichnet
   werden.
2. Jede Funktion soll auch zurückgeben, wie breit der "gedachte" Rahmen ist.
3. Innerhalb jeder Funktion soll am Ende der Roboter auf die linke untere Ecke
   zurückkehren und it seiner Nase in Richtung Osten zeigen.

Testen Sie Ihre Funktion. Lassen Sie zuerst das Wort `ROT` schreiben. 
Probieren Sie auch `TOR` aus.

Tipp: Für R und O dürfen Sie gerne die `circle`-Methode verwenden, siehe
[Dokumentation
ColabTurtlePlus](https://larryriddle.agnesscott.org/ColabTurtlePlus/documentation2.html).
Auch `penup`, `pendown` und `goto` könnten hilfreich sein.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
import ColabTurtlePlus.Turtle as turtle
turtle.clearscreen()

robo = turtle.Turtle()
robo.speed(13)

def zeichne_R(start, robo):
    robo.penup()
    robo.goto(start, 0)
    robo.pendown()
    robo.left(90)
    robo.forward(200)
    robo.right(90)
    robo.circle(-50, 180)
    robo.left(135)
    robo.forward(100)  # Direkte Linie für das Bein von R
    
    # Rückkehr zur Startposition und Ausrichtung nach Osten
    robo.penup()
    robo.goto(start, 0)
    robo.setheading(0)
    
    return 100  # Breite des R mit etwas Abstand


def zeichne_O(start, robo):
    robo.penup()
    robo.goto(start + 50, 0)  # Startposition für den Kreis
    robo.setheading(0)  # Sicherstellen, dass der Roboter nach Osten zeigt
    robo.pendown()
    robo.circle(50, 360)

    # Rückkehr zur Startposition und Ausrichtung nach Osten
    robo.penup()
    robo.goto(start, 0)
    robo.setheading(0)
    
    return 100  # Breite des O


def zeichne_T(start, robo):
    # Zeichne den vertikalen Strich des T
    robo.penup()
    robo.goto(start + 50, 0)  # Mittelposition für den vertikalen Strich
    robo.setheading(90)  # Nach oben ausrichten
    robo.pendown()
    robo.forward(200)
    
    # Zeichne den horizontalen Strich des T
    robo.penup()
    robo.goto(start, 200)  # Linke Position für den horizontalen Strich
    robo.setheading(0)  # Nach rechts ausrichten
    robo.pendown()
    robo.forward(100)  # Zeichne den horizontalen Strich
    
    # Rückkehr zur Startposition und Ausrichtung nach Osten
    robo.penup()
    robo.goto(start, 0)
    robo.setheading(0)
    
    return 100  # Breite des T


# Test der Funktionen
auswahl = 'ROT'  # Kann zu 'TOR' geändert werden für den anderen Test

if auswahl == 'ROT':
    start_R = -150  # Etwas weiter links beginnen für bessere Sichtbarkeit
    breite_R = zeichne_R(start_R, robo)
    
    start_O = start_R + breite_R + 10  # 10 Pixel Abstand zwischen den Buchstaben
    breite_O = zeichne_O(start_O, robo)
    
    start_T = start_O + breite_O + 10
    zeichne_T(start_T, robo)
else:
    start_T = -150
    breite_T = zeichne_T(start_T, robo)
    
    start_O = start_T + breite_T + 10
    breite_O = zeichne_O(start_O, robo)
    
    start_R = start_O + breite_O + 10
    zeichne_R(start_R, robo)
```
````
