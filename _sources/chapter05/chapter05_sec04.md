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

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

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
:class: minisolution, toggle
```python
# Eingabe
geburtsjahr = int(input('In welchem Jahr wurden Sie geboren? '))

# Verarbeitung: berechne Alter
aktuelles_jahr = 2023
alter = aktuelles_jahr - geburtsjahr

# Ausgabe
if alter < 18:
    print('Du bist noch nicht volljährig.!')
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
:class: minisolution, toggle
```python
# Einstellungen
preis_tshirt = 15.99
preis_pullover = 24.99
preis_jacke = 39.99

# Eingabe der Bestellung
anzahl_tshirts = int(input('Wie viele T-Shirts werden bestellt? '))
anzahl_pullover = int(input('Wie viele Pullover werden bestell? '))
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
print(f'Portokosten: {portokosten} EUR')
print(f'Gesamtpreis: {gesamtpreis:.2f} EUR')
```
````

```{admonition} Übung 5.3
:class: miniexercise

Wählen Sie sich Ihr Lieblingsrezept aus oder suchen Sie sich ein Rezept des
Tages heraus (siehe https://www.chefkoch.de/rezepte/was-koche-ich-heute/).
Notieren Sie sich die Zutatenlisten in zwei Listen. In der ersten Liste soll die
Menge einer Zutat pro Person stehen, in der zweiten Liste die Zutat selbst.

Lassen Sie dann den Computer fragen, für wie viele Personen gekocht werden soll.
Dann soll der Computer eine Einkaufsliste ausgeben, bei der die Mengenangaben
passend zur Personenanzahl skaliert sind. 

Beispiel Wrap-Pizza (https://www.chefkoch.de/rezepte/3252151483799016/Wrap-Pizza.html):

Computer: Für wie viele Personen soll gekocht werden?
Benutzer: 4
Computer:
Hier ist die Zutatenliste für 4 Personen:
4 Tortillas
8 EL Tomatenmark
4 EL Wasser
usw.
```
````{admonition} Lösung
:class: minisolution, toggle
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

```{admonition} Übung 5.4
:class: miniexercise
Schreiben Sie ein Programm, das den Benutzer nach einem Satz fragt. Anschließend
soll das Programm zählen, wie oft die Vokale a, e, i, o und u in dem Satz
vorkommen.

Zusatzfrage: Was passiert bei Großbuchstaben?
```
````{admonition} Lösung
:class: minisolution, toggle
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
Bei der obigen Lösung werden Großbichstaben nicht mitgezählt. Entweder werden noch zusätzlich die Vergleiche mit  'A', 'E', 'I', 'O' und 'U' durchgeführt, oder der eingebene Satz mit `.lower()` vorab zu Kleinbuchstaben konvertiert.

Bemerkung: Eleganter wäre die Schreibweise `anzahl_a += 1`.
````
