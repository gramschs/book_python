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
Laden Sie die Datei
[20220801_Marktwert_Bundesliga.csv](https://nextcloud.frankfurt-university.de/s/GESBZzRyXq6dLNC)
herunter. Die ersten 5 Zeilen sind Kommentare, die beim Einlesen übersprungen
werden sollten. Informieren Sie sich im Internet über die Option `skiprows` und
importieren Sie die Daten mit Pandas. Lassen Sie die ersten 10 Zeilen anzeigen.

* Welche Daten sind in der Tabelle enthalten?
* Welche Spalte wäre gut als Zeilenindex geeignet? 

Importieren Sie die Daten mit einem geeigneten Zeilenindex.
```
````{admonition} Lösung
:class: miniexercise, toggle
Die Tabelle enthält scheinbar Fußballvereine, ihre Ligazugehörigkeit, Wert und Kadergröße. Zumindest lauten die Spaltenindizes so. In der Tat sind dies die Werte des Transfermarktes der Bundesliga am 01.08.2022. Der Wert eines Vereines wird als Summe der Werte aller Fuballer geschätzt und ist in Mio. Euro angegeben.

Die Vereinsnamen sind ein guter Zeilenindex. Daher sollten die Daten folgendermaßen importiert werden:

```python
import pandas as pd

data = pd.read_csv('20220801_Marktwert_Bundesliga.csv', skiprows=5, index_col=0)
data.head(10)
```
````

```{admonition} Übung 8.2
:class: miniexercise
Laden Sie die Tabelle aus Übung 8.1. 

1. Verschaffen Sie sich einen Überblick: wie viele Spalten gibt es, wie viele Zeilen und  und wie viele Einträge sind gültig?
2. Filtern Sie die Tabelle nach allen Vereine der 2. Bundesliga (`2. Bundesliga`) und speichern Sie diese Daten in der Variable `zweite`.
3. Lassen Sie sich die statistischen Kennzahlen ausgeben. Was ist der höchste Kaderwert, was der kleinste? Wie viele Speiler hat ein Verein in der 2. Bundesliga durchschnittlich?
4. Lassen Sie sich die Daten des 1.FC Kaiserslautern anzeigen. 
```
````{admonition} Lösung
:class: miniexercise, toggle
```python
data.info()
```
Es gibt 3 Spalten (wenn wie oben die Vereine als Zeilenindex verwendet werden) und 56 Zeilen, die alle gültige Werte enthalten.

```python
mein_filter = data.loc[:, 'Ligazugehörigkeit'] == '2. Bundesliga'
zweite = data[mein_filter]

zweite.describe()
```
Der höchste Kaderwert ist 34.85 Mio. EUR, der kleinste 8.83 Mio. EUR. Es spielen durchschnittlich 27 Fußballer in den Zweitligavereinen.
```python
fck = zweite.loc['1.FC Kaiserslautern', :]
print(fck)
```
````

```{admonition} Übung 8.3
:class: miniexercise
Schreiben Sie ein Python-Programm, dass das Spiel Galgenmännchen umsetzt. Das
Spiel funktioniert folgendermaßen:

Der Computer wählt aus einer Liste von Wörtern zufällig eines aus. Anstatt das
Wort anzuzeigen, werden Unterstriche angezeigt. Wurde beispielsweise zufällig
das Wort "beispiel" ausgewählt, so wird 

<code>_ _ _ _ _ _ _ _ </code>

angezeigt. Danach darf der Spieler einen Buchstaben raten. Ist der Buchstabe im
gesuchten Wort, so wird er künftig korrekt angezeigt. Wurde beispielweise E
geraten, dann sieht die Anzeige so aus:

<code>_ e _ _ _ _ e _</code>

Es dürfen maximal 10 Buchstaben falsch geraten werden. Ein Galgenmännchen muss
nicht gezeichnet werden.

Tipps:
* Eine Liste der richtig geratenen Buchstaben ist hilfreich.
* Um zu testen, ob schon alle Buchstaben korrekt geraten wurden, kann auf die
  Existenz von `_` getestet werden. Das ist aber nur eine von vielen
  Möglichkeiten.
```
 
````{admonition} Lösung
:class: miniexercise, toggle
```python
from numpy.random import randint

def waehle_zufallswort():
    # Erzeugung einer Liste mit Wörtern und zufällige Auswahl eines Wortes, indem der Index zufällig gezogen wird
    woerterliste = ['python', 'matlab', 'cplusplus', 'java', 'javascript', 'ruby', 'perl', 'swift', 'golang', 'rust']
    anzahl_woerter = len(woerterliste)
    zufallsindex = randint(anzahl_woerter)
    return woerterliste[zufallsindex]     

def generiere_anzeigetext(wort, korrekt_geratene_buchstaben):
    # Starte mit leerem String
    anzeigetext = ''
    # ersetze jeden Buchstaben im Zufallswort durch sich Unterstrich und ein Leerzeichen,
    # aber nur, wenn er nicht in der Liste der richtig geratenen Buchstaben ist
    for zeichen in wort:
        if zeichen in korrekt_geratene_buchstaben:
            anzeigetext += zeichen + ' '
        else:
            anzeigetext += '_ '

    return anzeigetext

# Start
anzahl_versuche = 10
zufallswort = waehle_zufallswort()

print(f'Wir spielen Galgenmännchen. Sie haben {anzahl_versuche} Fehlversuche, um das Wort zu erraten.')
print('Es darf immer nur ein Kleinbuchstabe eingegeben werden.')
print('Los geht es.')

# Bereite Liste vor, in der richtig geratene Buchstaben gesammelt werden
geratene_richtige_buchstaben = []

# Schleifen zum Anzeigen und Abfragen der Buchstaben
anzeigetext = generiere_anzeigetext(zufallswort, geratene_richtige_buchstaben)
while anzahl_versuche > 0:
    # Anzeige des Rätselwortes und Abfrage eines Buchstabens
    print(f'Sie haben noch {anzahl_versuche} Fehlversuche, das Rätselwort lautet: {anzeigetext}')
    buchstabe = input('Welchen Buchstaben wählen Sie? ')

    # Test, ob Buchstabe vorkommt; wenn nicht, Anzahl Versuche reduzieren
    if buchstabe in zufallswort:
            geratene_richtige_buchstaben.append(buchstabe)
            print(f'Richtig, {buchstabe} ist im gesuchten Wort enthalten.')
    else:
            anzahl_versuche -= 1
            print(f'Leider kommt der Buchstabe {buchstabe} im gesuchten Wort nicht vor.')

    # Aktualisierung des Anzeigetextes
    anzeigetext = generiere_anzeigetext(zufallswort, geratene_richtige_buchstaben)
   
    # Test, ob bereits alle Buchstaben geraten wurden
    if '_' not in anzeigetext:
        print(f'Herzlichen Glückwunsch, Sie haben das Wort {zufallswort} erraten :-)')
        break

if anzahl_versuche == 0 and '_' in anzeigetext:
    print(f'Sie haben leider verloren. Das richtige Wort wäre {zufallswort} gewesen.') 
```
````


  



