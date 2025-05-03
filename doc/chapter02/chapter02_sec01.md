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

# 2.1 Taschenrechner und Ausgabe (print)

Ein Klassiker beim Erlernen einer neuen Programmiersprache ist das
Hallo-Welt-Programm. Dabei geht es darum, den Text "Hallo Welt" auf dem
Bildschirm anzeigen zu lassen. Klingt simpel, aber je nach Programmiersprache
kann auch diese einfache Aufgabe einen hohen Aufwand bedeuten. Bevor wir das
Hallo-Welt-Programm programmieren, nutzen wir erst Python als Taschenrechner, um
auch den Umgang mit dem Jupyter Notebook noch weiter zu festigen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie kennen die grundlegenden Rechenoperationen in Python.
* Sie wissen, was ein **Kommentar** ist.
* Sie können in Python einen Kommentar mit **#** schreiben.
* Sie können mit **print** das Ergebnis einer Rechnung anzeigen lassen.
* Sie wissen, dass Texte mit einfachen `'` oder doppelten `"` Anführungszeichen
  zu Beginn des Textes und zum Ende begrenzt werden. 
```

## Python als Taschenrechner

Bevor wir in die Programmierung einsteigen, benutzen wir Python erst einmal als
Taschenrechner. Im Folgenden sehen Sie, wie die Grundrechenarten in Python
verwendet werden:

Addition:

```{code-cell} ipython3
2+3
```

Subtraktion:

```{code-cell} ipython3
2-3
```

Multiplikation:

```{code-cell} ipython3
2*4
```

Division:

```{code-cell} ipython3
8/2
```

Potenzierung:

```{code-cell} ipython3
3**2
```

In diesem interaktiven Vorlesungsskript können Sie Python direkt ausprobieren.
Es ist ein großer Vorteil der Jupyter Notebooks, dass in einem Dokument
Text-Zellen und Code-Zellen gemischt werden können. Diesen Vorteil nutze ich
aus, um Ihnen den Einstieg in die Programmierung zu erleichtern. Die
Vorlesungsskripte sind so aufgebaut, dass ich Ihnen erst ein
Programmierkonstrukt erläutere und Sie dann die Möglichkeit haben, das neu
erlernte Wissen gleich in Python auszuprobieren.

Die obigen Zellen sind Code-Zellen. Sie können daher direkt in einer der oberen
Code-Zellen beispielsweise die Additionsaufgabe `2+3` in `2+5` abändern, um sich
mit den Python-Kommandos vertraut zu machen. Wenn Sie dieses Skript als Jupyter
Notebook durcharbeiten, können Sie direkt mit dem Cursor in eine der obigen
Code-Zellen klicken und den dort stehenden Code abändern. Wenn Sie dieses Skript
Online lesen, klicken Sie bitte zuerst auf das Raketensymbol oben rechts und auf
Live Code, um eine interaktive Code-Zelle erzeugen zu lassen. Beim ersten Start
des Live Codes kann es etwas länger dauern. Sie erkennen, dass die Code-Zelle
interaktiv geworden ist, wenn die Knöpfe `run`, `restart` und `restart & run
all` erschienen sind. Dann geben Sie Ihren Code ein und drücken auf run.

Technisch gesehen ist es einfacher, wenn Code-Zellen schon existieren. Im
Jupyter Notebook selbst lässt sich eine Code-Zelle einfach einfügen. In der
Online-Variante dieses Vorlesungsskriptes besteht diese Möglichkeit
bedauerlicherweise nicht. Daher werde ich für kleine Mini-Übungen zwischendurch
Code-Zellen einfügen, die aber noch keinen Code enthalten, sondern nur als
Platzhalter dienen sollen. Damit Sie solche Platzhalter-Code-Zellen erkennen,
beschrifte ich diese Zellen mit einem Kommentar. Das sieht dann folgendermaßen
aus:

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:
```

Alles was nach dem Hashtag # kommt, wird von Python ignoriert. Die sogenannten
**Kommentare**, die durch das Hashtag-Zeichen eingeleitet werden, sind für uns
Menschen bestimmt.

Selbstverständlich beherrscht Python auch Klammerregeln. Probieren Sie es aus!
Geben Sie in die Code-Zelle Ihren Code ein und lassen Sie die Code-Zelle
ausführen. Die Lösungen zu den Mini-Übungen finden Sie im
[Online-Skript](https://gramschs.github.io/book_python/intro.html) an der
Stelle, an der sich die jeweilige Mini-Übung befindet.

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie Python den Term $3\cdot (7-10)+5$ berechnen. 
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
3 * (7-10) + 5
```
````

## Ausgaben mit print

Jetzt lernen Sie das erste Python-Kommando kennen, um dem Computer eine
Anweisung zu geben. Bei den obigen Rechenaufgaben wurde automatisch das Ergebnis
der Rechnung angezeigt, sobald die Code-Zelle ausgeführt wurde. Dies ist eine
Besonderheit der Jupyter Notebooks, würde aber in einem normalen Python-Programm
nicht funktionieren. Auch möchte man vielleicht ein Zwischenergebnis anzeigen
lassen. Die interaktive Ausgabe der Jupyter Notebooks zeigt jedoch immer nur den
Inhalt der letzten Zeile an.

Für die Anzeige von Rechenergebnissen oder Texten gibt es in Python die
**print()**-Funktion. Die print()-Funktion in Python gibt den Wert oder die
Werte aus, die ihr als Argumente übergeben werden. Das kann zum Beispiel eine
Zahl sein oder eine Rechenaufgabe, wie in dem folgenden Beispiel.

```{code-cell} ipython3
print(2)
print(3+3)
```

In der ersten Zeile ist das Argument für die print()-Funktion die Zahl 2. Das
Argument wird in runde Klammern hinter den Funktionsnamen `print` geschrieben.
Ein Argument ist sozusagen der Input, der an die print()-Funktion übergeben
wird, damit der Python-Interpreter weiß, welcher Wert auf dem Bildschirm
angezeigt werden soll.

Das zweite Beispiel in der zweiten Zeile funktioniert genauso. Nur wird diesmal
eine komplette Rechnung als Argument an die print()-Funktion übergeben. In dem
Fall rechnet der Python-Interpreter erst den Wert der Rechnung, also `3+3=6` aus
und übergibt dann die `6` an die print()-Funktion. Die print()-Funktion wiederum
zeigt dann die `6` am Bildschirm an.

Insgesamt zeigt daher der Python-Interpreter erst eine 2 und dann in der
nächsten Zeile eine 6 an.

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie Python den Term $3:4$ berechnen und geben Sie das Ergebnis mit der print()-Funktion aus. 
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
print(3/4)
```
````

Python kann mit der print()-Funktion jedoch nicht nur Zahlen ausgeben, sondern
auch Texte. Ein erster Versuch, einfach den Text als Argument der
print()-Funktion zu übergeben, scheitert leider, wie das nächste Beispiel zeigt.

```{code-cell} ipython3
print(Hallo)
```

Es erscheint eine Fehlermeldung mit dem Fehler: `NameError: name 'Hallo' is not
defined`. Der Grund hierfür ist, dass der Python-Interpreter versucht, eine
sogenannte Variable oder ein Python-Kommando mit dem Namen `Hallo` zu finden. Da
es aber keines von beiden gibt, kommt die Fehlermeldung, dass `Hallo` nicht
definiert wurde. Um den Text ausgeben zu lassen, werden um den Text einfache
oder doppelte Anführungszeichen gesetzt, wie in dem folgenden Beispiel.

```{code-cell} ipython3
print('Hallo')
```

```{admonition} Mini-Übung
:class: miniexercise
Probieren Sie aus was passiert, wenn Sie die einfachen Anführungszeichen `'`
durch doppelte Anführungszeichen `"` ersetzen. Lassen Sie den Text Hallo Welt
ausgeben :-)
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
print("Hallo Welt")
```
````

In Python sind beide Arten von Anführungszeichen erlaubt und werden manchmal
auch gebraucht. Wenn beispielsweise ein Apostroph in einem Text gebraucht wird,
müssen die äußeren Anführungszeichen die doppelten Anführungszeichen sein. Der
Python-Interpreter erwartet nämlich immer ein Paar von Anführungszeichen, damit
eindeutig ist, wo der Text beginnt und wo er endet.

Die print()-Funktion kann noch einiges mehr, als wir in dieser Einführung
gesehen haben. Wir werden in einem späteren Kapitel im Zusammenhang mit den
sogenannten f-Strings nochmal darauf zurückkommen.

## Weiteres Lernmaterial

In dem folgenden Video wird zunächst die Installation von Python (Anaconda)
gezeigt. Im Gegensatz zu unserer Vorlesung wird aber die Entwickungsumgebung
PyCharm anstatt Jupyter Notebooks genutzt. Daher können Sie gerne den ersten
Teil des Videos überspringen und ab ca. Minute 9 einsteigen.

```{dropdown} Video "Dein erstes Python-Programm" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/oxXAb8IikHM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
