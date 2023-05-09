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

# 7.1 Digitale Logik: und, oder, nicht

In diesem Kapitel beschäftigen wir uns zuerst damit, wie kombinierte Bedingungen
in der Programmiersprache Python formuliert werden. In der Informatik bezeichnet
man dieses Themenfeld auch als **digitale Logik** oder **boolesche Algebra**. 

## Lernziele

```{admonition} Lernziele
:class: tip
Sie kennen die logischen Operatoren und können diese in Python einsetzen:
* logisches UND: `and`
* logisches ODER: `or`
* logisches NICHT: `not`
```

## Boolesche Algebra

In früheren Kapiteln haben wir den boolschen Datentyp kennengelernt: wahr oder
falsch. Man kann solche Ausdrücke auch kombinieren, z.B. könnte man fordern,
dass zwei Bedingungen gleichzeitg erfüllt sein sollen.

Beispiel beim Busfahren: Kinder unter 6 Jahren können kostenlos Bus fahren. Ab 6
Jahren braucht man eine Fahrkarte. Bis 14 Jahre zahlt man den Kinderpreis, ab 15
Jahren den Erwachsenenpreis. Die Bedingung für eine Kinderkarte lautet also:

$$\text{Alter} \geq 6 \text{ und } \text{Alter} \leq 14.$$

Keine Kinderfahrkarte braucht man, wenn man jünger als 6 ist oder älter als 14,
also:

$$\text{Alter} < 6 \text{ oder } \text{Alter} > 14.$$

Eine Fahrkarte (egal ob Kinderfahrkarte oder Erwachsenenfahrkarte) muss
mankaufen, wenn man kein Kind ist, also wenn

$$\text{nicht} \left( \text{Alter} < 6\right).$$

Gut, letzteres könnte man natürlicher einfacher mit $\text{Alter} \geq 6$
ausdrücken, aber das klappt auch nicht bei jeder Bedingung.

Im Folgenden beschäftigen wir uns daher mit der Verknüpfung von booleschen
Ausdrücken. Dieses Fachgebiet nennt man auch boolsche Algebra oder digitale
Logik. Wikipedia fasst hier die wichtigsten Regeln zur booleschen Algebra
zusammen: https://de.wikipedia.org/wiki/Boolesche_Algebra 

Wir werden in dieser Vorlesung uns aber auf die logischen Verknüpfungen oder
logischen Operatoren 

* UND
* ODER
* NICHT

beschränken. 

## Das logische UND

Beim logischen UND müssen beide Bedingungen erfüllt sein, damit insgesamt die
kombinierte Bedingung erfüllt ist. Vergleichbar ist dies mit einer
Reihenschaltung in der Elektrotechnik. Nur wenn beide Schalter eingeschaltet
sind, kann der Strom fließen.

Hier finden Sie den Link zu einem YouTube-Video (ca. 3:14 min) von Lehrer Schmidt zur UND-Schaltung:

https://www.youtube.com/watch?v=79WVEr2BVZI

Man schreibt die Ergebnisse der kombinierten Bedingungen normalerweise als eine
Tabelle auf. Die erste Zeile würde man so lesen: Wenn “Bedingung 1 wahr” ist UND
wenn “Bedingung 2 wahr” ist, so ist auch die kombinierte Bedingung “Bedingung 1
UND Bedingung 2” wahr. Wir verwenden hier schon die Python-Werte `True` für wahr
und `False` für falsch sowie den `and`-Operator für das logische UND:

Bedingung 1 | Bedingung 2 | Ergebnis mit ```and```
------------|-------------|--------------------------
True | True | True
False | True | False
True | False | False
False | False | False

Beispiel: Zwei Personen wollen einen Kinofilm sehen, der erst ab 18 erlaubt ist.
Nur wenn beide volljährig sind, können sie den Film gemeinsam besuchen:

```{code-cell} ipython3
alter_person1 = 19
alter_person2 = 22
if (alter_person1 >= 18) and (alter_person2 >= 18):
    print('Sie duerfen beide den Film sehen.')
else:
    print('Vielleicht darf einer von Ihnen den Film sehen, aber nicht beide.')
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Skript, das nach dem Alter einer Person fragt. Wenn das Alter
der Person zwischen 6 und 10 liegt, soll das Programm ausgeben “Wahrscheinlich
gehst Du in die Grundschule.”
```
```{code-cell} ipython3
# Hier Ihr Code
```
````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe
alter = int(input('Wie alt sind Sie?'))

# Verarbeitung und Ausgabe
if (6 <= alter) and (alter <= 10):
    print('Wahrscheinlich gehst Du in die Gundschule.')
```
````

## Das logische ODER

Beim logischen ODER muss nur eine der beiden Bedingungen erfüllt sein, damit
insgesamt die kombinierte Bedingung erfüllt ist. Damit ist natürlich die
Bedingung insgesamt auch erfüllt, wenn beide Bedingungen wahr sind. Vergleichbar
ist dies mit einer Parallelschaltung in der Elektrotechnik. Es reicht, wenn
einer der beiden Schalter eingeschaltet sind, damit der Strom fließen kann. Auch
wenn beide Schalter eingeschaltet sind, fließt Strom.

Hier finden Sie den Link zu einem YouTube-Video (ca. 2:42 min) von Lehrer
Schmidt zur ODER-Schaltung: https://www.youtube.com/watch?v=UNkXbvSN9w8

Auch bei der ODER-Verknüpfung schreibt man üblicherweise die Ergebnisse der
kombinierten Bedingungen in Form einer Tabelle. Die dritte Zeile würde man
beispielsweise so lesen: Wenn “Bedingung 1 wahr” ist ODER wenn “Bedingung 2
falsch” ist, so ist auch die kombinierte Bedingung “Bedingung 1 ODER Bedingung
2” wahr. Wir verwenden hier wiederum die Python-Werte `True` für wahr und
`False` für falsch sowie den logischen Oder-Operator `or`:

Bedingung 1 | Bedingung 2 | Ergebnis mit ```or```
------------|-------------|--------------------------
True | True | True
False | True | True
True | False | True
False | False | False

Beispiel: Zwei Personen wollen ein Auto mieten, dazu muss aber mindestens einer
von beiden den Führerschein besitzen.

```{code-cell} ipython3
person1_hat_fuehrerschein = True
person2_hat_fuehrerschein = False

if (person1_hat_fuehrerschein == True) or (person2_hat_fuehrerschein == True):
    print('Sie duerfen das Auto mieten.')
else:
    print('Keiner von beiden hat einen Fuehrerschein, geht nicht.')
```

Übrigens, der Vergleich `person1_hat_fuehrerschein == True` ist eigentlich
doppelt gemoppelt, da ja die Variable bereits den Datentyp bool hat. Wir könnten
also auch kürzer schreiben

```{code-cell} ipython3
person1_hat_fuehrerschein = True
person2_hat_fuehrerschein = False

if person1_hat_fuehrerschein or person2_hat_fuehrerschein :
    print('Sie duerfen das Auto mieten.')
else:
    print('Keiner von beiden hat einen Fuehrerschein, geht nicht.')
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Skript, das nach dem Alter einer Person fragt. Wenn die Person
jünger als 18 ist oder älter als 67, soll das Programm ausgeben: “Wahrscheinlich
sind Sie/bist Du nicht berufstätig.”
```
```{code-cell} ipython3
# Hier Ihr Code
```
````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe
alter =  int(input('Alter: '))

# Verarbeitung und Ausgabe
if (alter < 18) or (67 < alter):
    print('Wahrscheinlich sind Sie/bist Du nicht berufstätig.')
```
````

## Das logische NICHT

Das logische NICHT kehrt eine Aussage um. Wenn eine Bedingung wahr war, wird sie
falsch. War jedoch die Bedingung vorher wahr, wird sie nach Anwendung des
logischen NICHT falsch. Man schreibt auch diese Operation normalerweise als
Tabelle auf, wobei wir den logischen Nicht-Opertor `not` verwenden:

Bedingung 1 | Ergebnis mit ```not```
------------|--------------------------
True | False
False | True 

Beispiel: Wenn eine Person keinen Führerschein hat, muss sie den Bus nehmen.

```{code-cell} ipython3
person_hat_fuehrerschein = False

if not person_hat_fuehrerschein:
    print('Sie muessen Bus fahren.')
else:
    print('Sie duerfen Auto fahren.')
```

```{admonition} Mini-Übung
:class: miniexercise
Überlegen Sie zunächst, was ist das Ergebnis der folgenden Verknüpfungen: wahr
oder falsch?

* wahr UND wahr
* wahr ODER falsch
* NICHT wahr
* falsch ODER wahr
* wahr ODER (NICHT falsch)
* (NICHT wahr) UND falsch
* NICHT (wahr ODER falsch)
* (NICHT falsch) ODER (falsch UND falsch)

Probieren Sie dann in der nächsten Code-Zelle aus, ob Sie die richtigen
Ergebnisse hatten, indem Sie beispielsweise wahr und wahr in Python
ausprobieren, also beispielsweise `True and True` eingeben.
```
```{code-cell} ipython3
# Hier Ihr Code
```
````{admonition} Lösung
:class: minisolution, toggle
```python
# wahr UND wahr
True and True

# wahr ODER falsch
True or False

# NICHT wahr
not True

# falsch ODER wahr
False or True

# wahr ODER (NICHT falsch)
True or (not False)

# (NICHT wahr) UND falsch
(not True) and False

# NICHT (wahr ODER falsch)
not (True or False)

# (NICHT falsch) ODER (falsch UND falsch)
(not False) or (False and False)
```
````

## Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/075l6R42tkQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




