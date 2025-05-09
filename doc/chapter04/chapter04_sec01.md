---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: turtle
  language: python
  name: python3
---

# 4.1 for-Schleifen

In der Praxis kommt es oft vor, dass wir von vornherein wissen, wie oft wir eine
Handlung wiederholen wollen. Beispielsweise soll in einem Verein darüber
abgestimmt werden, ob Anna oder Bob zukünftig die Kasse verwalten soll. Alle
Vereinsmitglieder schreiben einen der beiden Namen auf einen Zettel und werfen
ihn in die Wahlurne. Jetzt beginnt die Wiederholung. Charlie greift in die Urne,
zieht einen Zettel heraus, liest den Namen vor und macht dann entweder bei Anna
oder bei Bob einen Strich auf dem Flipboard. Solange Zettel in der Urne sind,
wird diese Prozedur wiederholt. Wenn wir aber bereits vorher wissen, dass 12
Vereinsmitglieder abgestimmt haben, so wird Charlie 12 x diese Prozedur
wiederholen. In diesem Fall bietet sich die Umsetzung als sogenannte
Zählschleife an.

In Python gibt es zwei Varianten von Zählschleifen. Zum einen die Zählschleife,
bei der Elemente einer Liste abgearbeitet werden. Zum anderen die Zählschleife
mit einem Zahlenbereich.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können eine **for-Schleife mit Liste** programmieren.
* Sie wissen, wie die Fachbegriffe der einzelnen Bestandteil der Schleife
  lauten:
  * **Kopfzeile**, wird mit **Doppelpunkt :** abgeschlossen
  * Schlüsselwörter **for** und **in**
  * **Schleifenvariable**  
* Sie wissen, dass der Anweisungsblock des Schleifeninneren eingerückt werden
  muss. Die **Einrückung** muss immer mit der gleichen Anzahl von Zeichen
  (Leerzeichen oder Tab) erfolgen.
* Sie können Zahlenlisten mit der **range()**-Funktion erzeugen und diese mit
  der for-Schleife kombinieren.
```

## for-Schleifen mit Liste

Erkunden wir den folgenden Python-Code:

```{code-cell} ipython3
for i in [2, 4, 6, 8, 10]:
    print(i)
```

Nacheinander wird die Variable `i` auf die Werte in der Liste `[2, 4, 6, 8, 10]`
gesetzt und per `print()` ausgegeben. Dieses Programmkonstrukt nennt man eine
**for-Schleife**.

Eine for-Schleife beginnt mit dem Schlüsselwort **for**. Danach kommt der Name
der sogenannten **Schleifenvariable**, in diesem Fall also `i`. Als nächstes
folgt wieder ein Schlüsselwort, nämlich **in** und zuletzt eine Liste. Diese
Zeile nennt man **Kopfzeile**.

Python muss wissen, welche Kommandos für jeden Schleifendurchgang ausgeführt
werden sollen. Daher wird die Kopfzeile der Schleife mit einem Doppelpunkt `:`
beendet. Danach werden alle Kommandos aufgelistet, die ausgeführt werden sollen.
Damit Python weiß, wann es wieder mit dem normalen Programm weitergehen soll,
müssen wir dem Python-Interpreter das Ende der Schleife signalisieren. In vielen
Programmiersprachen wird das mit dem Schlüsselwort `end` gemacht oder es werden
Klammern gesetzt. In Python wird stattdessen mit **Einrückung** gearbeitet. Alle
Zeilen mit Anweisungen, die eingerückt sind, werden in der Schleife wiederholt.

In dem obigen Beispiel heißt die Schleifenvariable `i`. Sie nimmt beim 1.
Schleifendurchgang den Wert `2` an. Dann werden die Anweisungen im
Schleifeninneren ausgeführt, also die print()-Funktion für `i = 2` angewendet
und eine 2 ausgegeben. Dann wird die Schleife ein 2. Mal durchlaufen. Diesmal
nimmt die Schleifenvariable `i` den Wert `4` an und die print()-Funktion gibt 4
aus. Das geht so weiter bis zum 5. Schleifendurchgang, wo die Schleifenvariable
den Wert `i = 10` annimmt und eine 10 auf dem Bildschirm angezeigt wird. Da die
`10` das letzte Element der Liste war, macht der Python-Interpreter mit dem
normalen Programm weiter. Bei unserem kurzen Beispiel ist aber schon das Ende
des Programmes erreicht. Zusammengefasst, werden nacheinander die Elemente der
Liste `[2, 4, 6, 8, 10]` auf dem Bildschirm ausgegeben.

Allgemein hat die for-Schleife mit Liste folgende Syntax (= Grammatik einer
Programmiersprache):

```python3
for element in liste:
    anweisungen
```

## Anwendungsbeispiele der for-Schleife

Meistens geht es nicht darum, nur etwas einzeln anzuzeigen, sondern die Elemente
der Menge zu verarbeiten. Im nächsten Beispiel soll jedes Element der Liste
`[4,5,7,11,21` um 2 erhöht und dann angezeigt werden.

```{code-cell} ipython3
for zahl in [4,5,7,11,21]:
    zahl2 = zahl + 2
    print(zahl2)

print('Ich bin fertig!')
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, das die ersten 10 Quadratzahlen berechnet und ausgibt.
```

```{code-cell} ipython3
# Hier Ihr Code.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
for i in [1,2,3,4,5,6,7,8,9,10]:
    quadrat = i ** 2
    print(quadrat)
```
````

Für den Python-Interpreter ist es unerheblich, mit welchen Datentypen die Liste
gefüllt ist, die in der for-Schleife durchlaufen wird. Auch eine Liste mit
Strings stellt kein Problem dar, wie das folgende Beispiel zeigt:

```{code-cell} ipython3
monate = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 
'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']

for monat in monate:
    print(monat)
```

Am besten probieren Sie es einmal selbst aus:

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie eine for-Schleife, die die klassischen Schulnoten »sehr gut«  bis
»ungenügend« einzeln ausgibt. Zur Erinnerung: die deutschen Schulnoten
lauten sehr gut, gut, befriedigend, ausreichend, mangelhaft und ungenügend.
```

```{code-cell} ipython3
# Hier Ihr Code.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
# Erzeugung Liste
noten_liste = ["sehr gut", "gut", "befriedigend", "ausreichend", "mangelhaft", "ungenügend"]

# Ausgabe 
for note in noten_liste:
    print(note)
```
````

```{dropdown} Video "for-Schleife" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/ISo1uqLcVw8?si=HhdcBq1rzxtLZ10L" title="YouTube video player" frameborder="0" allow="accelerometer;
autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## for-Schleifen mit range()

In vielen Fällen möchten wir eine Schleife für eine bestimmte Anzahl von
Iterationen ausführen. In Python können wir dies mit Hilfe der
`range()`-Funktion erreichen. Die range()-Funktion generiert ein spezielles
Objekt von Zahlen, die wir dann anschließend in einer for-Schleife verwenden
können. Natürlich kann die Liste von Zahlen auch für andere Dinge genutzt
werden, aber die Verwendung für for-Schleifen ist sicherlich der häufigste
Einsatzzweck von range().

Die Syntax der range()-Funktion ist:

```python
range(stop)               # erzeugt Zahlen von 0 bis (stop - 1)
range(start, stop)        # erzeugt Zahlen von start bis (stop - 1)
range(start, stop, step)  # erzeugt Zahlen von start bis (stop - 1) mit der Schrittweite step
```

Es ist schwierig, sich den Inhalt von `range()` direkt anzuschauen. Am
einfachsten ist es, die range()-Funktion direkt mit der for-Schleife zu
kombinieren.

```python
for i in range(start, stop, step):
    anweisungen
```

Hier ist `i` die Schleifenvarible, die nacheinander bei jedem Schleifendurchgang
die Werte in der von range() erzeugten Liste annimmt. Im Folgenden finden Sie
einige Beispiele für die Verwendung von for-Schleifen mit range():

```{code-cell} ipython3
for i in range(5):
    print(i)
```

`range(5)` erzeugt eine Liste mit den Zahlen 0, 1, 2, 3, 4, die dann durch die
`print()`-Funktion nacheinander ausgegeben werden.

```{code-cell} ipython3
for i in range(2, 6):      
    print(i)
```

`range(2,6)` erzeugt eine Liste mit den Zahlen 2, 3, 4, 5. Achtung, die 6 gehört
nicht dazu, da das letzte Element der Liste ja die stop-Zahl - 1 ist.

```{code-cell} ipython3
for i in range(1, 10, 2): 
    print(i)
```

`range(1, 10, 2)` erzeugt die Liste 1, 3, 5, 7, 9.

Um die Bedeutung der Schrittweite `step` zu zeigen, können wir einmal eine
negative Schrittweite ausprobieren.

```{code-cell} ipython3
for i in range(10, 0, -1):
    print(i)
```

Die negative Schrittweite `step = -1` führt dazu, dass der Python-Interpreter
rückwärts zählt.

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie die Dreier-Zahlen von 3 bis 99 ausgeben, also 3, 6, 9, 12, 15, ..., 96, 99.
```

```{code-cell} ipython3
# Hier Ihr Code.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
for i in range(3, 100, 3):
    print(i)
```
````

Insbesondere, wenn die Anzahl der Wiederholungen feststeht, kommt die
for-Schleife in Kombination mit range() zum Einsatz. Im Folgenden sehen wir uns
ein Beispiel dazu an.

Beispiel: Berechnung der Summe der ersten 10 natürlichen Zahlen

```{code-cell} ipython3
summe = 0
for i in range(1, 11):
    summe += i

print("Die Summe der ersten 10 natürlichen Zahlen ist: ", summe)
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, dass die Summe der ersten n Quadratzahlen berechnet.
```

```{code-cell} ipython3
# Hier Ihr Code.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
n = 5  # Beispielwert
summe = 0

for i in range(1, n + 1):
    summe += i ** 2

print("Die Summe der ersten Quadratzahlen ist:", summe)
```

Hier ist die Variable `n` im Python-Code gesetzt worden. Schöner wäre eine interaktive Abfrage mit der input()-Funktion:
```python
n = int(input('Wie viele Quadratzahlen sollen summiert werden?))
```
Aber das war nicht gefragt.
````

```{dropdown} Video "for-Schleife mit range()" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/pQh5Idw2sKM?si=TKEewQnlA8At66KA" title="YouTube video player" frameborder="0" allow="accelerometer; 
autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, wie man in Python for-Schleifen verwendet,
um Wiederholungen umzusetzen. Wir haben zwei Varianten kennengelernt: die
for-Schleife mit Listen und die for-Schleife mit der range()-Funktion. Dabei
haben wir Begriffe wie Schleifenvariable, Kopfzeile und Einrückung eingeführt
und deren Bedeutung erklärt. Anhand von Beispielen und Übungen haben wir
gesehen, wie man Listen von Zahlen oder Texten durchläuft und die Elemente
weiterverarbeitet. Außerdem haben wir gelernt, wie man mit range() Zahlenfolgen
erzeugt – auch mit Startwert, Stoppwert und Schrittweite. Im nächsten Kapitel
werden wir das Thema Strings erneut aufgreifen und vertiefen.
