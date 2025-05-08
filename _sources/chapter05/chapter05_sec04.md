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

```{admonition} Übung 5.1
:class: miniexercise
Schreiben Sie ein Programm, das den Benutzer nach seinem Geburtsjahr fragt.
Danach rechnet das Programm aus, wie alt der Benutzer dieses Jahr wird. Wenn der
Benutzer dieses Jahr volljährig wird, soll das Programm ausgeben: "Hurra, Sie
werden oder wurden dieses Jahr volljährig!" Wenn der Benutzer schon volljährig
ist, soll das Programm ausgeben: "Sie sind bereits volljährig." Ansonsten soll
das Programm ausgeben: "Du bist noch nicht volljährig."
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe
geburtsjahr = int(input('In welchem Jahr wurden Sie geboren? '))

# Verarbeitung: berechne Alter
aktuelles_jahr = 2025
alter = aktuelles_jahr - geburtsjahr

# Ausgabe
if alter < 18:
    print('Du bist noch nicht volljährig.')
elif alter == 18:
    print('Hurra, Sie werden oder wurden dieses Jahr volljährig!')
else:
    print('Sie sind bereits volljährig.')
```
````

```{admonition} Übung 5.2
:class: miniexercise
Ein Onlineshop verkauft T-Shirts, Pullover und Jacken. Ein T-Shirt kostet 15,99
EUR, ein Pullover 24,99 EUR und eine Jacke 39,99 EUR. 

Schreiben Sie ein Programm, das abfragt, wie viele T-Shirts, Pullover und Jacken
bestellt werden sollen. Lassen Sie den Kaufpreis ausgeben. Dazu kommen aber noch
die Portokosten. Bei einem Kaufpreis unter 50 Euro betragen die Portokosten
13,95 Euro. Zwischen 50 und 100 Euro muss der Kunde 4,95 Euro Porto bezahlen. Ab
einem Kaufpreis von 100 Euro gibt es keine Portokosten mehr. Lassen Sie
zusätzlich die Portokosten und den Gesamtpreis ausgeben.

Testen Sie Ihr Programm mit drei Beispielen für die drei unterschiedlichen
Portokosten.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Einstellungen
preis_tshirt = 15.99
preis_pullover = 24.99
preis_jacke = 39.99

# Eingabe der Bestellung
anzahl_tshirts = int(input('Wie viele T-Shirts werden bestellt? '))
anzahl_pullover = int(input('Wie viele Pullover werden bestellt? '))
anzahl_jacken = int(input('Wie viele Jacken werden bestellt? '))

# Verarbeitung
kaufpreis = anzahl_tshirts * preis_tshirt + anzahl_pullover * preis_pullover + anzahl_jacken * preis_jacke

if kaufpreis < 50:
    portokosten = 13.95
elif kaufpreis < 100:
    portokosten = 4.95
else:
    portokosten = 0
gesamtpreis = kaufpreis + portokosten

# Ausgabe
print(f'Kaufpreis: {kaufpreis:.2f} EUR')
print(f'Portokosten: {portokosten:.2f} EUR')
print(f'Gesamtpreis: {gesamtpreis:.2f} EUR')
```
````

```{admonition} Übung 5.3
:class: miniexercise
In einer maschinenbautechnischen Anwendung müssen Sie einen geeigneten Werkstoff
basierend auf der Betriebstemperatur auswählen. Es gelten folgende Regeln:

- Temperaturen unter 0°C: Verwenden Sie "Spezialstahl S420"
- Temperaturen zwischen 0°C und 100°C: Verwenden Sie "Standardstahl S235"
- Temperaturen zwischen 100°C und 500°C: Verwenden Sie "Hitzebeständiger Stahl
  S355"
- Temperaturen über 500°C: Verwenden Sie "Hochtemperaturlegierung Inconel"

Schreiben Sie ein Python-Programm, das die Betriebstemperatur vom Benutzer
abfragt und den empfohlenen Werkstoff ausgibt.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe
temperatur = float(input('Geben Sie die Betriebstemperatur in °C ein: '))

# Verarbeitung und Ausgabe
if temperatur < 0:
    print('Empfohlener Werkstoff: Spezialstahl S420')
elif temperatur <= 100:
    print('Empfohlener Werkstoff: Standardstahl S235')
elif temperatur <= 500:
    print('Empfohlener Werkstoff: Hitzebeständiger Stahl S355')
else:
    print('Empfohlener Werkstoff: Hochtemperaturlegierung Inconel')
```
````

```{admonition} Übung 5.4
:class: miniexercise
Schreiben Sie ein Programm, das den Benutzer nach einem Satz fragt. Anschließend
soll das Programm zählen, wie oft die Vokale a, e, i, o und u in dem Satz
vorkommen.

Zusatzfrage: Was passiert bei Großbuchstaben?
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe
text = input('Geben Sie einen Satz ein: ')

# Verarbeitung
anzahl_a = 0
anzahl_e = 0
anzahl_i = 0
anzahl_o = 0
anzahl_u = 0

for zeichen in text:
    if zeichen == 'a':
        anzahl_a = anzahl_a + 1
    elif zeichen == 'e':
        anzahl_e = anzahl_e + 1
    elif zeichen == 'i':
        anzahl_i = anzahl_i + 1
    elif zeichen == 'o':
        anzahl_o = anzahl_o + 1
    elif zeichen == 'u':
        anzahl_u = anzahl_u + 1
        
# Ausgabe
print(f'Anzahl a: {anzahl_a}')
print(f'Anzahl e: {anzahl_e}')
print(f'Anzahl i: {anzahl_i}')
print(f'Anzahl o: {anzahl_o}')
print(f'Anzahl u: {anzahl_u}')
```
Bei der obigen Lösung werden Großbuchstaben nicht mitgezählt. Entweder werden
noch zusätzlich die Vergleiche mit  'A', 'E', 'I', 'O' und 'U' durchgeführt,
oder der eingebene Satz mit `.lower()` vorab zu Kleinbuchstaben konvertiert.

Bemerkung: Eleganter wäre die Schreibweise `anzahl_a += 1`.
````

```{admonition} Übung 5.5
:class: miniexercise

Wählen Sie sich Ihr Lieblingsrezept aus oder suchen Sie sich ein Rezept des
Tages heraus (siehe https://www.chefkoch.de/rezepte/was-koche-ich-heute/).
Notieren Sie sich die Zutatenlisten in zwei Listen. In der ersten Liste soll die
Menge einer Zutat pro Person stehen, in der zweiten Liste die Zutat selbst.

Lassen Sie dann den Computer fragen, für wie viele Personen gekocht werden soll.
Dann soll der Computer eine Einkaufsliste ausgeben, bei der die Mengenangaben
passend zur Personenanzahl skaliert sind. 

Beispiel Wrap-Pizza (https://www.chefkoch.de/rezepte/3252151483799016/Wrap-Pizza.html):

Computer: Für wie viele Personen soll gekocht werden?<br>
Benutzer: 4<br>
Computer:<br>
Hier ist die Zutatenliste für 4 Personen: <br>
4 Tortillas <br>
8 EL Tomatenmark <br>
4 EL Wasser <br>
usw.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Zutaten fuer Wrap-Pizza fuer eine Person
menge = [1, 2, 1, 1, 1, 1, 1, 1, 5, 45, 1]
zutat = ["Tortilla(s)", "EL Tomatenmark", "EL Wasser", "TL Pizzagewürz", "Kochschinken", "Parikaschote(n)", "Zwiebeln", "Tomate(n)", "Peperoni", "Käse", "Oregano"]

# Eingabe: Abfrage Personenanzahl
personenanzahl = int(input('Für wie viele Personen soll gekocht werden?'))

# Ausgabe
print(f'Hier ist die Zutatenliste für {personenanzahl} Personen:')
for i in range(len(menge)):
    aktuelle_menge = menge[i] * personenanzahl
    print(f'{aktuelle_menge} {zutat[i]}')
```
````

```{admonition} Übung 5.6
:class: miniexercise
Ein Unternehmen fertigt Bauteile mit fortlaufenden Seriennummern. Zur
Qualitätskontrolle sollen die Bauteile anhand ihrer Seriennummer wie folgt
klassifiziert werden:

1. Wenn die Seriennummer durch 2 teilbar ist, wird das Bauteil der
   "Qualitätsprüfung A" unterzogen.
2. Wenn die Seriennummer durch 5 teilbar ist, wird das Bauteil der
   "Spezialprüfung" unterzogen.
3. Alle anderen Bauteile durchlaufen die "Standardprüfung".

Schreiben Sie ein Programm, das:
- Den Benutzer nach einer Seriennummer fragt.
- Die entsprechende Prüfkategorie bestimmt und ausgibt.

Testen Sie Ihr Programm mit den Seriennummern 15, 10, 8 und 7.

*Tipp*: Verwenden Sie den modulo-Operator `%`, um die Teilbarkeit zu prüfen.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe der Seriennummer
seriennummer = int(input("Bitte geben Sie die Seriennummer ein: "))

# Initialisierung mit Standardprüfung
pruefkategorie = "Standardprüfung"

# Überprüfung der Teilbarkeit durch 2
if seriennummer % 2 == 0:
    pruefkategorie = "Qualitätsprüfung A"

# Überprüfung der Teilbarkeit durch 5 (überschreibt ggf. vorherige Kategorie)
if seriennummer % 5 == 0:
    pruefkategorie = "Spezialprüfung"

# Ausgabe der Ergebnisse
print(f"Die Seriennummer {seriennummer} wird der '{pruefkategorie}' zugewiesen.")
```

Testfälle:
- Seriennummer 15: Spezialprüfung (teilbar durch 5)
- Seriennummer 10: Spezialprüfung (teilbar durch 5)
- Seriennummer 8: Qualitätsprüfung A (teilbar durch 2)
- Seriennummer 7: Standardprüfung (weder durch 5 noch durch 2 teilbar)
````

```{admonition} Übung 5.7
:class: miniexercise
Bei der Fertigung von Zahnrädern für Getriebe werden Toleranzen durch den
Fertigungsprozess bedingt. Ein Zahnrad soll einen Durchmesser von 50 mm haben,
jedoch schwankt der tatsächliche Durchmesser aufgrund von
Fertigungsungenauigkeiten.

Schreiben Sie ein Programm, das:

1. Die Fertigung von 200 Zahnrädern simuliert.
2. Die Durchmesser der gefertigten Zahnräder folgen einer Normalverteilung mit
   Mittelwert 50 mm und Standardabweichung 0.1 mm.
3. Die Qualitätskontrolle akzeptiert nur Zahnräder mit folgenden Eigenschaften:
   - "Präzisionsklasse": Durchmesser zwischen 49.9 mm und 50.1 mm
   - "Standardklasse": Durchmesser zwischen 49.8 mm und 49.9 mm oder zwischen
     50.1 mm und 50.2 mm
   - "Ausschuss": Durchmesser kleiner als 49.8 mm oder größer als 50.2 mm
4. Das Programm soll:
   - Die Anzahl der Zahnräder in jeder Klasse ausgeben.
   - Die prozentuale Ausbeute (Nicht-Ausschuss) berechnen und ausgeben.
   - Die Kosten des Ausschusses berechnen, wenn jedes Zahnrad 15 €
     Materialkosten verursacht.

Hinweis: Vergleichen Sie auch, wie sich die Ausbeute verändert, wenn die
Standardabweichung auf 0.15 mm erhöht wird (schlechtere Fertigungsqualität) oder
auf 0.05 mm reduziert wird (bessere Fertigungsqualität).
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
import numpy as np

# Parameter festlegen
anzahl_zahnraeder = 200
soll_durchmesser = 50.0  # mm
standardabweichung = 0.1  # mm
materialkosten_pro_zahnrad = 15  # €

# Grenzwerte für die Qualitätsklassen
praezision_min = 49.9
praezision_max = 50.1
standard_min = 49.8
standard_max = 50.2

# Simulation der Fertigung (normalverteilte Durchmesser)
durchmesser = np.random.normal(soll_durchmesser, standardabweichung, anzahl_zahnraeder)

# Klassifizierung der Zahnräder
praezisionsklasse = 0
standardklasse = 0
ausschuss = 0

# Statt enumerate verwenden wir eine Zählvariable und eine for-Schleife
for i in range(anzahl_zahnraeder):
    d = durchmesser[i]
    if praezision_min <= d <= praezision_max:
        klasse = "Präzisionsklasse"
        praezisionsklasse += 1
    elif standard_min <= d < praezision_min or praezision_max < d <= standard_max:
        klasse = "Standardklasse"
        standardklasse += 1
    else:
        klasse = "Ausschuss"
        ausschuss += 1
    
    # Ausgabe für jedes 20. Zahnrad (zur übersichtlichen Darstellung)
    if (i + 1) % 20 == 0:
        print(f"Zahnrad {i+1}: Durchmesser = {d:.4f} mm - {klasse}")

# Auswertung
ausbeute_prozent = (praezisionsklasse + standardklasse) / anzahl_zahnraeder * 100
ausschuss_kosten = ausschuss * materialkosten_pro_zahnrad

# Ergebnisausgabe
print("\nQualitätsauswertung:")
print(f"Präzisionsklasse: {praezisionsklasse} Stück ({praezisionsklasse/anzahl_zahnraeder*100:.1f}%)")
print(f"Standardklasse: {standardklasse} Stück ({standardklasse/anzahl_zahnraeder*100:.1f}%)")
print(f"Ausschuss: {ausschuss} Stück ({ausschuss/anzahl_zahnraeder*100:.1f}%)")
print(f"\nGesamtausbeute: {ausbeute_prozent:.1f}%")
print(f"Kosten durch Ausschuss: {ausschuss_kosten:.2f} €")

# Simulation mit veränderter Fertigungsqualität
print("\n--- Simulation mit veränderter Fertigungsqualität ---")

# Bessere Qualität (geringere Standardabweichung)
std_besser = 0.05
durchmesser_besser = np.random.normal(soll_durchmesser, std_besser, anzahl_zahnraeder)
praezision_besser = 0
standard_besser = 0

# Zählen ohne List Comprehension
for d in durchmesser_besser:
    if praezision_min <= d <= praezision_max:
        praezision_besser += 1
    elif (standard_min <= d < praezision_min) or (praezision_max < d <= standard_max):
        standard_besser += 1

ausschuss_besser = anzahl_zahnraeder - praezision_besser - standard_besser
ausbeute_besser = (praezision_besser + standard_besser) / anzahl_zahnraeder * 100

# Schlechtere Qualität (höhere Standardabweichung)
std_schlechter = 0.15
durchmesser_schlechter = np.random.normal(soll_durchmesser, std_schlechter, anzahl_zahnraeder)
praezision_schlechter = 0
standard_schlechter = 0

# Zählen ohne List Comprehension
for d in durchmesser_schlechter:
    if praezision_min <= d <= praezision_max:
        praezision_schlechter += 1
    elif (standard_min <= d < praezision_min) or (praezision_max < d <= standard_max):
        standard_schlechter += 1

ausschuss_schlechter = anzahl_zahnraeder - praezision_schlechter - standard_schlechter
ausbeute_schlechter = (praezision_schlechter + standard_schlechter) / anzahl_zahnraeder * 100

# Vergleich der Ausbeuten
print(f"Ausbeute bei besserer Fertigung (Std.abw. = {std_besser} mm): {ausbeute_besser:.1f}%")
print(f"Ausbeute bei Standardfertigung (Std.abw. = {standardabweichung} mm): {ausbeute_prozent:.1f}%")
print(f"Ausbeute bei schlechterer Fertigung (Std.abw. = {std_schlechter} mm): {ausbeute_schlechter:.1f}%")
```
````

```{admonition} Übung 5.8
:class: miniexercise
Schreiben Sie ein Programm, das mit Turtle ein n-Eck zeichnet. Das n-Eck soll in
einen Kreis mit Radius $r$ passen. Die Anzahl der Ecken, der Radius des Kreises
und die Stiftfarbe sollen auf deutsch vom Benutzer abgefragt werden. Bei den
Stiftfarben darf nur aus den Farben rot, grün und blau ausgewählt werden. Wählt
der Benutzer eine falsche Stiftfarbe, soll eine Fehlermeldung ausgegeben werden
und die Stiftfarbe schwarz gewählt werden.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
import ColabTurtlePlus.Turtle as turtle
from numpy import sin, pi

# Vorbereitung des Turle-Feldes 
turtle.clearscreen()

# Abfrage der Benutzereingaben
anzahl_ecken = int(input('Geben Sie die Anzahl der Ecken an: '))
radius = int(input('Geben Sie den Radius des Kreises vor, in den das n-Eck passen soll: '))
stiftfarbe = input('Wählen Sie eine Stiftfarbe (rot, grün oder blau): ')

# Check der Stiftfarbe
if stiftfarbe.lower() == 'rot':
    turtle.pencolor('red')
elif stiftfarbe.lower() == 'grün':
    turtle.pencolor('green')
elif stiftfarbe.lower() == 'blau':
    turtle.pencolor('blue')
else:
    print('Sie haben eine ungültige Stiftfarbe gewählt.')
    turtle.pencolor('black')

# Berechnungen der Seitenlänge des n-Ecks
laenge = 2 * radius * sin(pi / anzahl_ecken)

# Zeichnen des n-Ecks
for i in range(anzahl_ecken):
    turtle.left(360 / anzahl_ecken)
    turtle.forward(laenge)
```
````
