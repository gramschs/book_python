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

In der letzten Vorlesung haben wir den boolschen Datentyp kennengelernt: wahr
oder falsch. Man kann solche Ausdrücke auch kombinieren, z.B. könnte man
fordern, dass zwei Bedingungen gleichzeitg erfüllt sein sollen. 

Beispiel beim Busfahren: Kinder unter 6 Jahren können kostenlos Bus fahren. Ab 6
Jahren braucht man eine Fahrkarte. Bis 14 Jahre zahlt man den Kinderpreis, ab 15
Jahren den Erwachsenenpreis: 

```python
alter = 12
if (6 <= alter) and (alter <= 14):
    print('Du darfst eine Kinderfahrkarte kaufen.')
```

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



## 4.2 Video zu logischen Operatoren im Allgemeinen

Schauen Sie sich auf YouTube das Video "SimpleClub: Negation, Konjunktion,
Disjunktion – Aussagenlogik 1" an (ca. 5:17 min):
https://www.youtube.com/watch?v=inwIsNIaWJM

Schreiben Sie anschließend die drei Wahrheitstafeln für 

1. Konjunktion / UND / and
2. Disjunktion / ODER / or
3. Negation / NICHT / not

auf. Zuletzt beantworten Sie bitte die folgenden zwei Fragen:

* Welche logische Verknüpfung entspricht in der Elektronik einer Reihenschaltung
  und welche einer Parallelschaltung? 
* Was sind Logikgatter?


Nun wenden wir uns der Umsetzung von logischen Verknüpfungen in Python zu.

## Video zu logischen Operatoren in Python

Schauen Sie sich auf YouTube das Video "Python Tutorial deutsch [12/24]" an,
siehe
https://www.youtube.com/watch?v=075l6R42tkQ&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=12
. Stoppen Sie regelmäßig und probieren Sie die dort gezeigten Beispiele in der
folgenden Code-Zelle aus: 

```python

```


## Aufgabe 

Was ist das Ergebnis: wahr oder falsch?

* wahr und wahr
* wahr oder falsch
* nicht wahr
* falsch oder wahr
* wahr oder nicht falsch
* nicht wahr und falsch
* nicht (wahr oder falsch)
* nicht falsch oder (falsch und falsch)

Probieren Sie in der nächsten Code-Zelle aus, ob Sie die richtigen Ergebnisse
hatten, indem Sie beispielsweise `wahr und wahr` in Python ausprobieren, also 
```python 
True and True
``` 
eingeben.


```python
True and True
```

## Aufgabe 

Schreiben Sie das Programm für einen Ticket-Automaten. Der Benutzer wird nach
dem Alter gefragt und ob ein Schülerausweis vorliegt. Das Programm gibt dann
aus, welches Ticket gekauft werden muss.

Alter | Ticket
------------ | -------------
0 - 5 | keine 
6 - 14 | Kinder-Ticket
15 - 21 und Schülerausweis | Kinder-Ticket
15 - 59 | Erwachsenen-Ticket
ab 60 | Senioren-Ticket


```python
alter = int(input('Bitte geben Sie Ihr Alter ein: '))
alter = int(input('Bitte geben Sie Ihr Alter ein: '))
alter = int(input('Bitte geben Sie Ihr Alter ein: '))
alter = int(input('Bitte geben Sie Ihr Alter ein: '))
hat_schuelerausweis = input('Haben Sie einen Schülerausweis (j/n)?')

if (0 <= alter) and (alter <= 5):
    print('Sie brauchen kein Ticket.')
elif (6 <= alter) and (alter <= 14):
    print('Sie brauchen ein Kinder-Ticket.')
elif (15 <= alter) and (alter <= 21) and (hat_schuelerausweis == 'j'):
    print('Sie brauchen ein Kinder-Ticket.')
elif (15 <= alter) and (alter <= 59):
    print('Sie brauchen ein Erwachsenen-Ticket.')
else:
    print('Sie brauchen ein Senioren-Ticket.')
```


## Schleifen: Wiederholung mit Bedingung "while"

Bei einer Wiederholung mit Bedingung wird eine Anweisung solange wiederholt, bis
die Bedingung erfüllt wird. Sie hat folgende Struktur:

```python
 while Bedingung: 
        anweisungsblock
```

Die bedingte Wiederholung wird mit dem Schlüsselwort `while` eingeleitet. Dann
folgt die Bedingung, die mit einem `:` abgeschlossen wird. Alle Anweisungen, die
wiederholt werden sollen, werden eingerückt. Diesen Teil nennt man das
Schleifeninnere, die Zeile `while Bedingung:` nennt man den Schleifenkopf. 

Bespiel: Wir möchten ein Programm schreiben, bei dem der Benutzer solange Zahlen
eingeben darf, die aufsummiert werden, bis die Null eingegeben wird. Für das
Aufsummieren benutzen wir eine Variable als Zwischenspeicher. Dies würde in
Python wie folgt umgesetzt:

```python
print('Dieses Programm addiert ganze Zahlen solange, bis Sie 0 eingeben.')
zahl = float(input('Geben Sie die erste Zahl ein: '))

summe = 0
while zahl != 0:
    summe = summe + zahl
    zahl = float(input('Geben Sie eine weitere Zahl ein: '))
print('Die Summe aller bisher eingegeben Zahlen ist: ', summe)
```

Probieren Sie den Code in der nächsten Code-Zelle aus:


```python
print('Dieses Programm addiert ganze Zahlen solange, bis Sie 0 eingeben.')
zahl = float(input('Geben Sie die erste Zahl ein: '))

summe = 0
while zahl != 0:
    summe = summe + zahl
    zahl = float(input('Geben Sie eine weitere Zahl ein: '))
print('Die Summe aller bisher eingegeben Zahlen ist: ', summe)
```

## Video zur while-Schleife

Schauen Sie sich auf YouTube das Video "Python Tutorial deutsch [13/24] die
while-Schleife" an, siehe
https://www.youtube.com/watch?v=sXLicTuJzB4&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=13
. Stoppen Sie regelmäßig und probieren Sie die dort gezeigten Beispiele in der
folgenden Code-Zelle aus. 

ACHTUNG: Falls Sie die Endlosschleife ausprobieren, können Sie oben in der
Menüleiste das schwarze Quadrat nutzen, um die Endlosschleife abzubrechen.

```python

```

## Aufgabe 

Schreiben Sie ein Programm, das die Zahlen von 1 bis 10 ausgibt.

```python

```

## Aufgabe 

Schreiben Sie ein Programm, das eine minimale Zahl $a$ und eine maximale Zahl
$b$ abfragt. Dann berechnet das Programm die Quadratzahlen von $a^2$ bis $b^2$
und gibt diese aus. Beispiel: Wenn der Benutzer `a = 3` eingibt und `b = 8`, so
soll das Programm `9, 16, 25, 36, 49, 64` ausgeben. 



```python

```

## Aufgabe 

Erweitern Sie Programm 4.8 so, dass erst überprüft wird, ob die eingegebene Zahl
$b$ auch wirklich größer als $a$ ist. Wenn dies nicht der Fall ist, soll solange
weiter nach einer Zahl $b$ gefragt werden, bis diese größer als a ist. 

Testen Sie Ihr Programm für die Beispiele $a=4$ und $b=10$ und anschließend für
$a=10$ und $b=4$.

```python

```


## Aufgabe 

Schreiben Sie ein Programm, welches die folgende Ausgabe bis zu einer vom
Benutzer gewählten Zahl fortsetzt:

```python
1 *
2 **
3 ***
4 ****
5 *****
6 ******
7 *******
```

Zusatz: Passen Sie das Programm so an, dass es einen Weihnachtsbaum aus
Sternchen zeichnet, dessen Anzahl von Zeilen (im Beispiels 7) vom Benutzer
gewählt werden kann:

```python
      * 1 *
     ** 2 **
    *** 3 ***
   **** 4 ****
  ***** 5 *****
 ****** 6 ******
******* 7 *******
      *****
      *****
```


Der Stamm besteht immer aus zwei Zeilen mit fünf Sternen. Der Benutzer darf dann
wählen, ob obige Grafik oder der Weihnachtsbaum gezeichnet wird.

Frage: Was passiert, wenn Sie eine negative Zahl eingeben?
<!-- #endregion -->

```python

```

## Aufgabe 

Unter
https://www.frankfurt-university.de/de/hochschule/fachbereich-2-informatik-und-ingenieurwissenschaften/corona-faqs-fuer-fb-2/
finden Sie die Erklärungen, bei welchen Krankheitssymptoman man an die
Hochschule kommen darf.

Schreiben Sie ein Programm, dass dem Benutzer mehrere Fragen nach Symptomen
stellt, z.B. "Haben Husten?" und auf die Antworten reagiert. Wenn z.B. die Frage
nach dem Husten mit "Ja" beantwortet wird, fragt das Programm nach, ob der
Husten trocken ist oder nur gelegenlich auftritt. Am Ende soll das Programm
entscheiden, ob der Benutzer an die Hochschule kommen darf oder nicht.

```python

```

## Aufgabe 

Aufgabe 3.7 lautete: 

Alkalimetalle sind die Stoffe Lithium (Li), Natrium (Na), Kalium (K), Rubidium
(Rb), Caesium (Cs). Schreiben Sie ein Programm, das Folgendes leistet: Der
Benutzer gibt die Formel eines chemischen Elementes an. Anschließend wird
gemeldet, ob es sich um ein Alkalimetall handelt oder nicht. 

Schreiben Sie Ihr Programm aus Aufgabe 3.7 so um, dass nur noch _eine_ if - else
- Struktur ohne elif verwendet wird, indem Sie logische Operatoren einsetzen.

