# 8.2 Numerisches Rechnen mit MATLAB

MATLAB ist als Matrix-Labor vor allem für das Rechnen mit Vektoren und Matrizen
ausgelegt. Daher erkunden wir in diesem Kapitel die grundlegenden Datentypen und
Rechenoperationen für Vektoren und Matrizen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können einen **Vektor** oder eine **Matrix** in MATLAB erzeugen.
* Sie wissen, wie Sie auf einzelne **Elemente** eines Vektors oder einer Matrix
  zugreifen.
* Sie beherrschen das **Slicing** in MATLAB.
* Sie können grundlegende **Rechenoperationen** mit Vektoren oder Matrizen
  ausführen.
* Sie können mit MATLAB das **Skalarprodukt** oder das **Vektorprodukt** von
  Vektoren berechnen.
* Sie können die **Determinante**, die **Eigenwerte** oder die **Eigenvektoren**
  einer Matrix berechnen.
```

## Vektoren

Vektoren sind sozusagen technisch gesehen Listen, die nur Zahlen enthalten, und
für die die typischen Vektoroperationen definiert sind. Zunächst beschäftigen
wir uns mit der Erzeugung von Vektoren.

### Erzeugung Zeilenvektor

Ein Vektor wird in MATLAB durch eckige Klammern `[  ]` erzeugt. Sie finden das
Zeichen für die eckige Klammer auf der Taste mit der 8, das Zeichen für die
eckige Klammer auf der Taste mit der 9. Zusätzlich müssen Sie die Taste Alt Gr
drücken, um die eckigen Klammern auf der Tastatur einzugeben.

Betrachten wir ein Beispiel. Hier wird ein Vektor mit den Elementen 1, 2, 3, 4,
5 erzeugt und dann anschließend in der Variablen `v` gespeichert. Zur Trennung
der einzelnen Elemente des Vektors verwenden wir das Komma. Tatsächlich würde
MATLAB auch ein Leerzeichen als Trennung akzeptieren. Im Zusammenhang mit
Matrizen ist aber das Komma einprägsamer, so dass wir beim Komma bleiben.

```matlab
v = [1, 2, 3, 4, 5]
```

### Erzeugung Spaltenvektor

Der Vektor, so wie wir ihn bisher erzeugt haben, ist ein Zeilenvektor. Möchten
wir ihn in einen Spaltenvektor umwandeln, so müssen wir ihn transponieren. Dafür
steht in MATLAB der einzelne Hochstrich `'`.

```matlab
a'
```

Soll direkt ein Spaltenvektor erzeugt werden, so verwenden wir das Semikolon
anstatt des Kommas.

```matlab
spaltenvektor = [1; 2; 3]
```

### Einfache Rechenoperationen

Mit Vektoren kann auch direkt gerechnet werden. Natürlich müssen dabei die
Dimensionen der Vektoren übereinstimmen. Bei der folgenden Addition  

```matlab
a = [-1.5, 2, 3.7]
b = [0, -1, -1.7]
a + b
```

wird von MATLAB das Ergebnis `[-1.5, 1, 2]` berechnet und angezeigt. Die
Subtraktion erfolgt analog.

Die Multiplikation `a * b` funktioniert jedoch nicht. Es erscheint eine
Fehlermeldung. Das liegt daran, dass es eine direkte Multiplikation von Vektoren
nicht gibt. Wir müssen erst entscheiden, ob elementweise multipliziert werden
soll oder ob vielleicht das Skalarprodukt oder das Vektorprodukt gemeint ist.

Bei der elementweisen Multiplikation wird dem Multiplikationsoperator `*` ein
Punkt `.` vorangestellt, also `.*`:

```matlab
a .* b
```

Das Ergebnis ist dann der Vektor `[0, -2.0000, -6.2900]`. So funktioniert auch
die elementweise Division. Dabei gibt es zwei Varianten:

```matlab
a ./ b
a .\ b
```

Bei der ersten Variante wird jedes Element des Vektors `a` durch das
entsprechende Element des Vektors `b` geteilt. Das `b` steht in Nenner des
Bruchstrichs `/`. Bei der zweiten Variante wird jedes Element des Vektors `b`
durch die entsprechenden Elemente des Vektors `a` geteilt. Der Bruchstrich `\`
zeigt an, dass `a` im Nenner stehen soll.

### Erzeugung eines Vektors mittels Doppelpunkt-Operator

Python verfügt über die Funktion `range()`, um Listen mit Zahlen zu erzeugen,
die einem bestimmten Muster folgen. Diese Funktion wird in MATLAB so häufig
gebraucht, dass sie sogar durch einen eigenen Operator anstatt einer Funktion
erreicht wird, durch den Doppelpunkt-Operator `:`.

Eine Liste mit den Zahlen von 5 bis 11 wird folgendermaßen generiert:

```matlab
a = 5 : 11
```

Auch hier ist eine Schrittweite versteckt enthalten. Der folgende Code erzeugt
gerade Zahlen von 4 bis 12:

```matlab
a = 4 : 2 : 12
```

So kann auch rückwärts gezählt werden.

```matlab
a = 12 : -2 :  4
```

Das folgende Video fasst die obigen Erklärungen zusammen.

```{dropdown} Video zu "Matlab - 1.4 Vektoren" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/zse9DvJPxHI"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Matrizen

MATLAB würde nicht Matrix-Labor heißen, wenn es nicht einen eigenen Datentyp für
Matrizen gäbe. Tatsächlich speichert MATLAB intern Vektoren als Matrix ab. Ein
Zeilenvektor ist eine $1\times N$-Matrix und ein Spaltenvektor eine $M\times
1$-Matrix. Daher betrachten wir uns als nächstes, wie Matrizen in MATLAB erzeugt
werden.

### Erzeugung von Matrizen

Bei den Vektoren haben wir gelernt, Leerzeichen oder Komma, um Elemente eines
Zeilenvektors aufzulisten, und Semikolon, um Elemente in einem Spaltenvektor
voneinander abzugrenzen. Eine Matrix wird zeilenweise eingegeben. Das Semikolon
markiert das Ende der Zeile.

```matlab
A = [1, 2, 3; 4, 5, 6; 7, 8, 9]
```

### Erzeugung von speziellen Matrizen

Für Matrizen, die häufig gebraucht werden, hat MATLAB eigene
Erzeugungsfunktionen. Beispielsweise generiert die Funktion

```matlab
A = zeros(5,3)
```

eine Matrix, die nur die Zahl Null enthält und die 5 Zeilen und 3 Spalten hat.
Analog dazu funktioniert das Kommando

```matlab
A = ones(5,3)
```

das eine Matrix mit Einsen erzeugt, die 5 Zeilen und 3 Spalten hat. Sehr häufig
gebraucht wird auch die Einheitsmatrix. Mit der Funktion `eye(N)` wird sie
erzeugt, wobei der Parameter `N` die Dimension der quadratischen Matrix angibt.

```matlab
E = eye(5)
```

Hier noch ein Video zu Matrizen in MATLAB.

```{dropdown} Video zu "Matlab - 1.5 Matrizen" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/bjGYz8eWN3A"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Skripte

Es ist umständlich, immer alles in das Kommandofenster einzugeben. Die
Entwicklungsumgebung MATLAB bietet einen Texteditor, um ein sogenanntes Skript
zu schreiben. Ein Skript ist wie ein Programm, also eine Aneinanderreihung von
Anweisungen an den MATLAB-Interpreter. Es wird als Text abgespeichert und trägt
die Dateiendung `.m`. Am einfachsten starten Sie den Editor, indem Sie auf `New
Script` klicken.

```{figure} pics/screenshot03.png
:alt: Screenshot MATLAB mit "New Script"
:width: 75%
:align: center
Screenshot MATLAB mit dem Button "New Script"
```

Sobald MATLAB den Texteditor öffnet, verändert sich das Layout von MATLAB. Das
Kommandofenster rutscht nach unten und wird kleiner, wohingegen der Texteditor
nun den größten Raum einnimmt.

```{figure} pics/screenshot04.png
:alt: Screenshot MATLAB mit Texteditor
:width: 75%
:align: center
Screenshot MATLAB mit geöffnetem Texteditor; ein Skript wird ausgeführt, indem
auf den Button "Run" geklickt wird (siehe 3)
```

Das Skript wird ausgeführt, indem Sie auf den Button "Run" klicken (siehe
Screenshot, 3). Es ist ratsam, am Anfang des Skriptes den Befehl `clear all`
einzufügen. Diese Anweisung sorgt dafür, dass alle sich im Speicher befindlichen
Variablen gelöscht werden.

Ein weiteres Video zu Skripten in MATLAB finden Sie hier.

```{dropdown} Video zu "Matlab - 1.6 Skripte" von Mathe? logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/hx26vljCKWQ"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zugriff auf Vektor- und Matrixelemente

Der Zugriff auf die Elemente eines Vektors erfolgt durch Angabe des Index des
Elements in runden Klammern. Beachten Sie, dass MATLAB im Gegensatz zu vielen
anderen Programmiersprachen einen Index verwendet, der bei 1 beginnt. Das
folgende Beispiel zeigt, wie auf das dritte Element des Vektors zugegriffen
wird.

```matlab
a = [1, 2, 3, 4, 5]
drittes_element = a(3)
```

Soll hingegen auf Elemente einer Matrix zugegriffen werden, müssen wir die Zeile
und die Spalte über den jeweiligen Index angeben. Auf die zweite Zeile und die
dritte Spalte wird folgendermaßen zugegriffen.

```matlab
A = [1, 2, 3, 4, 5; 6, 7, 8, 9, 10; 11, 12, 13, 14, 15]
element = A(2,3)
```

Damit wird die `8` aus der Matrix `A` extrahiert und kann weiter verarbeitet
werden.

Was aber, wenn wir auf ganze Zeilen oder ganze Spalten zugreifen möchten? Dazu
existiert das sogenannte **Slicing**. Mit Slicing ist gemeint, dass auf einen
zusammenhängenden Bereich des Vektors oder der Matrix zugegriffen werden soll.
Wir betrachten die $3\times 5$-Matrix $A$ von vorhin, also

```matlab
A = [1, 2, 3, 4, 5; 6, 7, 8, 9, 10; 11, 12, 13, 14, 15]
```

Um jetzt einen zusammenhängenden Bereich aus der Matrix zu extrahieren,
verwenden wir den Doppelpunkt-Operator ':'. Mit

```matlab
A(1, :)
```

greifen wir auf Elemente der ersten Zeile zu und gehen dabei in der Spalte von
Anfang bis Ende, da vor dem Doppelpunkt und nach dem Doppelpunkt nichts steht.
Das Ergebnis ist also die komplette erste Zeile `[1, 2, 3, 4, 5]`. Möchten wir
in der ersten Zeile von der zweiten Spalte zur vierten Spalte auf die Elemente
der Matrix zugreifen, schreiben wir den Startindex vor den Doppelpunkt und den
Stoppindex nach dem Doppelpunkt.

```matlab
A(1, 2:4)
```

Das Ergebnis sind die Elemente `[2, 3, 4]`. Diese Vorgehensweise funktioniert
auch für die Zeile. Der folgende MATLAB-Code extrahiert die komplette zweite und
dritte Zeile.

```matlab
A(2:3, :)
```

Das Ergebnis ist

$$\begin{pmatrix}
6 & 7 & 8 & 9 & 10 \\
11 & 12 & 13 & 14 & 15
\end{pmatrix}.$$

Das Slicing kann auch verwendet werden, um Teile einer Matrix zu ändern. Nehmen
wir an, wir möchten die zweite Spalte von A durch die Zahlen 102, 107 und 112
ersetzen. Wir könnten durch den folgenden Code erreichen.

```matlab
A(:, 2) = [102; 107; 112]
```

Die folgenden beiden Videos fassen zunächst den Doppelpunktoperator und dann das
Slicing zusammen.

```{dropdown} Video zu "Matlab - 2.1 Doppelpunkt- bzw. Colon-Operator" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/eX2RM355fSM"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Matlab - 2.2 Zugriff auf Teile von Matrizen" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/m6t5YuavGkI"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Fortgeschrittene Rechenoperationen für Vektoren und Matrizen

Das Skalarprodukt ist eine grundlegende Operation in der linearen Algebra. Das Skalarprodukt zweier Vektoren wird durch die Multiplikation der entsprechenden Komponenten der Vektoren und die Summierung dieser Produkte berechnet.

In MATLAB wird das Skalarprodukt von zwei Vektoren mit der Funktion `dot()` berechnet:

```matlab
v = [1, 2, 3]
w = [4, 5, 6]
skalarprodukt = dot(v, w)
```

Das Ergebnis ist $1\cdot 4 + 2\cdot 5 + 3\cdot 6 = 32$.

Das Vektorprodukt, auch bekannt als Kreuzprodukt, ist eine weitere wichtige Operation in der linearen Algebra, die speziell auf dreidimensionale Vektoren angewendet wird. Das Vektorprodukt von zwei Vektoren ist ein Vektor, dessen Länge/Betrag dem Flächeninhalt des Rechtecks entspricht, das durch die beiden Vektoren aufgespannt wird. Die Richtung des Vektorprodukts ist dadurch definiert, dass der Vektor senkrecht zu beiden Vektoren steht und mit ihnen ein Rechtssystem bildet.

In MATLAB wird das Vektorprodukt mit der Funktion `cross()` berechnet:

```matlab
v = [1, 2, 3]
w = [4, 5, 6]
vektorprodukt = cross(v, w)
```

Das Vektorprodukt ist der Vektor `[-3, 6, -3]`.

Die Determinante ist ein spezieller Wert, der nur für quadratische Matrizen definiert ist. Sie ist ein nützlicher Indikator für viele Eigenschaften der Matrix, einschließlich der Frage, ob die Matrix invertierbar ist und ob das lineare Gleichungssystem, das sie repräsentiert, Lösungen hat.

In MATLAB wird die Determinante einer Matrix mit der Funktion `det()` berechnet:

```matlab
A = [1, 2; 3, 4]
det_A = det(A)
```

Die Determinante der obigen Matrix $A$ ist $\det(A) = 1\cdot 4 - 3\cdot 2 = -2$.

Eigenwerte und Eigenvektoren sind weitere wichtige Konzepte in der linearen
Algebra, die in vielen Anwendungen, einschließlich der
Maschinenbauingenieurwissenschaften, der Informatik und der Datenanalyse,
nützlich sind. Die Eigenwerte einer Matrix sind die Lösungen der
charakteristischen Gleichung

$$\det(A-\lambda E) = 0,$$

wobei $E$ die Einheitsmatrix der passenden Dimension ist. Zu jedem Eigenwert
$\lambda$ kann dann der Eigenvektor $\vec{v}$ berechnet werden, der die
Gleichung

$$A\cdot \vec{v} = \lambda \vec{v}$$

erfüllt. Ein Eigenvektor ist also ein Vektor, der sich bei der Anwendung einer
linearen Transformation (repräsentiert durch die Matrix) nur um einen
Skalierungsfaktor ändert.

In MATLAB werden Eigenwerte und Eigenvektoren mit der Funktion `eig()`
berechnet:

```matlab
A = [1, 2; 3, 4]
[V, D] = eig(A)
```

In diesem Beispiel gibt der Code die Matrix `V` der Eigenvektoren und die
Diagonalmatrix `D` aus. Jede Spalte in V ist ein Eigenvektor, und die
entsprechenden Eigenwerte sind die Elemente auf der Diagonale in D.

Für weitere Betrachtungen empfehle ich die folgenden beiden Videos.

```{dropdown} Video zu "Matlab - 2.3 Kombination und Transformation von Matrizen" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/mh8Auf1eOpA"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Matlab - 2.4 Operationen auf Matrizen" Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/enUeKd-IMcw"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
