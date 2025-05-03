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

```{admonition} Übung 4.1
:class: miniexercise
Schreiben Sie ein Programm, das den folgenden Text ausgibt:

Januar ist der 1. Monat im Jahr. <br>
Februar ist der 2. Monat im Jahr. <br>
...<br>

Verwenden Sie dazu eine Liste der Monate und eine for-Schleife.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
monate = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 
'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']

for i in range(12):
    monat = monate[i]
    print(f'{monat} ist der {i+1}. Monat im Jahr.')
```
````

```{admonition} Übung 4.2
:class: miniexercise
Verwenden Sie das Turtle-Modul, um ein Quadrat zu zeichnen. Verwenden Sie dabei eine for-Schleife.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
import ColabTurtlePlus.Turtle as turtle

turtle.clearscreen()

for i in range(4):
    turtle.forward(100)
    turtle.right(90)
```
````

```{admonition} Übung 4.3
:class: miniexercise
Verwenden Sie das Turtle-Modul und eine for-Schleife, um ein n-Eck zeichnen zu lassen. Dabei soll die Anzahl der Seiten zuvor vom Benutzer abgefragt werden. Testen Sie anschließend ein Dreieck und ein Siebeneck.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
import ColabTurtlePlus.Turtle as turtle

turtle.clearscreen()

anzahl_seiten = int(input('Bitte geben Sie die Anzahl der Seiten des n-Ecks ein: '))

for i in range(anzahl_seiten):
    turtle.forward(30)
    turtle.right(360 / anzahl_seiten)
```
````

```{admonition} Übung 4.4
:class: miniexercise
Schreiben Sie ein Programm, das den Benutzer nach 5 Zahlen fragt und diese in einer Liste speichert. Anschließend soll das Programm die Summe der Zahlen in der Liste mithilfe einer for-Schleife berechnen und ausgeben.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
# Initalisierung der leeren Liste
zahlen = []

# Eingabe der 5 Zahlen durch einen Benutzer
for i in range(5):
    zahl = int(input("Bitte geben Sie eine Zahl ein: "))
    zahlen.append(zahl)

# Verarbeitung: Berechnung der Summe
summe = 0
for zahl in zahlen:
    summe = summe + zahl

# Ausgabe
print(f'Die Summe der Zahlen ist: {summe}.')
```
````

```{admonition} Übung 4.5
:class: miniexercise
In der Mathematik gibt es die Schreibweise

$$n! = n \cdot (n-1) \cdot ... \cdot 2 \cdot 1$$

So wird zum Beispiel $5!$ durch $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$ berechnet. Dies wird in der Mathematik als Fakultät von 5 bezeichnet.

Schreiben Sie ein Programm, das vom Benutzer die Zahl n abfragt, für die die Fakultät $n!$ berechnet werden soll. Das Programm soll dann die Fakultät berechnen und am Ende den Text

Die Fakultät von XX ist XX, also XX! = XX.

ausgeben. Dabei soll XX durch die korrekten Zahlen ersetzt werden. Beispiel

Die Fakultät von 5 ist 120, also 5! = 120.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe des Benutzers
n = int(input('Bitte gegen Sie die Zahl n ein, zu der die Fakultät berechnet werden soll: '))

# Verarbeitung
ergebnis = 1
for i in range(n, 1, -1):
    ergebnis = ergebnis * i

# Ausgabe
print(f'Die Fakultät von {n} ist {ergebnis}, also {n}! = {ergebnis}.') 
```
````

```{admonition} Übung 4.6
:class: miniexercise
Eine Firma stellt Schrauben her, deren Länge im Mittel 50 mm beträgt. Aufgrund
von Fertigungstoleranzen sind die Längen normalverteilt mit einer
Standardabweichung von 0.4 mm.

1. Erzeugen Sie zufällig die Längen von 1000 Schrauben.
2. Schreiben Sie Python-Code, um den Mittelwert dieser 1000 Schrauben zu
   berechnen. Lassen Sie ihn auf 2 Nachkommastellen genau ausgeben.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
import numpy as np

# Simulation von 1000 Schrauben
mittelwert = 50.0
stdabw = 0.4
anzahl = 1000

laengen = np.random.normal(mittelwert, stdabw, anzahl)

# Berechnung des Mittelwerts mit for-Schleife
summe = 0
for laenge in laengen:
    summe += laenge

mittelwert = summe / anzahl
print(f"Berechneter Mittelwert der Schrauben-Längen: {mittelwert:.2f} mm")
```
````
