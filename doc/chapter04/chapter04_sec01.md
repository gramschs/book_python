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

# 4.1 for-Schleifen mit Liste

In der Praxis kommt es oft vor, dass wir von vornherein wissen, wie oft wir eine
Handlung wiederholen wollen. Beispielsweise soll in einem Verein darüber
abgestimmt werde, ob Anna oder Bob zukünftig die Kasse verwalten soll. Alle
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
mit einem Zahlenbereich. In diesem Abschnitt behandeln wir Zählschleife mit
einer Liste.

```{admonition} Lernziele
:class: hint
* TODO
```


<!-- #region -->
## Grammatik der for-Schleife mit Liste

Die for-Schleife mit Liste hat folgende Syntax (= Grammatik einer Programmiersprache):

```python3
for element in liste:
    anweisungsblock
```

Eine Schleife beginnt mit dem Schlüsselwort **for**. Danach kommt der Name der sogenannten **Schleifenvariable**, in diesem Fall also `element`. Als nächstes folgt wieder ein Schlüsselwort, nämlich **in** und zuletzt die Liste.

Python muss wissen, welche Kommandos für jeden Schleifendurchgang ausgeführt werden sollen. Daher wird die Kopfzeile der Schleife mit einem Doppelpunkt `:` beendet. Danach werden alle Kommandos aufgelistet, die ausgeführt werden sollen. Damit Python weiß, wann es wieder mit dem normalen Programm weitergehen soll, müssen wir dem Python-Interpreter das Ende der Schleife signalisieren. In vielen Programmiersprachen wird das mit dem Schlüsselwort `end` gemacht oder es werden Klammern gesetzt. In Python wird stattdessen mit **Einrückung** gearbeitet. Alle Zeilen, die eingerückt sind, werden in der Schleife wiederholt.

Probieren wir es mit einem einfachen Beispiel:


<!-- #endregion -->

```python
for i in [2, 4, 6, 8, 10]:
    print(i)
```


Es werden nacheinander die Elemente der Menge `[2, 4, 6, 8, 10]` auf dem Bildschirm ausgegeben.

Meistens geht es nicht darum, nur etwas einzeln anzuzeigen, sondern die Elemente der Menge zu verarbeiten. Im nächsten Beispiel soll jedes Element der Liste `[4,5,7,11,21` um 2 erhöht und dann angezeigt werden.

```python
for zahl in [4,5,7,11,21]:
    zahl2 = zahl + 2
    print(zahl2)

print('Ich bin fertig!')
```

```{admonition} Mini-Übung
Schreiben Sie eine For-Schleife, die die klassischen Schulnoten "sehr gut"  bis "ungenügend" einzeln ausgibt. Zur Erinnerung: die deutschen Schulnotenlauten lauten sehr gut, gut, befriedigend, ausreichend, mangelhaft und ungenügend.
```
````{admonition} Lösung
:class: minisolution, toggle
```python
# Erzeugung Liste
noten_liste = ["sehr gut","gut", "befriedigend", "ausreichend", "mangelhaft", "ungenügend"];

# Ausgabe 
for note in noten_liste:
    print(note)
```
````



