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

````{admonition} Übung 12.1
:class: miniexercise
Gegeben ist der folgende Code mit Zeilennummern, um Messdaten zu visualisieren.
Suchen Sie die darin enthaltenen Fehler. Korrigieren Sie anschließend den Code.
```python
1  # Datenimport Messdaten
2  x = [-20, -15, -10, -5, 0, 5]
3  y = [152.38, 124.43, 88.91, 37.43, 5.52, -27.41]
4    
5  # Parabel durch die Messdaten
6  y_parabel = x**2
7   
8  # Plot der Messdaten mit zusätzlicher Parabel
9  plt.figure()
10 plt.scatter(x,y)
11 plt.plot(x, y_parabel)
12 plt.xlabel('Temperatur')
13 plt.ylabel('Materialeigenschaft')
14 plt.titel('Messdaten')
15 plt.show()
```
````

````{admonition} Lösung
:class: miniexercise, toggle
* Zeile 6: Listen dürfen nicht quadriert werden.
* Zeile 9: Der Aufruf plt.figure() fürht zu einer Fehlermeldung, da Matplotlib
  nicht importiert wurde.
* Zeile 14: plt.title() ist falsch geschrieben.
```python
import matplotlib.pyplot as plt

# Datenimport Messdaten
x = [-20, -15, -10, -5, 0, 5]
y = [152.38, 124.43, 88.91, 37.43, 5.52, -27.41]
    
# Parabel durch die Messdaten
y_parabel = []
for zahl in x:
    y_parabel.append(zahl**2)
   
# Plot der Messdaten mit zusätzlicher Parabel
plt.figure()
plt.scatter(x,y)
plt.plot(x, y_parabel)
plt.xlabel('Temperatur')
plt.ylabel('Materialeigenschaft')
plt.title('Messdaten')
plt.show()
```

Bemerkung: Hätten wir nicht eine Liste, sondern NumPy-Arrays genommen, um die
Messwerte zu speichern, hätte die Quadratur funktioniert.
````

```{admonition} Übung 12.2
:class: miniexercise
Laden Sie den Datensatz `studierendenzahlen_frankfurt_uas.csv` ([→ hier
Download](https://nextcloud.frankfurt-university.de/s/MzxHw2rDRdx5eRA)) herunter
und importieren Sie ihn mit Pandas. Die ersten drei Zeilen sind Kommentare und
müssen daher mit dem Argument `skiprows=3` übersprungen werden.

1. Lassen Sie die Studierendenzahlen männlich und weiblich visualisieren.
2. Berechnen Sie eine Regressionsgerade jeweils für die Studierendenzahlen
   weiblich und männlich. Wächst die Anzahl der männlichen oder der weiblichen
   Studierenden schneller?
3. Bewerten Sie mit Hilfe des $R^2$-Scores, ob die beiden Regressionsgeraden
   brauchbar sind.
4. Lassen Sie die Regressionsgeraden zusammen mit den Studierendenzahlen
   visualisieren.
```

````{admonition} Lösung
:class: miniexercise, toggle
Der Code zum Import der Studierendenzahlen ist:
```python
import pandas as pd

studizahlen = pd.read_csv('studierendenzahlen_frankfurt_uas.csv', skiprows=3, index_col=0)
studizahlen.head()
```
Der Index kann auf die erste Spalte gesetzt werden, muss aber nicht. Die
Visualisierung als Streudiagramm erfolgt mit folgenden Python-Code:
```python
import matplotlib.pyplot as plt

# Extraktion der Daten aus der Tabelle
y_maennlich = studizahlen['männlich']
y_weiblich = studizahlen['weiblich']
semester = studizahlen.index

# Streudiagramm
plt.figure()
plt.scatter(semester, y_maennlich)
plt.scatter(semester, y_weiblich)
plt.xticks(rotation = 45, ha='right')
plt.xlabel('Semester')
plt.ylabel('Anzahl Studierende')
plt.title('Entwicklung der Studierendenzahlen Frankfurt UAS')
plt.show()
```
Für die Regressionsgeraden brauchen wir Zahlen als Ursache, nicht Semester.
Daher basteln wir mit der `range`-Funktion x-Werte von 0 bis zur Anzahl der
Semester. Danach wenden wir `polyfit` mit Grad 1 an und lassen die beiden
Steigungen und die $R^2$-Scores ausgeben.
```python
from sklearn.metrics import r2_score
import numpy as np

anzahl_semester = len(semester)
x = range(anzahl_semester)

p_maennlich = np.polyfit(x, y_maennlich, 1)
p_weiblich  = np.polyfit(x, y_weiblich, 1)

print(f'Steigung bei der Entwicklung Studenten: {p_maennlich[0]:.2f}')
print(f'Steigung bei der Entwicklung Studentinnen: {p_weiblich[0]:.2f}')

r2_maennlich = r2_score(y_maennlich, np.polyval(p_maennlich, x))
r2_weiblich = r2_score(y_weiblich, np.polyval(p_weiblich, x))

print(f'R2-Score für Studenten: {r2_maennlich:.2f}')
print(f'R2-Score für Studentinnen: {r2_weiblich:.2f}')
```
Die Anzahl der weiblichen Studierenden wächst schneller als die der männlichen
Studierenden. Das Modell ist für Studenten weniger gut geeignet (R2 0.67), aber
für Studentinnen sehr gut (R2 0.9).

Zuletzt wird alles zusammen visualisiert.
```python3
# Erstelle Wertetabelle für das Diagramm
x_modell = np.linspace(0, anzahl_semester)
y_modell_maennlich = np.polyval(p_maennlich, x_modell)
y_modell_weiblich = np.polyval(p_weiblich, x_modell)

# Visualisierung Streudiagramm und Reggressionsgeraden als Liniendiagramm
plt.figure()
plt.scatter(semester, y_maennlich)
plt.scatter(semester, y_weiblich)
plt.plot(x_modell, y_modell_maennlich)
plt.plot(x_modell, y_modell_weiblich)
plt.xticks(rotation = 45, ha='right')
plt.xlabel('Semester')
plt.ylabel('Anzahl Studierende')
plt.title('Entwicklung der Studierendenzahlen Frankfurt UAS')
plt.show()
```
````

```{admonition} Übung 12.3
:class: miniexercise
Laden Sie die Biersteuerstatistik
([→ hier Download](https://nextcloud.frankfurt-university.de/s/Ejc2LFEW3Hz3mA9))
herunter.

1. Importieren Sie die Daten mit Pandas (8 Zeilen müssen übersprungen werden).
   Lassen Sie sich einen Überblick anzeigen. Was enthält die Tabelle?
2. Filtern Sie die Tabelle nach den Jahren 2020, 2021 und 2022 lassen Sie den
   Absatz von Bier in Hektolitern pro Monat visualisieren.
3. Stellen Sie eine Vermutung an. Durch welches Regressionspolynom könnte der
   Absatz von Bier pro Monat am besten erklärt werden?
4. Stellen Sie das Regressionspolynom für 2022 auf und visualisieren Sie es
   zusammen mit den Messwerten. Bewerten Sie es mit dem $R^2$-Score.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
import pandas as pd

daten = pd.read_csv('biersteuerstatistik.csv', skiprows=8)
daten.info()
```

Die Datei enthält 360 Einträge mit Jahr, Monat und Absatz von Bier in Hektolitern.

```python
import matplotlib.pyplot as plt

for jahr in [2020, 2021, 2022]:
    daten_pro_jahr = daten.loc[ daten['Jahr'] == jahr ]
    x = daten_pro_jahr.loc[:, 'Monat']
    y = daten_pro_jahr.loc[:, 'Absatz von Bier [hl]'] 
    plt.scatter(x,y, label=str(jahr))
plt.legend()
plt.xticks(rotation = 45, ha='right')
plt.xlabel('Monat')
plt.ylabel('Absatz von Bier [hl]')
plt.title('Bierstatistik')
plt.show()
```

Aufgrund der Visualisierung entscheiden wir uns für eine Annäherung durch eine
Regressionsparabel.

```python
import numpy as np
from sklearn.metrics import r2_score

data_2022 = daten.loc[daten['Jahr'] == 2022]

x = range(1, 13)
y = data_2022.loc[:, 'Absatz von Bier [hl]']

p2022 = np.polyfit(x, y, 2)
r2 = r2_score(y, np.polyval(p2022, x))
print(f'R2-Score: {r2:.1f}')

x_modell = np.linspace(1, 12)
y_modell = np.polyval(p2022, x_modell)

plt.figure()
plt.scatter(x, y)
plt.plot(x_modell, y_modell)
plt.xlabel('Monat')
plt.ylabel('Absatz von Bier [hl]')
plt.title('Bierstatistik für das Jahr 2022')
plt.show()
```
Das Modell ist mit einem $R^2$-Score von 0.8 gut.
````

```{admonition} Übung 12.4
:class: miniexercise
Verwenden Sie die Bierstatistik-Daten von 2021 aus Übung 12.3 und vergleichen Sie Regressionspolynome der Grade 1, 2, 3 und 4. 

1. Berechnen Sie für jeden Polynomgrad die Koeffizienten mit `polyfit()`.
2. Erstellen Sie für jeden Grad das entsprechende Modell mit `polyval()`.
3. Berechnen Sie jeweils den R²-Wert mit `r2_score()`.
4. Erstellen Sie eine Tabelle mit Polynomgrad und R²-Wert.
5. Visualisieren Sie alle vier Modelle zusammen mit den Originaldaten in einem Diagramm.
6. Diskutieren Sie: Welcher Polynomgrad ist am besten geeignet? Begründen Sie Ihre Antwort anhand der R²-Werte und der Visualisierung.
7. Was passiert, wenn Sie den Polynomgrad auf 11 erhöhen? Testen Sie es und erklären Sie das Ergebnis.
```

````{admonition} Lösung
:class: miniexercise, toggle
Teilaufgabe 1. bis 4. 
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Daten laden (gleich wie in Übung 12.3)
daten = pd.read_csv('data/biersteuerstatistik.csv', skiprows=8)
data_2021 = daten.loc[daten['Jahr'] == 2021, :]

# x-Werte (Monate 1-12) und y-Werte (Bierabsatz)
x = range(1, 13)
y = data_2021.loc[:, 'Absatz von Bier [hl]']

# Polynomgrade 1 bis 4 berechnen und R²-Werte ermitteln
print("Vergleich verschiedener Polynomgrade:")

r2_werte = {}
modelle = {}

for grad in range(1, 5):
    # Koeffizienten berechnen
    p = np.polyfit(x, y, grad)
    modelle[grad] = p
    
    # Modell anwenden
    y_modell = np.polyval(p, x)
    
    # R²-Wert berechnen
    r2 = r2_score(y, y_modell)
    r2_werte[grad] = r2
    
    print(f"Polynomgrad {grad}: R² = {r2:.4f}")
```

Teilaufgabe 5:
```python
plt.figure()
plt.scatter(x, y, color='black', label='Messdaten 2021')

# x-Werte für glatte Kurven
x_plot = np.linspace(1, 12, 100)
for grad in range(1, 5):
    y_plot = np.polyval(modelle[grad], x_plot)
    plt.plot(x_plot, y_plot, 
             label=f'Grad {grad} (R² = {r2_werte[grad]:.3f})')

plt.xlabel('Monat')
plt.ylabel('Absatz von Bier [hl]')
plt.title('Vergleich verschiedener Polynomgrade - Bierstatistik 2021')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```
Teilaufgabe 6:
* Grad 1 (linear): R² sehr niedrig, kann die Saisonalität nicht erfassen
* Grad 2 (quadratisch): deutliche Verbesserung, erfasst den Grundtrend
* Grad 3 (kubisch): weitere Verbesserung, kann asymmetrische Muster erfassen
* Grad 4: nur geringfügige Verbesserung, Risiko von Overfitting
Empfehlung: Grad 3 bietet das beste Verhältnis zwischen Overfitting und Underfitting

Teilaufgabe 7:
```python
p_11 = np.polyfit(x, y, 11)
y_modell_11 = np.polyval(p_11, x)
r2_11 = r2_score(y, y_modell_11)

print(f"Polynomgrad 11: R² = {r2_11:.4f}")

# Vergleich: bestes Modell (Grad 3) vs. Overfitting (Grad 11)
y_plot_3 = np.polyval(modelle[3], x_plot)
y_plot_11 = np.polyval(p_11, x_plot)

# Visualisierung von Grad 11
plt.figure()
plt.scatter(x, y, color='black', label='Messdaten 2022')
plt.plot(x_plot, y_plot_3,  label=f'Grad 3 (R² = {r2_werte[3]:.3f})')
plt.plot(x_plot, y_plot_11, label=f'Grad 11 (R² = {r2_11:.3f})')
plt.xlabel('Monat')
plt.ylabel('Absatz von Bier [hl]')
plt.title('Overfitting-Beispiel: Grad 3 vs. Grad 11')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```
Erklärung zu Grad 11: Das Polynom 11. Grades hat einen perfekten R²-Wert, aber

* es schwingt stark zwischen den Datenpunkten und
* es würde neue Daten schlecht vorhersagen (Overfitting).

Bei 12 Datenpunkten ist ein Polynom 11. Grades fast eine Interpolation und
praktisch unbrauchbar für Prognosen.
````

```{admonition} Übung 12.5
:class: miniexercise
Laden Sie den Datensatz `stromverbrauch_hessen.csv` ([→ hier
Download](https://nextcloud.frankfurt-university.de/s/ddfDzAAnJtJ4FZQ)) herunter
und analysieren Sie die Entwicklung des Stromverbrauchs in Hessen von 2000 bis
2021.

Hinweis: Die CSV-Datei enthält Kommentarzeilen am Anfang. Verwenden Sie
`skiprows=4` beim Einlesen mit Pandas.

1. Datenexploration:
   - Laden Sie den Datensatz und verschaffen Sie sich einen Überblick.
   - In welchem Zeitraum liegen die Daten vor?
   - Welche Verbrauchergruppen sind enthalten?

2. Visualisierung:
   - Erstellen Sie ein Liniendiagramm, das die Entwicklung des
     Gesamtstromverbrauchs über die Jahre zeigt.
   - Erstellen Sie ein weiteres Diagramm, das die drei Verbrauchergruppen
     (Industrie, Verkehr, Haushalte etc.) separat in diesem Diagramm darstellt.

3. Trend-Analyse mit linearer Regression:
   - Berechnen Sie für jede der vier Kategorien (insgesamt, Industrie, Verkehr,
     Haushalte etc.) eine lineare Regressionsgerade.
   - Ermitteln Sie jeweils die Steigung und interpretieren Sie diese: Welche
     Verbrauchergruppe zeigt den stärksten Rückgang/Anstieg pro Jahr?
   - Berechnen Sie für jede Regression den R²-Wert. Welche Kategorie lässt sich
     am besten durch einen linearen Trend erklären?

4. Prognose:
   - Verwenden Sie die lineare Regression für den Gesamtstromverbrauch, um eine
     Prognose für das Jahr 2025 zu erstellen.
   - Diskutieren Sie: Ist diese Prognose realistisch? Was spricht dafür/dagegen?

5. Erweiterte Analyse:
   - Der Verkehrssektor zeigt starke Schwankungen. Testen Sie, ob ein Polynom 2.
     oder 3. Grades den Verkehrsstromverbrauch besser erklärt als eine Gerade.
   - Vergleichen Sie die R²-Werte und visualisieren Sie alle drei Modelle.
```

````{admonition} Lösung
:class: minisolution, toggle
1\. Datenexploration
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Datenexploration
data = pd.read_csv('data/stromverbrauch_hessen.csv', skiprows=4, index_col=0)
data.info()
data.describe()
```

Zeitraum: 2000 bis 2021
Verbrauchergruppen:

* insgesamt
* Industrie
* Verkehr
* Haushalte, Gewerbe, Handel, Dienstleistungen und übrige Verbraucher

2\. Visualisierung
```python
# Gesamtstromverbrauch
plt.figure()
plt.plot(data.index, data['insgesamt'])
plt.title('Entwicklung des Gesamtstromverbrauchs in Hessen (2000-2021)')
plt.xlabel('Jahr')
plt.ylabel('Stromverbrauch [GWh]')
plt.grid(True, alpha=0.3)

# Verbrauchergruppen separat
plt.figure()
plt.plot(data.index, data['Industrie'], label='Industrie')
plt.plot(data.index, data['Verkehr'], label='Verkehr')
plt.plot(data.index, data['Haushalte, Gewerbe, Handel, Dienstleistungen und übrige Verbraucher'], label='Haushalte, Gewerbe etc.')
plt.title('Stromverbrauch nach Verbrauchergruppen')
plt.xlabel('Jahr')
plt.ylabel('Stromverbrauch [GWh]')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

3\. Trend-Analyse mit linearer Regression
```python
# Vorbereitung der Daten
x = range(2000, 2022) 
verbrauchergruppen = data.columns


regressionen = {}

for gruppe in verbrauchergruppen:
    y = data[gruppe]
    
    # Lineare Regression
    p = np.polyfit(x, y, 1)
    y_prognose = np.polyval(p, x)
    r2 = r2_score(y, y_prognose)
    
    # Steigung pro Jahr (p[0] ist Steigung, entspricht Änderung pro Jahr)
    steigung_pro_jahr = p[0]
    
    # Ausgabe der Ergebnisse
    print(f"{gruppe}:")
    print(f"  Steigung: {steigung_pro_jahr:.1f} GWh/Jahr")
    print(f"  R²-Wert: {r2:.4f}")
    print()
```
insgesamt: Steigung: -59.2 GWh/Jahr und R²-Wert: 0.0724<br>
Industrie: Steigung: -59.7 GWh/Jahr und R²-Wert: 0.4206<br>
Verkehr: Steigung: -4.5 GWh/Jahr und R²-Wert: 0.0268<br>
Haushalte etc.: Steigung: 4.9 GWh/Jahr und R²-Wert: 0.0006<br>

Den stärksten Rückgang hat die Gruppe der Industrie (-59.7 GWh/Jahr), den
stärksten Anstieg die Haushalte (+ 4.9 GWh/Jahr). Am ehesten lässt sich der
Stromverbrauch der Industrie mit einem linearen Modell erklären (R² = 0.4206).

4\. Prognose
```python
p = np.polyfit(x, data['insgesamt'], 1)
gesamtverbrauch_2025 = np.polyval(p, 2025)
print(f"Gesamtverbrauch für 2025: {gesamtverbrauch_2025:.1f} GWh")
```
Gesamtverbrauch für 2025: 34963.5 GWh

Der R²-Wert von 0.0724 für den Gesamtverbrauch ist schlecht, daher ist diese
Prognose fragwürdig.

5\. Erweiterte Analyse
```python
verkehr = data['Verkehr']

# Teste verschiedene Polynomgrade
grade = [1, 2, 3]
verkehr_modelle = {}

plt.figure()
plt.scatter(x, verkehr, label='Verkehrsdaten')

x_plot = np.linspace(2000, 2022, 100)
for grad in grade:
    p = np.polyfit(x, verkehr, grad)
    y_prognose = np.polyval(p, x)
    r2 = r2_score(verkehr, y_prognose)
    print(f'R2-Score für Grad {grad} = {r2:.2f}')
    verkehr_modelle[grad] = {'koeffizienten': p, 'r2': r2}
    
    # Visualisierung des Regressionspolynoms
    y_plot = np.polyval(p, x_plot)
    plt.plot(x_plot, y_plot, label=f'Grad {grad} (R² = {r2:.3f})')

plt.xlabel('Jahr')
plt.ylabel('Stromverbrauch Verkehr [GWh]')
plt.title('Verkehrssektor: Vergleich verschiedener Regressionsmodelle')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```
R2-Score für Grad 1 = 0.03<br>
R2-Score für Grad 2 = 0.04<br>
R2-Score für Grad 3 = 0.18<br>

Auch wenn der R²-Score für das Polynom 3. Grades besser ist als der für Grad 1
oder 2, zeigt die Visualisierung, dass das kubische Modell ungeeignet ist. Das
lokale Minimum liegt ungefähr im Jahr 2005, das lokale Maximum ungefähr 2025.
Damit muss das Polynom für Jahre vor 2000 immer weiter steigen. Demnach wäre der
Stromverbrauch für den Verkehrssektor umso höher, je weiter wir in die
Vergangenheit zurückgehen, was nicht realistisch ist. Entweder wir verwerfen das
Modell oder schränken es auf den betrachteten Zeitraum 2000 bis 2022 ein.
````
