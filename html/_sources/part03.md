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

# Programmverzweigung (if - elif - else)

## Einführung und Lernziele

Bisher haben wir kleinere Skripte geschrieben, bei denen die Anweisungen Zeile
für Zeile ausgeführt wurden. Ein Programm oder Skript, das nur aus einer
einfachen Aneinanderreihung von Befehlen besteht, nennt man linear. Bisher
hatten wir also nur lineare Programme.

In diesem und in den nächsten Skripten werden wir uns mit dem Thema
**Kontrollstruktur** beschäftigen. Kontrollstrukturen dienen dazu, den linearen
Ablauf der Programme oder Skripte aufzubrechen und beispielsweise auf Eingaben
der Benutzerinnen und Benutzer zu reagieren. Wir starten dazu mit der
Kontrollstruktur **Programmverzweigung**. Wenn ein Skript auf eine Eingabe oder
auf den aktuellen Zustand einer Variable reagieren soll, muss der
Python-Interpreter in der Lage sein, Vergleiche zu ziehen und entscheiden zu
können. Daher beschäftigen wir uns vorher mit dem **Datentyp Bool** und
**Vergleichen**.

## Der boolesche Datentyp

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


## Programmverzweigungen mit einen Zweig: if

Bei einer Programmverzweigung wird Code abhängig von einer Bedingung ausgeführt.
Im einfachsten Fall liegt ein if-Block vor. Die Syntax lautet wie folgt:

```python
if bedingung:
    anweisungsblock
```

Ist die Bedingung erfüllt, also "True", so wird der eingerückte Anweisungsblock
ausgeführt, ansonsten übersprungen. Damit ist gemeint, dass der
Python-Interpreter nach dem Ende des if-Blocks weiter macht, falls die Bedingung
nicht erfüllt (= False) wird.

Wir betrachten nun ein Beispiel:

```{code-cell} ipython3
alter = 17
if alter >= 18:
    print('Sie dürfen Alkohol kaufen.')
print('Bananen dürfen Sie immer kaufen, egal wie alt Sie sind ...')
```

Und könnte beispielsweise mit einer Benutzerabfrage kombiniert werden:
```python
alter = int(input('Wie alt sind Sie?'))
if (alter >= 18):
    print('Sie dürfen Alkohol kaufen.')
print('Bananen dürfen Sie immer kaufen, egal wie alt Sie sind...')
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Skript, das einen Benutzer oder eine Benutzerin nach der aktuellen Temperatur fragt. Wenn die Temperatur kleiner gleich 10 ˚C ist, soll ausgegeben werden: "Heute ist es aber kalt!"
```
```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```
````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe
temperatur = int(input('Welche Temperatur haben wir aktuell?'))

# Verarbeitung und Ausgabe
if temperatur <= 10:
    print('Heute ist es aber kalt!')
```
````

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Skript, das eine Benutzerin oder einen Benutzer nach einer Zahl fragt. 
Wenn die Zahl kleiner als 0 ist, soll ausgegeben werden: "Die Zahl ist negativ."
Wenn die Zahl genau gleich 0 ist, soll ausgegeben werden: "Die Zahl ist Null."
Wenn die Zahl größer als 0 ist, soll ausgegeben werden: "Die Zahl ist positiv."

Wie viele if-Blöcke brauchen Sie für die Umsetzung dieser Mini-Übung?
```
```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```
````{admonition} Lösung
:class: minisolution, toggle
```python
% Eingabe
zahl = float(input('Geben Sie bitte eine Zahl ein: '))

% Verarbeitung und Ausgabe
if zahl < 0:
    print('Die Zahl ist negativ.')

if zahl == 0:
    print('Die Zahl ist Null.')

if zahl > 0:
    print('Die Zahl ist positiv.')
```

Der Code erfordert drei if-Blöcke.
````

<iframe width="560" height="315" src="https://www.youtube.com/embed/b6KzYbM-Hvg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Programmverzweigungen mit zwei Zweigen: if – else

In unserem Alltag kommen häufig Entscheidungen zwischen zwei Möglichkeiten vor.
Wenn ich an eine T-Kreuzung komme, muss ich mich entscheiden: links oder rechts?
Betrete ich ein Gebäude entscheide ich zwischen Treppe oder Fahrstuhl. Mein
Alter entscheidet darüber, ob ich etwas darf oder nicht darf. Für diese Wahl
zwischen zwei Möglichkeiten gibt es **zweiteilige Programmverzweigungen**. 

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

Hier wieder das Beispiel mit dem Alter:  

```python
alter = int(input('Wie alt sind Sie? '))
if alter >= 18:
    print('Sie sind volljährig, Sie dürfen Alkohol kaufen.')
else:
    print('Sie sind noch nicht volljährig und dürfen daher keinen Alkohol kaufen.')

print('Jetzt haben wir aber genug über den Alkoholkauf geredet...')
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Skript, das nach dem aktuellen Monat fragt (1 für Januar, 2
für Februar, 3 für März, usw.). Wenn der aktuelle Monat Januar bis Juni ist,
soll ausgegeben werden: "Dieser Monat gehört zur 1. Jahreshälfte." Ansonsten
soll ausgegeben werden: "Dieser Monat gehört zur 2. Jahreshälfte."
```
```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```
````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe
monat = int(input('Geben Sie bitte den aktuellen Monat ein, 1 für Januar, 2 für Februar usw.'))

# Verarbeitung und Ausgabe
if monat <= 6:
    print('Dieser Monat gehört zur 1. Jahreshälfte.')
else:
    print('Dieser Monat gehört zur 2. Jahreshälfte.')
```
````

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
:class: minisolution, toggle
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

## Programmverzweigungen mit vielen Zweigen: if – elseif – else

Eins, zwei, drei, viele ... häufig müssen mehr als zwei Fälle unterschieden
werden. In einer Mini-Übung haben wir beispielsweise überprüft, ob eine Zahl
negativ oder positiv oder Null ist. Ein Beispiel aus dem Alltag ist der Kauf
einer Fahrkarte für den ÖPNV. Meist wird beim Ticketpreis unterschieden, ob die
Person jünger als 6 ist (keine Fahrkarte notwendig), zwischen 6 und 14 ist
(Schülerfahrkarte) oder älter als 14 (Erwachsenenfahrkarte). Da es jetzt drei
Altersklassen gibt, können wir kein if-else-Konstrukt benutzen, denn nur weil
die Person beispielsweise nicht jünger als 6 ist wissen wir noch lange nicht, ob
die Person eine Schülerfahrkarte oder eine Erwachsenenfahrkarte braucht. 

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
if-Konstrukts (`alter <= 14`) erfüllt ist. So geht es also nicht, zwischen drei
Bedingungen zu unterscheiden.

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

Tatsächlich läuft unser Programm-Code nur korrekt, wenn wir in den else-Zweig
noch zusätzlich zwischen "jünger als 14" und "älter als 14" unterscheiden.

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
Das Ergebnis davon ist die if-elif-else-Syntax. Allgemein sieht das
**if-elif-else-Konstrukt** so aus:


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

Hier die besser lesbare Version der Unterscheidung von Zahlen in negative
Zahlen, 0 und positive Zahlen aus der obigen Mini-Übung:

```{code-cell} ipython3
a = 17
if a == 0:
    print('a ist Null.')
elif a < 0:
    print('a ist negativ.')
else:
    print('a ist positiv.')
```

Und jetzt noch einmal eine besser lesbare Version des Fahrkartenautomaten:

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
:class: minisolution, toggle
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

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Skript, das die aktuelle Temperatur von einem Benutzer oder einer Benutzerin abfragt. Wenn die Temperatur
* <= - 10 ˚C ist, dann Ausgabe: "Es ist bitterkalt."
* <= 0 ˚C ist, dann Ausgabe: "Es ist kalt."
* <= 10 ˚C ist, dann Ausgabe: "Es ist kühl, aber OK."
* <= 20 ˚C ist, dann Ausgabe: "Es ist frühlingshaft."
* <= 30 ˚C ist, dann Ausgabe: "Es ist heiß!"
* \> 30 ˚C ist, dann Ausgabe: "Das ist ja nicht mehr auszuhalten heiß!!!"
```
```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```
````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe
temperatur = float(input('Welche Temperatur haben wir aktuell? '))

# Verarbeitung und Ausgabe
if temperatur <= - 10:
    print('Es ist bitterkalt.')
elif temperatur <= 0: 
    print('Es ist kalt.')
elif temperatur <= 10:
    print('Es ist kühl, aber OK.')
elif temperatur <= 20:
    print('Es ist frühlingshaft.')
elif temperatur <= 30:
    print('Es ist heiß!')
else:
    print('Das ist ja nicht mehr auszuhalten heiß!')
```
````

<iframe width="560" height="315" src="https://www.youtube.com/embed/f3YdEdYSNdk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Zusammenfassung

In diesem Kapitel haben Sie die erste Kontrollstruktur kennengelernt, um ein
lineares Python-Programm in ein nichtlineares Python-Programm zu verwandeln, das
auf Eingaben von Benutzer:innen oder Zustände von Variablen reagiert. Mit Hilfe
von if, elseif und else können Sie nun beliebig viele Verzweigungen
programmieren. Damit der Python-Interpreter den Programm-Code in einer
Verzweigung ausführt, muss die Bedingung für diese Verzweigung erfült sein.
Bedingungen sind entweder wahr oder falsch, was Python in einem booleschen
Datentyp abspeichert. Für die Auswertung der Bedingung haben wir bisher
Vergleiche von Zahlen betrachtet. Andere Bedingungen beispielsweise auch für
Texte werden wir noch kennenlernen.






