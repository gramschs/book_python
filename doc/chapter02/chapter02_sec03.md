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

# 2.3 Eingabe (input) und Zuweisungsoperator

Ohne die Eingabe von Daten sind Apps wertlos. In diesem Kapitel beschäftigen wir
uns daher einer direkten Eingabemöglichkeit in Python und lernen dazu die
input()-Funktion kennen. Um die input()-Funktion korrekt zu nutzen beschäftigen
wir uns mit Umwandlungen von Datentypen in andere Datentypen. Zuletzt gehen wir
noch auf die Stolperfalle ein, dass der Zuweisungsoperator `=` nicht die
mathematische Gleichheit überprüft.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können das **EVA-Prinzip** erklären.
* Sie können mit der **input()**-Funktion die Eingabe eines Benutzers abfragen
  und weiter verarbeiten.
* Sie können per **Typecasting** Datentypen in andere Datentypen umwandeln.
* Sie wissen, dass das Zeichen `=` ein **Zuweisungsoperator** ist und nicht für
  die mathematische Gleichheit zweier Ausdrücke steht.
```

## Ein- und Ausgabe sowie das EVA-Prinzip

Grundlegend geht es bei der Datenverarbeitung und vor allem bei der
wissenschaftlichen Programmierung darum, Daten zu verarbeiten, wie der Name ja
schon sagt sagt ;-) Selbst bei einer Smartphone-App zum Daddeln müssen Daten
verarbeitet werden, nämlich das aktuelle Level, wo hat die Spielerin oder der
Spieler gerade das Display berührt, was passiert in dem Spiel als nächstes usw.
Grundsätzlich folgen datenverarbeitende Systeme dem sogenannten **EVA-Prinzip**.

Wikipedia beschreibt das [EVA-Prinzip](https://de.wikipedia.org/wiki/EVA-Prinzip) wie folgt:
> "...Das EVA-Prinzip beschreibt ein Grundprinzip der Datenverarbeitung. Die
  Abkürzung leitet sich aus den ersten Buchstaben der Begriffe Eingabe,
  Verarbeitung und Ausgabe ab (englisch IPO model: input-process-output). Diese
  drei Begriffe beschreiben die Reihenfolge, in der Daten verarbeitet werden."

Typische Eingabe-Operationen sind dabei

* die Eingabe von Zeichen über eine Tastatur oder
* das Lesen von Dateien, die auf der Festplatte oder einem Speichermedium gespeichert sind.

Häufige Ausgabe-Operationen sind

* die Wiedergabe von Texten, Zahlen oder Bildern auf dem Bildschirm oder
* das Schreiben von Dateien auf Festplatte oder Speichermedium.

Mit der Ausgabe haben wir uns schon beschäftigt. Als nächstes geht es um die
Eingabe.

## Die input()-Funktion

Die einfachste und häufigste **Eingabe** erfolgt über die Tastatur. Die Funktion
`input()` stoppt das laufende Skript und erwartet eine Eingabe über die
Tastatur. Dabei wird der Text angezeigt, der zwischen den einfachen Hochkommata
steht. Bei Python wird die Eingabe als String interpretiert. Die Eingabe wird
mit der Taste Return/Enter abgeschlossen. Probieren wir es aus:

```python
input('Bitte geben Sie Ihren Namen ein: ')
```

Wir haben zwar jetzt auf Aufforderung einen Namen eingegeben, aber verarbeitet
wurde diese Eingabe nicht. Es passierte einfach nichts. Um die Eingabe
verarbeiten zu können, speichern wir sie zunächst in einer Variablen ab.

```python
x = input('Bitte geben Sie Ihren Namen ein: ')
```

Jetzt haben wir zwar den Namen in einer Variable gespeichert, aber so richtig
passiert ist immer noch nichts. Jetzt wäre es noch schön, wenn wir dem Benutzer
oder der Benutzerin unseres Skripts begrüßen können und einen entsprechenden Text
anzeigen lassen können. Dazu verwenden wir erneut die `print()`-Funktion.

```python
print('Hallo')
```

Jetzt können wir alles zusammensetzen.

```python
x = input('Bitte geben Sie Ihren Namen ein: ')
print('Hallo')
print(x)
```

Kopieren Sie diesen Code in die nächste Code-Zelle und probieren Sie es aus!

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

In dem folgenden Video sehen Sie weitere Erläuterungen zur input()-Funktion.

```{dropdown} Video "Die input()-Funktion" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/I9h1c-121Uk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Umwandlung von Datentypen

Die input()-Funktion hat eine Einschränkung. Bei ihrer Einführung wurde in einem
Nebensatz erwähnt, dass die input()-Funktion Strings zurückgibt. Das ist eine
häufige Fehlerquelle in der Programmierung, wenn man nach Zahlen fragt.
Glücklicherweise gibt es dafür eine einfache Lösung. Wir können einen String in
einen Integer oder Float verwandeln, indem wir die Funktionen `int()` oder
`float()` benutzen. Wenn also nach einer Zahl per input()-Funktion gefrgt werden
soll wie beispielsweise dem Alter einer Person, so lautet der Code wie folgt:

```python
x = int( input('Wie alt sind Sie?) )
print('Alter: ')
print(x)
```

Und soll es eine Fließkommazahl werden, so können wir folgendermaßen den
Python-Interpreter fragen lassen:

```python
x = int( input('Wie groß sind Sie gemessen in Metern?) )
print('Größe in m')
print(x)
```

Probieren Sie gerne beide Varianten in der nächsten Code-Zelle aus.

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

Wenn Sie mehr über das sogenannte Type-Casting erfahren wollen, finden Sie
Details in diesem Video.

```{dropdown} Video "Type-Casting in Python" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/u_ECGvn1Z2c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zuweisungsoperator

Wichtig ist, dass das `=` in der Informatik eine andere Bedeutung hat als in der
Mathematik. = meint nicht das Gleichheitszeichen, sondern den sogenannten
**Zuweisungsoperator**. Das ist in der Programmierung ein Kommando, das eine
Schublade befüllt oder technischer ausgedrückt, ein Objekt einer Variable
zuweist.

Sehr häufig findet man Code wie

```python
x = x + 1
```

Würden wir dies als Gleichung lesen, wie wir es aus der Mathematik gewohnt sind,
also $x = x+1$, könnten wir $x$ auf beiden Seiten subtrahieren und erhalten
$0=1$. Wir wissen, dass dies nicht wahr ist, also stimmt hier etwas nicht.

In Python sind "Gleichungen" keine mathematischen Gleichungen, sondern
Zuweisungen. "=" ist kein Gleichheitszeichen im mathematischen Sinne, sondern
eine Zuweisung. Die Zuweisung muss immer in der folgenden Weise zweistufig
gelesen werden:

1. Berechne den Wert auf der rechten Seite (also $x+1$).
2. Weise den Wert auf der rechten Seite dem auf der linken Seite stehenden
   Variablennamen zu.

Wir probieren eine solche Zuweisung in der folgenden Code-Zelle aus und benutzen
auch gleich die `print()`-Funktion, um den Wert der Variablen `x` ausgeben zu
lassen:

```{code-cell} ipython3
x = 4     
x = x + 1
print(x)
```

Der Zuweisungsoperator ist äußerst wichtig in der Python-Programmierung. Daher
empfehle ich Ihnen folgende Video.

```{dropdown} Video "Der Zuweisungsoperator" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/XKFQ2_et5k8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Das EVA-Prinzip ist das grundlegende Prinzip der Datenverarbeitung. Mit den
Python-Funktionen input() und print() und den Datentypen Integer, Float uund
String haben wir bereits die wichtigsten Bausteine zusammen, um kleine
Python-Programme zu schreiben.
