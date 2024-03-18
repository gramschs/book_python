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

```{admonition} Übung 7.1
:class: miniexercise
Schreiben Sie ein Programm, das einen Benutzer oder eine Benutzerin auffordert,
das Passwort einzugeben. Drei Versuche sind möglich. Bei dreimaliger
Falscheingabe soll das Programm abgebrochen werden.
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
versuche = 0
passwort = 'F6vfGV+vT6#>hZyu4c=z+?<8'

while versuche < 3:
    eingabe = input('Bitte geben Sie das Passwort ein: ')
    if eingabe == passwort:
        print('Das richtige Passwort wurde eingegeben. Zugriff gewährt.')
        break
    versuche += 1
```
````

```{admonition} Übung 7.2
:class: miniexercise
Schreiben Sie einen 1x1-Trainer. Gehen Sie dabei wie folgt vor:
1. Schreiben Sie eine *Funktion*, die eine 1x1-Aufgabe stellt (zum Beispiel:
   Wieviel ist 3 x 5?). Die Funktion soll überprüfen, ob die eingegebene Antwort
   korrekt ist. Bei einer falschen Antowrt soll das richtige Ergebnis ausgegeben
   werden.
2. Im Hauptprogramm soll der Benuzter gefragt werden, wie viele 1x1-Aufgaben
   trainiert werden sollen. Danach sollen entsprechend viele aufgaben gestellt
   werden. Am Ende soll das Hauptprogramm dem Benuzter mitteilen, wieviel
   Prozent der Aufgaben korrekt gelöst wurden.
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
import numpy as np

def stelle_aufgabe():
    zahl01 = np.random.randint(1, 11)
    zahl02 = np.random.randint(1, 11)
    antwort = int(input(f'Wieviel ist {zahl01} x {zahl02}? '))
    if antwort == zahl01 * zahl02:
        return True
    else:
        print(f'Leider falsch, das richtige Ergebnis wäre {zahl01 * zahl02} gewesen.')
        return False
    
anzahl_aufgaben = int(input('Wie viele Aufgaben sollen gestellt werden?'))
anzahl_richtige_antworten = 0
for i in range(anzahl_aufgaben):
    ist_richtig = stelle_aufgabe()
    if ist_richtig:
        anzahl_richtige_antworten += 1

prozent_richtige_antworten = anzahl_richtige_antworten / anzahl_aufgaben * 100
print(f'Sie haben {prozent_richtige_antworten:.1f} % der Aufgaben richtig gelöst.')
```
````

```{admonition} Übung 7.3
:class: miniexercise
Schreiben Sie das Spiel "Zahlenraten". Der Computer denkt sich eine Zahl
zwischen 1 und 100 aus. Dann fragt er Sie solange, welche Zahl er sich
ausgedacht hat, bis Sie die korrekte Zahl geraten haben. Außerdem gibt er Ihnen
Hinweise, z.B. "Meine gedachte Zahl ist kleiner." oder "Meine gedachte Zahl ist
größer." Sobald Sie die Zahl geraten haben, gibt der Computer aus, wie viele
Versuche Sie gebraucht haben und beendet das Spiel.
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
import numpy as np

zufallszahl = np.random.randint(1, 101)

versuche = 0
print('Ich habe mir eine Zahl zwischen 1 und 100 gedacht. Raten Sie, welche es ist!')
while True:
    versuche += 1
    antwort = int(input('Raten Sie meine Zahl: '))
    if antwort < zufallszahl:
        print('Meine gedachte Zahl ist größer.')
    elif antwort == zufallszahl:
        print(f'Hurra, Sie haben meine Zahl {zufallszahl} geraten und dazu {versuche} Versuche gebraucht.')
        break
    else:
        print('Meine gedachte Zahl ist kleiner.')
```
````

```{admonition} Übung 7.4
:class: miniexercise
Programmieren Sie einen Random Walk. Ein Random Walk ist eine zufällige
Irrfahrt. Der Turtle-Roboter soll zufällig eine Richtung bestimmen (0, 90, 180
oder 270 Grad) und 20 Schritte in diese Richtung gehen. Danach wird eine neue
Richtung zufällig bestimmt und der Roboter bewegt sich erneut 20 Schritte. 

Lassen Sie abfragen, wie viele Male diese Prozedur wiederholt werden soll.
Testen Sie beispielsweise 100 mal. Verlässt der Roboter dabei das Turtle-Feld?
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
import ColabTurtlePlus.Turtle as turtle
import numpy as np

turtle.clearscreen()

robo = turtle.Turtle()
robo.speed(13)

anzahl_wiederholungen = int(input('Wie oft soll der Roboter 20 Schritte laufen?'))

for i in range(anzahl_wiederholungen):
    zufallswinkel = np.random.randint(3) * 90
    robo.left(zufallswinkel)
    robo.forward(20)
```
````
