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

# 8.3 Objektorientierung


In den letzten Wochen haben wir uns die Grundlagen der Programmierung
erarbeitet:
* Ein- und Ausgabe (input, print)
* Kontrollstrukturen (if - elif - else)
* Schleifen (for, while)
* Funktionen.

In einigen Programmiersprachen wie beispielsweise C hätten wir damit auch alle
Sprachelement kennengelernt. Diese Programmierung nennt man **prozedurale
Programmierung**. Python gehört jedoch zu den objektorientierten
Programmiersprachen, so dass wir uns diese Woche dem Thema Objektorientierung
widmen.

* Kapitel 8.1: Was ist Objektorientierung?
* Kapitel 8.2: Klassen definieren - Attribute
* Kapitel 8.3: Klassen definieren - Methoden



## Aufgabe 8.1 Lesen

Lesen Sie bitte als erstes die folgenden Kapitel im Buch "Python" von Kalista:

* Kapitel 5.1 Was ist Objektorientierung?
* Kapitel 5.2 Eine einfache Klasse definieren



## 8.1 Was ist Objektorientierung?

Bei der bisherigen prozeduralen Programmierweise haben wir Funktionen und Daten
getrennt. Die Daten werden in Variablen gespeichert. Funktionen funktionieren
nach dem EVA-Prinzip. In der Regel erwartet eine Funktion eine Eingabe von
Daten, verarbeitet diese Daten und gibt Daten zurück. 

Angenommen, wir wollten ein Programm zur Verwaltung von Lottoscheinen schreiben.
Zu einem Lottoschein wollen wir Name, Adresse und die angekreuzten Zahlen
speichern. Dann müssten wir mit unserem bisherigen Wissen folgende Variablen pro
Lottoschein einführen:

* vorname
* nachname
* strasse
* postleitzahl
* stadt
* liste_mit_sechs_zahlen

Wenn jetzt viele Spielerinnen und Spieler Lotto spielen wollen, wie gehen wir
jetzt mit den Daten um? Legen wir eine Liste für die Vornamen und eine Liste für
die Nachnamen usw. an? Und wenn jetzt der 17. Eintrag in der Liste mit den sechs
angekreuzten Lottozahlen sechs Richtige hat, suchen wir dann den 17. Eintrag in
der Liste mit den Vornamen und den 17. Eintrag in der Liste mit den Nachnamen
usw.? Umständlich...

Die Idee der objektorientierten Programmierung ist, für solche Szenarien
**Objekte** einzuführen. Ein Objekt fasst verschiedene Eigenschaften wie hier
Vorname, Nachname, Straße, usw. zu einem Objekt Lottoschein zusammen. In der
Informatik wird eine Eigenschaft eines Objekts **Attribut** genannt. 

Damit hätten wir erst einmal nur einen neuen Datentyp. Ein Objekt macht noch
mehr aus, denn zu dem neuen Datentyp kommen noch Funktionen dazu, die die
Verwaltung des Objektes erleichtern. Funktionen, die zu einem Objekt gehören,
nennt man **Methoden**.


## Aufgabe 8.2 Video

Schauen Sie sich Video "Python Tutorial deutsch [21/24] - Objektorientierung
(Konzept)" an (ca. 6:35 min), siehe
https://www.youtube.com/watch?v=46yolPy-2VQ&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=21
.


Im Folgenden sehen Sie, wie ein Objekt in Python definiert wird. Die
Implementierung erfolgt als sogenannte **Klasse**. 

```python
class Beispiel:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
        
    def schreibe_vorname_nachname(self):
        print(self.vorname + ' ' + self.nachname)
        
    def schreibe_nachname_vorname(self):
        print(self.nachname + ', ' + self.vorname)
   
```

Jetzt erzeugen wir ein Objekt vom Typ `Beispiel` und speichern es in der
Variable `person`. Mit der Funnktion `type()` checken wir kurz, welcher Datentyp
in der Variablen `person`steckt:

```python
person = Beispiel('Alice', 'Wunderland')
type(person)
```

Nun können wir auch die beiden Methoden ausprobieren, die zu dem Objekt gehören.
Der Aufruf einer Methode funktioniert anders als eine Funktion. Man hängt an die
Variable, in der das Objekt gespeichert wurde, einen Punkt und dann die Methode
mit runden Klammern. Den Punkt nennt man in der Informatik **Punktoperator**. 

Hier ein Beispiel zu der Methode `schreibe_vorname_nachname()`: 

```python
person.schreibe_vorname_nachname()
```

Dann die zweite Methode, also `schreibe_nachname_vorname()`:

```python
person.schreibe_nachname_vorname()
```

Hinweis: Strings haben bereits vordefinierte Methoden, die sehr nützlich bei der
Manipulation von Strings sind.

Beispiele:
* `.upper()` wandelt alle Zeichen in Großbuchstaben um
* `.lower()` wandelt alle Zeichen in Kleinbuchstaben um
* `.isdigit()` prüft, ob der String in eine Zahl umgewandelt werden könnte


```python
x = 'Dies ist ein Beispielstring!'
print( x.upper() )
```

Führen Sie nachfolgende Code-Zelle aus und geben Sie ein mal `3` und einmal
`drei` ein:

```python
x = input('Zahl: ')
if x.isdigit() == True:
    print('{} kann in eine Zahl umgewandelt werden.'.format(x))
else:
    print('{} kann *nicht* in eine Zahl umgewandelt werden.'.format(x))   
```

Wenn Sie wissen wollen, welche eingebauten Methoden es für Strings oder andere
Datentypen noch gibt, können Sie die Funktion `dir()`. benutzen. Schauen Sie
sich die Methoden an und probieren Sie einige aus:

```python
dir(str)
```

```python

```

## 8.2 Klassen definieren - Attribute

<!-- #region -->
Jetzt definieren wir eine eigene Klasse, die eine Adresse verwalten soll. Ein
erstes Beispiel haben Sie ja oben schon gesehen.

Eingeleitet wird eine Klasse mit dem Schlüsselwort `class` und dann dem Namen
der Klasse. Da Klassen Objekte sind, ist es Standard, den ersten Buchstaben des
Klassennamens groß zu schreiben. 

```python
class Klassenname:
```

Bemerkung: Um Variablen von Objekten leichter zu unterscheiden, werden
Variablennamen klein geschrieben.

Danach folgt ein Abschnitt namens `def __init__(self):`, in dem die
Eigenschaften der Klasse aufgelistet werden. `init` steht dabei für
initialisieren, also den ersten Zustand, den das Objekt später haben wird. 

```python
class Klassenname:
    def __init__(self, eigenschaft1, eigenschaft2):
        self.attribut1 = eigenschaft1
        self.attribut2 = eigenschaft2
```

Probieren wir es mit der Adresse aus:
<!-- #endregion -->

```python
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
    
```

Wie Sie sehen, können die Eingabe-Parameter der `init()`-Methode die gleichen
Namen tragen wie die Attribute der Klasse, also `self.strasse = strasse`, müssen
sie aber nicht. Das Beispiel `self.postleitzahl = plz` zeigt, dass das Attribut
`self.postleitzahl` einfach den Wert des 4. Parameters bekommt, egal wie der
heißt.

Definieren wir jetzt unsere erste Adresse, der Eingabe-Parameter `self` wird
dabei weggelassen (warum kommt später).

```python
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')
```

Geben wir als nächstes aus, was in der Variable `adresse_fra_uas` gespeichert
ist. Probieren wir es mit der `print()`-Funktion:

```python
print(adresse_fra_uas)
```

Wie Sie sehen, wird der Name der Klasse und der Speicherort im RAM angegeben,
aber nicht der Inhalt. Die Funktion `print()` ist nicht für den Datentyp
`Adresse` entwickelt worden. Schließlich können die Python-Entwickler nicht
wissen, welche Klassen Sie entwickeln... 

Aber wir kommen wir jetzt an den Inhalt des Objektes `adresse_fra_uas`? Mit dem
Punktoperator.

```python
print(adresse_fra_uas.strasse)
```

```python
print(adresse_fra_uas.postleitzahl)
```

Damit können wir auch ganz normal rechnen, wenn das Attribut eine Zahl ist:

```python
adresse_fra_uas.postleitzahl + 11111
```

Mit dem Punktoperator können wir Attribute eines Objektes auch verändern.
Schauen wir uns zunächst an, welchen Inhalt `adress_fra_uas.postleitzahl` hat,
dann setzen wir eine neue Postleitzahl und schauen erneut, welchen Inhalt
`adress_fra_uas.postleitzahl` jetzt hat:

```python
print('davor: ')
print(adresse_fra_uas.postleitzahl)

adresse_fra_uas.postleitzahl = 77777

print('danach: ')
print(adresse_fra_uas.postleitzahl)
```

#### Aufgabe 8.3 Video

Schauen Sie sich das YouTube-Video "Python Tutorial deutsch [22/24] - Klassen
und Objekte" (ca. 14:34 min), siehe
https://www.youtube.com/watch?v=XxCZrT7Z3G4&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=22
an.

Stoppen Sie das Video regelmäßig und probieren Sie die dort gezeigten Beispiele
hier aus:

```python

```

## Aufgabe 8.4

Schreiben Sie eine Klasse, die Studierende mit den Eigenschaften
* Vorname
* Nachname
* Matrikel-Nummer verwalten kann.

Testen Sie anschließend Ihre Klasse, indem Sie ein Beispiel ausprobieren.

```python

```

## Aufgabe 8.5 Video

Bleibt noch die Frage offen, warum der `self`-Parameter beim Initialisieren
eines Objektes nicht angegeben wird. Schauen Sie sich dazu das YouTube-Video
"Python Tutorial deutsch [23/24] - Der self Parameter" (ca. 10:53 min), siehe
https://www.youtube.com/watch?v=CLoK-_qNTnU&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=23
an.


## 8.3 Klassen definieren - Methoden

Es ist bedauerlich, dass wir nicht eine `print()`-Funktion für unsere
Adressen-Klasse zur Verfügung haben. Definieren wir uns einfach eine ...

Da diese Funktion nicht allgemeingültig sein kann, sondern nur für die Objekte
`Adresse` funktionieren kann, gehört sie auch folgerichtig zur Klasse selbst.
Sie ist also keine Funktion, sondern eine Methode. 

Eine Methode wird definiert, indem innerhalb des Anweisungsblocks der Klasse
eine Funktion mit dem Schlüsselwort `def` definiert wird. Der erste Eingabewert
muss zwingend der `self`-Parameter sein. Hier ein Beispiel für eine
Print-Methode: 

```python
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
    
    def print(self):
        print('Straße: ', self.strasse)
        print('Hausnummer: ', self.hausnummer)
        print('Postleitzahl: ', self.postleitzahl)
        print('Stadt: ', self.stadt)
```

```python
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')
adresse_fra_uas.print()
```

Vielleicht möchten wir die Print-Ausgabe unterschiedlich haben, z.B. alles in
einer Zeile. Wir erweitern unsere Klasse mit einer neuen Methode namens
`print_einzeilig()`:

```python
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
    
    def print(self):
        print('Straße: ', self.strasse)
        print('Hausnummer: ', self.hausnummer)
        print('Postleitzahl: ', self.postleitzahl)
        print('Stadt: ', self.stadt)
        
    def print_einzeilig(self):
        print('{} {}, {} {}'.format(self.strasse, self.hausnummer, self.postleitzahl, self.stadt ))
```

```python
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')

print('zuerst so:')
adresse_fra_uas.print()

print('\n und \ndann einzeilig:')
adresse_fra_uas.print_einzeilig()
```

## Aufgabe 8.6 

Fügen Sie Ihrer Klasse zum Verwalten von Studierenden (siehe Aufgabe 8.4) zwei
Print-Funktionen hinzu. Die erste Print-Funktion soll in einer Zeile `Vorname
Nachname (xxxxxx)` ausgeben, wobei das xxxxxx für die Matrikel-Nummer steht,
also z.B.

```
Alice Wunderland (123456)
```

ausgeben. Die zweite soll `Nachname, Vorname (Matrikel-Nummer: xxxxxx)`
ausgeben, also z.B.

```
Wunderland, Alice (Matrikel-Nummer: 123456)
```


```python

```

Bisher hatten wir nur Methoden ohne weitere Eingabe-Parameter (natürlich mit dem
self-Parameter, der gehört zu allen Methoden dazu). Methoden können aber auch
weitere Parameter haben. Beispielsweise könnte man eine Print-Funktion
schreiben, bei der durch einen Parameter gesteuert wird, ob die Adresse in vier
oder in einer Zeile angezeigt wird:

```python
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
    
    def print(self, einzeilig):
        if einzeilig == True:
            print('{} {}, {} {}'.format(self.strasse, self.hausnummer, self.postleitzahl, self.stadt ))
        else:    
            print('Straße: ', self.strasse)
            print('Hausnummer: ', self.hausnummer)
            print('Postleitzahl: ', self.postleitzahl)
            print('Stadt: ', self.stadt)
    
```

Probieren wir es aus:

```python
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')

print('zuerst einzeilig:')
adresse_fra_uas.print(True)

print('\nund dann vierzeilig:')
adresse_fra_uas.print(False)
```

Zuletzt betrachten wir noch Methoden mit Rückgabewert. Wie bei Funktionen auch
genügt es mit dem Schlüsselwort `return` den Rückgabewert zu definieren. Sehr
häufig ist dabei der Fall, dass eine Eigenschaft des Objektes zurückgegeben
wird. Dann wird in der Regel der Methodenname

```
get_attribut()
```

gewählt.

Aber prinzipiell kann der Rückgabewert auch eine Berechnung oder ähnliches
enthalten.

```python
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
    
    def print(self, einzeilig):
        if einzeilig == True:
            print('{} {}, {} {}'.format(self.strasse, self.hausnummer, self.postleitzahl, self.stadt ))
        else:    
            print('Straße: ', self.strasse)
            print('Hausnummer: ', self.hausnummer)
            print('Postleitzahl: ', self.postleitzahl)
            print('Stadt: ', self.stadt)
 
    def get_stadt(self, grossschreibung):
        if grossschreibung == True:
            return self.stadt.upper()
        else:
            return self.stadt
```

Und auch diese Methode probieren wir aus. Je nachdem, ob die Methode mit `True`
oder `False` aufgerufen wird, gibt die Methode den String `self.stadt` zurück,
entweder normal geschrieben oder in Großbuchstaben.

```python
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')

print('zuerst normal:')
s = adresse_fra_uas.get_stadt(False)
print(s)

print('\nund dann groß geschrieben:')
s = adresse_fra_uas.get_stadt(True)
print(s)

```

## Aufgabe 8.7 Video 

Bitte schauen Sie sich das Video "Python Tutorial deutsch [24/24] - Methoden in
Klassen" an, ca. 18:18 min, die Werbung ab Minute 14:00 können Sie überspringen,
siehe
https://www.youtube.com/watch?v=58IjjwHs_4A&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=24
.

Stoppen Sie das Video regelmäßig und probieren Sie die im Video gezeigten
Beispiele hier aus:

```python

```

## Aufgabe 8.8

Erweitern Sie die Klasse zum Verwalten von Studierenden (Vorname, Name,
Matrikel-Nummer) um ein Attribut vorleistung_bestanden. Anfangs sollte dieses
Attribut auf `False` gesetzt werden. Implementieren Sie eine Methode, die es
ermöglicht, dieses Attribut auf `True` zu setzen.

Testen Sie anschließend Ihre erweiterte Klasse.

```python

```

## Aufgabe 8.9

Implementieren Sie eine Klasse Datum. Diese Klasse speichert Tag, Monat und Jahr
als Attribut. 
* Implementieren Sie Methoden, die diese Attribute verändern können. Dabei soll
  die Methode per Print()-Funktion warnen, wenn eine nicht zulässige Zahl
  verwendet wird und dann nicht die Änderung durchführen. 
* Implementieren Sie eine Methode `get_datum_deutsch()`, die das Datum als
  String nach dem Muster `TT.MM.JJJJ` zurückgibt, also z.B. '07.06.2021'.
* Implementieren Sie eine Methode `get_datum_britisch()`, die das Datum als
  String nach dem Muster `TT/MM/JJJJ` zurückgibt, also z.B. '07/06/2021'.
* Implementieren Sie eine Methode `get_datum_amerikanisch()`, die das Datum als
  String nach dem Muster `MM/TT/JJJJ` zurückgibt, also z.B. '06/07/2021'.

```python

```


