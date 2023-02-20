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

# Vergleiche und der boolesche Datentyp

Viele Möglichkeiten unserer Gesellschaft stehen nur Volljährigen offen und sind
damit an eine Altersangabe gebunden. Wenn jetzt ein Computersystem vorab prüfen
soll, ob Volljährigkeit vorliegt oder nicht, dann brauchen wir einen einfachen
Vergleich. Angenommen, wir würden das Alter der Benutzers oder der Benutzerin in
der Variable `alter` speichern. Damit wäre ein simples Beispiel für eine
einfache Bedingung der mathematische Ausdruck `alter < 18`. Der Wert der
Variablen `alter` wird also mit der Zahl 18 verglichen. Dieser Vergleich ist
entweder **wahr (True)** oder **falsch (False)**. Oder anders formuliert, ist
diese Bedingung entweder erfüllt oder nicht erfüllt. 

Um den Wahrheitswert einer Bedingung zu speichern, hat Python einen eigenen
Datentyp, einen sogenannten booleschen Datentyp. Nach dem englischen Wort wird
dieser Datentyp in der Informatik üblicherweise **Boolean** genannt. Das
besondere an diesem Datentyp ist, dass eine Variable diesen Datentyps nur zwei
verschiedene Werte annehmen kann, nämlich
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

Nachdem wir jetzt den Datentyp kennegelernt haben, mit dem Python das Ergebnis
eines Vergleichs speichert, kommen wir nun zu dem Vergleich selbst.

Zunächst beschäftigen wir uns mit mathematischen Vergleichen. In der Mathematik
ist ein Vergleich ein Ausdruck mit zwei Argumenten und einem Vergleichsoperator
in der Mitte. Die beiden Argumente können auch unterschiedliche Datentypen
haben, dann muss der Vergleichsoperator aber sinnvoll für diese Datentypen
definiert sein. Z.B. darf man einen Integer mit einem Float vergleichen 

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
* `!= ` ungleich

Im interaktiven Modus von Python können wir leicht den Wahrheitsgehalt von Vergleichen überprüfen. Wir setzen eine Variable auf den Wert 7:
```{code-cell} ipython3
x = 7
```
Jetzt probieren wir in den nachfolgenden Code-Zellen verschiedene Vergleichsoperatoren aus. Zur Erinnerung, 0 steht dabei für false (falsch) und 1 für wahr (true).

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
:class: minisolution, toggle
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

<iframe width="560" height="315" src="https://www.youtube.com/embed/ucsv_Nhhxmk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>