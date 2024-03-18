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

# 6.3 Lokale und globale Variablen

In Python gibt es zwei Arten von Variablen: lokale und globale Variablen. Der
Unterschied zwischen beiden liegt in ihrem Geltungsbereich, also wo im Programm
sie verwendet werden können. Vor allem bei der Definition von Funktionen ist die
Nichtbeachtung des Unterschieds eine häufige Fehlerquelle, weshalb wir in diesem
Kapitel den Unterschied beleuchten.

## Lernziele

```{admonition} Lernziele
:class: admonition-goals
Sie kennen den Unterschied zwischen **lokalen** und **globalen** Variablen.
```

## Lokale Variablen

Schauen Sie sich bitte folgende Funktionsimplementierung an. Was macht die
Funktion?

```{code-cell} ipython3
def erhoehe_um_eins(x):
    x = x + 1
```

Probieren wir es aus.

```{code-cell} ipython3
x = 17

print(f'Vor der Anwendung der Funktion ist x = {x}.')
erhoehe_um_eins(x)
print(f'Nach der Anwendung der Funktion ist x = {x}.')
```

Wir schauen in die Funktion "hinein", um zu sehen, ob vielleicht gar nicht
erhöht wurde.

```{code-cell} ipython3
def erhoehe_um_eins(x):
    print(f'Im Inneren der Funktion vor der Erhöhung ist x = {x}.')
    x = x + 1
    print(f'Im Inneren der Funktion nach der Erhöhung ist x = {x}.') 
```

Jetzt probieren wir nochmal aus, die Funktion auf `x = 17` anzuwenden:

```{code-cell} ipython
x = 17

print(f'Vor der Anwendung der Funktion ist x = {x}.')
erhoehe_um_eins(x)
print(f'Nach der Anwendung der Funktion ist x = {x}.')
```

Was ist passiert? Die Variable `x` in der Funktion ist eine **lokale Variable**.
Lokale Variablen sind Variablen, die innerhalb einer Funktion definiert werden.
Ihr Geltungsbereich ist auf die Funktion beschränkt, in der sie definiert
wurden. Das bedeutet, dass sie innerhalb der Funktion verwendet werden können,
aber außerhalb der Funktion nicht sichtbar oder zugänglich sind.

Es ist Absicht, dass Python strikt darauf achtet, lokale Variablen auf ihren
Geltungsbereich zu beschänken. Die Programmierer:innen einer Funktion können
vorab nicht wissen, wie alle anderen Variablen im Hauptprogramm heißen. Daher
müssen alle Variablen in der Funktion lokal bleiben, um nicht unabsichtlich
Variablen, die zufälligerweise den gleichen Namen tragen, zu überschreiben.

Möchte man erreichen, dass eine Funktion den Wert einer Variable ändert, kann
man dies über die Rückgabe und explizite Zuweisung erreichen. Dann ist aber
jedem Programmier und jeder Programmiererin, die diese Funktion benutzt,
explizit klar, dass damit der Wert der Variablen geändert wird.

```python
# modifizierte Funktion mit Rückgabe
def erhoehe_um_eins(x):
    x = x + 1
    return x

# Test
x = 17

print(f'Vor der Anwendung der Funktion ist x = {x}.')
x = erhoehe_um_eins(x)
print(f'Nach der Anwendung der Funktion ist x = {x}.')
```

## Globale Variablen

Globale Variablen sind Variablen, die außerhalb von Funktionen definiert werden.
Ihr Geltungsbereich erstreckt sich über das gesamte Programm, was bedeutet, dass
sie sowohl innerhalb als auch außerhalb von Funktionen verwendet werden können.
Das scheint zunächst unserem Experiment, eine Zahl um 1 zu erhöhen zu
widersprechen. Tatsächlich ist die Verwendung einer globalen Variable innerhalb
einer Funktion nur lesend möglich. Um auch einen Schreibzugriff zu erlauben,
gibt es die Möglichkeit, eine Variable als `global` zu definieren. Meine
persönliche Meinung ist aber, dass die Verwendung von globalen Variablen zu
fehleranfällig ist. Daher werde ich auf dieses Thema nicht weiter eingehen.

