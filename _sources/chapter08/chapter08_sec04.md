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

# Übungen

```{admonition} Übung 8.1
:class: miniexercise
Erstellen Sie eine Klasse `Auto` zur Verwaltung von Fahrzeuginformationen. Die Klasse soll folgende Attribute haben:
- `marke` (z.B. "VW", "BMW")
- `modell` (z.B. "Golf", "320i")
- `baujahr` (z.B. 2020)
- `kilometerstand` (z.B. 45000)

1. Implementieren Sie die `__init__`-Methode, die alle vier Attribute beim Erstellen eines Objekts initialisiert.
2. Erstellen Sie zwei Auto-Objekte mit unterschiedlichen Daten.
3. Geben Sie für beide Autos die Marke und den Kilometerstand aus.
4. Erhöhen Sie den Kilometerstand des ersten Autos um 1500 km und geben Sie den neuen Wert aus.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Auto:
    def __init__(self, marke, modell, baujahr, kilometerstand):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = kilometerstand


# Zwei Auto-Objekte erstellen
auto1 = Auto("VW", "Golf", 2020, 45000)
auto2 = Auto("BMW", "320i", 2018, 82000)

# Marke und Kilometerstand ausgeben
print(f"Auto 1: {auto1.marke}, {auto1.kilometerstand} km")
print(f"Auto 2: {auto2.marke}, {auto2.kilometerstand} km")

# Kilometerstand erhöhen
auto1.kilometerstand = auto1.kilometerstand + 1500
print(f"\nAuto 1 nach der Fahrt: {auto1.kilometerstand} km")
```
````

```{admonition} Übung 8.2
:class: miniexercise
Erweitern Sie die Klasse `Auto` aus Übung 8.1 um zwei Methoden:

1. `fahre(kilometer)`: Diese Methode erhält die gefahrenen Kilometer als Parameter und erhöht den Kilometerstand des Autos entsprechend.
2. `info()`: Diese Methode gibt eine Zeile mit allen wichtigen Informationen zum Auto zurück, z.B. "VW Golf (Baujahr 2020): 45000 km".

Testen Sie beide Methoden mit mindestens einem Auto-Objekt.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Auto:
    def __init__(self, marke, modell, baujahr, kilometerstand):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = kilometerstand
    
    def fahre(self, kilometer):
        """Erhöht den Kilometerstand um die gefahrenen Kilometer"""
        self.kilometerstand = self.kilometerstand + kilometer
    
    def info(self):
        """Gibt eine formatierte Info-Zeile zum Auto zurück"""
        return f"{self.marke} {self.modell} (Baujahr {self.baujahr}): {self.kilometerstand} km"


# Test der Methoden
auto1 = Auto("VW", "Golf", 2020, 45000)

# Info ausgeben
print(auto1.info())

# Eine Strecke fahren
auto1.fahre(250)
print(f"Nach 250 km Fahrt: {auto1.info()}")

# Noch eine Strecke fahren
auto1.fahre(1800)
print(f"Nach weiteren 1800 km: {auto1.info()}")
```
````

```{admonition} Übung 8.3
:class: miniexercise
Erstellen Sie eine Klasse `Artikel` für eine Einkaufsliste mit folgenden Attributen:
- `name` (z.B. "Milch", "Brot")
- `preis` (Preis pro Stück in Euro)
- `menge` (Anzahl der Artikel)

1. Implementieren Sie die `__init__`-Methode.
2. Schreiben Sie eine Methode `gesamtpreis()`, die den Gesamtpreis für diesen Artikel berechnet (Preis × Menge) und zurückgibt.
3. Schreiben Sie eine Methode `menge_aendern(neue_menge)`, die die Menge des Artikels auf einen neuen Wert setzt.
4. Testen Sie Ihre Klasse: Erstellen Sie einen Artikel, geben Sie den Gesamtpreis aus, ändern Sie die Menge und geben Sie den neuen Gesamtpreis aus.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Artikel:
    def __init__(self, name, preis, menge):
        self.name = name
        self.preis = preis
        self.menge = menge
    
    def gesamtpreis(self):
        """Berechnet den Gesamtpreis (Preis × Menge)"""
        return self.preis * self.menge
    
    def menge_aendern(self, neue_menge):
        """Ändert die Menge des Artikels"""
        self.menge = neue_menge


# Test der Klasse
artikel1 = Artikel("Milch", 1.29, 3)

print(f"Artikel: {artikel1.name}")
print(f"Gesamtpreis für {artikel1.menge} Stück: {artikel1.gesamtpreis():.2f} Euro")

# Menge ändern
artikel1.menge_aendern(5)
print(f"\nNach Mengenänderung:")
print(f"Gesamtpreis für {artikel1.menge} Stück: {artikel1.gesamtpreis():.2f} Euro")
```
````

```{admonition} Übung 8.4
:class: miniexercise
Erweitern Sie die Klasse `Artikel` aus Übung 8.3 um eine Methode `rabatt_anwenden(prozent)`, die einen prozentualen Rabatt auf den Preis anwendet.

Beispiel: Bei einem Artikel mit Preis 10.00 Euro und einem Rabatt von 20% soll der neue Preis 8.00 Euro betragen.

1. Implementieren Sie die Methode `rabatt_anwenden(prozent)`, die den Preis des Artikels entsprechend reduziert.
2. Schreiben Sie eine weitere Methode `ist_guenstig()`, die `True` zurückgibt, wenn der Gesamtpreis unter 5.00 Euro liegt, sonst `False`.
3. Testen Sie beide Methoden mit einem Artikel-Objekt.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Artikel:
    def __init__(self, name, preis, menge):
        self.name = name
        self.preis = preis
        self.menge = menge
    
    def gesamtpreis(self):
        """Berechnet den Gesamtpreis (Preis × Menge)"""
        return self.preis * self.menge
    
    def menge_aendern(self, neue_menge):
        """Ändert die Menge des Artikels"""
        self.menge = neue_menge
    
    def rabatt_anwenden(self, prozent):
        """Wendet einen prozentualen Rabatt auf den Preis an"""
        self.preis = self.preis * (1 - prozent / 100)
    
    def ist_guenstig(self):
        """Prüft, ob der Gesamtpreis unter 5 Euro liegt"""
        return self.gesamtpreis() < 5.0


# Test der Methoden
artikel1 = Artikel("Schokolade", 2.50, 3)

print(f"Artikel: {artikel1.name}")
print(f"Preis pro Stück: {artikel1.preis:.2f} Euro")
print(f"Gesamtpreis: {artikel1.gesamtpreis():.2f} Euro")
print(f"Ist günstig? {artikel1.ist_guenstig()}")

# Rabatt anwenden
print("\n20% Rabatt wird angewendet...")
artikel1.rabatt_anwenden(20)

print(f"Neuer Preis pro Stück: {artikel1.preis:.2f} Euro")
print(f"Neuer Gesamtpreis: {artikel1.gesamtpreis():.2f} Euro")
print(f"Ist günstig? {artikel1.ist_guenstig()}")
```
````

```{admonition} Übung 8.5
:class: miniexercise
Erstellen Sie eine Klasse `Buch` zur Verwaltung Ihrer persönlichen Bibliothek mit folgenden Attributen:
- `titel` (z.B. "1984")
- `autor` (z.B. "George Orwell")
- `seiten` (z.B. 328)
- `gelesen` (Boolean: True oder False)

1. Implementieren Sie die `__init__`-Methode. Das Attribut `gelesen` soll standardmäßig auf `False` gesetzt werden.
2. Schreiben Sie eine Methode `als_gelesen_markieren()`, die das Buch als gelesen markiert.
3. Schreiben Sie eine Methode `lesefortschritt(gelesene_seiten)`, die berechnet und zurückgibt, wie viel Prozent des Buches bereits gelesen wurden.
4. Testen Sie Ihre Klasse mit mindestens einem Buch.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Buch:
    def __init__(self, titel, autor, seiten):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten
        self.gelesen = False  # Standardmäßig noch nicht gelesen
    
    def als_gelesen_markieren(self):
        """Markiert das Buch als gelesen"""
        self.gelesen = True
    
    def lesefortschritt(self, gelesene_seiten):
        """Berechnet den Lesefortschritt in Prozent"""
        prozent = (gelesene_seiten / self.seiten) * 100
        return prozent


# Test der Klasse
buch1 = Buch("1984", "George Orwell", 328)

print(f"Buch: {buch1.titel} von {buch1.autor}")
print(f"Seiten: {buch1.seiten}")
print(f"Gelesen: {buch1.gelesen}")

# Lesefortschritt prüfen
print(f"\nLesefortschritt bei 100 Seiten: {buch1.lesefortschritt(100):.1f}%")
print(f"Lesefortschritt bei 250 Seiten: {buch1.lesefortschritt(250):.1f}%")

# Als gelesen markieren
buch1.als_gelesen_markieren()
print(f"\nBuch wurde fertig gelesen: {buch1.gelesen}")
```
````

```{admonition} Übung 8.6
:class: miniexercise
Implementieren Sie für die Klasse `Buch` aus Übung 8.5 die `__str__`-Methode, damit Bücher schön formatiert ausgegeben werden können.

Die `__str__`-Methode soll eine Zeile im folgenden Format zurückgeben:
- Wenn das Buch noch nicht gelesen wurde: "Titel von Autor (Seiten S.) - noch nicht gelesen"
- Wenn das Buch gelesen wurde: "Titel von Autor (Seiten S.) - ✓ gelesen"

Testen Sie Ihre Implementierung mit zwei Büchern: einem gelesenen und einem ungelesenen.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Buch:
    def __init__(self, titel, autor, seiten):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten
        self.gelesen = False
    
    def __str__(self):
        """Gibt eine formatierte Beschreibung des Buches zurück"""
        if self.gelesen:
            status = "✓ gelesen"
        else:
            status = "noch nicht gelesen"
        return f"{self.titel} von {self.autor} ({self.seiten} S.) - {status}"
    
    def als_gelesen_markieren(self):
        """Markiert das Buch als gelesen"""
        self.gelesen = True
    
    def lesefortschritt(self, gelesene_seiten):
        """Berechnet den Lesefortschritt in Prozent"""
        prozent = (gelesene_seiten / self.seiten) * 100
        return prozent


# Test der __str__-Methode
buch1 = Buch("1984", "George Orwell", 328)
buch2 = Buch("Der Prozess", "Franz Kafka", 256)

# Buch 2 als gelesen markieren
buch2.als_gelesen_markieren()

# Ausgabe mit print (verwendet automatisch __str__)
print(buch1)
print(buch2)

# Auch in einer Liste funktioniert es
meine_buecher = [buch1, buch2]
print("\nMeine Bücher:")
for buch in meine_buecher:
    print(f"- {buch}")
```
````

```{admonition} Übung 8.7
:class: miniexercise
Erstellen Sie eine kleine Bücherverwaltung mit Listen von Objekten. Verwenden Sie dafür die Klasse `Buch` aus den vorherigen Übungen.

1. Erstellen Sie eine Liste mit mindestens 5 verschiedenen Büchern. Markieren Sie einige davon als gelesen.
2. Schreiben Sie eine Funktion `finde_buch_nach_titel(buecher, titel)`, die in der Liste nach einem Buch mit dem angegebenen Titel sucht und das Buch-Objekt zurückgibt (oder `None`, falls nicht gefunden).<br>
Tipp: Mit der Methode `.lower()` können Sie einen String in Kleinbuchstaben umwandeln, was Vergleiche vereinfacht.
3. Schreiben Sie eine Funktion `ungelesene_buecher(buecher)`, die eine neue Liste mit allen noch nicht gelesenen Büchern zurückgibt.
4. Schreiben Sie eine Funktion `dicke_buecher(buecher, min_seiten)`, die alle Bücher zurückgibt, die mindestens die angegebene Seitenzahl haben.
5. Testen Sie alle drei Funktionen mit Ihrer Bücherliste.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Buch:
    def __init__(self, titel, autor, seiten):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten
        self.gelesen = False
    
    def __str__(self):
        if self.gelesen:
            status = "✓ gelesen"
        else:
            status = "noch nicht gelesen"
        return f"{self.titel} von {self.autor} ({self.seiten} S.) - {status}"
    
    def als_gelesen_markieren(self):
        self.gelesen = True


def finde_buch_nach_titel(buecher, titel):
    """Sucht ein Buch nach Titel"""
    for buch in buecher:
        if buch.titel.lower() == titel.lower():
            return buch
    return None


def ungelesene_buecher(buecher):
    """Gibt eine Liste aller ungelesenen Bücher zurück"""
    ungelesen = []
    for buch in buecher:
        if not buch.gelesen:
            ungelesen.append(buch)
    return ungelesen


def dicke_buecher(buecher, min_seiten):
    """Gibt alle Bücher zurück, die mindestens min_seiten haben"""
    dick = []
    for buch in buecher:
        if buch.seiten >= min_seiten:
            dick.append(buch)
    return dick


# Bücherliste erstellen
bibliothek = [
    Buch("1984", "George Orwell", 328),
    Buch("Der Prozess", "Franz Kafka", 256),
    Buch("Die Verwandlung", "Franz Kafka", 96),
    Buch("Harry Potter", "J.K. Rowling", 336),
    Buch("Der Hobbit", "J.R.R. Tolkien", 310)
]

# Einige als gelesen markieren
bibliothek[1].als_gelesen_markieren()  # Der Prozess
bibliothek[2].als_gelesen_markieren()  # Die Verwandlung
bibliothek[4].als_gelesen_markieren()  # Der Hobbit

# Test: Buch nach Titel suchen
print("=== SUCHE NACH TITEL ===")
gesuchtes_buch = finde_buch_nach_titel(bibliothek, "1984")
if gesuchtes_buch:
    print(f"Gefunden: {gesuchtes_buch}")
else:
    print("Buch nicht gefunden")

# Test: Ungelesene Bücher finden
print("\n=== UNGELESENE BÜCHER ===")
ungelesen = ungelesene_buecher(bibliothek)
print(f"Anzahl ungelesener Bücher: {len(ungelesen)}")
for buch in ungelesen:
    print(f"- {buch}")

# Test: Dicke Bücher finden (mindestens 300 Seiten)
print("\n=== BÜCHER MIT MINDESTENS 300 SEITEN ===")
dick = dicke_buecher(bibliothek, 300)
for buch in dick:
    print(f"- {buch}")
```
````

```{admonition} Übung 8.8
:class: miniexercise
Erstellen Sie ein vollständiges Programm zur Verwaltung einer Einkaufsliste mit der Klasse `Artikel` aus den vorherigen Übungen.

Anforderungen:

1. Erweitern Sie die Klasse `Artikel` um die `__str__`-Methode, die einen Artikel im Format "Name: Menge × Preis Euro = Gesamtpreis Euro" ausgibt (z.B. "Milch: 3 × 1.29 Euro = 3.87 Euro").

2. Erstellen Sie eine Liste mit mindestens 5 verschiedenen Artikeln für Ihren Einkauf.

3. Schreiben Sie folgende Funktionen:
   - `zeige_einkaufsliste(artikel_liste)`: Gibt alle Artikel formatiert aus
   - `gesamtkosten(artikel_liste)`: Berechnet die Gesamtkosten aller Artikel
   - `teuerster_artikel(artikel_liste)`: Findet den Artikel mit dem höchsten Gesamtpreis
   - `artikel_unter_preis(artikel_liste, max_preis)`: Gibt alle Artikel zurück, deren Gesamtpreis unter dem angegebenen Maximalpreis liegt

4. Testen Sie Ihr Programm:
   - Zeigen Sie die komplette Einkaufsliste an.
   - Geben Sie die Gesamtkosten aus.
   - Finden und zeigen Sie den teuersten Artikel.
   - Listen Sie alle Artikel auf, die weniger als 5 Euro kosten.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
class Artikel:
    def __init__(self, name, preis, menge):
        self.name = name
        self.preis = preis
        self.menge = menge
    
    def __str__(self):
        """Formatierte Ausgabe des Artikels"""
        return f"{self.name}: {self.menge} × {self.preis:.2f} Euro = {self.gesamtpreis():.2f} Euro"
    
    def gesamtpreis(self):
        """Berechnet den Gesamtpreis (Preis × Menge)"""
        return self.preis * self.menge
    
    def menge_aendern(self, neue_menge):
        """Ändert die Menge des Artikels"""
        self.menge = neue_menge
    
    def rabatt_anwenden(self, prozent):
        """Wendet einen prozentualen Rabatt auf den Preis an"""
        self.preis = self.preis * (1 - prozent / 100)


def zeige_einkaufsliste(artikel_liste):
    """Gibt alle Artikel formatiert aus"""
    print("=== EINKAUFSLISTE ===")
    for artikel in artikel_liste:
        print(f"- {artikel}")


def gesamtkosten(artikel_liste):
    """Berechnet die Gesamtkosten aller Artikel"""
    summe = 0
    for artikel in artikel_liste:
        summe = summe + artikel.gesamtpreis()
    return summe


def teuerster_artikel(artikel_liste):
    """Findet den Artikel mit dem höchsten Gesamtpreis"""
    teuerster = artikel_liste[0]
    for artikel in artikel_liste:
        if artikel.gesamtpreis() > teuerster.gesamtpreis():
            teuerster = artikel
    return teuerster


def artikel_unter_preis(artikel_liste, max_preis):
    """Gibt alle Artikel zurück, deren Gesamtpreis unter max_preis liegt"""
    guenstige = []
    for artikel in artikel_liste:
        if artikel.gesamtpreis() < max_preis:
            guenstige.append(artikel)
    return guenstige


# Einkaufsliste erstellen
einkaufsliste = [
    Artikel("Milch", 1.29, 3),
    Artikel("Brot", 2.49, 2),
    Artikel("Butter", 2.99, 1),
    Artikel("Äpfel", 0.49, 8),
    Artikel("Käse", 3.99, 2)
]

# Komplette Einkaufsliste anzeigen
zeige_einkaufsliste(einkaufsliste)

# Gesamtkosten berechnen und ausgeben
gesamt = gesamtkosten(einkaufsliste)
print(f"\nGesamtkosten: {gesamt:.2f} Euro")

# Teuersten Artikel finden
teuerster = teuerster_artikel(einkaufsliste)
print(f"\nTeuerster Artikel: {teuerster}")

# Günstige Artikel finden (unter 5 Euro)
print("\n=== ARTIKEL UNTER 5 EURO ===")
guenstige = artikel_unter_preis(einkaufsliste, 5.0)
for artikel in guenstige:
    print(f"- {artikel}")
```
````
