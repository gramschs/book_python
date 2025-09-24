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

# 8.1 Was sind Klassen und Objekte?

100 Studierende mit jeweils fünf Eigenschaften verwalten? Das wären 500 einzelne
Variablen, ein Albtraum! Die objektorientierte Programmierung löst dieses
Problem: Anstatt Daten und Funktionen getrennt zu behandeln, bündeln wir sie in
Objekten. In diesem Kapitel lernen wir, wie das funktioniert.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie verstehen das Konzept der objektorientierten Programmierung (OOP).
* Sie können zwischen einer **Klasse** und einem **Objekt** unterscheiden.
* Sie können eine einfache Klasse selbst implementieren.
* Sie wissen, was ein **Attribut** ist und können darauf lesend und schreibend
  zugreifen.
```

## Konzept

Bei der bisherigen prozeduralen Programmierung haben wir Funktionen und Daten
getrennt. Daten speichern wir in Variablen. Funktionen arbeiten dabei nach dem
EVA-Prinzip: Eingabe – Verarbeitung – Ausgabe. In der Regel erwartet eine
Funktion eine Eingabe von Daten, verarbeitet diese Daten und gibt Daten zurück.
In vielen Fällen ist die prozedurale Programmierung völlig ausreichend. Diese
Herangehensweise stößt an ihre Grenzen, wenn es darum geht, die reale Welt durch
komplexere Modelle nachzubilden.

Angenommen, wir wollten ein Programm zur Verwaltung von Studierenden schreiben,
die an einer Python-Vorlesung teilnehmen. Bereits vor Beginn der Vorlesung
müssen sich die Studierenden anmelden, um an der Vorlesung teilnehmen zu können.
In dem Formular werden

* Nachname
* Vorname
* Studiengang
* Semester
* Matrikelnummer

abgefragt. Angenommen, es melden sich 20 Studierende für die Python-Vorlesung
an. Welchen Datentyp benutzen wir nun zur Erfassung der Anmeldedaten?

Eine naheliegende Lösung wäre, für jeden Studierenden separate Variablen
anzulegen:

```python
# Studierende 1
nachname_1 = "Abendrot"
vorname_1 = "Anna"
studiengang_1 = "Maschinenbau"
semester_1 = 3
matrikelnummer_1 = "12345678"

# Studierende 2
nachname_2 = "Berliner"
vorname_2 = "Bob"
studiengang_2 = "Maschinenbau"
semester_2 = 5
matrikelnummer_2 = "87654321"

# ... und so weiter für alle 20 Studierenden.
```

Für 20 Studierende benötigen wir 100 Variablen! Das ist nicht nur
unübersichtlich, sondern auch unpraktisch. Was passiert, wenn wir später weitere
Informationen speichern möchten, wie beispielsweise die Klausurnote? Dann
müssten wir 20 weitere Variablen hinzufügen.

Eine andere Möglichkeit wäre die Verwendung von Listen:

```python
nachnamen = ["Abendrot", "Berliner", "Colorado", ...]
vornamen = ["Anna", "Bob", "Charlie", ...]
studiengänge = ["Maschinenbau", "Maschinenbau", "Elektrotechnik", ...]
semester = [3, 5, 2, ...]
matrikelnummern = ["12345678", "87654321", "11223344", ...]
```

Auch hier entstehen Probleme: Der Zusammenhang zwischen den Daten kann leicht
verloren gehen. Wenn wir beispielsweise einen Studierenden aus der Liste
entfernen möchten, müssen wir daran denken, den entsprechenden Eintrag in
allen fünf Listen zu löschen. Vergessen wir eine Liste, stimmen die Daten
nicht mehr überein.

Eine weitere Möglichkeit wäre, für jeden Studierenden ein Dictionary zu
verwenden. Damit könnten wir die Daten folgendermaßen zusammenfassen:

```python
student1 = {
    "nachname": "Abendrot",
    "vorname": "Anna",
    "studiengang": "Maschinenbau",
    "semester": 3,
    "matrikelnummer": "12345678"
}
```

Dictionaries sind zwar praktischer als viele einzelne Variablen oder parallele
Listen, haben aber auch Grenzen: Wir können zwar Daten bündeln, aber es gibt
keine feste Struktur. Tippfehler bei Schlüsseln oder fehlende Einträge fallen
erst zur Laufzeit auf. Außerdem können wir Funktionen zwar separat schreiben,
sie sind aber nicht automatisch mit den Daten verbunden.

Genau hier setzt die objektorientierte Programmierung an. Die Grundidee besteht
darin, Daten und die dazugehörigen Funktionen in einer gemeinsamen Struktur zu
bündeln.

```{dropdown} Video zu "Konzept der Objektorientierung" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/46yolPy-2VQ" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

## Die Lösung: Eine Klasse für Studierende

Die objektorientierte Programmierung löst dieses Problem elegant. Wir erstellen
eine sogenannte Klasse, die wie ein Formular oder ein Bauplan funktioniert:

```{code-cell} ipython
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
```

Mit dieser Klasse können wir nun ganz einfach einzelne Studierende erstellen:

```{code-cell} ipython3
# Einzelne Studierende erstellen (= Objekte)
student1 = Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678")
student2 = Student("Berliner", "Bob", "Maschinenbau", 5, "87654321")
student3 = Student("Colorado", "Charlie", "Elektrotechnik", 2, "11223344")
```

Die **Klasse** ist also vergleichbar mit einem Formular, das die Studierenden
zur Anmeldung ausfüllen müssen. Das Formular legt fest, welche Daten erhoben
werden. Zur Anmeldung wird die Klausurnote beispielsweise nicht abgefragt, auch
wenn sich Studierende das vielleicht wünschen würden. Ein **Objekt** dieser
Klasse ist dann jeder einzelne Studierende wie beispielsweise `student1` oder
`student2` mit den konkreten Daten. Die Eigenschaften, die in diesen Objekten
gemäß dem Bauplan gespeichert sind, werden **Attribute** genannt.

In diesem Kapitel konzentrieren wir uns zunächst auf Klassen, Objekte und
Attribute. Auf Methoden gehen wir im nächsten Kapitel genauer ein, geben aber in
der folgenden Zusammenfassung der Grundbegriffe der objektorientierten
Programmierung (OOP) schon einmal einen Ausblick auf den Fachbegriff Methode.

```{admonition} Grundbegriffe der objektorientierten Programmierung
:class: note
* Eine **Klasse** ist dabei wie ein Bauplan oder ein Formular: Sie legt fest,
  welche Daten und welche Funktionen zu einem bestimmten Typ von Dingen gehören.
* Ein **Objekt** ist eine konkrete Ausprägung einer Klasse, sozusagen ein
  Exemplar nach dem Bauplan. Ein Objekt »Studierender« enthält also die echten
  Angaben einer Person wie Nachname, Vorname und Matrikelnummer.
* Die einzelnen Daten, die ein Objekt speichert, nennt man **Attribute**.
* Neben Attributen können Klassen auch **Methoden** enthalten. Das sind
  Funktionen, die speziell für die Arbeit mit den Objekten gedacht sind.
```

## Zugriff auf die Daten eines Objekts

Nachdem wir ein Objekt erstellt haben, können wir auf seine Attribute (=
gespeicherte Daten) zugreifen:

```{code-cell} ipython3
# Objekt erstellen
student1 = Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678")

# Lesender Zugriff auf Attribute
print(student1.nachname)       # Ausgabe: Abendrot
print(student1.vorname)        # Ausgabe: Anna
print(student1.semester)       # Ausgabe: 3

# Schreibender Zugriff - Werte ändern
student1.semester = 4          # Anna ist jetzt im 4. Semester
student1.vorname = "Anna-Lena" # Vorname ändern

# Überprüfung der Änderung
print(student1.semester)       # Ausgabe: 4
print(student1.vorname)        # Ausgabe: Anna-Lena
```

Um auf ein Attribut zuzugreifen, verwenden wir die **Punkt-Notation** bzw. den
**Punkt-Operator**:

```python
objektname.attributname
```

Jedes Objekt hat seine eigenen Attribute:

```{code-cell} ipython
print(student1.nachname)  # "Abendrot"
print(student2.nachname)  # "Berliner"
# student1 und student2 sind völlig unabhängig voneinander
```

Schauen wir uns nun die Vorteile an, die Objekte in der Programmierung mit sich
bringen.

## Vorteile der objektorientierten Lösung

**1. Zusammengehörige Daten sind gebündelt:**
Alle Informationen zu einem Studierenden sind in einem Objekt gespeichert. Es
kann nichts "durcheinander geraten":

```{code-cell} ipython3
print(student1.nachname)       # "Abendrot"
print(student1.vorname)        # "Anna"
print(student1.studiengang)    # "Maschinenbau"
```

**2. Einfache Erweiterung:**
Neue Eigenschaften können leicht hinzugefügt werden, ohne bestehenden Code
zu ändern:

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
        self.klausurnote = None  # Neue Eigenschaft
```

Da wir nicht wollen, dass die Klausurnote durch die Studierenden bei der
Anmeldung gesetzt wird, haben wir diese Eigenschaft im `__init__()`-Abschnitt
bewusst weggelassen. Da die Klausurnote erst später vergeben wird, setzen wir
sie initial auf `None` (= kein Wert). Es bleibt also bei der alten Methode, ein
konkretes Objekt zu erzeugen, wie der folgende Code-Abschnitt zeigt.

```{code-cell} ipython3
student1 = Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678")

print(student1.klausurnote)
```

**3. Übersichtliche Verwaltung vieler Objekte:**
Anstatt 100 einzelner Variablen verwenden wir einfach eine Liste von Objekten:

```{code-cell} ipython3
# Liste mit Studierenden anlegen
studierende = [
    Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678"),
    Student("Berliner", "Bob", "Maschinenbau", 5, "87654321"),
    Student("Colorado", "Charlie", "Elektrotechnik", 2, "11223344")
]

# alle Namen ausgeben
for student in studierende:
    print(f"{student.vorname} {student.nachname}")
```

**4. Wiederverwendbarkeit:**
Die Klasse kann in verschiedenen Programmen wiederverwendet werden.

```{dropdown} Video zu "Klassen und Objekte" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/XxCZrT7Z3G4" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir das Grundkonzept der objektorientierten
Programmierung kennengelernt. Wir haben gesehen, dass eine Klasse wie ein
Bauplan oder ein Formular funktioniert und daraus Objekte mit konkreten Daten
entstehen. Die gespeicherten Informationen heißen Attribute. Im nächsten Kapitel
lernen wir die Methoden kennen, also Funktionen, die direkt zu einer Klasse
gehören.
