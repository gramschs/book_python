---
jupytext:
  cell_metadata_filter: -all
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Datentypen und Variablen

TODO

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie wissen, was **Datentypen** sind.
* Sie kennen den Unterschied zwischen **Ganzzahlen** und **Fließkommazahlen**
  und die dazugehörigen Datentypen **Integer** und **Float**.
```

## Los geht es mit dem Programmieren - Datentypen in Python

Der Computer kann Informationen nur als 0 oder 1 verarbeiten. Auf dem
Speichermedium oder im Speicher selbst werden Daten daher als eine Folge von 0
und 1 gespeichert. Damit es für uns Programmiererinnen und Programmierer
einfacher wird, Daten zu speichern und zu verarbeiten, wurden Datentypen
eingeführt.  

**Datentypen** fassen gleichartige Objekte zusammen und stellen passende
Operationen zur Verfügung. Es hängt von der Programmiersprache ab, welche
Datentypen zur Verfügung stehen, wie diese im Hintergrund gespeichtert werden
und welche Operationen damit möglich sind. In diesem Kapitel beschäftigen wir
uns mit den einfachen Datentypen

* Integer
* Float
* String

### Zahlen 

In der Programmierung unterscheidet man grundsätzlich zwischen zwei Zahlenarten,
den **Ganzzahlen** und den Gleitkommazahlen, die auch **Fließkommazahlen**
genannt werden. Die Ganzzahlen werden in der Mathematik als ganze Zahlen
bezeichnet. In der Informatik wird meist der englische Begriff **Integer**
verwendet. Mit Integern können wir ganz normal rechnen, also Operationen
ausführen. Einige davon haben wir ja bereits ausprobiert, als wir Python als
Taschenrechner benutzt haben:

```{code-cell} ipython3
2 * (3 + 4)
```

Sobald wir eine Division vorliegen haben, die nicht aufgeht, verlassen wir den
Bereich der ganzen Zahlen und kommen automatisch zu den Fließkommazahlen. In der
Informatik wird eine Fließkommazahl als Float bezeichnet. Python rechnet
automatisch mit dem richtigen Datentyp, wie Sie hier sehen:

```{code-cell} ipython3
2/5
```

Beachten Sie bitte: Das Dezimaltrennzeichen ist ein Punkt, nicht ein Komma wie
im Deutschen. Aber ansonsten funktioniert alles wie erwartet:

```{code-cell} ipython3
2.3 + 4.6
```

```{code-cell} ipython3
1.4 - 5.2
```

```{code-cell} ipython3
(-3.8) * 3.1
```

```{code-cell} ipython3
2.4 / 0.3
```

```{code-cell} ipython3
2.5**10
```

Das folgende Video fasst Zahlen in Python zusammen.

```{code-cell} ipython3
:tags: [remove-input]

IFrame(width=560, height=315, src="https://www.youtube.com/embed/VtiDkRDPA_c")
```

### Strings

Daten sind aber sehr oft keine Zahlen. Beispielsweise könnte man sich
vorstellen, eine Einkaufsliste zu erstellen und diese im Computer oder in einer
Notiz-App auf dem Handy zu speichern. Eine solche Zeichenkette heißt in der
Informatik **String**. Mit Zeichen meint man dabei Zahlen, Buchstaben oder
andere wie beispielsweise !"§$%&/()=?.

Strings werden in Python durch doppelte Anführungszeichen definiert:

```{code-cell} ipython3
"Dies ist ein String!"
```

Auf Strings und ihre Anwendungen kommen wir später noch zurück. Wenn Sie bereits
jetzt mehr erfahren wollen, können Sie sich folgendes Video ansehen.

```{code-cell} ipython3
:tags: [remove-input]

IFrame(width=560, height=315, src="https://www.youtube.com/embed/sTEf4_mrLvw")
```