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

# 4.2 Strings

Den Datentyp String haben Sie bereits zu Beginn im Kapitel "Einstieg in die
Programmierung" kennengelernt. Bis jetzt haben wir Strings vor allem dazu
benutzt, um mit der print()-Funktion etwas auszugeben. In diesem Jupyter
Notebook geht es nun darum, Strings auch zu manipulieren und mit den sogenannten
f-Strings auch formatierte Ausgaben zu produzieren.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, dass Strings unveränderliche Container sind und welche
  Konsequenzen das für die Programmierung hat.
* Sie können mit dem Index auf einzelne Zeichen eines Strings zugreifen.
* Sie können Strings mit dem Plus-Operator **verketten**.
* Sie können mit der **.replace()**-Methode einen Teilstring in einem String
  durch einen anderen Teilstring ersetzen.
* Sie können mit einem **f-String** den Wert einer Variablen in einen String
  einbetten und zur Laufzeit anzeigen lassen.
```

## Strings sind Container

Im deutschen Fachbegriff Zeichenketten steckt schon die Idee, Strings als eine
Verkettung von einzelnen Zeichen zu interpretieren. Mit dieser Idee ist dann
vielleicht auch nicht verwunderlich, dass die einzelnen Zeichen eines Strings
über den Index angesprochen werden können.

```{code-cell} ipython3
# Erzeugung und Anzeige String
mein_string = 'Hallo, Du da!'
print(mein_string)

# Zugriff auf einzelne Zeichen per Index
print('2. Zeichen: ')
print(mein_string[1])
```

Aber welche Zeichen gehören dazu? Probieren Sie die folgende Mini-Übung aus.

```{admonition} Mini-Übung
:class: miniexercise
Speichern Sie den String 'Hallo, Du da!' in einer Variable. Beantworten Sie
folgende Fragen zuerst durch Überlegen, dann durch Ausprobieren.

* Was ist der größte Index des String 'Hallo, Du da!'?
* Was passiert, wenn Sie versuchen, auf den Index 20 zuzugreifen?
* Welches Zeichen hat den Index 6?
```

```{code-cell} ipython3
# Hier Ihr Code.
```

````{admonition} Lösung
:class: minisolution, toggle
* Der größte Index ist 12.
* Beim Versuch, auf Index 20 zuzugreifen, gibt es eine Fehlermeldung:
  'IndexError: string index out of range'. Der Index 20 ist außerhalb des
  zulässigen Indexbereichs von 0 bis 12.
* Das Zeichen an Indexposition 6 ist ein Leerzeichen. Leerzeichen sind auch
  Zeichen und müssen mitgezählt werden.
````

Mit den beiden for-Schleifen der letzten beiden Abschnitte können wir die
Zeichen auch einzeln ausgeben lassen. Als erstes nutzen wir die for-Schleife
direkt:

```{code-cell} ipython3
for zeichen in 'Hallo, Du Da!':
    print(zeichen)
```

Als nächstes wird über den Index iteriert. Iteration ist der Fachbegriff für das
mehrfache Wiederholen einer Anweisung.

```{code-cell} ipython3
mein_string = 'Hallo, Du da!'
for i in range(13):
    zeichen = mein_string[i]
    print(zeichen)
```

Woher kommt die magische Zahl 13 in dem obigen `range()`-Objekt? Das ist die
Länge des Strings, die wir besser mit der `len()`-Funktion bestimmen lassen.

```{code-cell} ipython3
mein_string = 'Hallo, Du da!'
laenge = len(mein_string)
for i in range(laenge):
    zeichen = mein_string[i]
    print(zeichen)
```

## Strings sind unveränderlich

Bei Listen können wir einzelne Elemente der Liste direkt manipulieren, z.B.
können wir das dritte Element durch ein anderes ersetzen wie in dem folgenden
Beispiel.

```{code-cell} ipython3
meine_liste = ['Eins', 'Zwei', 'Drei', 'Vier', 'Fünf']
print('Am Anfang: ')
print(meine_liste)

# Austausch der 'Drei' durch 'MMMH'
meine_liste[2] = 'MMMH'
print('Nach dem Austausch:')
print(meine_liste)
```

Obwohl Strings genau wie Listen Container sind, funktioniert die Manipulation
eines einzelnen Zeichens in einem String leider nicht. Entfernen Sie in der
folgenden Code-Zelle den Kommentar vor `wort[0] = 'H'`. Was passiert?

```{code-cell} ipython3
wort = 'hallo!'
print('Am Anfang: ')
print(wort)

# Austausch des kleinen Buchstaben h durch ein großes H 
# wort[0] = 'H'
print('Nach dem Austausch:')
print(wort)
```

Der Python-Interpreter gibt eine Fehlermeldung aus: 'str' object does not
support item assignment'. Ein item ist ein einzelnes Element der Liste und
assignment ist das englische Wort für Zuweisung. Auf Deutsch lautet diese
Fehlermeldung also, dass ein String-Objekt die Zuweisung eines einzelnen
Elements/Zeichens nicht unterstützt. Oder anders ausgedrückt, es ist verboten,
einen String durch eine Zuweisung zu ändern.

Bei Strings handelt es sich um einen sogenannten **unveränderlichen Datentyp**.
Das bedeutet, dass der Inhalt eines Strings nach seiner Erstellung nicht mehr
verändert werden kann.

Es gibt andere Programmiersprachen wie beispielsweise C und MATLAB, in denen
Strings als veränderliche Objekte umgesetzt sind. Die Entwickler:innen von
Python haben sich bei der Entwicklung von Python aus Gründen der
Speichereffizienz und der Sicherheit von daraus abgeleiten Datentypen (z.B.
Dictionaries) dagegen entschieden.

## Und wenn doch ein String geändert werden soll?

Natürlich kann es dennoch vielfältige Gründe geben, einen String nach seiner
Erstellung noch abzuändern. Beispielsweise könnte bei einer Benutzereingabe ein
Tippfehler aufgetreten sein, der korrigiert werden soll. Obwohl Strings in
Python unveränderlich sind, gibt es immer noch viele Operationen, die auf
Strings ausgeführt werden können, wie z.B. das Anhängen von Strings, das Suchen
oder das Ersetzen von Teilstrings. Allerdings wird in diesen Fällen nicht der
ursprüngliche String modifiziert, sondern ein neuer String erzeugt.

### Verketten von Strings

Sie können Strings in Python einfach aneinanderhängen (verketten), indem Sie den
`+`-Operator verwenden. Hier ist ein Beispiel:

```{code-cell} ipython3
name  = 'Alice'
gruss = 'Hallo ' + name + '!'
print(gruss)
```

Allerdings haben Sie damit nicht wirklich den String geändert, sondern einen
neuen String erzeugt.

### Ersetzen von Teilstrings

Python bietet mehrere Methoden zum Suchen und Ersetzen von Teilstrings in einem
String. Eine dieser Methoden ist `.replace()`. Hier ist ein Beispiel:

```{code-cell} ipython3
text = 'MATLAB ist eine großartige Programmiersprache!'
neuer_text = text.replace('MATLAB', 'Python')
print(neuer_text)
```

In diesem Beispiel haben wir den Teilstring "MATLAB" durch den Teilstring
"Python" ersetzt. Wie Sie sehen, mussten wir für den abgeänderten Text eine neue
Variable namens `neuer_text` verwenden. Wenn mehrfach Änderungen des Strings
durchgeführt werden sollen, ist das Ausdenken von neuen Variablennamen lästig.
Dann kann der ursprüngliche Variablenname wiederverwendet werden, wie im
folgenden Beispiel.

```{code-cell} ipython3
text = 'MATLAB ist eine großartige Programmiersprache!'
text = text.replace('MATLAB', 'Python')
print(text)
```

Es gibt viele andere nützliche Operationen, die Sie auf Strings in Python
ausführen können, wie z.B. das Suchen von Teilstrings mit der `.find()`-Methode,
das Zählen von Vorkommen von Teilstrings mit der `.count()`-Methode und das
Konvertieren von Strings in Groß- oder Kleinbuchstaben mit den Methoden
`.upper()` und `.lower()`. In der nächsten Mini-Übung probieren wir noch einmal
die `.replace()`-Methode aus.

````{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, das in dem Spruch "Zehn Ziegen zogen 10 Kilogramm
Zucker zum Zoo." die Einheit Kilogramm durch Zentner ersetzt. Lassen Sie den
Spruch vor und nach der Korrektur ausgeben.
````

```{code-cell} ipython3
# Hier Ihr Code.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
spruch = 'Zehn Ziegen zogen 10 Kilogramm Zucker zum Zoo.'

print('Vor dem Anwenden der .replace()-Methode: ')
print(spruch)

print('Jetzt wird .replace() angewendet: ')
spruch = spruch.replace('Kilogramm', 'Zentner')
print(spruch)
```
````

## Formatierte Strings (f-Strings)

Zum Schluss behandeln wir noch formatierte Strings, die sogenannten f-Strings.
Seit Python 3.6 erleichtert dieser Typ von String die Programmierung. Falls Sie
Python-Code sehen, in dem Prozentzeichen vorkommen (ganz, ganz alt) oder die
.format()-Methode benutzt wird, wundern Sie sich nicht. In dieser Vorlesung
verwenden wir f-Strings.

f-Strings sind die Abkürzung für "formatted string literals". Sie ermöglichen
es, den Wert einer Variable oder einen Ausdruck direkt in den String
einzubetten. Dazu werden geschweifte Klammern verwendet, also `{` und `}` und zu
Beginn des Strings wird ein `f` eingefügt, um aus dem String einen f-String zu
machen. Der Python-Interpreter fügt dann zur Laufzeit des Programms den
entsprechenden Wert der Variable in den String ein.

Hier ein Beispiel:

```{code-cell} ipython3
name = 'Alice'
alter = 14
print(f'Mein Name ist {name} und ich bin {alter} Jahre alt.')
```

Insbesondere bei Ausgabe von Zahlen sind f-Strings besonders nützlich. Wenn nach
dem Variablennamen ein Doppelpunkt eingefügt wird, kann danach die Anzahl der
gewünschten Stellen vor dem Komma (hier natürlich ein Punkt) und der
Nachkommastellen festgelegt werden. Zusätzlich setzen wir ein `f` in die
geschweiften Klammern, um einen Float anzeigen zu lassen. Im folgenden Beispiel
geben wir $\pi$ auf zwei Nachkommastellen an.

```{code-cell} ipython3
from numpy import pi

print(f'Pi = {pi:.2f}')
```

Es ist schwierig, sich alle Formatierungsoptionen zu merken. Auf der
Internetseite
[https://cheatography.com/brianallan/cheat-sheets/python-f-strings-basics/](https://cheatography.com/brianallan/cheat-sheets/python-f-strings-basics/)
finden Sie eine umfangreiche Übersicht und können sich zudem ein pdf-Dokument
herunterladen.

````{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, mit dem der Flächeninhalt eines Rechtecks berechnet werden soll. Die beide Seitenlängen werden jeweils in den Variablen `laenge` und `breite` gespeichert (suchen Sie sich eigene Zahlen aus). Ausgegeben werden soll dann: "Der Flächeninhalt eines Rechtecks mit den Seiten XX und XX ist XX.", wobei XX durch die korrekten Zahlen ersetzt werden und der Flächeninhalt auf eine Nachkommastelle gerundet werden soll.
````

```{code-cell} ipython3
# Hier Ihr Code.
```

````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe
laenge = 5.5
breite = 6.3

# Verarbeitung
flaeche = laenge * breite

# Ausgabe 
print(f'Der Flächeninhalt eines Rechtecks mit den Seiten {laenge} und {breite} ist {flaeche:.1f}.')
```
````

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, dass Strings unveränderlich sind. Werden
Strings manipuliert, müssen wir das Ergebnis explizit in einer neuen Variablen
speichern, sollten wir mit dem manipuliertem String weiter arbeiten wollen. Im
nächsten Kapitel betrachten wir Zufallszahlen.
