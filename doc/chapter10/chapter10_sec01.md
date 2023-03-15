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

# 10.1 Das Modul NumPy

Im letzten Kapitel haben wir gelernt, Daten in Form von Tabellen als
Pandas-Objekte zu verwalten. Dabei arbeiten die Module Pandas, Scikit-Learn und
auch das Visualisierungsmodul Matplotlib, das wir in diesem Kapitel kennenlernen
werden, alle mit NumPy-Arrays. NumPy ist ein Akronym für **numerisches Python**.

Die Internetseite von NumPy

> https://NumPy.org

behauptet sogar von ihrem eigenen Paket, dass NumPy das (!!!) fundamentale Modul
für alle wissenschaftlichen Programme in Python ist — stimmt wahrscheinlich! Die
Bibliothek ist im Kern in der Programmiersprache C geschrieben und bietet vor
allem sehr effiziente Datenstrukturen für Vektoren, Matrizen und
mehrdimensionale Arrays an.  
 
In  diesem Abschnitt werden wir uns die grundlegenden Eigenschaften des
**NumPy-Array** erarbeiten, um für Matplotlib und Scikit-Learn die Basis zu
schaffen.

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie können **NumPy** mit seiner typischen Abkürzung **np** importieren.
* Sie können mit **np.array()** ein NumPy-Array aus einer Liste erzeugen.
* Sie können NumPy-Arrays, die nach einem Muster aufgebaut sind, erzeugen:
    * Array mit Einsen: **np.ones()**
    * Array mit Nullen: **np.zeros()**
    * Array mit Konstante: **np.full()**
    * Array mit vorgegebener Anzahl von Punkten in einem Intervall: **np.linspace()**
    * Array mit vorgebener Schrittweite in einem Intervall: **np.arange()**
* Sie können Basis-Attribute von NumPy-Arrays bestimmen wie beispielsweise
    * Anzahl der Dimensionen: **.ndim**
    * Größe der jeweiligen Dimension: **.shape**
    * Gesamtgröße des Arrays: **.size**
* Sie können NumPy-Funktionen auf NumPy-Arrays anwenden.
```

## NumPy ist schneller durch C

Alle Daten lassen sich letztendlich als eine Folge von Zahlen schreiben.
Beispielsweise kann ein Foto durch seine Pixel beschrieben werden
zusammengesetzt aus den Werten RGB (rot - grün - blau). Python bietet dafür
schon einen Datentyp, die Liste, in der Zahlen (Integer oder Float) gespeichert
werden können. Da Python eine interpretierte Programmiersprache ist und da in
der Liste auch andere Datentypen wie zum Beispiel Strings vorkommen dürfen, sind
Listen für große Datenmengen nicht geeignet. Stattdessen stellt das Modul NumPy
einen effizienten Datentyp zur Verfügung, das sogenannte **NumPy-Array**.  

Dazu kommen noch Funktionen, die wichtig für Arrays sind wir Vektoroperationen.
Tatsächlich sind die meisten NumPy-Operationen nicht in Python programmiert,
sondern in C. Damit sind NumPy-Funktionen sehr effizient und das tolle daran
ist, dass wir uns keine Gedanken über hardwarenahe Programmierung mit C oder C++
machen müssen :-)

Schauen wir uns für das Bestimmen des Maximums einer Liste von zufällig
erzeugten Zahlen zwischen 0 und 1 an. Zunächst erzeugen wir die Liste der 100
Zahlen. Dazu importieren wir NumPy mit seiner typischen Abkürzung `np`. im
Untermodul `np.random`gibt es eine Funktion namens `random_sample`, die
Zufallszahlen erzeugt.

```{code-cell}
---
vscode:
  languageId: python
---
import numpy as np

# erzeuge Liste
M = np.random.random_sample(100)

print(M)
```

Als nächstes berechnen wir das Maximum dieser Zahlen mit der im Python-Kern
eingebauten Standardfunktion `max`, dann mit `np.max`:

```{code-cell}
---
vscode:
  languageId: python
---
max_standard = max(M)
max_numpy = np.max(M)

print('Standard max = ', max_standard)
print('NumPy max = ', max_numpy)
```

Aber wie lange haben eigentlich die Berechnungen gedauert? Bei so kleinen Listen
lohnt es nicht, die Berechnung mit der Stoppuhr zu ermitteln, die typischen
Rechnenzeiten sind zu kurz. Aber JupyterLab bietet ein eingebautes Kommando,
nämlich `%timeit`. Der Vorteil dieses Kommandos ist, dass der Python-Interpreter
bei sehr kurzen Rechenzeiten einfach den Code mehrmals durchläuft und
Mittelwerte bildet.

```{code-cell}
---
vscode:
  languageId: python
---
%timeit max_standard = max(M)
%timeit max_numpy = np.max(M)
```

Sie sehen, die NumPy-Variante ist erheblich schneller als die Standard-Variante.


## Erzeugung von NumPy-Arrays

Im Gegensatz zu Python-Listen enthalten NumPy-Arrays nur Elemente des gleichen
Datentyps. Wenn eine Liste nur aus gleichen Datentypen besteht, können wir
direkt aus der Liste ein NumPy-Array erzeugen. Dazu verwenden wir `array()` aus
dem Numpy-Modul.

```{code-cell}
---
vscode:
  languageId: python
---
liste = [1, 2, 3, 4, 5]
a = np.array(liste)

print(a)
print( type(a) )
```

Sehr häufig kommen aber auch zwei-  oder gar dreidimensionale Arrays vor. In der
Mathematik würde man ein eindimensionales Array als Vektor bezeichnen, ein
zweidimensionales Array als Matrix (= Excel-Tabelle) und ein dreidimensionales
Array als Tensor. Die Position eines Elementes wird dabei durch ganze Zahlen
gekennzeichnet (entspricht bei 1d-Arrays ja den Listen). Für zweidimensionale
NumPy-Arrays brauchen wir daher zwei Indizes, für dreidimensionale Arrays drei.
Die folgende Grafik zeigt das Nummerierungsschema:

```{figure} pics/fig_numpy_array.png
---
width: 600px
name: pics/fig_numpy_array
---
Nummerierungsschema bei NumPy-Arrays

([Quelle:](https://predictivehacks.com/tips-about-NumPy-arrays/))
```

Im Folgenden fokussieren wir uns zunächst auf 1D- und 2D-Arrays und betrachten
uns verschiedene Erzeugungsmethoden. Die entsprechende (englischsprachige)
Dokumentation finden Sie hier:

> https://numpy.org/doc/stable/reference/routines.array-creation.html
 
Wir starten mit Arrays, die mit 0 oder 1 oder einer konstanten Zahl gefüllt
sind. Dazu verwenden wir die NumPy-Funktionen
* `np.zeros(dimension)`
* `np.ones(dimension)`
* `np.full(dimension, zahl)`

```{code-cell}
---
vscode:
  languageId: python
---
# 1d-Array gefüllt mit Nullen
x = np.zeros(5)
print(x)
```

```{code-cell}
---
vscode:
  languageId: python
---
# 2d-Array gefüllt mit Nullen
x = np.zeros( (5,7) )
print(x)
```

```{code-cell}
---
vscode:
  languageId: python
---
# 1d-Array gefüllt mit Einsen
x = np.ones(7)
print(x)
```

```{code-cell}
---
vscode:
  languageId: python
---
# 2d-Array gefüllt mit Nullen
x = np.ones( (3,4) )
print(x)
```

```{code-cell}
---
vscode:
  languageId: python
---
# 2d-Array gefüllt mit einem konstanten Wert
x = np.full( (3,4), -17.7)
print(x)
```

```{admonition} Mini-Übung
:class: miniexercise
Erzeugen Sie folgende Arrays:
* 1d-Array der Dimension 7 gefüllt mit 0
* 1d-Array der Dimension 7 gefüllt mit -1
* 2d-Array der Dimension (7,5) gefüllt mit 1
* 2d-Array der Dimension (2,4) gefüllt mit $\pi$
* 1d-Array der Dimension 8 gefüllt mit $\sqrt{5}$
```

```{code-cell}
---
vscode:
  languageId: python
---
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
x1 = np.zeros(7)
x2 = np.full(7, -1)
X3 = np.ones( (7,5) )
X4 = np.full( (2,4), np.pi)
x5 = np.full(8, np.sqrt(5))
```
````

Die folgenden 1d-Arrays werden nach einem gleichmäßigen Muster gefüllt. Dazu
benutzen wir die NumPy-Funktionen

* `np.linspace(start, stopp, anzahl)`
* `np.arange(start, stopp, schrittweite)`

```{code-cell}
---
vscode:
  languageId: python
---
# 1d-Array, das gleichmäßig zwischen start und stopp mit num Werten gefüllt wird
# im Beispiel: start = 1, stopp = 10, num = 25 
x = np.linspace(1, 10, 25)
print(x)
```

```{code-cell}
---
vscode:
  languageId: python
---
# 1d-Array, das bei start beginnt, step dazu addiert und bis kurz vor stopp geht
# im Beispiel: start = 1, stopp = 20, step = 2
x = np.arange(1, 20, 2)
print(x)
```

Zuletzt betrachten wir noch Erzeugungsfunktionen, die seltener vorkommen, aber
dennoch nützlich sein können: 

* `np.random.random_sample(dimension)`: gleichmäßig verteilt zwischen 0 und 1
* `np.random.normal(m, s, dimension)`: normalverteilt mit Mittelwert m und
  Standardabweichung s

```{code-cell}
---
vscode:
  languageId: python
---
# 2d-Array mit gleichmäßig zwischen 0 und 1 verteilten Zufallszahlen
x = np.random.random_sample( (2,3) )
print(x)
```

```{code-cell}
---
vscode:
  languageId: python
---
# 2d-Array mit normalverteilten Zufallszahlen 
x = np.random.normal(0, 1, (3,4) )
print(x)
```

```{code-cell}
---
vscode:
  languageId: python
---
# 2d-Array als Einheitsmatrix der Größe m x m, hier m = 5
x = np.eye(5)
print(x)
```

```{admonition} Mini-Übung
:class: miniexercise
Erzeugen Sie folgende Arrays:

* 2d-Array mit der Dimension (3,4) und Zufallszahlen gleichmäßig zwischen 0 und
1 verteilt 
* 1d-Array mit der Dimension 17 und Zufallszahlen standardnormalverteilt (d.h.
welcher Mittelwert und welche Standardabweichung?) 
* 2d-Array mit der Dimension (1,5) und normalverteilten Zufallszahlen,
Mittelwert 37.5, Standardabweichung 0.8 
* 1d-Array mit allen geraden Zahlen von 100 bis 200 (inklusive) 
* 1d-Array mit 100 Punkten im Intervall [-1,1] 
* 1d-Array mit 0, 0.1, 0.2, 0.3, ..., 1.5
```

```{code-cell}
---
vscode:
  languageId: python
---
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
X1 = np.random.random_sample((3,4))
x2 = np.random.normal(0, 1, 17)
X3 = np.random.normal( 37.5, 0.8, (1,5))
x4 = np.arange(100, 201, 2)
x5 = np.linspace(-1, 1, 100)
x6 = np.arange(0, 1.6, 0.1)
```
````


## Attribute von NumPy-Arrays

Damit wir besser verstehen, welche Attribute die NumPy-Arrays haben können,
erzeugen wir uns zufällig drei NumPy-Arrays. Damit aber nicht bei jeder neuen
Ausführung der Code-Zelle neue Zufallszahlen gezogen werden, fixieren wir den
Seed des Zufallszahlengenerators (vereinfacht gesagt kommen jetzt immer die
gleichen Zufallszahlen) und benutzen die Erzeugungsmethode
`np.random.randint(grenze, size=dimension)`:

```{code-cell}
---
vscode:
  languageId: python
---
import numpy as np
       
np.random.seed(0)

x = np.random.randint(10, size=7)
y = np.random.randint(10, size=(2, 3))

print('x = ')
print(x)

print('y = ')
print(y)
```

Bei den Listen haben wir eine Funktion kennengelernt, mit der die Anzahl der
Elemente in der Liste bestimmt werden kann: `len()`. Listen sind eindimensional,
aber NumPy-Arrays können mehrdimensional sein. Daher gibt es hier auch mehr
Eigenschaften für die Beschreibung:

* Anzahl der Dimensionen: `.ndim`
* Größe der jeweiligen Dimension: `.shape`
* Gesamtgröße des Arrays: `.size`

Die Größe `.shape` haben wir ja in der obigen Abbildung schon bereits
kennengelernt.

```{code-cell}
---
vscode:
  languageId: python
---
print('x = ')
print(x)

print( x.ndim )
print( x.shape )
print( x.size )
```

```{code-cell}
---
vscode:
  languageId: python
---
print('y = ')
print(y)

print( y.ndim )
print( y.shape )
print( y.size )
```

## Zugriff einzelner Elemente eines Arrays

Der Zugriff bei eindimensionalen Arrays erfolgt genau wie bei Listen über den
**Zugriffsoperator** `[]`. Auch hier wird ab 0 beginnend gezählt.

```{code-cell}
---
vscode:
  languageId: python
---
x = np.random.randint(10, size=7)
print(x)

drittes_element = x[2]
print( drittes_element )
```

Interessant wird es zu sehen, wie auf mehrdimensionale Arrays zugegriffen wird.
Zur Erinnerung, zweidimensionale Arrays haben zwei Indizes (axis 0 und axis 1),
dreidimensionale Arrays haben drei Indizes (axis 0, axis 1 und axis 2).

```{code-cell}
---
vscode:
  languageId: python
---
print('y = ')
print(y)

element = y[0,2]
print(element)
```

So kann man übrigens auch die Werte einzelner Elemente des Arrays ändern:

```{code-cell}
---
vscode:
  languageId: python
---
print('vorher y = ')
print(y)

y[1,1] = 777
print('nachher y = ', y)
```

## Funktionen auf NumPy-Arrays anwenden

NumPy-Arrays ermöglichen die Verarbeitung mit den typischen mathematischen
Funktionen und den üblichen Statistik-Größen. Schauen wir uns einfach ein paar
Beispiele an:

```{code-cell}
---
vscode:
  languageId: python
---
# erzeuge 11 x-Werte im Intervall [-2*pi, 2*pi]
x = np.linspace( -2*np.pi, 2*np.pi, 11)
print(x)

# Sinus-Funktion
y1 = np.sin(x)
print(y1)

# Kosinus-Funktion
y2 = np.cos(x)
print(y2)

# Exponentialfunktion
y3 = np.exp(x)
print(y3)

# Potenzfunktion, z.B. y = x hoch 5
y4 = np.power(x, 5)
print(y4)
```

```{code-cell}
---
vscode:
  languageId: python
---
# erzeuge 3x4-Matrix mit Zufallszahlen
X = np.random.random_sample((3,4))
print(X)

# Summe über alle Elemente
s1 = np.sum(X)
print('s1', s1)

# Summe in Richtung Achse 0
s2 = np.sum(X, axis=0)
print('s2', s2)

# Summe in Richtung Achse 1
s3 = np.sum(X, axis=1)
print('s3', s3)

# Maximum über alle Elemente
max1 = np.max(X)
print('max1', max1)

# Maximum in Richtung Achse 0
max2 = np.sum(X, axis=0)
print('max2', max2)

# Maximum in Richtung Achse 1
max3 = np.sum(X, axis=1)
print('max3', max3)
```

## Zusammenfassung 

In diesem Abschnitt haben wir das NumPy-Array kennengelernt, eine sehr
effiziente Datenstruktur. Die Erzeugungsmethoden nach einem Muster werden wir
vor allem für die Visualisierung von Funktionen brauchen. Das Bestimmen der
Basis-Attribute wird wichtig werden, wenn wir NumPy-Arrays aus
Pandas-DataFrame-Objekten extrahieren, um damit maschinelle Lernalgorithmen zu
füttern.
