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

# 5.3 Programmverzweigungen mit mehreren Zweigen: if -- elif -- else

In unserem Alltag kommen häufig Entscheidungen zwischen zwei Möglichkeiten vor.
Wenn ich an eine T-Kreuzung komme, muss ich mich entscheiden: links oder rechts?
Betrete ich ein Gebäude, entscheide ich zwischen Treppe und Fahrstuhl. Mein
Alter entscheidet darüber, ob ich etwas darf oder nicht darf. Für diese Wahl
zwischen zwei Möglichkeiten gibt es Programmverzweigungen mit zwei Weigen. Und
auch bei Programmverzweigungen mit zwei Zweigen hört es noch nicht auf, denn
vielleicht kommt man ja an eine Viererkreuzung. Daher behandeln wir in diesem
Kapitel Programmverzweigungen mit mehreren Zweigen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können Programmverzweigungen mit zwei Zweigen mittels **if - else**
  implementieren.
* Sie können mehrteilige Programmverzweigungen mit **if - elif - else**
  implementieren.
```

## Programmverzweigungen mit zwei Zweigen: if – else

Wir erweitern die Syntax mit dem if-Block um ein neues Element, nämlich den
sogenannten **else-Block**:

```python
if bedingung:
    anweisungsblock 1
else:
    anweisungsblock 2
```

Wichtig ist, dass die Anweisungen, die nur bedingt ausgeführt werden sollen,
eingerückt sind!

Falls die Bedingung erfüllt ist, wird der 1. Anweisungsblock ausgeführt,
ansonsten der 2. Anweisungsblock. Danach führt der Python-Interpreter alles nach
dem if-else-Konstrukt aus, d.h. der Interpreter macht mit dem normalen
Programmablauf weiter.

Hier erneut ein Beispiel mit dem Alter.

```python
alter = int(input('Wie alt sind Sie? '))
if alter >= 18:
    print('Sie sind volljährig, Sie dürfen Alkohol kaufen.')
else:
    print('Sie sind noch nicht volljährig und dürfen daher keinen Alkohol kaufen.')

print('Jetzt haben wir aber genug über den Alkoholkauf geredet...')
```

Wir vertiefen die zweifache Verzweigung mit einer Mini-Übung.

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Skript, das nach der aktuellen Temperatur fragt. Wenn die
aktuelle Temperatur kleiner gleich 3 ˚C ist, dann lassen Sie ausgeben:
"Vorsicht, es besteht Glatteisgefahr!" und ansonsten "Kein Grund zur Sorge."
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe
temperatur = float(input('Welche Temperatur haben wir aktuell?'))

# Verarbeitung und Ausgabe
if temperatur <= 3:
    print('Vorsicht, es besteht Glatteisgefahr!')
else:
    print('Kein Grund zur Sorge.')
```
````

## Programmverzweigungen mit vielen Zweigen: if – elif – else

Eins, zwei, drei -- viele ... häufig müssen mehr als zwei Fälle unterschieden
werden. In einer Mini-Übung haben wir beispielsweise überprüft, ob eine Zahl
negativ oder positiv oder Null ist. Ein Beispiel aus dem Alltag ist der Kauf
einer Fahrkarte für den ÖPNV. Meist wird beim Ticketpreis unterschieden, ob die
Person jünger als 6 ist (keine Fahrkarte notwendig), zwischen 6 und 14 ist
(Schülerfahrkarte) oder älter als 14 (Erwachsenenfahrkarte). Da es jetzt drei
Altersklassen gibt, können wir kein if-else-Konstrukt benutzen, denn nur weil
die Person beispielsweise nicht jünger als 6 ist wissen wir noch lange nicht, ob
die Person eine Schülerfahrkarte oder eine Erwachsenenfahrkarte braucht.

Beachten Sie die Wahl der Vergleichsoperatoren: Bei `alter <= 14` ist eine
Person mit genau 14 Jahren noch in der Kategorie 'Schülerfahrkarte'. Bei `alter
< 15` wäre dies ebenso der Fall. Überlegen Sie bei der Implementierung genau, ob
Randwerte in- oder exklusiv behandelt werden sollen.

Probieren wir es einfach:

```{code-cell} ipython3
alter = 8
if alter < 6:
    print('keine Fahrkarte notwendig')
if alter <= 14:
    print('Schülerfahrkarte')
if alter > 14:
    print('Erwachsenenfahrkarte')
```

Sieht zunächst einmal gut aus. Für ein Alter von 8 Jahren wird tatsächlich
Schülerfahrkarte ausgegeben. Wenn wir jetzt aber das Alter auf 5 Jahre setzen,
so bekommen wir zwei Ausgaben:

```{code-cell} ipython3
alter = 5
if alter < 6:
    print('keine Fahrkarte notwendig')
if alter <= 14:
    print('Schülerfahrkarte')
if alter > 14:
    print('Erwachsenenfahrkarte')
```

Wir erhalten die Ausgabe `"keine Fahrkarte notwendig"`, weil die Bedingung des
ersten if-Konstrukts erfüllt ist (`alter < 6`). Danach wird aber auch noch die
Ausgabe `"Schülerfahrkarte"` angezeigt, weil auch die Bedingung des zweiten
if-Konstrukts (`alter <= 14`) erfüllt ist. Diese Variante eignet sich also nicht
zur Unterscheidung dreier Bedingungen.

Probieren wir es mit einem zusätzlichen if-else-Konstrukt für die Unterscheidung
der Kinder.

```{code-cell} ipython3
alter = 5

if alter < 6:
    print('keine Fahrkarte notwendig')
else:
    print('Schülerfahrkarte')

if alter > 14:
    print('Erwachsenenfahrkarte')
```

Jetzt sind aber Erwachsene problematisch:

```{code-cell} ipython3
alter = 27

if alter < 6:
    print('keine Fahrkarte notwendig')
else:
    print('Schülerfahrkarte')

if alter > 14:
    print('Erwachsenenfahrkarte')
```

Der Programmcode funktioniert nur korrekt, wenn wir in den else-Zweig noch
zusätzlich zwischen "jünger als 14" und "älter als 14" unterscheiden.

Führen Sie die folgende Code-Zelle mehrfach aus. Ändern Sie dabei das Alter.
Probieren Sie beispielsweise 5, 8, 11, 16, 21 und Ihr Alter aus.

```{code-cell} ipython3
alter = 27

if alter < 6:
    print('keine Fahrkarte notwendig')
else:
    if alter <= 14:
        print('Schülerfahrkarte')
    else:
        print('Erwachsenenfahrkarte')
```

Um den obigen Code besser zu verstehen, zeichen wir den Ablauf schematisch:

```{image} pics/part02_fahrkarte.png
:name: part02_fahrkarte
```

Es wäre schöner, wenn es für solche Mehrfachverzweigungen etwas
übersichtlicheren Code gäbe. Und in der Tat, den gibt es. Man könnte sozusagen
den Start des else-Konstruktes mit dem nachfolgenden if-Konstrukt verschmelzen.
`elif` ist eine Kurzform für `else if` und ermöglicht es, mehrere Bedingungen
nacheinander zu prüfen, ohne die Einrückungstiefe zu erhöhen. Das Ergebnis davon
ist die if-elif-else-Syntax. Allgemein sieht das **if-elif-else-Konstrukt** so
aus:

```python
if bedingung 1:
    anweisungsblock 1
elif bedingung 2:
    anweisungsblock 2
elif bedingung 3:
    anweisungsblock 3   
...
else:
    anweisungsblock n
```

Wichtig: Bei einem if-elif-else-Konstrukt werden die Bedingungen der Reihe nach
geprüft. Sobald eine Bedingung erfüllt ist, wird der zugehörige Anweisungsblock
ausgeführt und alle nachfolgenden Bedingungen werden ignoriert. Daher ist die
Reihenfolge der Bedingungen entscheidend für die korrekte Funktionsweise des
Programms.

Hier die besser lesbare Version der Unterscheidung von Zahlen in negative
Zahlen, 0 und positive Zahlen aus der Mini-Übung:

```{code-cell} ipython3
a = 17
if a == 0:
    print('a ist Null.')
elif a < 0:
    print('a ist negativ.')
else:
    print('a ist positiv.')
```

Hier die besser lesbare Version des Fahrkartenautomaten:

```{code-cell} ipython3
alter = 27

if alter < 6:
    print('keine Fahrkarte notwendig')
elif alter <= 14:
    print('Schülerfahrkarte')
else:
    print('Erwachsenenfahrkarte')
```

````{admonition} Mini-Übung
:class: miniexercise
Sie finden den aktuellen Bußgeldkatalog für Geschwindigkeitsüberschreitungen mit
dem PKW im Internet auf der Seite:
https://www.bussgeldkatalog.org/geschwindigkeitsueberschreitung/ Schreiben Sie
ein Skript, dass abhängig von der Geschwindigkeitsüberschreitung ausgibt,
welche Strafe in Euro verhängt wird. Die Tabelle für das Jahr 2022 lautet wie
folgt:
```{image} pics/part02_bussgeldkatalog.png
:name: part02_bussgeldkatalog
```
````

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe
verstoss = int(input('Wieviel zu schnell ist die Person gefahren? '))

# Verarbeitung und Ausgabe
if verstoss <= 10:
    print('20 EUR')
elif verstoss <= 15: 
    print('40 EUR')
elif verstoss <= 20:
    print('60 EUR')
elif verstoss <= 25:
    print('100 EUR')
elif verstoss <= 30:
    print('150 EUR')
elif verstoss <= 40:
    print('200 EUR')
elif verstoss <= 50:
    print('320 EUR')
elif verstoss <= 60:
    print('480 EUR')
elif verstoss <= 70:
    print('600 EUR')
else:
    print('700 EUR')
```
````

Wenn Sie das Thema elif/else vertiefen wollen, können Sie sich das folgende
Video ansehen.

```{dropdown} Video "elif und else" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/f3YdEdYSNdk"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, wie man mit if, elif und else in Python
Programmverzweigungen mit zwei oder mehr Entscheidungszweigen umsetzt, um
unterschiedliche Fälle gezielt abzufragen und übersichtlich zu strukturieren. Im
nächsten Kapitel werden wir die Strukturierung des Code in kleinere Einheiten
erlernen (Funktionen).
