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

# 8.1 Debugging

Diese Woche beschäftigen wir uns vor allem mit der Fehlersuche. Selbst erfahrene
Softwareentwickler-Teams machen Fehler bei der Programmierung. Die Suche nach
Fehlern im Programm ist schwierig, kann aber durch technische Hilfsmittel
unterstützt werden, allen voran durch den Debugger (= eine Art
Fehlersuch-Werkzeug). Damit Sie den Debugger nutzen können, benötigen Sie eine
IDE (= integrated development environment) mit Debugger, also eine integrierte
Entwicklungsumgebung mit Fehlersuch-Werkzeugen. Zum Schluss beschäftigen wir uns
noch mit Testen und Dokumentation.

* Kapitel 10.1 Fehlersuche (Debugging)
* Kapitel 10.2 IDEs (integrierte Entwicklungsumgebungen)
* Kapitel 10.3 Testen und Kommentare


## 10.1 Fehlersuche (Debugging)


Aber was ist überhaupt ein Bug? In der Informatik wird ein Programmfehler
**Bug** genannt. Wie in dieser Erklärung
[Wikipedia:Programmfehler](https://de.wikipedia.org/wiki/Programmfehler)
erläutert, gibt es verschiedene Arten von Programmfehlern. Am häufigsten sind 

* syntaktische Fehler und
* semantische Fehler.

**Syntaktische Fehler** sind Fehler, bei denen das Entwickler-Team gegen die
Regeln der Programmiersprache verstoßen hat. Z.B. produziert eine fehlende
Klammer einen Syntaxfehler:
<!-- #endregion -->

```python
print('Hallo'
```

Syntaktische Fehler braucht man nicht im eigentlichen Sinn zu suchen, denn
syntaktische Fehler führen dazu, dass das Programm abbricht. Schwieriger
hingegen ist es, die Ursache des syntaktischen Fehlers zu ermitteln und den
Fehler zu beheben. Oft ist es hilfreich, die Fehlermeldung in eine
Internet-Suchmaschine einzugeben. Oft haben andere Programmierer ebenfalls schon
diesen Fehler im Programm gehabt und es gibt Erläuterungen zu dieser Fehlerart.

**Semantische Fehler** sind besonders schwer zu finden. Bei semantischen Fehlern
gibt es keine Fehlermeldung des Interpreters und das Programm läuft auch, ohne
abzustürzen. Aber das Ergebnis entspricht nicht dem, was die Entwicklerin oder
der Entwickler beabsichtigt hatte.  

In dem folgenden Programm beispielsweise soll der Notendurchschnitt von
Praxisbericht (Gewichtung 80 %) und Präsentation (20 %) berechnet werden.
Schauen Sie sich den Programmcode an. Wo ist der Fehler?

```python
note_praxisbericht = 2.7
note_praesentation = 2.3

noten_durchschnitt = 0.8 * note_praesentation + 0.2 * note_praesentation
print('Notendurchschnitt: ', noten_durchschnitt)
```

Der folgende Code soll den Benutzer nach mehreren Noten fragen und dann den
Durchschnitt berechnen. Bitte geben Sie die Noten 2, 2, 2 ein und dann 0 zum
Beenden. Der Durchschnitt ist 2, aber was berechnet das Programm? Wo ist der
Fehler?

```python
summe = 0
anzahl = 0
weitere_note_eingeben = True

while weitere_note_eingeben == True:
    note = float(input('Bitte geben Sie eine Note ein. Wenn Sie die Note 0 eingeben, ist die Noteneingabe beendet. '))
    if note == 0:
        weitere_note_eingeben = False
    else:
        summe = note
        anzahl = anzahl + 1
        
durchschnitt = summe / anzahl
print('Der Durchschnitt der Noten ist ', durchschnitt)
```

Aber wie gehen wir jetzt vor, um sicherzustellen, dass das von uns entwickelte
Programm auch den beabsichtigten Zweck erfüllt? Als erstes überlegen wir uns
Testfälle. Dazu später mehr. Auf dem Papier notieren wir uns, was das Programm
für Zwischenergebnisse liefern sollte, welche Ausgaben und welches
Gesamtergebnis. Für ein Testbeispiel mit den Noten 1.3, 3.7 und 2.3 hätten wir
also folgenden *wünschenswerten* Ablauf:

```
summe = 0
anzahl = 0
weitere_note_eingeben = True
Benutzereingabe: note = 1.3
else-Zweig: 
    summe = 1.3 
    anzahl  = 1
Benutzereingabe: note = 3.7
else-Zweig:
    summe = 5.0
    anzahl = 2
Benutzereingabe: note = 2.3
else-Zweig
    summe = 7.3
    anzahl = 3
Benutzereingabe: 0
if-Zweig:
    weitere_note_eingeben = False
durchschnitt = 7.3/3 = 2.433333333333333
Ausgabe: Der Durchschnitt der Noten ist 2.433333333333333
```

Leider fehlt uns derzeit der Einblick in unseren Programm-Code. Eine sehr
einfache und schnelle Methode ist die Fehlersuche durch print-Anweisungen. Diese
Methode funktioniert immer, kann aber bei größeren Programmen auch schnell
unübersichtlich werden. Daher ist die Weiterentwicklung der "Debugging by
Printing"-Methode der Debugger. Erweitern wir unser Programm mit
print-Anweisungen und sehen wir, was passiert, wenn wir die Noten 1.3, 3.7, 2.3
und 0 eingeben:

```python
summe = 0
print('summe = ', summe)
anzahl = 0
print('anzahl = ', anzahl)
weitere_note_eingeben = True
print('weitere_note_eingeben = ', weitere_note_eingeben)

while weitere_note_eingeben == True:
    note = float(input('Bitte geben Sie eine Note ein. Wenn Sie die Note 0 eingeben, ist die Noteneingabe beendet. '))
    print('note = ', note)
    if note == 0:
        weitere_note_eingeben = False
        print('if-Zweig: note = ', note)
        print('if-Zweig: weitere_note_eingeben = ', weitere_note_eingeben)
    else:
        summe = note
        print('else-Zweig: summe = ', summe)
        anzahl = anzahl + 1
        print('else-Zweig: anzahl = ', anzahl)
        
durchschnitt = summe / anzahl
print('durchschnitt = ', durchschnitt)
print('Der Durchschnitt der Noten ist ', durchschnitt)
```

## Aufgabe 

Kopieren Sie den folgenden Code in eine Code-Zelle. Finden Sie die Fehler und
korrigieren Sie die Fehler.

```python
passwort = input("Hallo, Pirat! Wie lautet das Passwort: )
if passwort in ["Arrr!"):
    print('Ich grüße Sie!')
elif
print("Zugang verweigert.")
```


```python

```

## Aufgabe 

Ein Zeitreisender kommt auf Sie zu. Fragen Sie ihn nach dem Jahr, aus dem er
kommt und begrüßen Sie ihn. Falls er aus einem Jahr vor 1900 kommt mit "Sie
kommen ja aus der Vergangenheit!", zwischen 1900 und 2021 mit "Sie stammen also
aus unserer Zeit!" und ansonsten mit "Können Sie mir die Lottozahlen von
nächster Woche verraten?". Schreiben Sie als erstes Ihr eigenes Programm in der
nächsten Code-Zelle:

```python

```

 Vergleichen Sie anschließend Ihr Programm mit dem folgenden Code und
 korrigieren Sie die Fehler.
 
 ```python
jahr == int.input("Ein Zeitreisender??? Aus welchem Jahr kommen Sie denn? '))

if jahr <= 1900
    print ('Sie kommen ja aus der Vergangenheit!')
elif jahr > 1900 && year < 2020:
    print ("Sie stammen also aus unserer Zeit!")
elif:
    print ("Können Sie mir die Lottozahlen von nächster Woche verraten?'')
```

```python

```

## Aufgabe

Die folgende Klasse initalisiert ein Objekt mit Vorname, Nachname und definierte
eine Methode vorstellen. Anschließend wird die Klasse benutzt. Korrigieren Sie
die Fehler. 

```python
classy Person:
  def __initalize__(self, vorname, nachname):
    self.first = vorname
    self.last = nach_name
  def vorstellen(self):
  print("Guten Tag. Mein Name ist + " self.vorname + " " + self.last)

erste_person = Person("Homer", "Simpson")
2te_person = Person("Marge", "Simpson")

erste_person.vorstellen()
2te_person.self.vorstellen
```


```python

```

## Integrierte Entwicklungsumgebungen

Integrierte Entwicklungsumgebungen (=IDE = integrated development environment)
unterstützen die Softwareentwicklung. Für MATLAB gibt es nur eine integrierte
Entwicklungsumgebung, nämlich MATLAB selbst. Für Python gibt es zahlreiche IDEs.
Dabei ist der Funktionsumfang meist vergleichbar, so dass man nach persönlichen
Vorlieben entscheiden kann.

* Jupyter Notebooks oder Jupyter Labs sind nicht im eigentlichen Sinne IDEs, die
  Grenze zu ziehen ist aber schwierig.
* Für Python ist pyCharm von der Firma JetBrains sehr beliebt, siehe
  https://www.jetbrains.com/pycharm/ . Diese IDE gibt es als kostenlose Version
  mit eingeschränkter Funktionalität oder als kostenpflichtige
  Professional-Variante. Studierende können sich bei JetBrains mit ihrer
  studentischen E-Mail-Adresse registrieren und können sich dann kostenlos die
  Pro-Version herunterladen. U.a. bietet die Pro-Version auch die Unterstützung
  von Jupyter Notebooks. 
* Microsoft entwickelt seit 2015 den sogenannten Visual Code Editor, eine IDE
  für alle möglichen Programmiersprachen, siehe https://code.visualstudio.com.
* Spyder ist eine IDE, die für die wissenschaftliche Programmierung sehr gerne
  genutzt wird.



## Testen und Kommentare

Jedes Programm sollte umfangreich getestet werden, bevor es zum Einsatz kommt.
Dabei fällt es den Software-Entwicklerteams oft schwer, die eigene Sofwtare zu
testen, denn man hat die eigenen Vorstellungen im Kopf, die ja auch so im
Programm umgesetzt wurden. In Software-Firmen gibt es daher oft eigene Teams,
die das Testen von Software übernehmen.

Leider gibt es auch tragische Softwarefehler. Auf der Wikipedia-Seite [Liste von
Programmfehlerbeispielen](https://de.wikipedia.org/wiki/Liste_von_Programmfehlerbeispielen)
finden Sie einige der bekanntesten Softwarefehlern. Zum Beispiel ist dies der 1.
Eintrag: "Beim Kampfflugzeug F-16 brachte der Autopilot das Flugzeug in
Rückenlage, wenn der Äquator überflogen wurde. Dies kam daher, dass man keine
„negativen“ Breitengrade als Eingabedaten bedacht hatte. Dieser Fehler wurde
sehr spät während der Entwicklung der F-16 mithilfe eines Simulators entdeckt
und beseitigt."

Die folgenden Regeln sind daher bei der Programmierung hilfreich:

1. Überlegen Sie sich Testfälle für Ihr Programm, bevor Sie es schreiben.
2. Fügen Sie nur nach und nach kleine Häppchen zu Ihrem Programm hinzu und
   testen Sie sofort, ob der neue Code-Abschnitt das Gewünschte erledigt.
3. Fügen Sie Kommentare mit # ein, um zu anderen Entwicklern zu erklären, was
   ein bestimmter Code-Abschnitt tut und was mögliche Ergebnisse sein könnten.



## Aufgabe 

Wir hatten bereits die Aufgabe mit dem Einmaleins-Trainer. Jetzt greifen wir die
Aufgabe auf, testen Abschnitte und benutzen Kommentare. Also...

Sie möchten ein Programm schreiben, mit dem ein Benutzer das Einmaleins üben
kann. Zu Anfang darf der Benutzer wählen, wie viele Aufgaben gestellt werden.
Der Computer zieht Zufallszahlen zwischen 1 und 10 und stellt die
Einmaleins-Aufgaben, z.B. die Frage: "Was ist 4x7?". Der Benutezr gibt die
Antwort ein. Wenn die Antwort richtig ist, gibt der Computer "Richtig!" aus.
Ansonsten gibt der Computer den Hinweis: "Leider falsch, die richtige Antwort
wäre xx gewesen." Am Ende gibt der Computer aus, wie viele Aufgaben richtig
gelöst wurden und wieviel Prozent das sind.

Schreiben Sie jetzt eine Funktion, bei der der Benutzer gefragt wird, wie viele
Aufgaben gestellt werden sollen und die die Anzahl der Aufgaben zurückgibt. Was
kann dabei alles schiefgehen? Tipp: suchen Sie im Internet nach der
String-Methode isdigit(). Wie können Sie als Programmiererin sicherstellen, dass
die Eingabe des Benutzers gültig ist? Testen Sie Ihre Funktion.

```python
# Funktion

```

```python
# Test

```

Schreiben Sie als nächstes eine Funktion, die eine Einmaleins-Aufgabe stellt
(kein Rückgabewert). Testen Sie die Funktion.

```python
# Funktion stelle_einmaleins_aufgaben()

```

```python
# Test

```

Erweitern Sie nun die Funktion, die Einmaleins-Aufgaben stellt um ein Argument,
wie viele Aufgaben gestellt werden sollen. Testen Sie die Funktion. 

```python
# erweiterte Funktion stelle_einmaleins_aufgaben(anzahl)


```

```python
# Test

```

Erweitern Sie nun die Funktion, die Einmaleins-Aufgaben stellt um eine Prüfung
des richtigen Ergebnisses. Testen Sie die Funktion, indem Sie einmal ein
falsches Ergebnis und einmal ein richtiges Ergebnis eingeben.

```python
# erweiterte Funktion stelle_einmaleins_aufgaben(anzahl) und Prüfung


```

```python
# Test

```

Erweitern sie nun erneut die Funktion, die Einmaleins-Aufgaben stellt. Nun soll
die Funktion noch einen Rückgabewert liefern, nämlich die Anzahl der richtig
gelösten Aufgaben. Bauen Sie print-Anweisungen ein, um zu testen, ob die Anzahl
der richtig gelösten Aufgaben korrekt mitgezählt wird. Im fertigen Programm
werden diese print-Anweisungen wieder entfernt. Testen Sie die Funktion, auch
den Rückgabewert.

```python
# erweiterte Funktion anzahl_richtige_aufgaben = stelle_einmaleins_aufgaben(anzahl) 


```

```python
# Test 


```

Zuletzt schreiben Sie ein Programm, das aus den beiden Funktionen einen
Einmaleins-Trainer zusammensetzt, und zusätzlich in Prozent ausgibt, wie viele
Aufgaben richtig gelöst wurden.


## Aufgabe 

Was könnte folgender Code für einen Zweck haben?

```python
siege_computer = 0
if wahl_computer == 'Stein':
    if wahl_benutzer == 'Stein':
        print('Unentschieden, ich hatte ebenfalls Stein.')
    elif wahl_benutzer == 'Schere':
        print('Punkt für mich, Stein schleift Schere.')
        siege_computer += 1
    else # wahl_benutzer == 'Papier'
        print('Punkt für Sie, Papier umwickelt Stein.')
        siege_benutzer +=1
```

Korrigieren sie die 4 Fehler. 


```python

```
