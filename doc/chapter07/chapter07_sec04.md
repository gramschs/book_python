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

TODO


```{admonition} Übung 7.1 ???
1. Schreiben Sie eine *Funktion*, mit der das kleine Einmaleins geübt werden
   kann. Die Funktion soll als Eingabe die Anzahl der gewünschten Aufgaben haben
   und als Ausgabe die Anzahl der richtigen Antworten. Innerhalb der Funktion
   sollen dem Benutzer zufällige Einmaleins-Aufgaben gestellt werden. Es soll
   gleich eine Rückmeldung gegeben werden, ob das Ergebnis richtig oder falsch
   ist und ggf. was das richtige Ergebnis gewesen wäre.
2. Schreiben Sie anschließend ein *Programm*, das den Benutzer fragt, wie viele
   1x1-Aufgaben trainiert werden sollen. Anschließend wird die Funktion aus
   Schritt 1 aufgerufen. Am Ende soll der Benutzer darüber informiert werden,
   wie viel Prozent der Aufgaben richtig gelöst wurden.
```

Zahl erraten: Implementieren Sie ein einfaches Zahlenratespiel. Das Programm sollte eine Zufallszahl zwischen 1 und 100 auswählen und den Benutzer so lange nach einer Zahl fragen, bis er die ausgewählte Zahl erraten hat. Verwenden Sie dazu eine while-Schleife und die Funktion input() um die Eingaben des Benutzers zu erhalten.

import random
gesuchte_zahl = random.randint(1, 100)
geratene_zahl = None

while geratene_zahl != gesuchte_zahl:
    geratene_zahl = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein: "))
    if geratene_zahl < gesuchte_zahl:
        print("Zu niedrig!")
    elif geratene_zahl > gesuchte_zahl:
        print("Zu hoch!")
print("Herzlichen Glückwunsch! Sie haben die Zahl erraten.")


Beispiel 3: Begrenzung der Anzahl von Versuchen

In diesem Beispiel begrenzen wir die Anzahl der Versuche, die ein Benutzer hat, um ein Passwort korrekt einzugeben. Wenn das Passwort nach 3 Versuchen nicht korrekt eingegeben wurde, bricht die Schleife ab.

versuche = 0
passwort = "python"

while versuche < 3:
    eingabe = input("Bitte geben Sie das Passwort ein: ")
    if eingabe == passwort:
        print("Zugriff gewährt.")
        break
    versuche += 1
else:
    print("Zu viele falsche Versuche. Zugriff verweigert.")
