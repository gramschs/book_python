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

# 7.2 Schleifen mit Bedingung (while)

Ein typisches Beispiel aus dem Alltag, bei dem wir etwas wiederholen, solange
eine Bedingung erfüllt ist, ist das Kochen von Wasser. Moderne Wasserkocher
haben einen eingebauten Temperatursensor, der die Temperatur des Wassers misst.
Solange die Wassertemperatur kleiner als 100 ˚C ist, wird das Wasser
erhitzt. Sobald die 100 ˚C erreicht sind, wird der Wasserkocher
abgeschaltet. Solche Wiederholungen wollen wir nun mit Python umsetzen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können eine Schleife mit Bedingung als **while**-Schleife in Python
  implementieren.
* Sie können mit **break** eine Schleife vorzeitig abbrechen.
* Sie können mit **continue** eine Schleife vorzeitig fortsetzen.
```

## Syntax der while-Schleife

Bei einer Wiederholung mit Bedingung werden eine oder mehrere Anweisungen
solange wiederholt, wie die Bedingung erfüllt ist. Die sogenannte while-Schleife
hat folgende Struktur:

```python
 while Bedingung: 
        anweisungsblock
```

Die bedingte Wiederholung wird mit dem Schlüsselwort `while` eingeleitet. Dann
folgt die Bedingung, die mit einem `:` abgeschlossen wird. Alle Anweisungen, die
wiederholt werden sollen, werden eingerückt. Diesen Teil nennt man das
Schleifeninnere, die Zeile `while Bedingung:` nennt man den Schleifenkopf.

```{warning}
While-Schleifen sind ein mächtiges Werkzeug in Python, aber es ist wichtig, sie
sorgfältig zu verwenden. Eine schlecht definierte Bedingung könnte dazu führen,
dass die Schleife **unendlich** läuft, was zu Problemen führen kann.
```

Um auf das Beispiel mit dem Wasserkocher zurückzukommen ... auch wenn wir jetzt
keinen echten Temperatursensor haben, würde eine while-Schleife, die einen
Wasserkocher simuliert, folgendermaßen aussehen.

```{code-cell}
temperatur = 20
while temperatur <= 100:
  print(f'aktuelle Wassertemperatur: {temperatur} ˚C')
  temperatur += 10 
print('Befehl an Wasserkocher: schalte das Heizelement aus!')
print('Das Wasser ist fertig gekocht!')
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, das einen Countdown von 10 nach 0 implementiert.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
zaehler = 10
while zaehler >= 0:
    print(zaehler)
    zaehler = zaehler - 1
```
````

```{dropdown} Video "Schleifen mit Bedingung" von Programmieren Starten
<iframe width="560" height="315" src="https://www.youtube.com/embed/sXLicTuJzB4"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Schleifen abbrechen mit break

Die `break`-Anweisung kann verwendet werden, um die Schleife vorzeitig zu
beenden, auch wenn die Bedingung der `while`-Schleife noch `True` ist. Hier ist
ein Beispiel:

```{code-cell}
zaehler = 0
while zaehler < 5:
    if zaehler == 3:
        break
    print(f'Der Zaehler hat aktuell den Wert: {zaehler}.')
    zaehler = zaehler + 1
```

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, das vom Benutzer natürliche Zahlen abfragt und diese
quadriert und ausgibt. Wird eine 0 eingegeben, soll die Eingabe der Zahlen
abgebrochen werden und die Meldung "Sie haben 0 eingegeben, das Programm wird
beendet." ausgegeben werden.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
while True:
    zahl = int(input('Geben Sie eine natürliche Zahl ein (0 zum Beenden): '))
    if zahl == 0:
        print('Sie haben 0 eingegeben, das Programm wird beendet.')
        break
    quadratzahl = zahl**2
    print(f'Das Quadrat von {zahl} ist {quadratzahl}.')
```
````

## Schleifen vorzeitig fortsetzen mit continue

Die `continue`-Anweisung wird verwendet, um den aktuellen Durchgang der Schleife
zu beenden und sofort mit dem nächsten Schleifendurchgang zu beginnen. Hier ist
ein Beispiel:

```{code-cell}
zaehler = 0
while zaehler < 5:
    zaehler = zaehler + 1
    if zaehler == 3:
        continue
    print(f'Der Zaehler hat aktuell den Wert: {zaehler}.')
```

In diesem Beispiel wird "Der Zaehler hat aktuell den Wert: 3" nicht ausgegeben,
da die `continue`-Anweisung dafür sorgt, dass vorzeitig der nächste
Schleifendurchgang begonnen wird, sobald `zaehler` den Wert `3` erreicht.

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein Programm, das eine Zahl abfragt und deren Wurzel berechnet
und ausgibt. Wird eine negative Zahl eingegeben, so soll die Wurzelberechnung
übersprungen werden. Insgesamt soll das Programm solange laufen, bis drei
Wurzeln berechnet wurden.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
zaehler = 0
while zaehler < 3:
    zahl = int(input('Geben Sie eine positive Zahl ein: '))
    if zahl < 0:
        print('Sie haben eine negative Zahl eingegeben, davon kann keine Wurzel berechnet werden.')
        continue
    wurzel = zahl**0.5
    print(f'Die Wurzel von {zahl} ist {wurzel}.')
    zaehler += 1
```
````

## Zusammenfassung und Ausblick

Von den Schleifen kommen wir im nächsten Kapitel zu einem komplett anderem
Thema: Dictionaries.
