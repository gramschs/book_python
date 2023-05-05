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
:class: minisolution, toggle
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
:class: minisolution, toggle
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
<div class="ascii-art">
    *
   ***
  *****
 *******
*********
   |||
   |||
   |||
Der Tannenbaum ist insgesamt 8 Zeilen hoch.
</div>
```

````{admonition} Lösung
:class: minisolution, toggle
```python
def zeichne_tannenbaum(blaetterhoehe, stammhoehe):
    # Blätter zeichnen
    for i in range(blaetterhoehe):
        print(' ' * (blaetterhoehe - i - 1) + '*' * (2 * i + 1))
    # Stamm zeichnen
    for i in range(stammhoehe):
        print(' ' * (blaetterhoehe - 1 - 1)  + 3  * '|')

    # Gesamthöhe berechnen und zurückgeben
    gesamthoehe = blaetterhoehe + stammhoehe
    return gesamthoehe


# Test
L = zeichne_tannenbaum(5, 3)
print(f'Der Tannenbaum ist insgesamt {L} Zeilen hoch.')
```
````

```{admonition} Übung 6.4
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
:class: minisolution, toggle
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
    robo.goto(start + 50, 0)
    robo.left(45)
    
    # Rückkehr
    robo.penup()
    robo.goto(start,0)
    
    return 50


def zeichne_O(start, robo):
    robo.penup()
    robo.goto(start + 50, 0)
    robo.pendown()
    robo.circle(50,360)

    # Rückkehr
    robo.penup()
    robo.goto(start,0)
    
    return 100

def zeichne_T(start, robo):
    robo.penup()
    robo.goto(start + 50, 0)
    robo.left(90)
    robo.pendown()
    robo.forward(200)
    robo.penup()
    robo.goto(start + 0,200)
    robo.right(90)
    robo.pendown()
    robo.goto(start + 100,200)
    
    # Rückkehr
    robo.penup()
    robo.goto(start, 0)
    
    return 100
   
auswahl =  'ROT'

if auswahl == 'ROT':
    start_R = -100
    breite_R = zeichne_R(start_R, robo)
    start_O = start_R + breite_R + 10
    breite_O = zeichne_O(start_O, robo)
    start_T = start_O + breite_O + 10
    zeichne_T(start_T, robo)
else:
    start_T = -100
    breite_T = zeichne_T(start_T, robo)
    start_O = start_T + breite_T + 10
    breite_O = zeichne_O(start_O, robo)
    start_R = start_O + breite_O + 10
    zeichne_R(start_R, robo)
```
````

