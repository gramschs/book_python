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

Eine Funktion in Python ist eine Zusammenfassung von Anweisungen, die dazu
dienen, eine bestimmte Teilaufgabe zu lösen. Dabei arbeitet die Funktion in
ihrer allgemeinsten Form nach dem EVA-Prinzip. Die Funktion übernimmt Objekte
als Eingabe, verarbeitet diese und liefert Objekte als Ergebnis zurück. Wie die
Funktion dabei im Inneren genau funktioniert (Verarbeitung), ist unwichtig.

Beispielsweise gibt es im Modul `numpy` die Funktion `sqrt()`. Wir wissen, dass
wir der Funktion eine Zahl übergeben müssen (Eingabe), z.B. `sqrt(5)`. Die
Funktion liefert dann als Ergebnis $\sqrt{5}$ zurück. Welches Verfahren zur
Berechnung der Wurzel verwendet wurde, wissen wir nicht. 

Insbesondere muss die Teilaufgabe, die die Funktion löst, nichts mit Mathematik
zu tun haben. Eine Funktion in der Informatik hat nichts mit einer
mathematischen Funktion zu tun, auch wenn oft mathematische Funktionen als
Beispiel verwendet werden. Ein Beispiel für eine nicht-mathematische Funktion
haben Sie mit `input()` bereits kennengelernt. Die Funktion nimmt einen Text
entgegen, z.B. die Frage "Wie groß sind Sie?". Dann wird dieser Text
verarbeitet, in diesem Fall auf dem Bidschirm angezeigt und die Antwort
eingelesen. Die Antwort kann dann in einer Variablen gespeichert werden.

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie kennen die Fachbegriffe 
  * **Aufruf** einer Funktion,
  * **Argumente** oder **Parameter** einer Funktion und
  * **Rückgabewert** einer Funktion.
* Sie können eine einfache Funktion selbst implementieren.
```

## Die Benutzung von Funktionen (oder der Aufruf von Funktionen)

Der Aufruf einer Funktion hat folgende Syntax:

```python
rueckgabewert = funktion( argument1, argument2, ... )
```

Eine Funktion wird benutzt, indem man den Namen der Funktion und dann in runden
Klammern ihre **Parameter** als Liste hinschreibt. Die konkreten Parameter einer
Funktion beim Aufruf werden die **Argumente der Funktion** genannt. Welche
Argumente für eine Funktion verwendet werden dürfen, hängt von der
Implementierung der Funktion ab.

Beispielsweise kann als Argument für die `len()`-Funktion ein String übergeben
werden oder eine Liste. Stellen Sie eine Vermutung auf: was könnte die
`len()`-Funktion bewirken?

```{code-cell} ipython3
len('Hallo')
```

```{code-cell} ipython3
len([1,2,3,4,8,2])
```

In der Regel geben Funktionen wieder Ergebnisse zurück. Diese werden
**Rückgabewert** genannt. Beispielsweise können die Rückgabewert einer Variable
zugewiesen werden, um mit dem Ergebnis weiter zu arbeiten.

```{code-cell} ipython3
laenge1 = len('Hallo')
laenge2 = len(['Apfel', 'Banane', 'Erdbeere'])

if laenge1 < laenge2:
    print('Das Wort Hallo enthält weniger Buchstaben als Früchte im Obstsalat.')
else:
    print('Das Wort Hallo enthält mehr Buchstaben als Einträge in der Liste.')
```

## Definition von einfachen Funktionen

Einfache Funktionen werden mit dem Schlüsselwort `def` gefolgt vom
Funktionsnamen definiert. Die Code-Anweisungen der Funktion werden eingerückt. 

```python
def meine_funktion():
    anweisung01
    anweisung02
     ...

```

Erstes Beispiel:

Die folgende Funktion hat kein Argument und keine Rückgabe.

```{code-cell} ipython3
def gruesse_ausrichten():
    print('Ich grüße Sie!')
```

Nachdem die Funktion `gruesse_ausrichten()` so implementiert wurde, können wir
sie im Folgenden direkt verwenden.

```{code-cell} ipython3
gruesse_ausrichten()
```

Und natürlich kann man sie in Programmverzweigungen und Schleifen einbauen.

```{code-cell} ipython3
for i in range(7):
    gruesse_ausrichten()
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie eine Funktion, die mit Turtle ein Rechteck zeichnet. Testen Sie Ihre Funktion auch.
```
````{admonition} Lösung
:class: minisolution, toggle
```python
import ColabTurtlePlus.Turtle as turtle
turtle.clearscreen()

def zeichne_rechteck():
    rechteck = turtle.Turtle()
    for i in range(2):
        rechteck.forward(100)
        rechteck.left(90)
        rechteck.forward(50)
        rechteck.left(90)
        
zeichne_rechteck()
```
````

Das folgende Video zeigt Ihnen nochmal, wie in Python Funktionen definiert
werden.

<iframe width="560" height="315" src="https://www.youtube.com/embed/LQCfN5HS9xI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


