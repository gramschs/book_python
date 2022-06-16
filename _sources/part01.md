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

# Einstieg in die Programmierung mit Python

## Lernziele

Dieses Jupyter Notebook ist der Einstieg in die wissenschaftliche Programmierung
mit Python. Zuerst werden wir Python als Taschenrechner benutzen. Danach
beschäftigen wir uns mit grundlegenden Begriffen der Informatik, nämlich

* Hardware und Software,
* Programm und Skript,
* kompilierte und interpretierte Programmiersprachen sowie
* Betriebssystem, Anwendungssoftware (App) und Bibliotheken (Toolbox).

Nach dem kurzen Ausflug in die Theorie der Informatik widmen wir uns einfachen
Datentypen und Variablen. Zusammen mit einfachen Python-Kommandos, um Eingaben
einer Benutzerin oder eines Benutzers abzufragen und auf dem Bildschirm
auszugeben, wird es uns möglich, erste kleinere Python-Skripte zu schreiben.
Das entspricht auch dem grundlegenden Ablauf in der Datenverarbeitung, dem
EVA-Prinzip, das für Eingabe, Verarbeitung und Ausgabe steht.

## Python als Taschenrechner

Was ist überhaupt Python? Wikipedia erklärt 
[Python](https://de.wikipedia.org/wiki/Python_(Programmiersprache)) folgendermaßen: 

> Python ([ˈpʰaɪθn̩], [ˈpʰaɪθɑn], auf Deutsch auch [ˈpʰyːtɔn]) ist eine
  universelle, üblicherweise interpretierte, höhere Programmiersprache. Sie hat
  den Anspruch, einen gut lesbaren, knappen Programmierstil zu fördern. So
  werden beispielsweise Blöcke nicht durch geschweifte Klammern, sondern durch
  Einrückungen strukturiert.

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
Kommentar `# Hier Ihr Code`. Alles was nach dem Hashtag kommt, wird von Python
ignoriert. Die sogenannten Kommentare, die durch das Hashtag-Zeichen eingeleitet
werden, sind für uns Menschen bestimmt.

Wenn Sie dieses Skript in einem Jupyter Notebook durcharbeiten, können Sie
direkt in die nächste Code-Zelle (nach der Kommentarzeile) Ihren Python-Code
schreiben und ausführen lassen. Wenn Sie dieses Skript Online lesen, klicken Sie
bitte zuerst auf das Raketensymbol oben rechts und auf Live Code, um eine
interaktive Code-Zelle erzeugen zu lassen. Beim ersten Start des Live Codes kann
es etwas länger dauern. Sie erkennen, dass die Code-Zelle interaktiv geworden
ist, wenn die Knöpfe `run`, `restart` und `restart & run all` erschienen sind.
Dann geben Sie Ihren Code  (nach der Kommentarzeile) ein und drücken auf run. 

```{code-cell} ipython3
# Hier Ihr Code

```

Selbstverständlich beherrscht Python auch Klammerregeln. Probieren Sie es aus!
Kleinere Übungen zum sofortigen Ausprobieren sind in sogenannten Mini-Übungen.
Erst kommt der Text der Übungsaufgabe, dann eine leere Code-Zelle mit dem
Kommentar `# Hier Ihr Code` und zum Abschluss die Lösung. Anfangs ist die Lösung
verdeckt, aber Sie können Sie jederzeit aufklappen, um Ihre Lösung zu
kontrollieren.

```{exercise}
:label: part01_miniexercise01
Lassen Sie Python den Term $3\cdot (7-10)+5$ berechnen. 
```
```{code-cell} ipython3
# Hier Ihr Code

```
````{solution} part01_miniexercise01
:label: part01_minisolution01
:class: dropdown
```python
3 * (7-10) + 5
```
````

## Python als Programmiersprache

Programme oder Skripte, die in Python programmiert werden, können in der Regel
auch nur in Python ausgeführt werden. 

Aber ... 
* Was ist überhaupt ein Programm oder ein Skript? 
* Was ist der Unterschied zwischen einer App und einer Software? 
* Was sind Programmiersprachen?
* Was ist ein Interpreter und was ist ein Compiler?
* Und was hat es mit den Toolboxen auf sich?

Fangen wir erstmal von vorne an mit der grundlegen Bedeutung des Fachbegriffes
Software im Unterschied zu Hardware.

### Hardware und Software

Computer, mobile Geräte wie Smartphones oder auch technische Systeme wie eine
Anlagensteuerung bestehen aus zwei Komponenten: Hardware und Software. Dabei
bezeichnen wir mit Hardware alle physischen Kompenten eines Systems, also die
elektronischen und mechanischen Bauteile. Die Software dahingegen umfasst die
Programme und deren Dokumentation sowie Daten. Man könnte auch sagen, dass
Hardware die materiellen Teile eines Computersystems bezeichnet, während
Software die nicht-materiellen Teile zusammenfasst. 

Bitte schauen Sie sich jetzt kurz um. Welche Hardware fällt Ihnen auf, wenn Sie
den Blick schweifen lassen? Tragen Sie in die nächste Text-Zelle Ihre Hardware
ein.

```{exercise}
:label: part01_miniexercise02
Notieren Sie sich Hardware ein, die Sie gerade sehen oder die Ihnen generell einfällt:
* xxx
* xxx
```
````{solution} part01_miniexercise02
:label: part01_minisolution02
:class: dropdown
* Monitor
* Maus
* Tastatur
* PC
* Webcam (Kamera)
* Headset
* ...
````

Nachdem Sie Ihre Komponenten notiert haben, können Sie den Begriff
[Hardware](https://de.wikipedia.org/wiki/Hardware) noch einmal bei Wikipedia
nachlesen. Wikibooks bietet auch ein passendes Buch zu
[Computerhardware](https://de.wikibooks.org/wiki/Computerhardware) an.

Software ist eine Zusammenfassung der nicht-materiellen Komponenten eines
Computersystems. Wikipedia listet hier gleich drei verschiedene ISO-Normen zur
Definition von [Software](https://de.wikipedia.org/wiki/Software) auf.

Wir verwenden im Folgenden die weitreichendste Definition von Software, wonach
Software

* Programme
* Dokumentation und
* Daten

umfasst.

Die letzteren beiden Begriffe sind am einfachsten zu erklären, Mit Dokumentation
sind Bedienungsanleitungen und Handbücher gemeint, aber auch die technische
Dokumentation, die für andere Informatiker:innen gedacht ist und in die
Benutzer:innen eines Computersystems in der Regel keinen Einblick haben. Daten
wiederum sind alle Beobachtungen oder Messungen. In der digitalisierten Form
werden sie normalerweise durch Zahlenwerte repräsentiert. 

Es gibt viele Programmiersprachen und jede hat ihre Vorteile und ihre Nachteile.
Aber was ist eine Programmiersprache überhaupt? Eine Programmiersprache ist die
formale Sprache zur Formulierung von Datenstrukturen und Algorithmen (= Abfolge
von Anweisungen), die von einem Computer ausgeführt werden können. Es gibt nicht
die wichtigste oder beste Programmiersprache, sondern die Auswahl der
Programmiersprache sollte sich stets nach der anvisierten Anwendung richten. Der
sogenannte Tiobe-Index zeigt die Beliebtheit der 50 wichtigsten
Programmiersprachen: 

https://www.tiobe.com/tiobe-index/ 

In der Anfangszeit der Computer waren Programmiersprachen noch sehr nahe am
Computern ausgerichtet. Hier sehen Sie ein Beispiel, wie in der
Programmiersprache Assembler die Meldung "Hallo Welt" auf dem Monitor angezeigt
wird:

```{figure} pics/part01_assembler.png
:name: part01_assembler

"Hallo Welt" in Assembler (Quelle: https://de.wikipedia.org/wiki/Assemblersprache)
```

In Python ist dieser Programmcode wesentlich kürzer (in die Code-Zelle klicken
und run ausführen):

```{code-cell} ipython3
print('Hallo Welt')
```

```{exercise}
:label: part01_miniexercise03
Kopieren Sie die Zeile `print('Hallo Welt')` in die nächste Code-Zelle unter die Kommentarzeile und ersetzen Sie Welt durch Ihren Namen. Ihr erstes Computerprogramm in Python :-)
```
```{code-cell} ipython3
# Hier Ihr Code

```
````{solution} part01_miniexercise03
:label: part01_minisolution03
:class: dropdown
```python
print('Hallo Simone')
```
````

Heute werden nur noch die sogenannten höheren Programmiersprachen verwendet (wie
Python, MATLAB oder C++), die für Menschen leichter verständlich sind. Dafür
müssen dann Programme, die in höheren Programmiersprachen geschrieben sind, in
**Maschinensprache** übersetzt werden. Verschiedene Programmiersprachen
verwenden dazu unterschiedliche Prinzipien. Die beiden wichtigsten Vertreter
sind **Compiler-Programmiersprachen** und **Interpreter-Programmiersprachen**. 

Bei Compiler-Programmiersprachen wird der Programmcode vorab in Maschinensprache
übersetzt und der Anwender erhält die Anwendungssoftware in Maschinensprache
(bei Windows beispielsweise als exe-Datei). Den Vorgang des Übersetzens nennt
man **Kompilieren**. Bei Interpreter-Sprachen wird der Code in dem Moment in
Maschinensprache übersetzt, in dem das Programm läuft bzw. ausgeführt wird.
Während also das Programm läuft, muss gleichzeitig – quasi im Hintergrund – der
Übersetzer arbeiten und die höhere Programmiersprache in Maschinensprache
**interpretieren**. Daher der Name Interpreter-Sprache. Manchmal wird Code, der
kompiliert wurde und dann eigenständig lauffähig ist, als **Programm**
bezeichnet. Dahingegen wird Code, der interpretiert wird und dringend auf einen
gerade laufenden Interpreter angewiesen ist, oft als Skript bezeichnet. Im
Alltag geht diese Unterscheidung meist unter und wir verwenden den Begriff
Programm auch für Python-Skripte.

```{exercise}
:label: part01_miniexercise04
Recherchieren Sie im Internet und notieren Sie Ihre Antworten.

1. Ordnen Sie folgende Programmiersprachen den beiden Kategorien Compiler-Sprache oder Interpreter-Sprache zu: C, C++, Fortran, Java, Matlab und Python.
2. Stellen Sie eine Vermutung auf: in welcher Programmiersprache können die schnelleren Programme geschrieben werden?
3. Raten Sie: welche Programmiersprachen sind leichter zu lernen und warum?
```
````{solution} part01_miniexercise04
:label: part01_minisolution04
:class: dropdown
* Antwort 1:
Compiler-Sprache: C, C++, Fortran
Interpreter-Sprache: Java, Matlab, Python
* Antwort 2:
In der Regel sind Programme, die in einer Compiler-Sprache geschrieben wurden, schneller als interpretierte Programme. 
* Antwort 3:
In der Regel sind interpretierte Programmiersprachen leichter zu lernen, da beispielsweise Code zeilenweise auf seine Korrektheit hin überprüft werden kann.
````

Die wichtigste Software eines jeden Computersystems ist das **Betriebssystem**.
Das [Betriebssystem](https://de.wikipedia.org/wiki/Betriebssystem) umfasst alle
Computerprogramme, die notwendig sind, um überhaupt den Computer zu betreiben,
zu starten oder zu benutzen. Das Betriebssystem hat laut Wikipedia folgende
Aufgaben: 

> ... Benutzerkommunikation; Laden, Ausführen, Unterbrechen und Beenden von
  Programmen; Verwaltung und Zuteilung der Prozessorzeit; Verwaltung des
  internen Speicherplatzes für Anwendungen; Verwaltung und Betrieb der
  angeschlossenen Geräte; Schutzfunktionen z. B. durch Zugriffsbeschränkungen."

Viele Menschen denken bei Software zuerst an **Anwendungssoftware** (siehe
https://de.wikipedia.org/wiki/Anwendungssoftware). Das sind Computerprogramme,
die einen speziellen Zweck erfüllen sollen und den Benutzer oder die Benutzerin
bei Aufgaben unterstützen. Im Englischen werden solche Computerprogramme auch
als **Application** (= Anwendung, Verwendung, Einsatz) bezeichnet. 2008 hat die
Firma Apple den "iOS App Store" gegründet, um Anwendungssoftware für das iPhone
zu vertreiben. Seitdem wird immer häufiger auch im deutschen Sprachraum der Name
Application oder App für verwendet. Vielfach steht "Application" eher für
PC-Anwendungssoftware und der Kurzname "App" für Anwendungssoftware für Tablets
und Smartphones.  

Für Softwareentwickler sind — neben der Programmiersprache und den
Software-Entwicklungswerkzeugen — vor allem Bibiotheken wichtig. Eine
**Bibliothek** (siehe https://de.wikipedia.org/wiki/Programmbibliothek) ist eine
Sammlung von Programmen, die zwar einen bestimmten Zweck haben, aber
eigenständig nicht lauffähig werden. Diese Programmbibiotheken werden von
Programmiererinnen und Programmieren benutzt, um nicht ständig neu das Rad
erfinden zu müssen. Beispielsweise würde es den Software-Entwickungsprozess
verlangsamen, wenn jedesmal neu ein Programm geschrieben werden müsste, dass die
Wurzel einer Zahl berechnet oder ein Ergebnis einer Berechnung in eine Datei auf
die Festplatte schreibt. Diese Spezialaufgaben wurden bereits von anderen
Software-Entwickler:innen implmentiert und werden dann über die Bibliotheken der
Gemeinschaft zur Verfügung gestellt.

## Einfache Datentypen: Integer, Floats und Strings

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

In der Programmierung unterscheidet man grundsätzlich zwischen zwei Zahlenarten,
den **Ganzzahlen** und den Gleitkommazahlen/**Fließkommazahlen**. Die Ganzzahlen
werden in der Mathematik als ganze Zahlen bezeichnet. In der Informatik wird
meist der englische Begriff **Integer** verwendet. Mit Integern können wir ganz
normal rechnen, also Operationen ausführen. Einige davon haben wir ja bereits
ausprobiert, als wir Python als Taschenrechner benutzt haben:

```{code-cell} ipython3
2 * (3 + 4)
```

Sobald wir eine Division vorliegen haben, die nicht aufgeht, verlassen wir den Bereich der ganzen Zahlen und kommen automatisch zu den Fließkommazahlen. In der Informatik wird eine Fließkommazahl als Float bezeichnet. Python rechnet automatisch mit dem richtigen Datentyp, wie Sie hier sehen:

```{code-cell} ipython3
2/5
```

Beachten Sie bitte: Das Dezimaltrennzeichen ist ein Punkt, nicht ein Komma wie im Deutschen. Aber ansonsten funktioniert alles wie erwartet:

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

Daten sind aber sehr oft keine Zahlen. Beispielsweise könnte man sich
vorstellen, eine Einkaufsliste zu erstellen und diese im Computer oder in einer
Notiz-App auf dem Handy zu speichern. Eine solche Zeichenkette heißt in der
Informatik **String**. Mit Zeichen meint man dabei Zahlen, Buchstaben oder
andere wie beispielsweise !"§$%&/()=?.

Strings werden in Python durch doppelte Anführungszeichen definiert:

```{code-cell} ipython3
"Dies ist ein String!"
```
Auf Strings und ihre Anwendungen kommen wir später noch zurück.

## Variablen

**Variablen** sind beschriftete Schubladen. Oder anders formuliert sind
Variablen Objekte, denen man einen Namen gibt. Technisch gesehen sind diese
Schubladen ein kleiner Bereich im Arbeitsspeicher des Computers. Was in diesen
Schubladen aufbewahrt wird, kann sehr unterschiedlich sein. Beispielsweise die
Telefonnummer des ADAC-Pannendienstes, die 10. Nachkommastelle von Pi oder die
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

Wichtig ist, dass das = in der Informatik eine andere Bedeutung hat als in der
Mathematik. = meint nicht das Gleichheitszeichen, sondern den sogenannten
Zuweisungsoperator. Das ist in der Programmierung ein Kommando, das eine
Schublade befüllt oder technischer ausgedrückt, ein Objekt einer Variable
zuweist.

Variablen müssen initialisiert (erstmalig mit einem Wert versehen) werden, bevor
sie verwendet werden können, sonst tritt ein Fehler auf. 

```{exercise}
:label: part01_miniexercise05
Schreiben Sie in die nächste Code-Zelle einfach den Buchstaben `n` unter die Kommentarzeile und lassen Sie dann die Code-Zelle mit `run` vom Python-Interpreter ausführen. Was beobachten Sie? Recherchieren Sie im Internet nach der Fehlermeldung. 
```
```{code-cell} ipython3
# Hier Ihr Code

```
````{solution} part01_miniexercise05
:label: part01_minisolution05
:class: dropdown
```python
n
```
Der Interpreter zeigt in rot eine Fehlermeldung an: "NameError: name 'n' is not defined". Damit weist der Interpreter darauf hin, dass die Variable bisher nicht mit einem Wert versehen wurde, sie ist nicht intialisiert worden. Daher kann damit auch nicht gearbeitet werden.
````

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

```{code-cell} ipython3
x = 4     
x = x + 1
x
```

Python gibt automatisch den Variablennamen mit seinen Inhalt aus, wenn die Variable als letztes in der Code-Zelle steht. Gerade wenn man ein Programm entwickelt, ist dies sehr praktisch, weil man schnell sieht, welchen Inhalt Variablen haben. 

Richtlinien für Variablennamen:

Früher war der Speicherplatz von Computern klein, daher wurden häufig nur kurze Variablennamen wie beispielsweise i oder N verwendet. Heutzutage ist es Standard, nur in Ausnahmefällen (z.B. in Schleifen, dazu kommen wir noch) kurze Variablennamen zu nehmen. Stattdessen werden Namen benutzt, bei denen man erraten kann, was die Variable für einen Einsatzzweck hat. Beispielsweise lässt der Code

```{code-cell} ipython3
m = 0.19
n = 80
b = n + m * n
b
```

nur schwer vermuten, was damit bezweckt wird. Oder können Sie erahnen, was dort passieren soll?
Dagegen erahnt man bei diesem Code schon eher, was bezweckt wird:

```{code-cell} ipython3
mehrwertsteuersatz = 19/100
nettopreis = 80
bruttopreis = nettopreis + mehrwertsteuersatz * nettopreis
bruttopreis
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

```{exercise}
:label: part01_miniexercise06
Initialisieren Sie eine Variable namens alter mit Ihrem aktuellen Alter, eine Variable ``rentenalter`` mit dem Zahlenwert ``67`` und berechnen Sie dann, wie viele Jahre es noch bis zum Renteneintritt dauert. 
```
```{code-cell} ipython3
# Hier Ihr Code

```
````{solution} part01_miniexercise06
:label: part01_minisolution06
:class: dropdown
```python
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

Die einfachste und häufigste **Eingabe** erfolgt über die Tastatur. Die Funktion
`input()` stoppt das laufende Skript und erwartet eine Eingabe über die
Tastatur. Dabei wird der Text zwischen den einfachen Hochkommata angezeigt. Bei
Python wird die Eingabe als String interpretiert. Die Eingabe wird mit der Taste
Return/Enter abgeschlossen. Probieren wir es aus:

```python
input('Bitte geben Sie Ihren Namen ein: ')
```

Wir haben zwar jetzt auf Aufforderung eine Zahl eingegeben, aber verarbeitet
wurde diese Eingabe nicht. Es passierte einfach nichts. Um die Eingabe
verarbeiten zu können, speichern wir sie zunächst in einer Variablen ab. 

```python
x = input('Bitte geben Sie Ihren Namen ein: ');
```

Jetzt haben wir zwar den Namen in einer Variable gespeichert, aber so richtig passiert ist immer noch nichts. Jetzt wäre es noch schön, wenn wir dem Benutzer oder der Benuzerin unseres Skripts begrüßen können und einen entsprechenden Text anzeigen lassen können. Dazu gibt es in Python die Funktion `print()`. Damit wird - ähnlich wie bei der Funktion `input()` - der Text zwischen den einfachen Hochkommata ausgegeben.

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
# Hier Ihr Code

```


## Zusammenfassung und Ausblick

Der Einstieg in die wissenschaftliche Programmierung mit Python ist zunächst theoretisch. Zuerst haben wir uns mit grundlegenden Fachbegriffen der theoretischen Informatik und dem EVA-Prinzip beschäftigt. Aber bereits mit den ersten Funktionen in Python wie `input()` und `print()` sowie der Benutzung von Variablen können wir erste Python-Skripte programmieren.








