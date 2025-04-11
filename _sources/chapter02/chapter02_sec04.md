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

```{admonition} Übung 2.1
:class: miniexercise
Zu welchen Datentypen gehören folgende Ausdrücke? Stellen Sie erst eine
Vermutung auf. Überprüfen Sie dann Ihre Vermutung mit der Funktion `type()`.

* 6 + 2
* 6 + 2.5
* 6 / 2
* 6 / 2.0
* 4 - 2
* 3 * 'Katze'
```

````{admonition} Lösung
:class: miniexercise, toggle
Meine Vermutungen sind:

* 6 + 2 -> Ganzzahl (int)
* 6 + 2.5 -> Gleitkommazahl (float)
* 6 / 2 -> Gleitkommazahl (float)
* 6 / 2.0 -> Gleitkommazahl (float)
* 4 - 2 -> Ganzzahl (int)
* 3 * 'Katze' -> Zeichenkette (str)

Um meine Vermutungen zu überprüfen, können wir den folgenden Code ausführen:

```python
print(type(6 + 2))
print(type(6 + 2.5))
print(type(6 / 2))
print(type(6 / 2.0))
print(type(4 - 2))
print(type(3 * 'Katze'))
```

Die Ausgabe des Codes bestätigt meine Vermutungen:

```markdown
<class 'int'>
<class 'float'>
<class 'float'>
<class 'float'>
<class 'int'>
<class 'str'>
```
````

```{admonition} Übung 2.2
:class: miniexercise
Schreiben Sie einen Witze-Generator. Zuerst soll nach einem Namen gefragt
werden. Danach soll der Python-Interpreter den folgenden Witz ausgeben, wobei an
der Stelle XXX der abgefragte Name stehen soll.

<hr>

Fritz macht 

XXX 

einen Kaffee. Es bleibt heißes Wasser übrig. Fritz fragt: "Was
soll ich mit dem restlichen Wasser machen?" 

XXX 

antwortet: "Einfrieren! Heißes Wasser kann man immer gebrauchen."

<hr> 

Testen Sie Ihr Programm mit verschiedenen Namen.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Namen des Benutzers abfragen
name = input('Wie ist dein Name? ')

# Den Witz generieren
print('Fritz macht')
print(name)
print('einen Kaffee. Es bleibt heißes Wasser übrig. Fritz fragt: "Was soll ich mit dem restlichen Wasser machen?"')
print(name)
print('antwortet: "Einfrieren! Heißes Wasser kann man immer gebrauchen."')
```
````

```{admonition} Übung 2.3
:class: miniexercise
Schreiben Sie ein Python-Programm, das eine Länge vom Benutzer abfragt, die in
Zoll gemessen wurde. Das Programm soll dann diese Länge in Zentimeter umrechnen
und ausgeben. Tipp: 1 Zoll sind 2.54 cm.

Testen Sie Ihr Programm beispielsweise mit der Länge 10 Zoll, die 25.4
Zentimetern entspricht. 
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe: Abfrage der Daten
laenge_in_zoll = float(input('Bitte geben Sie die Länge in Zoll ein: '))

# Verarbeitung: Umrechnung Zoll in Zentimeter
laenge_in_zentimeter = laenge_in_zoll * 2.54

# Ausgabe
print(laenge_in_zoll)
print('Zoll entsprechen ')
print(laenge_in_zentimeter)
print('Zentimetern.')
```
````

```{admonition} Übung 2.4
:class: miniexercise
Schreiben Sie ein Programm, das zuerst nach einer Zahl fragt und danach nach
einer zweiten Zahl fragt. Anschließend gibt das Programm aus, welche beiden
Zahlen gewählt wurden und was das Produkt der beiden Zahlen ist.

Testen Sie anschließend Ihr Programm mit kleinen 1x1-Aufgaben, die Sie sich
selbst ausdenken.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe der beiden ahlen durch Abfrage
zahl1 = float(input('Bitte geben Sie die erste Zahl ein: '))
zahl2 = float(input('Bitte geben Sie die zweite Zahl ein: '))

# Verarbeitung
produkt = zahl1 * zahl2

# Ausgabe
print('Die beiden Zahlen sind ')
print(zahl1)
print('und')
print(zahl2)
print('Das Produkt der beiden Zahlen ist: ')
print(produkt)
```
````

```{admonition} Übung 2.5
:class: miniexercise
Schreiben Sie ein Programm, dass die Kosten für eine Party ermittelt. Zuerst
soll der Python-Interpreter nach der Raummiete fragen, dann nach den
Gesamtkosten des Pizzadienstes und den Gesamtkosten des Getränkelieferanten.
Lassen Sie dann die Gesamtkosten der Party ausgeben und zuletzt die Kosten pro
Gast.

Testen Sie anschließend, ob Ihr Programm für die folgenden Angaben korrekt rechnet:
* Eingabe Raummiete: 230 EUR
* Eingabe Pizzadienst: 168 EUR
* Eingabe Getränkelieferant: 80 EUR
* Eingabe Anzahl Gäste: 12
* Ausgabe: Gesamtkosten für die Party: 478 EUR
* Ausgabe: Kosten pro Gast: 39.833333 EUR
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# Eingabe der Daten durch Abfrage
raummiete = float(input('Wie viel kostet die Raummiete? '))
pizzadienst = float(input('Wie viel kostet der Pizzadienst? '))
getraenkelieferant = float(input('Wie viel kostet der Getränkelieferant? '))
anzahl_gaeste = int(input('Wie viele Gäste kommen zur Party? '))

# Verarbeitung
gesamtkosten = raummiete + pizzadienst + getraenkelieferant
kosten_pro_gast = gesamtkosten / anzahl_gaeste

# Ausgabe
print('Die Gesamtkosten für die Party betragen:')
print(gesamtkosten)
print('Die Kosten pro Gast betragen:')
print(kosten_pro_gast)
```
````
