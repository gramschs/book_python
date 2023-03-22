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

# 6.1 Funktionen selbst schreiben

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

Eine Funktion ist eine Zusammenfassung von python, der eine bestimmte Teilaufgabe
löst. Dabei arbeitet die Funktion nach dem EVA-Prinzip. Die Funktion übernimmt
Objekte als Eingabe, verarbeitet diese und liefert Objekte als Ergebnis zurück.
Wie die Funktion dabei im Inneren genau funktioniert (Verarbeitung), ist
unwichtig.

Beispielsweise gibt es im Modul `math` die Funktion `sqrt()`. Wir wissen, dass
wir der Funktion eine Zahl übergeben müssen (Eingabe), z.B. `sqrt(5)`. Die
Funktion liefert dann als Ergebnis $\sqrt{5}$ zurück. Welches Verfahren zur
Berechnung der Wurzel verwendet wurde, wissen wir nicht. 

Insbesondere muss die Teilaufgabe, die die Funktion löst, nichts mit Mathematik
zu tun haben. Eine Funktion in der Informatik hat nichts mit einer
mathematischen Funktion zu tun, auch wenn oft mathematische Funktionen als
Beispiel verwendet werden. Ein Beispiel für eine nicht-mathematische Funktion
haben Sie mit `print()` bereits kennengelernt.


## Die Benutzung von Funktionen (oder der Aufruf von Funktionen)

Der Aufruf einer Funktion hat folgende Syntax:

```python
funktion( argument1, argument2, ...)
```

Eine Funktion wird benutzt, indem man den Namen der Funktion hinschreibt und
dann in runden Klammern ihre Parameter, die sogenannten Argumente der Funktion.
Welche Argumente für eine Funktion verwendet werden dürfen, hängt von der
Implementierung der Funktion ab.

Beispielsweise kann als Argument für die `len()`-Funktion ein String übergeben
werden oder eine Liste. Stellen Sie eine Vermutung auf: was bewirkt die
`len()`-Funktion?

```python
len('Hallo')
```

```python
len([1,2,3,4,8,2])
```

In der Regel geben Funktionen wieder Ergebnisse zurück. Diese können einer
Variable zugewiesen werden, um mit dem Ergebnis weiter zu arbeiten.

```python
laenge1 = len('Hallo')
laenge2 = len(['Apfel', 'Banane', 'Erdbeere'])

if laenge1 < laenge2:
    print('Das Wort Hallo enthält weniger Buchstaben als Früchte im Obstsalat.')
else:
    print('Das Wort Hallo enthält mehr Buchstaben als Einträge in der Liste.')
```


## Definition von einfachen Funktionen

Die allgemeine Syntax zur Definition einer eigenen Funktion sieht wie folgt aus:

```python
def meine_funktion():
    """Optionaler Docstring zur Erklärung."""

    # Implementierung der Funktion
    anweisung01
    anweisung02
     ...

```

Erstes Beispiel:

Die folgende Funktion hat keine Eingabewert (Argumente, Input) und keine
Rückgabe (Ausgabe, Return-Value).



```python
def gruesse_ausrichten():
    print('Ich grüße Sie!')
```

Nachdem die Funktion `gruesse_ausrichten()`so implementiert wurde, können wir
sie im Folgenden direkt verwenden.

```python
gruesse_ausrichten()
```

Und natürlich kann man sie in Programmverzweigungen und Schleifen einbauen.

```python
for i in range(7):
    gruesse_ausrichten()
```

```python
soll_gegruesst_werden = input('Soll gegrüßt werden (j/n)? ')

if soll_gegruesst_werden == 'j':
    gruesse_ausrichten()
else:
    print('Auf Wiedersehen!')
```

## Video zu Funktionen

Schauen Sie sich auf YouTube das Video "Python Tutorial deutsch [18/24]" an (ca.
7:36 min), siehe
https://www.youtube.com/watch?v=LQCfN5HS9xI&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=18.
Stoppen Sie regelmäßig und probieren Sie die dort gezeigten Beispiele in der
folgenden python-Zelle aus: 

```python

```


## Definition von Funktionen mit Parametern

Meistens haben Funktionen Argumente, um Eingaben/Input entgegennehmen und
verarbeiten zu können. Das Argument wird bei der Implementierung der Funktion
mit einem Platzhalter/Variable eingeführt. 

Die allgemeine Syntax zur Definition einer eigenen Funktion mit Parametern sieht
wie folgt aus:

```python
def meine_funktion(arg1, arg2, ..., argn):
    """Optionaler Docstring zur Erklärung."""

    # Implementierung der Funktion
    anweisung01
    anweisung02
     ...

```




```python
def gruesse_ausrichten_mit_parameter(name):
    print('Ich grüße', name)
```

Der Aufruf einer Funktion ohne passende Argumente führt zu einer Fehlermeldung.

```python
gruesse_ausrichten_mit_parameter()
```

Daher müssen wir die modifizierte Funktion nun wie folgt aufrufen:

```python
gruesse_ausrichten_mit_parameter('Studierende')
```

Die Funktion `gruesse_ausrichten_mit_parameter()` hat aber keinen Rückgabewert.
Das können wir wie folgt testen:

```python
x = gruesse_ausrichten_mit_parameter('Alice')
type(x)
```

`x` ist vom Typ `NoneType` oder anders ausgedrückt, es hat keinen Datentyp. 

Sind Funktionen ohne Rückgabewert sinnvoll?

Ja, denn so können pythonblöcke vereinfacht werden. Sollte in einem Programm python
mehrmals ausgeführt werden, lohnt es sich, diesen in eine Funktion auszulagern,
um diese einfach aufrufen zu können.





## Video Funktionen mit Parametern

Schauen Sie sich auf YouTube das Video "Python Tutorial deutsch [19/24]" an (ca.
9:06 min), siehe
https://www.youtube.com/watch?v=af9ORp1Pty0&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=19.
Stoppen Sie regelmäßig und probieren Sie die dort gezeigten Beispiele in der
folgenden python-Zelle aus: 


```python

```


## Funktionen mit Parametern und Rückgabewert

In der Regel jedoch haben Funktionen einen Rückgabewert.

Die allgemeine Syntax zur Definition einer eigenen Funktion mit Parametern und
Rückgabewert sieht wie folgt aus:

```python
def meine_funktion(arg1, arg2, ..., argn):
    """Optionaler Docstring zur Erklärung."""

    # Implementierung der Funktion
    anweisung01
    anweisung02
     ...

    return ergebnis  # optional, die Funktion kann auch keine Rückgabe haben
```

Schauen wir uns ein Beispiel an:



```python
def berechne_quadrat(x):
    return x*x
```

```python
for x in range(1,11):
    y = berechne_quadrat(x) 
    ausgabe = '{} * {} = {}'.format(x, x, y)
    print(ausgabe)
```

Funktionen können auch mehrere Argumente haben.

```python
def berechne_rechteck_flaeche(a,b):
    flaeche = a*b
    return flaeche
```

```python
# main program

# Eingabe
a = int(input('Länge des Rechtecks: '))
b = int(input('Breite des Rechtecks: '))

# Verarbeitung
flaeche = berechne_rechteck_flaeche(a,b)

# Ausgabe
print('berechnete Fläche: ', flaeche)


```

##  Video Funktionen Funktionen mit Rückgabewert

Schauen Sie sich auf YouTube das Video "Python Tutorial deutsch [20/24]" an (ca.
12:02 min), siehe
https://www.youtube.com/watch?v=ehSP-sYoKCY&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=20.
Stoppen Sie regelmäßig und probieren Sie die dort gezeigten Beispiele in der
folgenden python-Zelle aus: 



```python

```


## Funktionen mit mehreren Rückgabewerten

```python
def funktion(arg1, arg2, ...):
    # Verarbeitung
    anweisung01
    anweisung02
    ...
    
    return ergebnis1, ergebnis2
```

Es ist auch möglich, mehrere Ergebnisse gleichzeitig zurückzugegen. Diese werden
einfach nach dem Schlüsselwort `return` mit Kommas getrennt gelistet. 


```python
def potenzen_bis_vier(x):
    x_hoch_2 = x**2
    x_hoch_3 = x**3
    x_hoch_4 = x**4
    return x_hoch_2, x_hoch_3, x_hoch_4
```

```python
for x in range(1,11):
    print(potenzen_bis_vier(x))
```

```python
for x in range(1,5):
    potenz2, potenz3, potenz4 = potenzen_bis_vier(x)
    print('Die 2. Potenz von {} ist {}, die dritte ist {} und die vierte ist {}.'.format(x, potenz2, potenz3, potenz4))
```

## Ausführung von Funktionen: lokale und globale Variablen

Schauen Sie sich bitte folgende Funktionsimplementierung an. Was macht die
Funktion?

```python
def erhoehe_um_eins(x):
    x = x + 1
```

```python
x = 17
print(x)

# jetzt Funktion anwenden
print('jetzt Funktion auf x anwenden...')
erhoehe_um_eins(x)
print(x)
```

Wir schauen in die Funktion "hinein", um zu sehen, ob vielleicht gar nicht
erhöht wurde.

```python
def erhoehe_um_eins(x):
    print('in der Funktion vor der Erhöhung:')
    print(x)
    
    # Erhöhung
    x = x + 1
    
    print('in der Funktion nach der Erhöhung:')
    print(x)    
```

```python
x = 17
print(x)

# jetzt Funktion anwenden
print('jetzt Funktion auf x anwenden...')
erhoehe_um_eins(x)
print(x)
```

Was ist passiert? Die Variable `x` in der Funktion ist eine lokale Variable. Es
ist Zufall, das sie so heißt, wie die Variable außerhalb der Funktion. Ein
Programmierer einer Funktion kann nicht vorab wissen, wie alle anderen Variablen
genannt werden. Daher müssen alle Variablen in der Funktion lokal bleiben, um
nicht unabsichtlich Variablen, die dummerweise oder absichtlich den gleichen
Namen tragen, zu verändern.

Möchte man erreichen, dass eine Funktion den Wert einer Variable ändert, kann
man dies über die Rückgabe und explizite Zuweisung erreichen.

```python
def erhoehe_um_eins(x):
    x = x + 1
    return x

x = 17
print('vorher', x)
 
x = erhoehe_um_eins(x)
print('nachher', x)
```