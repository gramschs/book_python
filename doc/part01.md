# Einstieg in die Programmierung

## Lernziele

Dieses Jupyter Notebook ist der Einstieg in die wissenschaftliche Programmierung
mit Python. Zuerst werden wir Python als Taschenrechner benutzen. Danach
beschäftigen wir uns mit grundlegenden Begriffen der Informatik, nämlich

* Hardware und Software,
* Betriebssystem, Anwendungssoftware (App) und Bibliotheken
* Programm und Skript sowie
* kompilierte und interpretierte Programmiersprachen.

Nach dem kurzen Ausflug in die Theorie der Informatik widmen wir uns einfachen
Datentypen und Variablen. Zusammen mit einfachen Python-Kommandos, um Eingaben
einer Benutzerin oder eines Benutzers abzufragen und auf dem Bildschirm
auszugeben, wird es uns möglich, erste kleinere Python-Skripte zu schreiben.
Das entspricht auch dem grundlegenden Ablauf in der Datenverarbeitung, dem
EVA-Prinzip, das für Eingabe, Verarbeitung und Ausgabe steht.

## Python als Taschenrechner

Was ist überhaupt Python? Wikipedia erklärt Python folgendermaßen: 

> "Python ([ˈpʰaɪθn̩], [ˈpʰaɪθɑn], auf Deutsch auch [ˈpʰyːtɔn]) ist eine
  universelle, üblicherweise interpretierte, höhere Programmiersprache. Sie hat
  den Anspruch, einen gut lesbaren, knappen Programmierstil zu fördern. So
  werden beispielsweise Blöcke nicht durch geschweifte Klammern, sondern durch
  Einrückungen strukturiert." 
  (Quelle: [Wikipedia](https://de.wikipedia.org/wiki/Python_(Programmiersprache))

Aber benutzen wir Python erst einmal als Taschenrechner, bevor wir mit der
Programmierung starten. Im Folgenden sehen Sie, wie die Grundrechenarten in
Python verwendet werden:

Addition:

```python
2+3
```

Subtraktion:

```python
2-3
```

Multiplikation:

```python
2*4
```

Division:

```python
8/2
```

Potenzierung:

```python
3**2
```

In diesem interaktiven Vorlesungsskript können Sie Python direkt ausprobieren.
In der gleich folgenden Code-Zelle ist Platz für Ihren Python-Code. Die
Code-Zelle ist zunächst mit einem Kommentar beschriftet, in diese Fall mit dem
Kommentar 

```python
# Geben Sie nach diesem Kommentar Ihren Code ein:
```
Alles was nach dem Hashtag # kommt, wird von Python ignoriert. Die sogenannten
Kommentare, die durch das Hashtag-Zeichen eingeleitet werden, sind für uns
Menschen bestimmt.

Wenn Sie dieses Skript in einem Jupyter Notebook durcharbeiten, können Sie
direkt in die nächste Code-Zelle (nach der Kommentarzeile) Ihren Python-Code
schreiben und ausführen lassen. Wenn Sie dieses Skript Online lesen, klicken Sie
bitte zuerst auf das Raketensymbol oben rechts und auf Live Code, um eine
interaktive Code-Zelle erzeugen zu lassen. Beim ersten Start des Live Codes kann
es etwas länger dauern. Sie erkennen, dass die Code-Zelle interaktiv geworden
ist, wenn die Knöpfe `run`, `restart` und `restart & run all` erschienen sind.
Dann geben Sie Ihren Code  (nach der Kommentarzeile) ein und drücken auf run.

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:
```

Selbstverständlich beherrscht Python auch Klammerregeln. Probieren Sie es aus!

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie Python den Term $3\cdot (7-10)+5$ berechnen. 
```
```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:
```
````{admonition} Lösung
:class: minisolution, toggle
```python
3 * (7-10) + 5
```
````

## Grundlegende Begriffe beim Programmieren

Programme oder Skripte, die in Python programmiert werden, können in der Regel
auch nur in Python ausgeführt werden. 

Aber ... 
* Was ist überhaupt ein Programm oder ein Skript? 
* Was ist der Unterschied zwischen einer App und einer Software? 
* Was sind Programmiersprachen?
* Was ist ein Interpreter und was ist ein Compiler?
* Und was hat es mit Bibliotheken auf sich?

Fangen wir erstmal von vorne an mit der grundlegen Bedeutung des Fachbegriffes
Software im Unterschied zu Hardware.





### Programmiersprachen und das erste Python-Programm

Es gibt viele Programmiersprachen und jede hat ihre Vorteile und ihre Nachteile.
Aber was ist eine Programmiersprache überhaupt? Eine **Programmiersprache** ist
die formale Sprache zur Formulierung von Datenstrukturen und Algorithmen (=
Abfolge von Anweisungen), die von einem Computer ausgeführt werden können. 

Es gibt nicht die wichtigste oder beste Programmiersprache, sondern die Auswahl
der Programmiersprache sollte sich stets nach der anvisierten Anwendung richten.
Der sogenannte Tiobe-Index zeigt die Beliebtheit der 50 wichtigsten
Programmiersprachen: 

https://www.tiobe.com/tiobe-index/ 

In der Anfangszeit der Computer waren Programmiersprachen noch sehr nahe am
Computern ausgerichtet. Hier sehen Sie ein Beispiel, wie in der
Programmiersprache Assembler die Meldung "Hallo Welt" auf dem Monitor angezeigt
wird:

```{figure} pics/part01_assembler.png
:name: part01_assembler

"Hallo Welt" in Assembler (Quelle: [Wikipedia/Assemblersprache](https://de.wikipedia.org/wiki/Assemblersprache))
```

In Python ist dieser Programmcode wesentlich kürzer:

```python
print('Hallo Welt')
```

```{admonition} Mini-Übung
:class: miniexercise
Kopieren Sie die Zeile `print('Hallo Welt')` in die nächste Code-Zelle unter die Kommentarzeile und ersetzen Sie Welt durch Ihren Namen. Ihr erstes Computerprogramm in Python :-)
```
```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:
```
````{admonition} Lösung
:class: minisolution, toggle
```python
print('Hallo Simone')
```
````

Heute werden nur noch die sogenannten **höheren Programmiersprachen** verwendet
(wie Python, MATLAB oder C++), die für Menschen leichter verständlich sind.
Dafür müssen dann Programme, die in höheren Programmiersprachen geschrieben
sind, in **Maschinensprache** übersetzt werden. Verschiedene Programmiersprachen
verwenden dazu unterschiedliche Prinzipien. Die beiden wichtigsten Vertreter
sind 

* **Compiler-Programmiersprachen** und
* **Interpreter-Programmiersprachen**. 

Bei Compiler-Programmiersprachen wird der Programmcode vorab in Maschinensprache
übersetzt und der Anwender erhält die Anwendungssoftware in Maschinensprache
(bei Windows beispielsweise als exe-Datei). Den Vorgang des Übersetzens nennt
man **kompilieren**. Bei Interpreter-Sprachen wird der Code in dem Moment in
Maschinensprache übersetzt, in dem das Programm läuft bzw. ausgeführt wird.
Während also das Programm läuft, muss gleichzeitig – quasi im Hintergrund – der
Übersetzer arbeiten und die höhere Programmiersprache in Maschinensprache
**interpretieren**. Daher der Name Interpreter-Sprache. Manchmal wird Code, der
kompiliert wurde und dann eigenständig lauffähig ist, als **Programm**
bezeichnet. Dahingegen wird Code, der interpretiert wird und dringend auf einen
gerade laufenden Interpreter angewiesen ist, oft als Skript bezeichnet. Im
Alltag geht diese Unterscheidung meist unter und wir verwenden den Begriff
Programm auch für Python-Skripte.


## Los geht es mit dem Programmieren - Datentypen in Python

Der Computer kann Informationen nur als 0 oder 1 verarbeiten. Auf dem
Speichermedium oder im Speicher selbst werden Daten daher als eine Folge von 0
und 1 gespeichert. Damit es für uns Programmiererinnen und Programmierer
einfacher wird, Daten zu speichern und zu verarbeiten, wurden Datentypen
eingeführt.  

**Datentypen** fassen gleichartige Objekte zusammen und stellen passende
Operationen zur Verfügung. Es hängt von der Programmiersprache ab, welche
Datentypen zur Verfügung stehen, wie diese im Hintergrund gespeichtert werden
und welche Operationen damit möglich sind. In diesem Vorlesungsskript
beschäftigen wir uns mit den einfachen Datentypen

* Integer
* Float
* String

### Zahlen 

In der Programmierung unterscheidet man grundsätzlich zwischen zwei Zahlenarten,
den **Ganzzahlen** und den Gleitkommazahlen, die auch **Fließkommazahlen**
genannt werden. Die Ganzzahlen werden in der Mathematik als ganze Zahlen
bezeichnet. In der Informatik wird meist der englische Begriff **Integer**
verwendet. Mit Integern können wir ganz normal rechnen, also Operationen
ausführen. Einige davon haben wir ja bereits ausprobiert, als wir Python als
Taschenrechner benutzt haben:

```{code-cell} ipython3
2 * (3 + 4)
```

Sobald wir eine Division vorliegen haben, die nicht aufgeht, verlassen wir den
Bereich der ganzen Zahlen und kommen automatisch zu den Fließkommazahlen. In der
Informatik wird eine Fließkommazahl als Float bezeichnet. Python rechnet
automatisch mit dem richtigen Datentyp, wie Sie hier sehen:

```{code-cell} ipython3
2/5
```

Beachten Sie bitte: Das Dezimaltrennzeichen ist ein Punkt, nicht ein Komma wie
im Deutschen. Aber ansonsten funktioniert alles wie erwartet:

```{code-cell} ipython3
2.3 + 4.6
```

```{code-cell} ipython3
1.4 - 5.2
```

```{code-cell} ipython3
(-3.8) * 3.1
```

```{code-cell} ipython3
2.4 / 0.3
```

```{code-cell} ipython3
2.5**10
```

Das folgende Video fasst Zahlen in Python zusammen.

```{code-cell} ipython3
:tags: [remove-input]

IFrame(width=560, height=315, src="https://www.youtube.com/embed/VtiDkRDPA_c")
```

### Strings

Daten sind aber sehr oft keine Zahlen. Beispielsweise könnte man sich
vorstellen, eine Einkaufsliste zu erstellen und diese im Computer oder in einer
Notiz-App auf dem Handy zu speichern. Eine solche Zeichenkette heißt in der
Informatik **String**. Mit Zeichen meint man dabei Zahlen, Buchstaben oder
andere wie beispielsweise !"§$%&/()=?.

Strings werden in Python durch doppelte Anführungszeichen definiert:

```{code-cell} ipython3
"Dies ist ein String!"
```

Auf Strings und ihre Anwendungen kommen wir später noch zurück. Wenn Sie bereits
jetzt mehr erfahren wollen, können Sie sich folgendes Video ansehen.

```{code-cell} ipython3
:tags: [remove-input]

IFrame(width=560, height=315, src="https://www.youtube.com/embed/sTEf4_mrLvw")
```

### Variablen 

**Variablen** sind beschriftete Schubladen. Oder anders formuliert sind
Variablen Objekte, denen man einen Namen gibt. Technisch gesehen sind diese
Schubladen ein kleiner Bereich im Arbeitsspeicher des Computers. Was in diesen
Schubladen aufbewahrt wird, kann sehr unterschiedlich sein. Beispielsweise die
Telefonnummer des ADAC-Pannendienstes, die 10. Nachkommastelle von $\pi$ oder die
aktuelle Position des Mauszeigers können in den Schubladen enthalten sein. 

Wir verwenden Variablen, um bestimmte Werte oder ein bestimmtes Objekt zu
speichern. Eine Variable wird durch **Zuweisung** erzeugt. Damit meinen wir,
dass eine Schublade angelegt wird und die Schublade dann erstmalig gefüllt wird.
Das erstmalige Füllen der Schublade nennt man in der Informatik auch
**Initialisieren**.

```{code-cell} ipython3
x = 0.5
```

Sobald die Variable x in diesem Beispiel durch eine Zuweisung von 0.5 erstellt
wurde, können wir sie verwenden:

```{code-cell} ipython3
x * 3
```

```{code-cell} ipython3
x + 17.8
```

Variablen müssen initialisiert (erstmalig mit einem Wert versehen) werden, bevor
sie verwendet werden können, sonst tritt ein Fehler auf. 

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie in die nächste Code-Zelle einfach den Buchstaben `n` unter die Kommentarzeile und lassen Sie dann die Code-Zelle mit `run` vom Python-Interpreter ausführen. Was beobachten Sie? Recherchieren Sie im Internet nach der Fehlermeldung. 
```
```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```
````{admonition} Lösung
:class: minisolution, toggle
```python
n
```
Der Interpreter zeigt in rot eine Fehlermeldung an: "NameError: name 'n' is not defined". Damit weist der Interpreter darauf hin, dass die Variable bisher nicht mit einem Wert versehen wurde, sie ist nicht intialisiert worden. Daher kann damit auch nicht gearbeitet werden.
````



Gerne können Sie sich auch folgendes Video auf YouTube ansehen, das eine
Einführung in das Thema Variablen in Python gibt.

```{code-cell} ipython3
:tags: [remove-input]

IFrame(width=560, height=315, src="https://www.youtube.com/embed/jfOLXKPGXJ0")
```

### Zuweisungsoperator

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
auch gleich die `print()`-Funktion, die wir bei unserem ersten Python-Programm
"Hallo Welt" bereits kennengelernt haben, um den Wert der Variablen `x` ausgeben
zu lassen:

```{code-cell} ipython3
x = 4     
x = x + 1
print(x)
```

Der Zuweisungsoperator ist äußerst wichtig in der Python-Programmierung. Daher
empfehle ich Ihnen folgende Video.

```{code-cell} ipython3
:tags: [remove-input]

IFrame( width=560, height=315, src="https://www.youtube.com/embed/XKFQ2_et5k8")
```

### Richtlinien für Variablennamen

Früher war der Speicherplatz von Computern klein, daher wurden häufig nur kurze
Variablennamen wie beispielsweise i oder N verwendet. Heutzutage ist es
Standard, nur in Ausnahmefällen (z.B. in Schleifen, dazu kommen wir noch) kurze
Variablennamen zu nehmen. Stattdessen werden Namen benutzt, bei denen man
erraten kann, was die Variable für einen Einsatzzweck hat. Beispielsweise lässt
der Code

```{code-cell} ipython3
m = 0.19
n = 80
b = n + m * n
print(b)
```

nur schwer vermuten, was damit bezweckt wird. Oder können Sie erahnen, was dort passieren soll?
Dagegen erahnt man bei diesem Code schon eher, was bezweckt wird:

```{code-cell} ipython3
mehrwertsteuersatz = 19/100
nettopreis = 80
bruttopreis = nettopreis + mehrwertsteuersatz * nettopreis
print(bruttopreis)
```

Verwenden Sie für Variablennamen nur ASCII-Zeichen, also keine Umlaute wie ö, ü
oder ß. Zahlen sind erlaubt, aber nicht am Anfang des Namens. Es ist sinnvoll,
lange Variablen durch einen Unterstrich besser lesbar zu gestalten (sogenannte
Snake-Case-Formatierung). Ich empfehle für Variablennamen beispielsweise
`dateiname_alt` oder `dateiname_neu`, wenn beispielsweise eine Datei umbenannt
wird. Sie sind frei in der Gestaltung der Variablennamen, verboten sind nur die
sogannnten **Schlüsselwörter**. Schlüsselwörter sind beispielsweise eingebaute
Kommandos an den Python-Interpreter. Würden Sie diese als Variablennamen
benutzen, wüsste der Python-Interpreter nicht, ob das Kommando oder die Variable
gemeint ist.

```{admonition} Mini-Übung
:class: miniexercise
Initialisieren Sie eine Variable namens alter mit Ihrem aktuellen Alter, eine Variable ``rentenalter`` mit dem Zahlenwert ``67`` und berechnen Sie dann, wie viele Jahre es noch bis zum Renteneintritt dauert. 
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: minisolution, toggle
```python
# Geben Sie nach diesem Kommentar Ihren Code ein:
alter = 21
rentenalter = 67
print(rentenalter - alter)
```
````

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

### Die input()-Funktion

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
x = input('Bitte geben Sie Ihren Namen ein: ');
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
x = input('Bitte geben Sie Ihren Namen ein: ');
print('Hallo')
print(x)
```

Kopieren Sie diesen Code in die nächste Code-Zelle und probieren Sie es aus!

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

In dem folgenden Video sehen Sie weitere Erläuterungen zur input()-Funktion.

```{code-cell} ipython3
:tags: [remove-input]

IFrame(width=560, height=315, src="https://www.youtube.com/embed/I9h1c-121Uk")
```

### Umwandlung von Datentypen

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
Details in diesem Video:

```{code-cell} ipython3
:tags: [remove-input]

IFrame(width=560, height=315, src="https://www.youtube.com/embed/u_ECGvn1Z2c")
```

## Zusammenfassung und Ausblick

Der Einstieg in die wissenschaftliche Programmierung mit Python ist zunächst
theoretisch. Zuerst haben wir uns mit grundlegenden Fachbegriffen der
theoretischen Informatik und dem EVA-Prinzip beschäftigt. Aber bereits mit den
ersten Funktionen in Python wie `input()` und `print()` sowie der Benutzung von
Variablen können wir erste Python-Skripte programmieren.
