# Übungen zur Wiederholung

```{admonition} Übung
:class: miniexercise
Ordnen Sie ein: welche der beiden Programmiersprachen MATLAB oder Python ist
eine Interpreter-Sprache und welche eine Compiler-Sprache? Welche Vor- und Nachteile haben Interpreter-Sprachen?

Recherchieren Sie im Internet: Was ist Cython und was ist der MATLAB Coder?
```

```{admonition} Lösung
:class: miniexercise, toggle
Sowohl MATLAB als auch Python sind beides Interpreter-Sprachen. Sie werden in Echtzeit ausgeführt, anstatt vorab in Maschinencode kompiliert zu werden, wie es bei Compiler-Sprachen der Fall ist.

Vorteile von Interpreter-Sprachen sind:

* **Leichtere Fehlersuche:** Da der Interpreter den Code Zeile für Zeile ausführt, erkennt man leichter, in welcher Zeile der Fehler auftritt.

* **Plattformunabhängigkeit:** Interpreter-Sprachen sind oft plattformübergreifend, was bedeutet, dass sie auf verschiedenen Betriebssystemen ausgeführt werden können, ohne dass der Code geändert werden muss.


Nachteile von Interpreter-Sprachen sind:

* **Geschwindigkeit:** Interpreter-Sprachen sind in der Regel langsamer als kompilierte Sprachen, da der Code zur Laufzeit und nicht vorab übersetzt wird.

* **Schutz des Quellcodes:** Bei Interpreter-Sprachen ist es einfacher, den Quellcode zu lesen und zu verstehen, was bedeutet, dass er weniger geschützt ist als bei kompilierten Sprachen.

Was Cython und MATLAB Coder betrifft:

**Cython** ist eine Erweiterung von Python, die zusätzlich C-Datentypen unterstützt. Mit Cython können Python-Entwickler Python-Code in die Compiler-Sprachen C oder C++ übersetzen und kompilieren, um die Ausführungszeit zu verkürzen.

**MATLAB Coder** ist ein MATLAB-Tool, das MATLAB-Code in C oder C++ Code umwandelt. Dies kann verwendet werden, um den MATLAB-Code auf Plattformen auszuführen, die MATLAB nicht unterstützen, oder um die Geschwindigkeit der Ausführung zu verbessern, indem der Code vorab kompiliert wird.
```

````{admonition} Übung
:class: miniexercise
Was gibt der folgende Code aus? Lesen Sie das Programm und versuchen Sie nur durch Nachdenken die Ausgabe des Programms auf Papier zu schreiben.

```python
def meine_funktion(n):
    a = 0
    b = 1
    meine_liste = [a, b]
    for i in range(n-2):
        c = a + b
        meine_liste.append(c)
        a = b
        b = c
    return meine_liste

zahlen = meine_funktion(8)
print(zahlen)
```
````

```{admonition} Lösung
:class: miniexercise, toggle
Das Python-Programm gibt 

[0, 1, 1, 2, 3, 5, 8, 13]

aus. Das ist übrigens die sogenannte [Fibonacci-Folge](https://de.wikipedia.org/wiki/Fibonacci-Folge).
```

```{admonition} Übung
:class: miniexercise
Schreiben Sie ein **Python**-Programm, das das Spiel ["Schere - Stein - Papier"](https://de.wikipedia.org/wiki/Schere,_Stein,_Papier) umsetzt.

Die Spielregeln sind wie folgt:

Der Computer fragt den wählt zufällig einen Gegenstand aus (ohne ihn auszugeben)
und fragt den Spieler nach seiner Wahl. Schere gewinnt gegen Papier, Papier
gewinnt gegen Stein und Stein gewinnt gegen Schere. Der Sieg bringt dem
jeweiligen Spieler einen Punkt. Haben beide den gleichen Gegenstand gewählt,
zählt das als unentschieden, also 0 Punkte. Lassen Sie Spieler und Computer
solange gegeneinander spielen, bis einer von beiden 3 Punkte erreicht hat.

Wünschenswert sind auch Ausgaben wie z.B. der aktuelle Spielstand oder am Ende die Gratulation an den Sieger.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
from numpy.random import randint 

gegenstaende = ['Schere', 'Stein', 'Papier']

punkte_computer = 0
punkte_spieler  = 0

while True:
    # Wahl des Computers
    zufallsindex = randint(0,3)
    computerwahl = gegenstaende[zufallsindex]

    # Wahl des Spielers
    spielerwahl  = input('Was wählen Sie? Schere, Stein oder Papier?')
    while spielerwahl not in gegenstaende:
        print(f'Sie haben {spielerwahl} gewählt, was nicht in der Liste ist. Achten Sie auf die korrekte Schreibweise.')
        spielerwahl  = input('Was wählen Sie? Schere, Stein oder Papier?')
    
    # Vergleich, wer gewonnen hat
    if computerwahl == 'Schere':
        if spielerwahl == 'Schere':
            print('Unentschieden')
        elif spielerwahl == 'Stein':
            print('Stein schleift Schere, der Spieler hat gewonnen.')
            punkte_spieler = punkte_spieler + 1
        else:
            print('Schere schneidet Papier, der Computer hat gewonnen.')
            punkte_computer = punkte_computer + 1
    elif computerwahl == 'Stein':
        if spielerwahl == 'Schere':
            print('Stein schleift Schere, der Computer hat gewonnen.')
            punkte_computer = punkte_computer + 1
        elif spielerwahl == 'Stein':
            print('Unentschieden.')
        else:
            print('Papier umwickelt Stein, der Spieler hat gewonnen.')
            punkte_spieler = punkte_spieler + 1
    else:
        if spielerwahl == 'Schere':
            print('Schere schneidet Papier, der Spieler hat gewonnen.')
            punkte_spieler = punkte_spieler + 1
        elif spielerwahl == 'Stein':
            print('Papier umwickelt Stein, der Computer hat gewonnen.')
            punkte_computer = punkte_computer + 1
        else:
            print('Unentschieden.')

    # Ausgabe des aktuellen Spielstandes
    print(f'### Spielstand {punkte_spieler} : {punkte_computer} (Spieler : Computer) ###')

    # Abbruch der Schleife, wenn Computer oder Spieler 3 Punkte erreicht hat
    if punkte_computer == 3 or punkte_spieler == 3:
        break

# Gratulation
if punkte_spieler == 3:
    print('Herzlichen Glückwunsch, Sie haben gewonnnen.')
else:
    print('Leider hat der Computer gewonnen.')
```
````

````{admonition} Übung
:class: miniexercise
Suchen Sie in dem folgenden Code die Fehler durch Nachdenken. Korrigieren Sie anschließend das Programm in Python.

```python
def berechne_wurzel(x):
    ergebnis = sqrt(x)
    return ergebnis

x = input('Geben Sie eine Zahl ein: ')

print(f'Die Wurzel der Zahl ist {x}.')
```
````

````{admonition} Lösung
:class: miniexercise, toggle
1. Die Funktion `sqrt()` existiert nicht im Python-Standard, sondern muss zuerst
   durch ein Modul wie beispielsweise Math oder NumPy importiert werden. 
2. Die Wurzel existiert nur für nicht-negative Zahlen. Es sollte also vorab
   überprüft werden, ob der Benutzer eine nicht-negative Zahl eingegeben hat.
3. Die input()-Funktion gibt einen String zurück, der in einer Zahl konvertiert
   werden muss.
4. Die print()-Anweisung gibt nicht die Wurzel aus, sondern die eingebene Zahl.

Das korrigierte Programm könnte folgendermaßen aussehen:
```python
from numpy import sqrt

def berechne_wurzel(x):
    ergebnis = sqrt(x)
    return ergebnis

x = float(input('Geben Sie eine Zahl ein: '))
while x < 0:
    x = float(input('Die Zahl muss nicht-negativ sein. Geben Sie eine Zahl ein: '))
y = berechne_wurzel(x)

print(f'Die Wurzel der Zahl ist {y}.')
```
````

```{admonition} Übung
:class: miniexercise
1. Laden Sie die Kursdaten des DAX aus dem Jahr 2022 herunter (→ hier [Download](https://nextcloud.frankfurt-university.de/s/5qNaNjb945p2mk3),
   Quelle: [https://www.boerse-frankfurt.de](https://www.boerse-frankfurt.de/index/DAX/kurshistorie/historische-kurse-und-umsaetze). 
2. Importieren Sie die Tabelle. Überspringen Sie dazu die erste Zeile.
3. Verschaffen Sie sich einen Überblick. 
    * Wie viele Datensätze sind in der Tabelle enthalten?
    * Gibt es leere Zellen?
    * Was steht in den einzelnen Spalten?
    * Was ist das höchste Tageshoch, das 2022 erreicht wurde?
    * Wie viele Tage sind in der Tabelle enthalten? Speichern Sie diese Zahl in
      der Variablen `anzahl_tage`? Warum sind es eigentlich nicht 365 Tage?
4. Visualisieren Sie den Kurs zum Börsenschluss `Schluss`. Lassen Sie dazu auf
   der x-Achse die Tage von 1 bis `anzahl_tage` laufen.
5. Lassen Sie eine Regressionsgerade durch den Kursstand zum Börsenschluss
   berechnen.
6. Visualisieren Sie den Börsenkurs zusammen mit der Regressionsgeraden.
7. Was prognostiziert das Regressionsmodell für Mitte 2023? Tipp: Sie können mit
   251 Werktagen für das gesamte Jahr rechnen, siehe https://www.ferienwiki.de/tools/werktagerechner
```

````{admonition} Lösung
:class: miniexercise, toggle
Import und Übersicht:
```python
import pandas as pd
data = pd.read_csv('dax2022.csv', skiprows=1)
data.info()
```
Es sind 257 Datensätze, alle Zellen sind gefüllt. Es gibt die Spalten Datum, Eröffnung, Schluss, Tageshoch, Tagestief und Umsatz in EUR. Die statistischen Kennzahlen ermitteln wir mit `.describe()`.
```python
data.describe()
```
Das höchste Tageshoch waren 16285.35 EUR.

In der Tabelle sind 257 Tage enthalten, weil die Börse nur an Werktagen geöffnet hat.
```python
anzahl_tage = data.loc[:, 'Datum'].count()
print(anzahl_tage)
```
Visualisierung als Liniendiagramm
```python
import matplotlib.pyplot as plt

x = range(1, anzahl_tage+1)
y = data.loc[:, 'Schluss'] 

plt.figure()
plt.plot(x,y)
plt.xlabel('Tag')
plt.ylabel('Schluss')
plt.title('DAX 2022');
```

Das Regressionsmodell prognostiziert für Mitte 2023 einen DAX-Wert von 12031.61 EUR.

```python
import numpy as np

# Regressionsgerade
koeffizienten = np.polyfit(x,y, 1)

# Visualisierung
x_modell = np.linspace(1, anzahl_tage, 100)
y_modell = np.polyval(koeffizienten, x_modell)

plt.figure()
plt.plot(x,y)
plt.plot(x_modell, y_modell, color='red')
plt.xlabel('Tag')
plt.ylabel('Schluss')
plt.title('DAX 2022');

# Prognose für Mitte 2023 
x_prognose = 257 + 251/2 
y_prognose = np.polyval(koeffizienten, x_prognose)

print(f'Prognose DAX Mitte 2023: {y_prognose:.2f}')
```
````
