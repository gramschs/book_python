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

# 5.1 Vergleiche und der boolesche Datentyp

Viele Möglichkeiten unserer Gesellschaft stehen nur Volljährigen offen und sind
damit an eine Altersangabe gebunden. Wenn jetzt ein Computersystem vorab prüfen
soll, ob Volljährigkeit vorliegt oder nicht, dann brauchen wir einen einfachen
Vergleich. Daher beschäftigen wir uns in diesem Kapitel mit Vergleichen und dem
Datentyp Bool.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie kennen den Datentyp **Bool** mit seinen beiden Werten `True` und `False`.
* Sie kennen die wichtigsten **Vergleichsoperatoren** für Zahlen und Strings.
```

## Der Datentyp Bool

Zurück zu dem Beispiel mit der Überprüfung der Volljährigkeit. Angenommen, wir
speichern das Alter der Benutzers oder der Benutzerin in der Variable `alter`.
Damit wäre ein simples Beispiel für eine einfache Bedingung der mathematische
Ausdruck `alter < 18`. Der Wert der Variablen `alter` wird also mit der Zahl 18
verglichen. Dieser Vergleich ist entweder **wahr (True)** oder **falsch
(False)**. Oder anders formuliert, diese Bedingung ist entweder erfüllt oder
nicht erfüllt.

Um den Wahrheitswert einer Bedingung zu speichern, hat Python einen eigenen
Datentyp, einen sogenannten booleschen Datentyp. Nach dem englischen Wort wird
dieser Datentyp in der Informatik üblicherweise **Bool** oder **Boolean**
genannt. Das besondere an diesem Datentyp ist, dass eine Variable diesen
Datentyps nur zwei verschiedene Werte annehmen kann, nämlich

* True: Wahrheitswert ist wahr oder
* False: Wahrheitswert ist falsch.

Aber wie kann man dann überprüfen, welcher Datentyp in einer Variablen
gespeichert ist? Dazu gibt es das Kommando `type`. Führen Sie die nächste
Code-Zelle aus.

```{code-cell} ipython3
a = False
type(a)
```

## Vergleiche mit Zahlen

Nachdem wir jetzt den Datentyp kennengelernt haben, mit dem Python das Ergebnis
eines Vergleichs speichert, kommen wir nun zu dem Vergleich selbst.

Zunächst beschäftigen wir uns mit mathematischen Vergleichen. In der Mathematik
ist ein Vergleich ein Ausdruck mit zwei Argumenten und einem Vergleichsoperator
in der Mitte. Die beiden Argumente können auch unterschiedliche Datentypen
haben, dann muss der Vergleichsoperator aber sinnvoll für diese Datentypen
definiert sein. Zum Beispiel darf man einen Integer mit einem Float vergleichen

`3 < 17.2`

aber

`3 < 'vier'`

ist nicht sinnvoll und undefiniert. Es gibt die folgenden Vergleichsoperatoren
in Python:

* `<`   kleiner
* `<=`  kleiner oder gleich
* `>`   größer
* `>=`  größer oder gleich
* `==`  gleich
* `!=` ungleich

Im interaktiven Modus von Python können wir leicht den Wahrheitsgehalt von
Vergleichen überprüfen. Wir setzen eine Variable auf den Wert 7:

```{code-cell} ipython3
x = 7
```

Jetzt probieren wir in den nachfolgenden Code-Zellen verschiedene
Vergleichsoperatoren aus.

Ist x genau gleich 15?

```{code-cell} ipython3
x == 15    
```

Ist x kleiner als 42?

```{code-cell} ipython3
x < 42
```

Ist x genau 30?

```{code-cell} ipython3
x == 30
```

Ist x ungleich 42?

```{code-cell} ipython3
x != 42 
```

Ist x größer als 30?

```{code-cell} ipython3
x > 30
```

Ist x größer gleich 30?

```{code-cell} ipython3
x >= 30
```

```{admonition} Mini-Übung
:class: miniexercise
Wählen Sie sich eine Zahl. Testen Sie anschließend:
* Ist Ihre Zahl kleiner gleich 5?
* Ist Ihre Zahl genau 17?
* Ist Ihre Zahl nicht gleich 17?
* Ist Ihre Zahl positiv?
* Ist Ihre Zahl kleiner als -17.7?
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe: Wahl meiner Zahl
x = 33

# kleiner gleich 5?
x <= 5

# genau gleich 17?
x == 17

# nicht gleich 17?
x != 17

# positiv?
x > 0

# kleiner als -17.7?
x < -17.7
```
````

```{dropdown} Video "Vergleiche in Python" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/ucsv_Nhhxmk"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Vergleiche mit Strings

Als nächstes werden wir uns mit der Verwendung von Strings in Vergleichen
beschäftigen. Strings werden häufig in Vergleichen verwendet, um festzustellen,
ob zwei Strings gleich sind oder ob ein String in einem anderen enthalten ist.

Um festzustellen, ob zwei Strings in Python gleich sind, können wir den
Gleichheitsoperator `==` verwenden. Der Gleichheitsoperator gibt `True` zurück,
wenn die beiden Strings exakt übereinstimmen, und `False`, wenn sie sich
unterscheiden.

```{code-cell} ipython3
string01 = 'Hallo'
string02 = 'Welt'
string03 = 'Hallo'
string04 = 'hallo'

print(string01 == string02)  # Ausgabe: False
print(string01 == string03)  # Ausgabe: True
print(string01 == string04)  # Ausgabe: False
```

In diesem Beispiel sind die Strings `string01` und `string03` gleich. Der String
`string02` ist jedoch unterschiedlich von `string01`, daher ist das Ergebnis
`False`. Beachten Sie auch, dass der String `string04` nicht gleich `string01`
ist, obwohl er den gleichen Wert hat, da Groß- und Kleinschreibung in Python bei
der Vergleichsoperation berücksichtigt werden.

Um zu überprüfen, ob ein String in einem anderen enthalten ist, können wir den
Operator `in` verwenden. Der Operator `in` gibt `True` zurück, wenn der String
in dem anderen String enthalten ist, und `False`, wenn nicht.

```{code-cell} ipython3
string01 = 'Hallo Welt'
string02 = 'Welt'
string03 = 'Python'

print(string02 in string01)  # Ausgabe: True
print(string03 in string01)  # Ausgabe: False
```

In diesem Beispiel ist der String `string02` in dem String `string01` enthalten,
daher ist das Ergebnis `True`. Der String `string03` ist jedoch nicht in
`string01` enthalten, daher ist das Ergebnis `False`.

Beachten Sie, dass bei der Überprüfung die Groß- und Kleinschreibung in Python
beachtet werden muss. Wenn wir also nach dem String `'welt'` suchen, erhalten wir
`False`, da der String `'Welt'` großgeschrieben ist.

Wir können auch andere Vergleichsoperationen wie <, >, <=, >= mit Strings
verwenden. Diese Operationen vergleichen die Strings nach ihrem
lexikographischen Wert, d.h. sie vergleichen die Zeichen eines Strings in der
Reihenfolge, in der sie auftreten.

```{code-cell} ipython3
a = "Apfel"
b = "Banane"

print(a < b)  # Ausgabe: True
print(a > b)  # Ausgabe: False
print(a <= b)  # Ausgabe: True
print(a >= b)  # Ausgabe: False
```

In diesem Beispiel ist `'Apfel'` kleiner als `'Banane'`, da "A" im Alphabet vor
"B" steht, daher ist das Ergebnis des `<`-Operators `True`. Der `>`-Operator
gibt `False` zurück, da `'Apfel'` nicht größer als `'Banane'` ist. Der
`<=`-Operator gibt `True` zurück, da `'Apfel'` kleiner oder gleich `'Banane'`
ist. Der `>=`-Operator gibt `False` zurück, da `'Apfel'` nicht größer oder
gleich `'Banane'` ist.

````{admonition} Mini-Übung
:class: miniexercise
Gegeben sind die folgenden Strings:
```python
material1 = "Stahl"
material2 = "Aluminium"
material3 = "Stahllegierung"
material4 = "aluminium"
```
Überprüfen Sie folgende Vergleiche und notieren Sie, ob das Ergebnis `True` oder
`False` ist:

1. Ist `material1` lexikographisch größer als `material2`?
2. Enthält `material3` den String `material1`?
3. Sind `material2` und `material4` identisch?
4. Überprüfen Sie mit dem `in-`Operator, ob die Zeichenfolge "leg" in
   `material3` vorkommt.
5. Ist `material4` lexikographisch kleiner als `material1`?
````

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
material1 = "Stahl"
material2 = "Aluminium"
material3 = "Stahllegierung"
material4 = "aluminium"

# 1. Ist material1 lexikographisch größer als material2?
print(material1 > material2)  # True, da 'S' im Alphabet nach 'A' kommt

# 2. Enthält material3 den String material1?
print(material1 in material3)  # True, da "Stahl" in "Stahllegierung" enthalten ist

# 3. Sind material2 und material4 identisch?
print(material2 == material4)  # False, da Groß-/Kleinschreibung unterschiedlich ist

# 4. Überprüfen Sie mit dem in-Operator, ob die Zeichenfolge "leg" in material3 vorkommt.
print("leg" in material3)  # True, da "leg" in "Stahllegierung" enthalten ist

# 5. Ist material4 lexikographisch kleiner als material1?
print(material4 < material1)  # False, da Großbuchstaben im ASCII-Code vor Kleinbuchstaben kommen
```
````

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir den booleschen Datentyp Bool mit seinen Werten True
und False kennengelernt. Wir haben Vergleichsoperatoren (<, >, ==, !=, <=, >=)
für Zahlen und Strings untersucht und gesehen, wie String-Vergleiche auf
lexikographischer Ordnung basieren. Außerdem haben wir den 'in'-Operator zur
Überprüfung von Teil-Strings kennengelernt.
