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

# 6.2 Funktionen mit Parameter und Rückgabe

Vorgefertigte Funktionen haben wir schon mir Argument und Rückgabewert
aufgerufen. In diesem Kapitel geht es darum, selbst eine Funktion zu
implementieren, die Argumente entgegennimmt, diese verarbeitet und dann
Rückgabewerte liefert.

## Lernziele

```{admonition} Lernziel
:class: goals
Sie können eine Funktion mit Parametern und Rückgabewerten selbst
implementieren.
```

## Definition von Funktionen mit Parametern

Meistens haben Funktionen Argumente, um Eingaben entgegennehmen und verarbeiten
zu können. Das Argument wird bei der Implementierung der Funktion mit einer
Variablen eingeführt. 

Die allgemeine Syntax zur Definition einer eigenen Funktion mit Parametern sieht
wie folgt aus:

```python
def meine_funktion(arg1, arg2, ..., argn):
    anweisung01
    anweisung02
     ...
```

Funktionen werden mit dem Schlüsselwort `def` gefolgt vom Funktionsnamen und
einer Liste von Parametern in Klammern definiert. Die Code-Anweisungen der
Funktion werden eingerückt.

Als Beispiel betrachten wir erneut die Funktion, die Grüße ausrichtet. Doch
jetzt erweitern wir die Funktion. Die modifizierte Variante soll konkret eine
Person grüßen.

```{code-cell} ipython3
def gruesse_ausrichten_mit_parameter(name):
    print(f'Ich grüße {name}!')
```

Der Aufruf einer Funktion ohne passende Argumente führt nun zu einer
Fehlermeldung.

```python
gruesse_ausrichten_mit_parameter()
```

Daher müssen wir die modifizierte Funktion nun wie folgt aufrufen:

```{code-cell} ipython3
gruesse_ausrichten_mit_parameter('Anna')
```

Die Funktion `gruesse_ausrichten_mit_parameter()` hat aber keinen Rückgabewert.
Das können wir wie folgt testen:

```{code-cell} ipython3
x = gruesse_ausrichten_mit_parameter('Alice')
type(x)
```

`x` ist vom Typ `NoneType` oder anders ausgedrückt, in der Variablen `x` ist
kein Datentyp gepeichert.

Sind Funktionen ohne Rückgabewert sinnvoll? Ja, denn so können Python-Programme
vereinfacht werden. Sollte in einem Programm ein Block von Anweisungen mehrmals
ausgeführt werden, lohnt es sich, diesen in eine Funktion auszulagern, um diese
einfach aufrufen zu können.

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie eine Funktion, die mit Turtle ein Rechteck zeichnet. Die beiden
Seitenlängen des Rechtecks sollen als Argumente der Funktion übergeben werden.
Testen Sie Ihre Funktion auch.
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
import ColabTurtlePlus.Turtle as turtle
turtle.clearscreen()

def zeichne_rechteck(seite1, seite2):
    rechteck = turtle.Turtle()
    for i in range(2):
        rechteck.forward(seite1)
        rechteck.left(90)
        rechteck.forward(seite2)
        rechteck.left(90)
        
a = 100
b = 30
zeichne_rechteck(a,b)
```
````

Das folgende Video fasst Funktionen mit Argumenten in Python zusammen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/af9ORp1Pty0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Funktionen mit Parametern und Rückgabewerten

In der Regel jedoch haben Funktionen einen Rückgabewert. Die allgemeine Syntax
zur Definition einer eigenen Funktion mit Parametern und Rückgabewert sieht wie
folgt aus:

```python
def meine_funktion(arg1, arg2, ..., argn):
    anweisung01
    anweisung02
     ...

    return rueckgabewert1, rückgabewert2, ...  
```

An der Definitionszeile ändert sich nichts. Zuerst wird das Schlüsselwort `def`
verwendet, dann folgt der Funktionsname und zuletzt werden die Parameter in
Klammern aufgelistet. Der Rückgabewert der Funktion wird dann durch das
Schlüsselwort `return` im Inneren der Funktion, also im eingerückten Teil
definiert. Die Funktion kann einen oder mehrere Rückgabewerte zurückliefern. Bei
mehreren Rückgabewerten werden diese einfach durch Komma getrennt.

Schauen wir uns ein Beispiel an. Die folgende Funktion nimmt einen Parameter
entgegen und gibt einen Rückgabewert zurück.

```{code-cell} ipython3
def berechne_quadratzahl(zahl):
    return zahl * zahl
```

Jetzt können wir die Funktion ausprobieren.

```{code-cell} ipython3
for x in range(1,11):
    y = berechne_quadratzahl(x) 
    print(f'{x} mal {x} ist {y}')
```

Als nächstes kommt ein Beispiel mit zwei Rückgabewerten. Nicht nur die
Quadratzahl, sondern auch die Kubikzahl soll berechnet werden.

```{code-cell} ipython3
def berechne_quadrat_kubik(zahl):
    quadrat = zahl**2
    kubik = zahl**3
    return quadrat, kubik
```

Und erneut testen wir die Funktion.

```{code-cell} ipython3
for x in range(1,6):
    x_hoch_2, x_hoch_3 = berechne_quadrat_kubik(x)
    print(f'x = {x}, x^2 = {x_hoch_2}, x^3 = {x_hoch_3}')
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, das mit Turtle ein Rechteck zeichnet, wobei die
beiden Seitenlängen als Argumente der Funktion übergeben werden. Die Funktion
soll den Umfang des Rechtecks und den Flächeninhalt zurückgeben. Lassen Sie
anschließend Umfang und Flächeninhalt ausgeben.
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
import ColabTurtlePlus.Turtle as turtle
turtle.clearscreen()

def zeichne_rechteck(seite1, seite2):
    # Zeichnung des Rechecks
    rechteck = turtle.Turtle()
    for i in range(2):
        rechteck.forward(seite1)
        rechteck.left(90)
        rechteck.forward(seite2)
        rechteck.left(90)
        
    # Berechnung Umfang und Flächeninhalt
    umfang = 2 * seite1 + 2 * seite2
    flaeche = seite1 * seite2
    
    # Rückgabe
    return umfang, flaeche
    
# Test der Funktion      
a = 100
b = 30
U,A = zeichne_rechteck(a,b)
print(f'Der Umfang ist {U:.2f} Längeneinheiten, der Flächeninhalt des Rechtecks ist {A:.2f} Flächeneinheiten.')
```
````

Auch zu dem Thema Funktionen mit Rückgabe gibt es ein Video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ehSP-sYoKCY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
