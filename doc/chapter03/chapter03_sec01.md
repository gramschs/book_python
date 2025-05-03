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

# 3.1 Listen

Bisher haben wir drei verschiedene Datentypen kennengelernt:

* Integer (ganze Zahlen),
* Float (Fließkommazahlen) und
* String (Zeichenketten).

Damit können wir einzelne Objekte der realen Welt gut abbilden. Mit einem String
können wir den Namen einer Person erfassen, mit einem Integer das Alter der
Person und mit einem Float die Körpergröße der Person gemessen in Meter. Was uns
aber bisher fehlt ist, eine Sammlung von Namen oder eine Sammlung von
Körpergrößen verwalten zu können. Daher werden wir uns in diesem Jupyter
Notebook mit Listen beschäftigen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, dass **Container** Datentypen sind, die andere Objekte als Sammlung verwalten.
* Sie können eine **Liste** erzeugen.
* Sie wissen, was der Fachbegriff **Index** bedeutet.
* Sie können lesend und schreibend auf die Elemente einer Liste zugreifen, beherrschen also
    * **Lesezugriff** und 
    * **Schreibzugriff**.
* Sie können mit dem Plus-Operator + Listen **verketten**.
* Sie können Elemente aus einer Liste löschen:
    * Löschung per Index: Funktion **del**
    * Löschung nach Wert: Methode **remove**
```

+++

## Container für Sammlungen

In der Mathematik gibt es den Begriff des Vektors. Einen Vektor kann man als
eine Sammlung von Zahlen interpretieren. Dabei müssen Vektoren nicht immer eine
geometrische Interpretation haben. Beispielsweise steht der Vektor

(116, 144, 199)

für ein sehr schönes Blau, wenn die drei Komponenten als die Intensität der
Farbanteile Rot - Grün - Blau interpretiert werden. Diese Art Farben zu
beschreiben, wird RGB-Wert genannt (siehe auch [Wikipedia →
RGB-Farbraum](https://de.wikipedia.org/wiki/RGB-Farbraum)). Die Internetseite
[https://www.color-hex.com](https://www.color-hex.com/) ermöglicht es, die
RGB-Werte verschiedener Farbtöne zu ermitteln.

Wir könnten aber auch eine Namensliste mit den Mitgliedern einer WG führen
wollen, z.B. [“Alice”, “Bob”, “Charlie”]. Damit verlassen wir die mathematische
Welt der Zahlen und damit des Vektors. Aber auch für diese Anwendungsszenarien
wäre es schön, Daten gemeinsam zu sammeln und zu verwalten.

Der Fachbegriff für Datentypen, die dafür gedacht sind, Daten als Sammlung zu
verwalten, ist **Container**. In Python gibt es verschiedene Container:

* Listen: list
* Tupel: tuple
* Dictionaries: dict
* Mengen: set

Wir behandeln in diesem Abschnitt die Listen.

+++

## Listen erzeugen mit []

Eine Liste wird in Python durch eckige Klammern [  ] erzeugt.

Betrachten wir ein Beispiel. Hier wird eine Liste mit den Elementen 1, 2, 3, 4,
5 erzeugt und dann anschließend in der Variablen `liste_beispiel` gespeichert.
Mit der Funktion `print()` lassen wir den Inhalt der Liste ausgeben.

```{code-cell} ipython3
liste_beispiel = [1, 2, 3, 4, 5]
print(liste_beispiel)
```

Probieren Sie in der nächsten Mini-Übung selbst aus, wie eine Liste erzeugt
wird.

+++

```{admonition} Mini-Übung
:class: miniexercise
Erzeugen Sie eine Liste mit Ihrem Vornamen, Ihrem Nachnamen und Ihrer Körpergröße in m. Welche Datentypen brauchen Sie für diese drei Objekte? Lassen Sie Ihre Liste auch ausgeben.
```

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
person = ['Alice', 'Musterfrau', 1.61]
print(person)
```
Vor- und Nachname werden durch Strings repräsentiert, die Körpergröße als Float.
````

Im folgenden Video können Sie sich die Erzeugung von Listen nochmal ansehen.

```{dropdown} Video "Python Tutorial - Listen" von Programmieren starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/ihF8bZoauBs"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Elemente aus einer Liste herausholen: Zugriff

Jede Liste hat einen Index. Man kann sich eine Liste wie eine Straße mit einer
Sammlung von Häusern vorstellen. Um ein Haus in der Straße zu finden, hat es
eine Hausnummer. Und das ist in der Informatik der **Index**, also die Position
in der Liste, an der ein Element zu finden ist.

In jeder Programmiersprache gibt es Container mit einem Index, wobei der Index
in der Regel durch Integer repräsentiert wird. Allerdings gibt es Unterschiede,
bei welcher Zahl die Nummerierung beginnt. **Python fängt mit der Null an.**
Dann können wir mit dem Index sozusagen nachsehen, welches Element an dieser
Index-Position gespeichert ist. Das nennt man in der Informatik **Lesezugriff**.
Oder wir können das Element an einer bestimmten Index-Position gegen ein neues
Element austauschen. Das nennt man dann **Schreibzugriff**.

Um auf ein Element einer Liste zugreifen zu können (egal ob lesend oder
schreibend), verwenden wir eckige Klammern und den Index. Der Lesezugriff für
das erste Element sieht biepielsweise so aus:

```{code-cell} ipython3
# Erzeugung einer Liste
meine_liste = ['rot', 'grün', 'blau', 'gelb', 'weiß', 'schwarz']

# Lesezugriff mit Position 1, also Index 0
erstes_objekt = meine_liste[0]
print(erstes_objekt)
```

In der nächsten Mini-Übung wird der Lesezugriff genutzt, um ein Element in einer
neuen Variable zu speichern.

+++

```{admonition} Mini-Übung
:class: miniexercise
Speichern Sie das 4. Element der Liste `meine_liste = ['rot', 'grün', 'blau', 'gelb', 'weiß', 'schwarz']` in der Variable `vier` ab und lassen Sie es ausgeben.
```

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
meine_liste = ['rot', 'grün', 'blau', 'gelb', 'weiß', 'schwarz']

vier = meine_liste[3]
print(vier)
```
````

+++

Der Schreibzugriff erfolgt ebenfalls mit eckigen Klammern und dem Index.

Im folgenden Code sehen Sie, wie in der Liste die Farbe weiß durch lila ersetzt wird.

```{code-cell} ipython3
# Erzeugung Liste
meine_liste = ['rot', 'grün', 'blau', 'gelb', 'weiß', 'schwarz']

# Schreibzugriff
meine_liste[4] = 'lila'
print(meine_liste)
```

Der Zugriff auf Listen wird auch in dem folgenden Video erklärt.

```{dropdown} Video "Python Tutorial - Zugriff auf Listen" von Programmieren starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/_XzWPXvya2w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Liste + Liste = verkettete Liste

Auch wenn es im ersten Moment verrückt erscheint, Python kann Listen addieren.
Am besten schauen wir uns ein Beispiel an:

```{code-cell} ipython3
liste_de = ['rot', 'grün', 'blau']
liste_en = ['red', 'green', 'blue']

# Verkettung zweier Listen durch +
liste_de_en = liste_de + liste_en
print(liste_de_en)
```

Das Aneinanderhängen von Elementen zweier Container nennen wir in der Informatik
**Verkettung**. Oft wird auch der englische Begriff **Concatenation** verwendet.

In der folgenden Mini-Übung können Sie die Verkettung ausprobieren.

+++

````{admonition} Mini-Übung
:class: miniexercise
Erzeugen Sie eine Liste mit den Monaten März, April und Mai und speichern Sie
diese Liste in der Variable `fruehling`. Erzeugen Sie anschließend die Listen
`sommer`, `herbst` und `winter` mit den jeweils passenden Monaten. Verketten Sie
die vier Listen und speichern Sie in der Variable `jahr` ab. Lassen Sie zuletzt das 
Jahr anzeigen.

Welchen Index hat Ihr Geburtsmonat in der Liste `jahr`?
````

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Listen mit Monaten
fruehling = ['März', 'April', 'Mai']
sommer = ['Juni', 'Juli', 'August']
herbst = ['September', 'Oktober', 'November']
winter = ['Dezember', 'Januar', 'Februar']

# Jahr
jahr = fruehling + sommer + herbst + winter
print(jahr)
```
Der März hat den Index 0, der April den Index 1 usw.. Der letzte Monat ist der
Februar, der den Index 11 hat.
````

+++

## Wie lang ist eine Liste?

Manchmal möchte man wissen, wie viele Elemente in einer Liste enthalten sind.
Dafür gibt es in Python die eingebaute Funktion `len()` – kurz für length, also
Länge.

```{code-cell} ipython3
farben = ['rot', 'grün', 'blau']
anzahl_farben = len(farben)
print(anzahl_farben)
```

In diesem Beispiel enthält die Liste `farben` drei Elemente, daher gibt
`len(farben)` den Wert 3 zurück.

Diese Funktion ist besonders nützlich, wenn man mit Listen arbeitet, deren Länge
sich verändert, zum Beispiel, wenn Einträge hinzugefügt oder gelöscht werden.

```{admonition} Mini-Übung
:class: miniexercise
Erzeugen Sie eine Liste mit Ihren drei Lieblingsgerichten. Verwenden Sie
`len()`, um die Länge der Liste zu bestimmen, und geben Sie sie aus.
```

```{code-cell} ipython
# Hier Ihr Code.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
gerichte = ['Pizza', 'Lasagne', 'Sushi']
print(len(gerichte))
```
````

## Elemente löschen mit del und remove

Die Verkettung der Listen führt dazu, dass die Listen länger werden. Die
Umkehrung davon fehlt noch, das Kürzen von Listen. Wie so oft in Python gibt es
mehrere Möglichkeiten, ein Element aus einer Liste zu entfernen, also zu
löschen. Die Anweisung `del` löscht das Element an einer bestimmten Position.
Zuerst kommt die Anweisung, dann das Listenelement mit Index:

```{code-cell} ipython3
meine_liste = ['Null', 'Eins', 'Zwei', 'Drei', 'Vier', 'Fünf']
print('Vor dem Löschen: ')
print(meine_liste)

del meine_liste[2]
print('Nach dem Löschen')
print(meine_liste)
```

Wie Sie sehen ist das dritte Element in der Liste gelöscht worden, da die
Nummerierung des Index bei 0 startet.

+++

Vielleicht möchte man aber gar nicht ein Element an einer bestimmten Position
löschen, sondern einen bestimmten Eintrag. Das folgende Beispiel implementiert
eine Einkaufsliste in Python. Sobald ein Lebensmittel gekauft ist, soll es von
der Liste gestrichen werden.

```{code-cell} ipython3
einkaufsliste = ['Milch', 'Kaffee', 'Brötchen', 'Marmelade']

print('Einkaufsliste: ')
print(einkaufsliste)

einkaufsliste.remove('Brötchen')
print('Nach dem Einkauf in der Bäckerei: ')
print(einkaufsliste)

einkaufsliste.remove('Milch')
einkaufsliste.remove('Kaffee')
einkaufsliste.remove('Marmelade')
print('Nach dem Einkauf im Supermarkt: ')
print(einkaufsliste)
```

Die Vorgehensweise, um das Element `Milch` zu löschen, ist diesmal komplett
anders. Diesmal hängen wir an die Variable `einkaufsliste` einen Punkt und dann
den Namen des Kommandos `remove()`. Wieso das?

Das Kommando `del` ist so wichtig und universell, dass es mit allen Containern
funktioniert. Daher ist dieser Befehl als eine sogenannte **Funktion** im
Python-Kern implementiert. Das Kommando `remove()` bezieht sich jedoch nur auf
die Liste. Daher ist dieser Befehl als eine sogenannte **Methode**
implementiert. Eine Methode ist eine Funktion, die zu einem Datentyp dazugehört.

In späteren Kapiteln werden wir selbst Funktionen und Methoden
(Objektorientierung) implementieren und auf die Unterschiede detaillierter
eingehen. Im Moment begnügen wir uns mit der Tatsache, dass es Funktionen wie

* input()
* print()
* del()

gibt und Methoden, die mit einem Punkt an das Objekt angehängt werden wie z.B.
`.remove()`.

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, wie man mit Listen mehrere Werte in Python
strukturiert speichern kann. Wir wissen nun, wie Listen erstellt, gelesen,
verändert, verkettet und verkürzt werden. Außerdem kennen wir mit `len()` eine
einfache Möglichkeit, die Länge einer Liste zu bestimmen. Diese Konzepte bilden
die Grundlage für viele weiterführende Themen wie Schleifen und Interaktionen,
die in späteren Kapiteln behandelt werden.
