# 8.3 Programmieren in MATLAB

Ein Programmierkurs in MATLAB erfordert eine ganze Vorlesung. In diesem Kapitel vergleichen wir nur die Programmierkonstrukte aus Python mit denen von MATLAB. Gerne können Sie Details in dem Vorlesungsskript

> [https://gramschs.github.io/book_matlab/](https://gramschs.github.io/book_matlab/intro.html)

nachlesen.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie kennen die wesentlichen Gemeinsamkeiten und Unterschiede zwischen Python und MATLAB hinsichtlich
* Eingabe
* Verarbeitung (Variablen und Datentypen)
* Ausgabe
* Funktionen
* Vergleiche
* Programmverzweigungen
* Schleifen
* Diagramme
* Regression
```

## Eingabe, Verarbeitung und Ausgabe

Die Eingabe erfolgt in MATLAB mit der Funktion `input()`. Im Unterschied zu
Python liefert die input()-Abfrage eine Zahl zurück, keinen String. Tatsächlich
wird oft mit indirekten Abfrgaen gearbeitet wie beispielsweise: "Haben Sie einen
Führerschein? Geben Sie 0 ein für Nein und 1 für Ja."

Für die Ausgabe gibt es zwei Funktionen. Die Funktion `disp()` gibt den Inhalt
einer Variablen direkt aus. Die Funktion `fprintf()` ermöglicht weitere
Formatierungsmöglichkeiten ähnlich zu der print()-Funktion von Python mit
f-Strings. Es wird in den String ein Platzhalter `%f` eingesetzt und dann,
nachdem der String abgeschlossen wurde, nach einem Komma die Variable.

Das folgende Beispiel fragt nach einem Nettpreis und gibt dann den Bruttopreis
mit einem Mehrwertsteuersatz von 19 %.

```matlab
nettopreis = input('Bitte geben Sie den Nettopreis ein: ')
bruttopreis = nettopreis + 0.19 * nettopreis
fprintf('Der Bruttopreis ist %f EUR.', bruttopreis)
```

Zwischenrechnungen werden von MATLAB automatisch am Bildschirm ausgegeben. Wenn
das nicht gewünscht ist, kann die Ausgabe durch ein Semikolon am Ende der Zeile
unterdrückt werden.

## Funktionen

In MATLAB werden häufig Funktionen gebraucht. Zunächst einmal sind Funktionen in
MATLAB ebenso Blöcke von Anweisungen, die eine bestimmte Funktionalität
implementieren. Weil MATLAB aber mehr auf Mathematik hin ausgerichtet ist,
stellen sie meist "echte" mathematische Funktionen mit einer Eingabe und einer
Ausgabe dar.

Die Grundstruktur einer Funktion in MATLAB ist wie folgt:

```matlab
function [ergebnis1, ergebnis2,...] = funktionsname(input1, input2,...)
    % Anweisungen
    ergebnis1 = ...
    ergebnis2 = ...
end
```

Die Funktion wird mit dem Schlüsselwort `function` eingeleitet. Danach kommen
die Variablen, deren Werte von der Funktion zurückgegeben werden sollen. Das
wird durch den Zuweisungsoperator `=` deutlich gemacht. Zuletzt folgt der
Funktionsname mit den Eingabeparametern. Die Anweisungen im Inneren der Funktion
werden durch das `end` abgeschlossen.

Die folgende Funktion berechnet zu einem gegebenen Radius den Umfang und die
Fläche und gibt beide Werte zurück.

```matlab
function [umfang, flaeche] = berechne_umfang_flaeche(radius)
    umfang = 2 * pi * radius;
    flaeche = pi * radius^2;
end
```

Sie muss unter dem Namen `berechne_umfang_flaeche.m` abgespeichert werden, damit
sie dann im Kommandofenster oder in einem anderen Skript benutzt werden kann.

```matlab
[U, A] = berechne_umfang_flaeche(5)
```

Die folgenden Videos bieten eine ausführliche Einführung zum Thema Funktionen in MATLAB.

```{dropdown} Video zu "Matlab - 3.1 Einleitung Funktionen" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/ifMkS0rnQ_A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Matlab - 3.2 Input/Output bei Funktionen" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/psyGbqwBD2s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Matlab - 3.3 Formale Definition von Funktionen" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/FMfTxKd3gOw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Matlab - 3.4 Unterfunktionen" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/i1c3IPCb82E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Matlab - 3.5 Geltungsbereich" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/ebqojVhnPwo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Programmverzweigungen

MATLAB kennt ebenfalls Vergleiche und den booleschen Datentyp. Die
Vergleichsoperatoren sind mit Ausnahme des "ungleich"-Operators auch identisch:

* `<` kleiner
* `<=` kleiner oder gleich
* `>` größer
* `>=` größer oder gleich
* `==` gleich
* `~=` ungleich

Das Ergebnis eines Vergleichs ist entweder `true` oder `false`. MATLAB verwendet
hier also Kleinbuchstaben im Vergleich zu Python mit `True` und `False`.

Basierend auf dem Ergebnis eines Vergleichs kann Code ausgeführt werden. Das
entsprechende Verzweigungskonstrukt lautet

```matlab
if x < 10
    disp('Die Zahl ist kleiner als 10.')
elseif x < 15
    disp('Die Zahl ist nicht kleiner als 10, aber kleiner als 15.')
else
    disp('Die Zahl ist größer oder gleich 15.')
end
```

Wie Sie sehen, werden nach den Bedingungen keine Doppelpunkte gesetzt. Die
Verzweigung wird mit einem `end` abgeschlossen.

```{dropdown} Video zu "Matlab - 4.1 if else elseif" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/9FA1RP4vj6U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

In MATLAB gibt es noch eine Art der Programmverzeigung, die es in Python nicht
gibt. Die sogenannte `switch`-Verzweigung ist vor allem dann interessant, wenn
sehr viele Bedingungen überprüft werden sollen, kann aber jederzeit durch ein
if-elseif-else ersetzt werden.

```{dropdown} Video zu "Matlab - 4.2 switch - Anweisung" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/bkXKQKux-Dc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Schleifen

Natürlich kennt MATLAB auch Schleifen. Sowohl die while-Schleife als auch die
for-Schleife können in MATLAB benutzt werden.

Eine Schleife mit Bedingung wird mit `while` eingeleitet. Wir setzen einen
Zähler auf Eins und erhöhen in jedem Schleifendurchgang den Wert des Zählers um
Eins, solange wie der Zähler kleiner gleich 10 ist.

```matlab
zaehler = 1;
while zaehler <= 10
    disp(zaehler)
    zaehler = zaehler + 1;
end
```

```{dropdown} Video zu "Matlab - 4.3 while-Anweisung" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/sSw9QKAjESE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

Bei der for-Schleife wird eine Liste von Zahlen abgearbeitet oder ein
Zahlenbereich durchlaufen. Das folgende Code-Beispiel gibt nacheinander die
Zahlen 2, 6, 8 und -1 auf dem Bildschirm aus.

```matlab
for zahl = [2, 6, 8, -1]
    disp(zahl)
end
```

Wieder wird die Schleife nicht durch einen Doppelpunkt eingeleitet. Die Schleife
wird durch das `end` beendet. Alternativ kann der Doppelpunktoperator genutzt
werden, um eine Liste mit Zahlen nach einem Muster zu generieren. Der folgende
Code zählt von 10 runter.

```matlab
for zahl = 10: -1 : 0
    disp(zahl)
end
disp('Die Rakete startet...')
```

```{dropdown} Video zu "Matlab - 4.4 for - Anweisung" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/2qGElJdocnI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

In beiden Schleifen-Varianten sind `continue` und `break` möglich, um die
Schleife vorzeitig zu einem neuen Schleifendurchgang zu veranlassen oder die
Schleife vorzeitig abzubrechen. Wer an Details interessiert ist, findet sie in
den folgenden Videos.

```{dropdown} Video zu "Matlab - 4.5 continue - Anweisung" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/VdHhQhIjasg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Matlab - 4.6 break - Anweisung" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/bIXuZXPSblU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Diagramme

Bei der Einführung in die Datenvisualisierung mit Matplotlib in Python haben wir
absichtlich die zustandsorientierte Schnittstelle der Bibliothek genutzt. Diese
wurde nach dem Vorbild von MATLAB gestaltet, so dass Diagramme mit den uns
bekannten Anweisungen funktionieren.

```matlab
x = linspace(-3, 3, 100);
y = 3 .* x + 7;

figure();
plot(x,y);
xlabel('Ursache');
ylabel('Wirkung');
title('Liniendiagramm');
```

Auch das Balkendiagramm mit `bar()` und das Streudiagramm mit `scatter()`
funktionieren wie gewohnt, solange die Daten rein numerisch, also aus Zahlen,
bestehen. Die Verarbeitung von Strings ist in MATLAB etwas komplizierter, so
dass Balkendiagramme mit Strings als Klassenbezeichnungen etwas umständlicher
umzusetzen sind.

Ein weiterer Unterschied tritt auf, wenn zwei Diagramme in einer Grafik
gemeinsam dargestellt werden sollen. Dann muss nach dem ersten Diagramm der
Befehl `hold on` ausgeführt werden, damit die nachfolgenden Diagramme in
dieselbe Grafik gezeichnet werden.

```{dropdown} Video zu "Matlab - 5.1 Plot erstellen" von Mathe? Logisch!
<iframe width="560" height="315" src="https://www.youtube.com/embed/2admMlXzlSw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Regression

Als letztes Beispiel für MATLAB betrachten wir die Regression. Zunächst
betrachten wir erneut ein künstliches Beispiel mit sieben Messwerten, die wir
als Streudiagramm visualisieren.

```matlab
x = [-1, 0, 1, 2, 3, 4, 5]
y = [5.4384, 14.3252, 19.2451, 23.3703, 18.2885, 13.8978, 3.7586]

figure()
scatter(x,y)
xlabel('Ursache')
ylabel('Wirkung')
title('Künstliche Messdaten');
```

Die Funktion zur Bestimmung eines Regressionspolynoms lautet `polyfit(x, y,
grad)`. Wie bei der entsprechenden Python-Funktion werden der Funktion zunächst
die Messwerte übergeben (Ursache zuerst, Wirkung als zweites). Als drittes
Argument wird der gewünschte Polynomgrad übergeben. Wir probieren eine
Regressionsparabel.

```matlab
p = polyfit(x, y, 2)
```

Mit `polyval(p, x)` werten wir ein Polynom `p` an der Stelle `x` aus. Um also
die Regressionsparabel zusätzlich zu den Messwerten zu visualisieren, verwenden
wir den folgenden Code.

```matlab
% Künstliche Messdaten
x = [-1, 0, 1, 2, 3, 4, 5];
y = [5.4384, 14.3252, 19.2451, 23.3703, 18.2885, 13.8978, 3.7586];

% Regression
p = polyfit(x, y, 2);
x_modell = linspace(-1, 5, 100);
y_modell = polyval(p, x_modell);

% Visualisierung
figure();
scatter(x,y);
hold on;
plot(x_modell, y_modell);
xlabel('Ursache');
ylabel('Wirkung');
title('Künstliche Messdaten');
```

In diesem Beispiel haben wir Kommentare benutzt, um die einzelnen
Code-Abschnitte besser kenntlich zu machen. Wie Sie sehen ist das
Kommentarzeichen in MATLAB ein Prozentzeichen `%`.

## Weiteres Lehrmaterial

Wer an weiteren Details zu MATLAB interessiert ist, kann das Vorlesungsskript

> [https://gramschs.github.io/book_matlab/intro.html](https://gramschs.github.io/book_matlab/intro.html)

nutzen, um anhand von Mini-Übungen die MATLAB-Kenntnisse zu vertiefen. Zum
anderen empfehle ich die YouTube-Playlist

> [So lernst Du
> Matlab](https://www.youtube.com/playlist?list=PLbvyqE-qsk65zQMPD6zlek3WfCz-e1BKY)

von Mathe? Logisch!, aus der auch die bisher verlinkten Videos stammen, die aber
auch noch anderen Themen behandelt.
