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

# 8.3 OOP in der Praxis

Mit Klassen, Objekten und Methoden haben wir die Grundlagen der
objektorientierten Programmierung kennengelernt. In diesem Kapitel schauen wir
uns an, wie wir diese Konzepte in der Praxis anwenden: Wir verwalten mehrere
Objekte in Listen und sorgen dafür, dass unsere Objekte sich schön ausgeben
lassen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können Objekte in Listen speichern und verwalten.
* Sie können Listen von Objekten durchlaufen und durchsuchen.
* Sie verstehen die `__str__`-Methode und können sie implementieren.
* Sie können ein vollständiges objektorientiertes Programm zur Datenverwaltung erstellen.
* Sie verstehen, wie OOP bei der Lösung praktischer Probleme hilft.
```

## Listen von Objekten verwalten

In der Praxis arbeiten wir selten mit nur einem Objekt. Angenommen, wir müssten
die Daten aller Studierenden eines Kurses verwalten. Mit einzelnen Variablen
wäre das ein Albtraum, aber mit Listen von Objekten wird es elegant und
übersichtlich. Listen können nicht nur Zahlen oder Strings enthalten, sondern
auch Objekte. Das macht sie zu einem mächtigen Werkzeug für die Datenverwaltung.

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer

# Liste mit mehreren Studierenden erstellen
studierende = [
    Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678"),
    Student("Berliner", "Bob", "Maschinenbau", 5, "87654321"),
    Student("Colorado", "Charlie", "Elektrotechnik", 2, "11223344"),
    Student("Dietrich", "Diana", "Maschinenbau", 1, "99887766")
]

print(f"Anzahl Studierende: {len(studierende)}")
```

Mit for-Schleifen können wir einfach über alle Objekte in der Liste iterieren:

```{code-cell} ipython3
# Alle Studierenden begrüßen
for student in studierende:
    print(f"Hallo {student.vorname} {student.nachname}!")

print()

# Nur die Namen ausgeben
for student in studierende:
    print(f"{student.vorname} {student.nachname} ({student.studiengang})")
```

Oft müssen wir bestimmte Objekte aus einer Liste herausfiltern oder suchen:

```{code-cell} ipython3
# Nach einem bestimmten Nachnamen suchen
gesuchter_name = "Berliner"
for student in studierende:
    if student.nachname == gesuchter_name:
        print(f"Gefunden: {student.vorname} {student.nachname}")
        break

print()

# Alle Maschinenbau-Studierenden finden
maschinenbauer = []
for student in studierende:
    if student.studiengang == "Maschinenbau":
        maschinenbauer.append(student)

print("Maschinenbau-Studierende:")
for student in maschinenbauer:
    print(f"- {student.vorname} {student.nachname}")
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie Code, der alle Studierenden im 3. Semester oder höher findet und
deren Namen ausgibt. Verwenden Sie die bereits erstellte `studierende`-Liste.
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Studierende im 3. Semester oder höher
hoeheres_semester = []
for student in studierende:
    if student.semester >= 3:
        hoeheres_semester.append(student)

print("Studierende im 3. Semester oder höher:")
for student in hoeheres_semester:
    print(f"- {student.vorname} {student.nachname} ({student.semester}. Semester)")
```
````

## Die __str__-Methode für schöne Ausgabe

Wenn wir Objekte mit `print()` ausgeben, erhalten wir oft kryptische Meldungen
statt nützlicher Informationen. Die `__str__`-Methode löst dieses Problem
elegant.

Schauen wir uns an, was passiert, wenn wir ein Objekt direkt ausgeben:

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer

student = Student("Müller", "Max", "Maschinenbau", 3, "12345678")
print(student)  # Kryptische Ausgabe wie <__main__.Student object at 0x...>
```

Das ist nicht sehr hilfreich! Python zeigt nur den Objekttyp und eine
Speicheradresse an.

Die `__str__`-Methode ist eine spezielle Methode, die Python automatisch aufruft, wenn ein Objekt als String dargestellt werden soll:

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
    
    def __str__(self):
        return f"{self.vorname} {self.nachname} ({self.studiengang}, {self.semester}. Semester)"

student = Student("Müller", "Max", "Maschinenbau", 3, "12345678")
print(student)  # Jetzt: Max Müller (Maschinenbau, 3. Semester)
```

Der Unterschied wird besonders bei Listen von Objekten deutlich:

```{code-cell} ipython3
# Ohne __str__-Methode
class StudentOhne:
    def __init__(self, nachname, vorname):
        self.nachname = nachname
        self.vorname = vorname

# Mit __str__-Methode  
class StudentMit:
    def __init__(self, nachname, vorname):
        self.nachname = nachname
        self.vorname = vorname
    
    def __str__(self):
        return f"{self.vorname} {self.nachname}"

student_ohne = StudentOhne("Schmidt", "Sarah")
student_mit = StudentMit("Schmidt", "Sarah")

print("Ohne __str__:")
print(student_ohne)

print("\nMit __str__:")
print(student_mit)

# Bei Listen wird der Unterschied noch deutlicher
liste_ohne = [StudentOhne("Müller", "Max"), StudentOhne("Weber", "Lisa")]
liste_mit = [StudentMit("Müller", "Max"), StudentMit("Weber", "Lisa")]

print(f"\nListe ohne __str__: {liste_ohne}")
print(f"Liste mit __str__: {liste_mit}")
```

Eine gute `__str__`-Methode sollte:

* kurz und informativ sein,
* die wichtigsten Informationen** enthalten und
* für Menschen lesbar sein.

```{admonition} Mini-Übung
:class: miniexercise
Erweitern Sie die Student-Klasse um eine `__str__`-Methode, die den Namen und
das Semester in der Form "Anna Abendrot (3. Semester)" ausgibt. Testen Sie Ihre
Lösung mit mindestens zwei Objekten.
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
    
    def __str__(self):
        return f"{self.vorname} {self.nachname} ({self.semester}. Semester)"

# Test der Lösung
student1 = Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678")
student2 = Student("Berliner", "Bob", "Elektrotechnik", 1, "87654321")

print(student1)  # Anna Abendrot (3. Semester)
print(student2)  # Bob Berliner (1. Semester)
```
````

## Ein vollständiges Beispiel: Kursverwaltung

Jetzt bringen wir alles zusammen: Eine vollständige Student-Klasse mit allen
gelernten Methoden und eine praktische Kursverwaltung, die zeigt, wie mächtig
OOP in der Praxis ist.

```{code-cell} ipython3
class Student:
    def __init__(self, nachname, vorname, studiengang, semester, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.studiengang = studiengang
        self.semester = semester
        self.matrikelnummer = matrikelnummer
        self.noten = []
    
    def __str__(self):
        return f"{self.vorname} {self.nachname} ({self.studiengang}, {self.semester}. Sem)"
    
    def vollstaendiger_name(self):
        return f"{self.vorname} {self.nachname}"
    
    def note_hinzufuegen(self, note):
        self.noten.append(note)
    
    def notendurchschnitt(self):
        if len(self.noten) == 0:
            return 0.0
        return sum(self.noten) / len(self.noten)
    
    def semester_erhoehen(self):
        self.semester += 1
```

Wir erstellen nun den Kurs mit den teilnehmenden Studierenden und lassen alle
anzeigen.

```{code-cell} ipython3
# Kurs erstellen und mit Studierenden füllen
python_kurs = [
    Student("Abendrot", "Anna", "Maschinenbau", 3, "12345678"),
    Student("Berliner", "Bob", "Maschinenbau", 5, "87654321"),
    Student("Colorado", "Charlie", "Elektrotechnik", 2, "11223344"),
    Student("Dietrich", "Diana", "Informatik", 1, "99887766"),
    Student("Eberhard", "Emil", "Maschinenbau", 4, "55443322")
]

# Alle Kursteilnehmer anzeigen
print("=== Python-Kurs Teilnehmer ===")
for student in python_kurs:
    print(f"- {student}")

print(f"\nGesamtzahl: {len(python_kurs)} Studierende")
```

Wir können nun nach dem Studiengang filtern, das durchschnittliche Semester
berechnen oder Noten verwalten.

```{code-cell} ipython3
# Nach Studiengang filtern
def studierende_nach_studiengang(studierende, studiengang):
    gefunden = []
    for student in studierende:
        if student.studiengang == studiengang:
            gefunden.append(student)
    return gefunden

maschinenbauer = studierende_nach_studiengang(python_kurs, "Maschinenbau")
print(f"\n=== Maschinenbau-Studierende ({len(maschinenbauer)}) ===")
for student in maschinenbauer:
    print(f"- {student}")

# Durchschnittliches Semester berechnen
semester_summe = 0
for student in python_kurs:
    semester_summe = semester_summe + student.semester
durchschnitt_semester = semester_summe / len(python_kurs)
print(f"\nDurchschnittliches Semester: {durchschnitt_semester:.1f}")

# Noten verwalten (Beispiel)
print("\n=== Noten eintragen ===")
python_kurs[0].note_hinzufuegen(1.7)  # Anna
python_kurs[0].note_hinzufuegen(2.3)
python_kurs[1].note_hinzufuegen(2.0)  # Bob

print(f"{python_kurs[0].vollstaendiger_name()}: Durchschnitt {python_kurs[0].notendurchschnitt():.1f}")
print(f"{python_kurs[1].vollstaendiger_name()}: Durchschnitt {python_kurs[1].notendurchschnitt():.1f}")
```

Interessant für eine Kursverwaltung sind statistische Auswertungen.

```{code-cell} ipython3
# Hilfsfunktionen für die Kursverwaltung
def kurs_statistik(studierende):
    """Zeigt eine Übersicht über den Kurs"""
    print("=== KURS-STATISTIK ===")
    print(f"Teilnehmer gesamt: {len(studierende)}")
    
    # Maschinenbau-Studierende zählen
    maschinenbau_anzahl = 0
    for student in studierende:
        if student.studiengang == "Maschinenbau":
            maschinenbau_anzahl = maschinenbau_anzahl + 1
    
    print(f"Maschinenbau-Studierende: {maschinenbau_anzahl}")
    
    # Niedrigstes und höchstes Semester finden
    semester_min = studierende[0].semester
    semester_max = studierende[0].semester
    for student in studierende:
        if student.semester < semester_min:
            semester_min = student.semester
        if student.semester > semester_max:
            semester_max = student.semester
    
    print(f"Semester-Spanne: {semester_min}. bis {semester_max}. Semester")

def student_suchen(studierende, nachname):
    """Sucht einen Studierenden nach Nachname"""
    for student in studierende:
        if student.nachname.lower() == nachname.lower():
            return student
    return None

# Statistik anzeigen
kurs_statistik(python_kurs)

# Student suchen
print("\n=== SUCHE ===")
gefunden = student_suchen(python_kurs, "Berliner")
if gefunden:
    print(f"Gefunden: {gefunden}")
    print(f"Matrikelnummer: {gefunden.matrikelnummer}")
else:
    print("Student nicht gefunden")
```

Mit wenigen Zeilen Code haben wir ein funktionsfähiges Verwaltungssystem
erstellt und schließen das Beispiel mit der nächsten Mini-Übung ab.

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie eine Funktion `erstsemester_finden(studierende)`, die eine Liste
aller Studierenden im 1. Semester zurückgibt. Testen Sie die Funktion mit dem
`python_kurs`.
```

```{code-cell} ipython3
# Geben Sie nach diesem Kommentar Ihren Code ein:

```

````{admonition} Lösung
:class: miniexercise, toggle
```python
def erstsemester_finden(studierende):
    """Findet alle Studierenden im 1. Semester"""
    erstsemester = []
    for student in studierende:
        if student.semester == 1:
            erstsemester.append(student)
    return erstsemester

# Test der Funktion
erstsemester = erstsemester_finden(python_kurs)
print(f"Erstsemester ({len(erstsemester)}):")
for student in erstsemester:
    print(f"- {student}")
```
````

## Zusammenfassung und Ausblick

Listen kombiniert mit Objekten sind ein mächtiges Werkzeug zur Verwaltung von
Daten. Dabei ist es hilfreich, vordefinierte Methoden wie beispielsweise
`__str__` zu implementieren, um die Objekte benutzerfreundlich zu machen. Mit
diesem Kapitel schließen wir die Objektorientierte Programmierung ab, um uns den
Themen Matlab und Simulink zu widmen.
