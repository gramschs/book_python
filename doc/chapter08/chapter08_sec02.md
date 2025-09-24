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

# 8.2 Methoden und der self-Parameter

Bisher haben wir gelernt, wie wir Daten in Objekten speichern können. Aber
Objekte können mehr als nur Daten speichern, sonst könnten wir auch Dictionaries
nehmen. Ihren großen Vorteil erlangen Objekte durch Methoden.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie verstehen, was Methoden sind und wie sie sich von normalen Funktionen
  unterscheiden.
* Sie können einfache Methoden in einer Klasse implementieren und aufrufen.
* Sie verstehen den `self`-Parameter und wissen, warum er benötigt wird.
* Sie können über `self` auf Objektattribute zugreifen und diese verändern.
* Sie können Methoden schreiben, die mit den Daten des jeweiligen Objekts
  arbeiten.
```

## Methoden sind Funktionen, die zu einer Klasse gehören

Eine **Methode** ist im Grunde eine Funktion, die direkt zu einer Klasse gehört.
Statt die Funktion separat zu schreiben, definieren wir sie innerhalb der
Klasse. Dadurch kann die Funktion direkt mit den Daten des Objekts arbeiten.

Schauen wir uns ein Beispiel an. Angenommen, wir möchten für einen Studierenden
den vollständigen Namen ausgeben. Bisher würden wir das so machen:

```python
# Ohne Methoden, d.h. mit normaler Funktion
def vollstaendiger_name(student):
    return f"{student.vorname} {student.nachname}"

student1 = Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678")
print(vollstaendiger_name(student1))  # Anna Abendrot
```

Mit einer Methode können wir das eleganter lösen:

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
    
    # Das ist eine Methode!
    def vollstaendiger_name(self):
        return f"{self.vorname} {self.nachname}"

# Objekt erstellen
student1 = Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678")

# Methode aufrufen
print(student1.vollstaendiger_name())  # Anna Abendrot
```

Der wichtigste Unterschied zwischen Funktionen und Methoden ist, wo und wie wir
sie aufrufen:

Normale Funktion:

```python
# Funktion wird separat definiert
def vollstaendiger_name(student):
    return f"{student.vorname} {student.nachname}"

# Aufruf: funktion(objekt)
ergebnis = vollstaendiger_name(student1)
```

Methode:

```python
# Methode wird in der Klasse definiert
class Student:
    def vollstaendiger_name(self):
        return f"{self.vorname} {self.nachname}"

# Aufruf: objekt.methode()
ergebnis = student1.vollstaendiger_name()
```

Nicht nur der Ort (in oder außerhalb der Klasse) unterscheidet sich, sondern
auch die Syntax beim Aufruf:

* Normale Funktion: `funktion(objekt)`
* Methode: `objekt.methode()`

Erweitern wir unsere Klasse Student um eine weitere nützliche Methode:

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
    
    def vollstaendiger_name(self):
        return f"{self.vorname} {self.nachname}"
    
    def begruessung(self):
        return f"Hallo, ich bin {self.vorname} und studiere {self.studiengang}."

# Ausprobieren
student1 = Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678")
student2 = Student("Berliner", "Bob", "Maschinenbau", 1, "87654321")

print(student1.vollstaendiger_name())  # Anna Abendrot
print(student1.begruessung())          # Hallo, ich bin Anna und studiere Maschinenbau.
print()
print(student2.vollstaendiger_name())  # Bob Berliner
print(student2.begruessung())          # Hallo, ich bin Bob und studiere Maschinenbau.
```

Anhand des obigen Beispiels stellen wir fest:

1. Der `self`-Parameter: Jede Methode hat als ersten Parameter `self`. Dieser
Parameter bezieht sich auf das konkrete Objekt, für das die Methode aufgerufen
wird. Mehr dazu lernen wir im nächsten Abschnitt.
2. Zugriff auf Attribute: Innerhalb einer Methode greifen wir mit
`self.attributname` auf die Attribute des Objekts zu.
3. Jedes Objekt ruft seine eigene Methode auf: Obwohl beide Objekte die gleiche
   Methode `begruessung()` verwenden, geben sie unterschiedliche Ergebnisse
   zurück, je nach ihren eigenen Daten.

```{admonition} Mini-Übung
:class: miniexercise
Versuchen Sie selbst, eine Methode zu schreiben! Erweitern Sie die
Klasse Student um eine Methode `studieninfo()`, die eine Zeile wie "Anna
Abendrot studiert Maschinenbau im 3. Semester" zurückgibt.
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
    
    def vollstaendiger_name(self):
        return f"{self.vorname} {self.nachname}"
    
    def studieninfo(self):
        return f"{self.vollstaendiger_name()} studiert {self.studiengang} im {self.semester}. Semester"

# Test der neuen Methode
student1 = Student("Müller", "Max", "Maschinenbau", 3, "12345678")
print(student1.studieninfo())  # Max Müller studiert Maschinenbau im 3. Semester
```
In dieser Musterlösung rufen wir in der `studieninfo()`-Methode die andere
Methode `vollstaendiger_name()` auf. Das geht mit `self.vollstaendiger_name()`.
Auch Methoden können andere Methoden der gleichen Klasse verwenden!
````

Im nächsten Abschnitt schauen wir uns genauer an, was es mit diesem mysteriösen
`self`-Parameter auf sich hat.

```{dropdown} Video zu "Methoden in Klassen" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/58IjjwHs_4A" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

## Der self-Parameter

Im vorigen Abschnitt haben wir gesehen, dass jede Methode einen `self`-Parameter
hat. In diesem Abschnitt klären wir, was self ist, warum wir es brauchen und wie
es funktioniert.

`self` ist ein Verweis auf das konkrete Objekt, für das eine Methode aufgerufen
wird. Angenommen, wir haben mehrere Studierende und jeder soll sich vorstellen.
Woher weiß die Methode `begruessung()`, ob sie "Hallo, ich bin Anna" oder
"Hallo, ich bin Bob" sagen soll? Genau hier kommt `self` ins Spiel.

Schauen wir uns ein Beispiel an:

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
    
    def begruessung(self):
        # self bezieht sich auf das Objekt, das diese Methode aufruft
        print(f"Hallo, ich bin {self.vorname} {self.nachname}")
        print(f"Meine Matrikelnummer ist {self.matrikelnummer}")

# Zwei verschiedene Objekte erstellen
student1 = Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678")
student2 = Student("Berliner", "Bob", "Elektrotechnik", 1, "87654321")

# Gleiche Methode, aber verschiedene Objekte
student1.begruessung()
print()
student2.begruessung()
```

Wenn wir `student1.begruessung()` aufrufen, dann ist `self` in der Methode eine
Referenz auf `student1`. Bei `student2.begruessung()` bezieht sich `self` auf
`student2`. Ohne `self` wüsste eine Methode nicht, auf welches Objekt sie sich
bezieht.

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
    
    def zeige_semester(self):
        print(f"{self.vorname} ist im {self.semester}. Semester")

# Verschiedene Studierende in verschiedenen Semestern
studierende = [
    Student("Müller", "Max", "Maschinenbau", 3, "12345678"),
    Student("Schmidt", "Sarah", "Elektrotechnik", 1, "87654321"),
    Student("Weber", "Tim", "Informatik", 5, "11111111")
]

# Für jeden Studierenden die Methode aufrufen
for studi in studierende:
    studi.zeige_semester()  # self wird automatisch gesetzt!
```

Mit self können wir auf alle Attribute des aktuellen Objekts zugreifen. Die
Syntax ist einfach: `self.attributname`.

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
    
    def alle_infos_anzeigen(self):
        print("--- Studierendendaten ---")
        print(f"Name: {self.vorname} {self.nachname}")
        print(f"Studiengang: {self.studiengang}")
        print(f"Semester: {self.semester}")
        print(f"Matrikelnummer: {self.matrikelnummer}")

student = Student("Johnson", "Lisa", "Maschinenbau", 2, "98765432")
student.alle_infos_anzeigen()
```

Hier kommt der "magische Teil": Obwohl jede Methode `self` als ersten Parameter
hat, übergeben wir beim Aufruf keinen Wert dafür. Python macht das automatisch!
Wir schreiben:

```python
student.alle_infos_anzeigen()
```

Python macht daraus intern:

```python
Student.alle_infos_anzeigen(student)
```

Das bedeutet: Wenn wir `objekt.methode()` schreiben, übergibt Python automatisch
das Objekt als ersten Parameter `(self)` an die Methode.

`self` ermöglicht es uns nicht nur, Attribute zu lesen, sondern auch zu
verändern:

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
    
    def semester_erhoehen(self):
        """Erhöht das Semester um 1 (für den Semesterübergang)"""
        self.semester = self.semester + 1
        print(f"{self.vorname} ist jetzt im {self.semester}. Semester")
    
    def aktuelles_semester_anzeigen(self):
        print(f"{self.vorname} ist im {self.semester}. Semester")

# Ausprobieren
student = Student("Müller", "Max", "Maschinenbau", 3, "12345678")
student.aktuelles_semester_anzeigen()  # Max ist im 3. Semester

student.semester_erhoehen()            # Max ist jetzt im 4. Semester
student.aktuelles_semester_anzeigen()  # Max ist im 4. Semester
```

```{admonition} Mini-Übung
:class: miniexercise
Erweitern Sie die Klasse Student um zwei neue Methoden:
1. `note_eintragen(note)` - fügt eine Note zur Notenliste hinzu (verwenden Sie
   eine Liste `self.noten`)
2. `notendurchschnitt()` - berechnet und gibt den Durchschnitt aller Noten
   zurück

Tipp: Initialisieren Sie die Notenliste in `__init__` als leere Liste. Falls
noch keine Noten vorhanden sind, soll die Methode den Durchschnitt 0.0
zurückgeben.
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
        self.noten = []  # Leere Liste für Noten
    
    def note_eintragen(self, note):
        """Fügt eine Note zur Notenliste hinzu"""
        self.noten.append(note)
        print(f"Note {note} für {self.vorname} eingetragen")
    
    def notendurchschnitt(self):
        """Berechnet den Durchschnitt aller Noten"""
        if len(self.noten) == 0:
            return 0.0
        return sum(self.noten) / len(self.noten)

# Test der neuen Methoden
student = Student("Müller", "Max", "Maschinenbau", 3, "12345678")
student.note_eintragen(2.3)  # Note 2.3 für Max eingetragen
student.note_eintragen(1.7)  # Note 1.7 für Max eingetragen
student.note_eintragen(2.0)  # Note 2.0 für Max eingetragen

print(f"Durchschnitt: {student.notendurchschnitt()}")  # Durchschnitt: 2.0
```
````

```{dropdown} Video zu "Der self Parameter" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/CLoK-_qNTnU" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

## Zusammenfassung und Ausblick

Methoden sind Funktionen, die zu einer Klasse gehören und direkt mit Objektdaten
arbeiten können. Der `self`-Parameter ermöglicht jeder Methode den Zugriff auf das
konkrete Objekt, das sie aufruft.
