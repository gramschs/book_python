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

# 3.3 Das Modul Turtle

In der Informatik nennt man Grafiken, die dadurch entstehen, dass ein Roboter
Linien auf eine Leinwand zeichnet, Turtle-Grafiken. Der Roboter wird dabei mit
einfachen Kommandos gesteuert. Beschrieben wird er durch seine Position (x- und
y-Koordinaten in einem kartesischen Koordinatensystem) und seine Ausrichtung.
Der "Stift" des Roboters kann von seinen Eigenschaften her ebenfalls variieren.
So können beispielsweise verschiedenfarbige Stifte verwendet werden oder die
Linienstärke kann verändert werden.

Der Kern von Python enthält bereits ein Modul namens `turtle`, um eine solche
Turtle-Grafik zu erzeugen. Da wir in dieser Vorlesung mit Jupyter Notebooks
arbeiten, verwenden wir jedoch das Modul `colabTurtlePlus`, das das Turtle-Modul mit
Funktionalitäten für Jupyter Notebooks erweitert.

```{admonition} Hinweis: Installation notwendig
:class: warning
Das Modul colabTurtlePlus ist kein Standardmodul und muss daher nachinstalliert
werden. Bitte beachten Sie die Hinweise zur Installation "Module
nachinstallieren" und die dazugehörige Mini-Übung unten.
```

## Lernziele 

```{admonition} Lernziele
:class: admonition-goals
* Sie können ein fehlendes Modul mit **conda** oder **pip** nachinstallieren.
* Sie wissen, was eine **Turtle-Grafik** ist.
* Sie können das Modul **colabTurtlePlus** importieren.
* Sie können ein Roboterfeld initalisieren und den Roboter mit einfachen Kommandos über das Roboterfeld steuern.
```

+++

## Module nachinstallieren

Um ein Python-Modul bzw. ein Python-Paket aus einem Jupyter Notebook
nachzuinstallieren, gibt es grundsätzlich zwei Möglichkeiten: mit **conda** oder
mit **pip**. Conda ist ein Paket-Manager, der in der Anaconda-Distribution
enthalten ist und in der Regel für die Installation von Python-Paketen verwendet
wird, während pip ein Paket-Manager ist, der mit Python selbst installiert wird.

Hier sind Schritt-für-Schritt-Anleitungen, wie man ein Python-Modul mit conda
oder pip in einem Jupyter Notebook nachinstallieren kann.

### Installation mit conda

<ol>
<li>Öffnen Sie das Jupyter Notebook.</li>
<li>Erstellen Sie eine neue Code-Zelle und geben Sie folgenden Befehl ein:
<p><code>!conda install &lt;paketname&gt;</code></p>
<p>Ersetzen Sie dabei &lt;paketname&gt; durch den Namen des zu installierenden Pakets.</p>
<li>Führen Sie die Zelle aus, indem Sie auf den Run-Button klicken.</li>
<li>Warten Sie, bis das Paket heruntergeladen und installiert wurde.</li>
<li>Überprüfen Sie, ob das Paket korrekt installiert wurde, indem Sie eine weitere
   Code-Zelle erstellen und das Paket importieren:
<p><code>import &lt;paketname&gt;</code></p>
<p>Wenn kein Fehler auftritt, wurde das Paket erfolgreich installiert.</p>
</ol>

### Installation mit pip

<ol>
<li>Öffnen Sie das Jupyter Notebook.</li>
<li>Erstellen Sie eine neue Code-Zelle und geben Sie folgenden Befehl ein:</li>
<p><code>!pip install &lt;paketname&gt;</code></p>
<p>Ersetzen Sie dabei &lt;paketname&gt; durch den Namen des zu installierenden Pakets.</p>
<li>Führen Sie die Zelle aus, indem Sie auf den Run-Button klicken.</li>
<li>Warten Sie, bis das Paket heruntergeladen und installiert wurde.</li>
<li>Überprüfen Sie, ob das Paket korrekt installiert wurde, indem Sie eine weitere Code-Zelle erstellen und das Paket importieren:</p>
<p><code>import &lt;paketname&gt;</code></p>
<p>Wenn kein Fehler auftritt, wurde das Paket erfolgreich installiert.</p>
</ol>

### Wann conda und wann pip?

Es ist wichtig zu beachten, dass conda und pip unterschiedliche
Paket-Repositories verwenden. Wenn ein Paket mit conda installiert wurde, sollte
es nicht mit pip aktualisiert oder deinstalliert werden, da dies zu
Inkompatibilitäten führen kann. Umgekehrt sollte ein mit pip installiertes Paket
nicht mit conda aktualisiert oder deinstalliert werden. 

In dieser Vorlesung arbeiten wir mit der Anaconda-Distribution. Sie sollten also
immer zuerst versuchen, das fehlende Modul mit conda nachzuinstallieren. Nur
wenn es nicht in der Anaconda-Distribution enthalten ist, nehmen Sie bitte pip.
Die beiden folgenden Links verlinken auf die Liste der verfügbaren Pakete:

* [https://docs.anaconda.com/anaconda/packages/pkg-docs/](https://docs.anaconda.com/anaconda/packages/pkg-docs/)
* [https://pypi.org](https://pypi.org)

```{admonition} Mini-Übung
:class: miniexercise
Installieren Sie jetzt das Modul `ColabTurtlePlus`, das leider nicht in der Anaconda-Distribution enthalten ist. Mehr Details zu diesem Modul finden Sie unter [https://pypi.org/project/ColabTurtlePlus/](https://pypi.org/project/ColabTurtlePlus/).
```
````{admonition} Lösung
:class: miniexercise, toggle
```markdown
!pip install ColabTurtlePlus
import ColabTurtlePlus
```
````


## Ein Turtlefeld initalisieren 

Als erstes werden alle Funktionalitäten des Turtle-Moduls geladen. Die typische
Abkürzung für dieses Modul ist `turtle`.

```{code-cell} ipython3
import ColabTurtlePlus.Turtle as turtle
``` 

Es erscheint eine Meldung, nämlich der Hinweis: "Put clearscreen() as the first
line in a cell (after the import command) to re-run turtle commands in the
cell". Mit dem Kommando `turtle.clearscreen()` wird ein Turtlefeld initalisiert
und gleichzeitig können später die vorhandenen Grafiken damit gelöscht werden,
wenn die Code-Zelle erneut ausgeführt wird.

Mit `dir(turtle)` können wir erkunden, was an Funktionalitäten vorhanden ist.

```{code-cell} ipython3
dir(turtle)
``` 

Dann folgen wir der Anweisung, zuerst das Kommando `clearscreen()` zu benutzen.

```{code-cell} ipython3
turtle.clearscreen()
``` 

Es erscheint eine leere Leinwand, die 800 Bildpunkte breit ist und 600
Bildpunkte hoch ist. Bildpunkte werden normalerweise als **Pixel** bezeichnet,
was wiederum mit px abgekürzt wird. 

Als nächstes setzen wir einen Roboter mitten in das Feld. Der Roboter soll den
Namen Robo tragen. Da Variablen traditionell klein geschrieben werden, wird mit
der folgenden Code-Zeile ein Roboter-Objekt namens `robo` initalisiert.

```{code-cell} ipython3
robo = turtle.Turtle()
``` 

Der virtuelle Roboter wird durch ein Dreieck gekennzeichent. Die Spitze des
Dreiecks zeigt in die Richtung, in die der Roboter aktuell schaut.

## Der Roboter bewegt sich

Der Roboter wird mit einfachen Befehlen wie vorwärts, links, rechts, usw.
gesteuert. Die Befehle sind dabei englisch. Da sie an den Roboter gerichtet
sind, wird zuerst der Name des Roboters verwendet, dann ein Punkt gesetzt und
zuletzt der Befehlsname geschrieben. In die runden Klammern kommen die
Argumente, z.B. um wie viele Schritte der Roboter sich vorwärts bewegen soll.

Mit dem Befehl

```python3
robo.forward(schritte)
```

wird der Roboter vorwärts bewegt und legt insgesamt `schritte` (gemessen in Pixeln) zurück.

Mit den Befehlen 

```python3
robo.left(winkel)
```

und 

```python3
robo.right(winkel)
```

wird der Roboter nach links (gegen den Uhrzeigersinn) oder rechts (im
Uhrzeigersinn) gedreht. Der Drehwinkel wird durch die Variable `winkel`
im Gradmaß bestimmt.

Um jetzt den kompletten Code zusammen zu haben, wiederholen wir die bisherigen
Code-Zeilen in der folgenden Code-Zelle und experimentieren dann in der
übernächsten Code-Zelle mit der Steuerung des Roboters. Wenn Sie das Turtle-Feld
wieder auf seinen Ausgangszustand zurücksetzen möchten, führen Sie erneut die
Code-Zelle mit der Erzeugung und Initialisierung aus.

```{code-cell} ipython3
# Initalisierung des Feldes und Löschung bereits vorhandener Grafiken
turtle.clearscreen()

# Erzeugung eines Roboters mit Namen robo und Platzierung auf dem Feld
robo = turtle.Turtle()

# Robo bewegt sich
robo.forward(100)
robo.left(120)
robo.forward(50)
```

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie den Roboter ein Rechteck der Länge 200 px und Höhe 100 px zeichnen. Am Ende soll der Roboter in die ursprüngliche Richtung hin ausgerichtet sein, also nach Osten bzw. rechts.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
turtle.clearscreen()
robo = turtle.Turtle()
robo.forward(200)
robo.left(90)
robo.forward(100)
robo.left(90)
robo.forward(200)
robo.left(90)
robo.forward(100)
robo.left(90)
```
Anmerkung: natürlich hätten wir den Roboter auch viermal nach rechts drehen lassen können.
````

## Robo kann noch mehr... 

Die folgenden Befehle an den Roboter dienen zur Steuerung der Bewegung:

* forward(schritte): Der Roboter bewegt sich vorwärts, die Streckenlänge wird in
  Schritten `schritte` angegeben.
* backward(schritte): Der Roboter bewegt sich rückwärts, die Streckenlänge wird
  in Schritten `schritte` angegeben.
* right(winkel): Der Roboter dreht sich nach rechts, der Winkel `winkel` wird in
  Grad angegeben. 
* left(winkel): Der Roboter dreht sich nach links, der Winkel `winkel` wird in
  Grad angegeben.  
* goto(x,y): Der Roboter läuft direkt zu der angegeben Position (x,y).

Der Stift wird mit folgenden Befehlen eingestellt:

* penup(): Der Stift wird hochgehoben. Bewegt sich der Roboter, hinterlässt er
  keine Zeichnung. 
* pendown(): Der Stift wird abgesetzt, ab jetzt zeichnet der Roboter wieder.
* pensize(breite): Die Breite der Striche wird eingestellt, z.B. ist
  `robo.pensize(10)` ein breiter Strich.  

Für die Farbe gibt es das folgende Kommando:

* pencolor(farbe): Ändert die Farbe der Striche, z.B. stellt der Befehl
  `robo.pencolor('red')` auf rote Farbe um. Die Farben werden als String
  übergeben und entsprechen den englischen Farben.

Mehr Details finden Sie in der
[Turtle-Dokumentation von ColabTurtlePlus](https://larryriddle.agnesscott.org/ColabTurtlePlus/documentation.html).

Zum Abschluss noch eine Mini-Übung.

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie den Roboter ein gleichseitiges Dreieck zeichnen. Die erste Seite soll rot sein, die zweite grün und die dritte blau.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
turtle.clearscreen()
robo = turtle.Turtle()

robo.pencolor('red')
robo.forward(50)
robo.left(120)
robo.pencolor('green')
robo.forward(100)
robo.left(120)
robo.pencolor('blue')
robo.forward(100)
robo.left(120)
robo.pencolor('red')
robo.forward(50)
```
````

