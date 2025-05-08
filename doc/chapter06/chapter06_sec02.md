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

Vorgefertigte Funktionen haben wir schon mit Argument und Rückgabewert
aufgerufen. In diesem Kapitel geht es darum, selbst eine Funktion zu
implementieren, die Argumente entgegennimmt, diese verarbeitet und dann
Rückgabewerte liefert.

## Lernziele

```{admonition} Lernziel
:class: goals
* Sie können eine Funktion mit Parametern und Rückgabewerten selbst
  implementieren.
* Sie können zwischen Parametern und Argumenten einer Funktion unterscheiden.
```

## Definition von Funktionen mit Parametern

Meistens haben Funktionen Argumente, um Eingaben entgegennehmen und verarbeiten
zu können. Das Argument wird bei der Implementierung der Funktion mit einer
Variablen eingeführt.

Die allgemeine Syntax zur Definition einer eigenen Funktion mit Parametern sieht
wie folgt aus:

```python
def meine_funktion(para1, para2, ..., paran):
    anweisung01
    anweisung02
     ...
```

Funktionen werden mit dem Schlüsselwort `def` gefolgt vom Funktionsnamen und
einer Aufzählung von Parametern in Klammern definiert. Die Code-Anweisungen der
Funktion werden eingerückt.

Als Beispiel betrachten wir erneut die Funktion, die Grüße ausrichtet. Doch
jetzt erweitern wir die Funktion. Die modifizierte Variante soll konkret eine
Person grüßen.

```{code-cell} ipython3
def gruesse_ausrichten_mit_parameter(name):
    print(f'Ich grüße {name}!')
```

Der Aufruf einer Funktion ohne passende Argumente führt nun zu einer
Fehlermeldung. Entfernen Sie in der nächsten Code-Zelle das Kommentarzeichen.

```{code-cell} ipython3
# gruesse_ausrichten_mit_parameter()
```

Daher müssen wir die modifizierte Funktion nun mit einem Argument aufrufen:

```{code-cell} ipython3
gruesse_ausrichten_mit_parameter('Anna')
```

Hinweis: Bei Funktionen unterscheiden wir zwischen einem **Parameter** einer
Funktion und einem **Argument**. Die formalen Parameter sind die Variablennamen
in der Funktionsdefinition (z.B. `name` in `def
gruesse_ausrichten_mit_parameter(name):`). Sie dienen als Platzhalter für die
Werte, die beim Funktionsaufruf übergeben werden. Die aktuellen Argumente sind
dagegen die konkreten Werte, die beim Aufruf der Funktion übergeben werden (z.B.
`'Anna'` in `gruesse_ausrichten_mit_parameter('Anna')`). Der formale Parameter
`name` nimmt also beim Funktionsaufruf den Wert des Arguments `'Anna'` an und
steht innerhalb der Funktion als Variable zur Verfügung.

Die Funktion `gruesse_ausrichten_mit_parameter()` hat aber keinen Rückgabewert.
Das können wir wie folgt testen:

```{code-cell} ipython3
x = gruesse_ausrichten_mit_parameter('Alice')
type(x)
```

`x` ist vom Typ `NoneType`. Das bedeutet, dass in der Variablen `x` der
spezielle Python-Wert `None` gespeichert ist. `None` ist ein eigener Datentyp in
Python und repräsentiert die Abwesenheit eines Wertes oder ein 'nichts'.
Funktionen, die keinen expliziten Rückgabewert mit `return` angeben, geben
automatisch `None` zurück.

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

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

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

Das folgende Video fasst Funktionen mit Parametern in Python zusammen.

```{dropdown} Video "Funktionen mit Parametern" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/af9ORp1Pty0"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Funktionen mit Parametern und Rückgabewerten

In der Regel jedoch haben Funktionen einen Rückgabewert. Die allgemeine Syntax
zur Definition einer eigenen Funktion mit Parametern und Rückgabewert sieht wie
folgt aus:

```python
def meine_funktion(para1, para2, ..., paran):
    anweisung01
    anweisung02
     ...

    return rueckgabewert1, rueckgabewert2, ...  
```

An der Definitionszeile ändert sich nichts. Zuerst wird das Schlüsselwort `def`
verwendet, dann folgt der Funktionsname und zuletzt werden die Parameter in
Klammern aufgelistet. Der Rückgabewert der Funktion wird dann durch das
Schlüsselwort `return` im Inneren der Funktion, also im eingerückten Teil
definiert. Die Funktion kann einen oder mehrere Rückgabewerte zurückliefern. Bei
mehreren Rückgabewerten werden diese einfach durch Komma getrennt.

Für Experten:  Bei mehreren Rückgabewerten erzeugt Python intern ein sogenanntes
Tupel, das all diese Werte enthält. Daher kann man das Ergebnis einer solchen
Funktion auch direkt einer einzelnen Variablen zuweisen und erhält dann ein
Tupel, oder man kann die Werte durch Kommas getrennt mehreren Variablen zuweisen
(Unpacking).

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

Wenn eine Funktion mehrere Werte zurückgibt, haben wir verschiedene
Möglichkeiten, diese zu verarbeiten. Meist weisen wir jedem Rückgabewert eine
eigene Variable zu, wie in `x_hoch_2, x_hoch_3 = berechne_quadrat_kubik(x)`. Man
muss jedoch nicht immer alle Rückgabewerte verwenden. Benötigt man zum Beispiel
nur den ersten Rückgabewert, kann man schreiben: `x_hoch_2, _ =
berechne_quadrat_kubik(x)`. Der Unterstrich `_` ist eine Konvention in Python,
die signalisiert, dass dieser Wert ignoriert wird.

Alternativ kann man auch alle Rückgabewerte als Tupel einer einzelnen Variable
zuweisen: `ergebnis = berechne_quadrat_kubik(x)`. Dann greift man über den Index
auf die einzelnen Werte zu: `ergebnis[0]` für das Quadrat und `ergebnis[1]` für
den Kubikwert.

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, das mit Turtle ein Rechteck zeichnet, wobei die
beiden Seitenlängen als Argumente der Funktion übergeben werden. Die Funktion
soll den Umfang des Rechtecks und den Flächeninhalt zurückgeben. Lassen Sie
anschließend Umfang und Flächeninhalt ausgeben.
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

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

```{dropdown} Video "Funktionen mit Rückgabewert" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/ehSP-sYoKCY"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Funktionen mit Parametern und Rückgabewerten ermöglichen flexible Eingaben und
die Rückgabe von Ergebnissen, was unsere Programme modular und wiederverwendbar
macht. Im nächsten Kapitel lernen wir, wie Variablen unterschiedliche
Gültigkeitsbereiche haben können - entweder nur innerhalb einer Funktion (lokal)
oder im gesamten Programm (global).
