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

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

1. Schreiben Sie ein Programm, das den Benutzer nach seinem Namen und seinem Alter fragt und dann eine Begrüßungsnachricht ausgibt, die den Namen und das Alter des Benutzers enthält. Verwenden Sie eine f-String, um den Namen und das Alter des Benutzers in die Begrüßungsnachricht einzufügen.

2. Schreiben Sie ein Programm, das den Benutzer nach seiner E-Mail-Adresse fragt und dann eine Bestätigungsmeldung ausgibt, die die E-Mail-Adresse des Benutzers enthält. Verwenden Sie eine f-String, um die E-Mail-Adresse des Benutzers in die Bestätigungsmeldung einzufügen.
   
3. Schreiben Sie ein Programm, das den Benutzer nach zwei Zahlen fragt und dann die Summe, das Produkt und den Quotienten dieser Zahlen ausgibt. Verwenden Sie eine f-String, um die Zahlen und die Ergebnisse in die Ausgabe einzufügen.
 
4. Schreiben Sie ein Programm, das eine Liste von Namen enthält und dann eine Nachricht ausgibt, die jeden Namen in der Liste einzeln begrüßt. Verwenden Sie eine Schleife und eine f-String, um die Nachricht für jeden Namen in der Liste zu erstellen.

5. Schreiben Sie ein Programm, das eine Zeichenkette enthält und dann eine Nachricht ausgibt, die angibt, wie viele Vorkommen eines bestimmten Buchstabens in der Zeichenkette vorhanden sind. Verwenden Sie eine f-String, um den Buchstaben und die Anzahl der Vorkommen in die Nachricht einzufügen.

Aufgabe 1: Schreiben Sie ein Programm, das eine Liste von Zahlen von 1 bis 5 enthält und diese Zahlen nacheinander mit Hilfe einer for-Schleife ausgibt.

```python
zahlen = [1, 2, 3, 4, 5]

for zahl in zahlen:
    print(zahl)

```

Aufgabe 2: Schreiben Sie ein Programm, das den Benutzer nach 3 Namen fragt und diese in einer Liste speichert. Anschließend soll das Programm die Namen in der Liste mithilfe einer for-Schleife ausgeben.

```python
namen = []

for i in range(3):
    name = input("Bitte geben Sie einen Namen ein: ")
    namen.append(name)

for name in namen:
    print(name)
```

Aufgabe 3: Schreiben Sie ein Programm, das den Benutzer nach 5 Zahlen fragt und diese in einer Liste speichert. Anschließend soll das Programm die Summe der Zahlen in der Liste mithilfe einer for-Schleife berechnen und ausgeben.

```python
zahlen = []

for i in range(5):
    zahl = int(input("Bitte geben Sie eine Zahl ein: "))
    zahlen.append(zahl)

summe = 0
for zahl in zahlen:
    summe += zahl

print("Die Summe der Zahlen ist:", summe)
```

Aufgabe 4: Schreiben Sie ein Programm, das den Benutzer nach einer beliebigen Anzahl von Namen fragt (der Benutzer gibt zuerst die Anzahl der Namen ein) und diese in einer Liste speichert. Anschließend soll das Programm jeden Namen in Großbuchstaben mithilfe einer for-Schleife ausgeben.

```python
anzahl_namen = int(input("Wie viele Namen möchten Sie eingeben? "))

namen = []
for i in range(anzahl_namen):
    name = input("Bitte geben Sie einen Namen ein: ")
    namen.append(name)

for name in namen:
    print(name.upper())
```

Aufgabe 5: Schreiben Sie ein Programm, das den Benutzer nach einer beliebigen Anzahl von Ganzzahlen fragt (der Benutzer gibt zuerst die Anzahl der Zahlen ein) und diese in einer Liste speichert. Anschließend soll das Programm die geraden Zahlen in der Liste mithilfe einer for-Schleife ausgeben.

```python
anzahl_zahlen = int(input("Wie viele Zahlen möchten Sie eingeben? "))

zahlen = []
for i in range(anzahl_zahlen):
    zahl = int(input("Bitte geben Sie eine Zahl ein: "))
    zahlen.append(zahl)

print("Die geraden Zahlen sind:")
for zahl in zahlen:
    if zahl % 2 == 0:
        print(zahl)
```

Aufgabe 1: Verwenden Sie das Turtle-Modul, um ein Quadrat zu zeichnen. Verwenden Sie dabei eine for-Schleife.

```python
import turtle

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.done()
```

Aufgabe 2: Verwenden Sie das Turtle-Modul und eine for-Schleife, um ein Polygon mit einer vom Benutzer eingegebenen Anzahl von Seiten zu zeichnen.

```python
import turtle

seiten = int(input("Bitte geben Sie die Anzahl der Seiten des Polygons ein: "))

for i in range(seiten):
    turtle.forward(100)
    turtle.right(360 / seiten)

turtle.done()
```

Aufgabe 3: Verwenden Sie das Turtle-Modul und eine for-Schleife, um 5 gleichmäßig verteilte Kreise zu zeichnen, die einen gemeinsamen Mittelpunkt haben (ein Blumenmuster).

```python
import turtle

for i in range(5):
    turtle.circle(50)
    turtle.right(360 / 5)

turtle.done()
```

Aufgabe 4: Verwenden Sie das Turtle-Modul und zwei verschachtelte for-Schleifen, um ein Gittermuster aus Quadraten zu zeichnen. Das Gitter soll aus 3x3 Quadraten bestehen, wobei jedes Quadrat eine Seitenlänge von 50 Pixeln hat.

```python
import turtle

for i in range(3):
    for j in range(3):
        for k in range(4):
            turtle.forward(50)
            turtle.right(90)
        turtle.forward(50)
    turtle.right(180)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)

turtle.done()
```

Aufgabe 5: Verwenden Sie das Turtle-Modul und eine for-Schleife, um eine Spirale zu zeichnen. Die Spirale soll aus Linien bestehen, die in regelmäßigen Abständen um 90 Grad gedreht sind. Die Länge der Linien soll bei jedem Schritt um 10 Pixel zunehmen.

```python
import turtle

schritte = 20
laenge = 10

for i in range(schritte):
    turtle.forward(laenge)
    turtle.right(90)
    laenge += 10

turtle.done()
```

