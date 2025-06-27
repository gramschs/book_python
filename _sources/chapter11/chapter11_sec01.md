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

# 11.1 Kontinuierliche Daten visualisieren

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können **Matplotlib** mit der üblichen Abkürzung **plt** importieren.
* Sie können Funktionen als **Liniendiagramm** visualisieren.
* Sie können Messwerte als **Streudiagramm** darstellen.
* Sie verstehen den Unterschied zwischen Linien- und Streudiagrammen.
```

## Liniendiagramme

Liniendiagramme werden zur Visualisierung benutzt, wenn die Daten kontinuierlich
sind und zu jedem x-Wert ein y-Wert vorliegt. Am häufigsten ist dies der Fall,
wenn die Daten von einer mathematischen Funktion stammen oder wenn Messungen über
die Zeit erfasst werden. Obwohl die Daten theoretisch für jeden x-Wert vorliegen
und wir daher Millionen von (x,y)-Punkten zeichnen könnten, benutzen wir eine
Wertetabelle mit wenigen (x,y)-Paaren. Die Anzahl der (x,y)-Paare bestimmt dann,
wie "glatt" die Visualisierung wirkt.

Erzeugen wir eine Liste mit x-Werten und dazugehörigen y-Werten.

```{code-cell}
x = [-2, -1, 0, 1, 2]
y = [4, 1, 0, 1, 4]
```

Danach lassen wir den Python-Interpreter diese Werte zeichnen. Dazu benötigen
wir das Modul `matplotlib`, genauer gesagt nur einen Teil dieses Moduls namens
`pyplot`. Daher laden wir es zuerst mit der typischen Abkürzung `plt`.

```{code-cell}
import matplotlib.pyplot as plt
```

Matplotlib bietet zwei Schnittstellen an, die Funktionen und Methoden des Moduls
zu benutzen. Die erste Schnittstelle ist **zustandsorientiert**, die zweite
**objektorientiert**. Die zustandsorientierte Schnittstelle ist älter. Die
Entwicklerinnen und Entwickler des Matplotlib-Moduls orientierten sich zunächst
an der kommerziellen Software MATLAB und griffen erst in einer späteren Phase
auf Objektorientierung zurück.

Bei der zustandsorientierten Schnittstelle werden Funktionen benutzt, die auf
das aktuelle Objekt wirken. Das hat Nachteile, wenn beispielsweise mehrere Plots
in einer Grafik gegenübergestellt werden. Dann ist es schwierig zuzuordnen, was
gerade das aktuelle Objekt ist. Daher hilft die zweite Matplotlib-Schnittstelle,
die objektorientierte Schnittstelle, mehrere Objekte auseinanderzuhalten.

Zunächst werden wir die zustandsorientierte Schnittstelle benutzen, um den
Vorteil auszunutzen, MATLAB-ähnliche Syntax verwenden zu können.

Zunächst erstellen wir ein Liniendiagramm mit der Funktion `plt.plot()`. Zuvor
öffnen wir mit `plt.figure()` eine neue Zeichenfläche, die Figure genannt wird.

```{code-cell}
plt.figure()
plt.plot(x, y)
plt.show()
```

Aber zurück zum Plot, sieht krakelig aus. Eigentlich sollte dies eine Parabel im
Intervall [-2,2] werden. Mit nur fünf Punkten und der Tatsache, dass diese fünf
Punkte mit geraden Linien verbunden werden, sieht es etwas unschön aus. Besser
wird es mit mehr Punkten, aber die wollen wir jetzt nicht von Hand erzeugen. Wir
verwenden das Modul `numpy` für numerisches Python, das wir wieder einmal zuerst
laden müssen.

Die Funktion `np.linspace(a, b, Anzahl)` erzeugt Punkte im Intervall [a,b] und
zwar genauso viele, wie durch die Option `Anzahl` vorgegeben werden. Damit
können wir jetzt eine feiner aufgelöste Wertetabelle erstellen und
visualisieren.

```{code-cell}
import numpy as np

x = np.linspace(-2, 2, 100) 
y = x**2

plt.figure()
plt.plot(x, y)
plt.show()
```

Als nächstes beschäftigen wir uns mit Beschriftungen. Mit den Funktionen
`xlabel()` und `ylabel()` beschriften wir die x- und y-Achse. Mit `title()` wird
der Titel gesetzt.

```{code-cell}
# Daten
x = np.linspace(-10, 10, 200)
y = np.sin(x)

# Visualisierung
plt.figure()
plt.plot(x, y)
plt.xlabel('Zeit in Sekunden')
plt.ylabel('Stromstärke in Ampere')
plt.title('Wechselstrom')
plt.show()
```

```{admonition} Mini-Übung
:class: miniexercise 
Plotten Sie folgende Funktionen: 
    
* lineare Funktion, z.B. f(x) = 3x + 7
* Sinus,
* Kosinus,
* Exponentialfunktion und
* Wurzelfunktion.

Bei welcher Funktion müssen Sie besonders auf das Definitionsgebiet der
Funktion achten?
```

```{code-cell}
# Hier Ihr Code:
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-3, 3, 101)
y1 = 3 * x1 + 7

x2 = np.linspace(-2 * np.pi, 2 * np.pi, 101)
y2 = np.sin(x2)
y3 = np.cos(x2)

x4 = np.linspace(-3, 3, 101)
y4 = np.exp(x4)

x5 = np.linspace(0, 5, 101)
y5 = np.sqrt(x5)

plt.figure()
plt.plot(x5,y5)
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('Mini-Übung');
```
Bei der Wurzelfunktion muss man auf das Definitionsgebiet achten, da sie nur für
$x >= 0$ definiert ist.
````

## Streudiagramme

Bei Streudiagrammen werden nicht die Punkte (x₁,y₁) mit (x₂,y₂) mit
(x₃,y₃) usw. durch Linien verbunden, sondern jeder Punkt wird einzeln an seiner
Koordinatenstelle dargestellt. Ob dazu ein Punkt, Kreis, Dreieck oder
Quadrat oder ein anderes Symbol verwendet wird, bleibt dem Anwender überlassen.
Streudiagramme heißen im Englischen Scatter-Plot, daher lautet die entsprechende
Matplotlib-Funktion auch `scatter()`.

```{code-cell}
import numpy as np
import matplotlib.pyplot as plt

# Daten
x = np.linspace(-2*np.pi, 2*np.pi, 25)
y = np.sin(x)

# Streudiagramm
plt.figure()
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sinus-Funktion als Streudiagramm')
plt.show()
```

Über die Option `marker=` lässt sich das Symbol einstellen, mit dem das
Streudiagramm erzeugt wird. Voreingestellt ist ein ausgefüllter Kreis. Weitere
Optionen für die Marker-Symbole sind in der Matplotlib-Dokumentation gelistet:

> <https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers>

Die Farbe der Marker oder auch der Linien lässt sich mit dem optionalen Argument
`color=` einstellen.

Wenn wir beispielsweise an jedem Wochentag die Temperatur an zwei Orten messen,
bietet es sich an, beide Messreihen in einem Diagramm zu visualisieren.
Dazu werden wir unterschiedliche Marker und unterschiedliche Farben verwenden.

```{code-cell}
# Daten - simulierte Temperaturmessungen
x = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']
y1 = [18, 22, 19, 21, 20, 23, 24]  # Frankfurt
y2 = [16, 20, 17, 19, 18, 21, 22]  # Offenbach

# Streudiagramme
plt.figure()
plt.scatter(x, y1, marker='+', s=100, color='blue')
plt.scatter(x, y2, marker='o', s=50, color='red')
plt.xlabel('Wochentag')
plt.ylabel('Temperatur [°C]')
plt.title('Temperaturmessungen')
plt.show()
```

Dann ist es aber auch gut, die Visualisierung zu beschriften. Dazu kennzeichnet
man jeden einzelnen Plot-Aufruf mit einem sogenannten Label, z.B.
`plt.scatter(x, y1, label='Frankfurt')`. Zuletzt verwendet man die Funktion
`legend()`, die eine Legende mit allen Label-Einträgen erzeugt, bei denen die
Farben der Kurven und die Marker korrekt zu den Namen (Labels) zugeordnet
werden.

```{code-cell}
# Daten
x = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']
y1 = [18, 22, 19, 21, 20, 23, 24]  # Frankfurt
y2 = [16, 20, 17, 19, 18, 21, 22]  # Offenbach

# Streudiagramme mit Legende
plt.figure()
plt.scatter(x, y1, marker='+', s=100, color='blue', label='Frankfurt')
plt.scatter(x, y2, marker='o', s=50, color='red', label='Offenbach')
plt.xlabel('Wochentag')
plt.ylabel('Temperatur [°C]')
plt.title('Temperaturmessungen in der Region')
plt.legend()
plt.show()
```

```{admonition} Mini-Übung
:class: miniexercise
Erstellen Sie ein Streudiagramm mit folgenden Spezifikationen:
- x-Werte: Zahlen von 1 bis 20
- y-Werte: Zufallszahlen zwischen 10 und 30 (verwenden Sie `np.random.uniform(10, 30, 20)`)
- Marker: rote Dreiecke (marker='^')
- Titel: "Zufällige Messwerte"
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
import matplotlib.pyplot as plt
import numpy as np

# Daten generieren
np.random.seed(42)  # Für reproduzierbare Ergebnisse
x = range(1, 21)    # Zahlen von 1 bis 20
y = np.random.uniform(10, 30, 20)  # Zufallszahlen zwischen 10 und 30

# Streudiagramm erstellen
plt.figure()
plt.scatter(x, y, marker='^', color='red', s=60)
plt.xlabel('Messung Nr.')
plt.ylabel('Messwert')
plt.title('Zufällige Messwerte')
plt.show()
```
````

## Wann verwendet man welchen Diagrammtyp?

Für bekannte Funktionen wie Sinus oder Kosinus würde man normalerweise
Liniendiagramme verwenden. Streudiagramme eignen sich eher für die Visualisierung
von Messungen oder wenn man Korrelationen zwischen zwei Variablen untersuchen möchte.

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir die Grundlagen der Datenvisualisierung mit
Matplotlib kennengelernt. Liniendiagramme eignen sich für kontinuierliche Daten,
mathematische Funktionen und Zeitreihen, bei denen die Datenpunkte sinnvoll
miteinander verbunden werden können. Streudiagramme sind ideal für diskrete
Messpunkte, Korrelationsanalysen und Situationen, in denen die Einzelpunkte im
Fokus stehen. Im nächsten Kapitel werden wir uns mit Balkendiagrammen und
Histogrammen beschäftigen, die für andere Datentypen geeignet sind.
