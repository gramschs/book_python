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
Gegeben ist der folgende Code mit Zeilennummern, um Messdaten zu visualisieren. Suchen Sie die darin enthaltenen Fehler. Korrigieren Sie anschließend das Programm.
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
14 plt.titel('Messdaten');
```
````

````{admonition} Lösung
:class: miniexercise, toggle
* Zeile 6: Listen dürfen nicht quadriert werden.
* Zeile 9: Der Aufruf plt.figure() fürht zu einer Fehlermeldung, da Matplotlib nicht importiert wurde.
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
plt.title('Messdaten');
```

Bemerkung: Hätten wir nicht eine Liste, sondern NumPy-Arrays genommen, um die Messwerte zu speichern, hätte die Quadratur funktioniert. Die folgende Alternative korrigiert auch alle Fehler.
```python
import matplotlib.pyplot as plt
import numpy as np

# Datenimport Messdaten
x = np.array([-20, -15, -10, -5, 0, 5])
y = np.array([152.38, 124.43, 88.91, 37.43, 5.52, -27.41])
    
# Parabel durch die Messdaten
y_parabel = x**2
   
# Plot der Messdaten mit zusätzlicher Parabel
plt.figure()
plt.scatter(x,y)
plt.plot(x, y_parabel)
plt.xlabel('Temperatur')
plt.ylabel('Materialeigenschaft')
plt.title('Messdaten');
```
````

```{admonition} Übung 12.2
:class: miniexercise
Laden Sie den Datensatz `studierendenzahlen_frankfurt_uas.csv` ([→ hier Download](https://nextcloud.frankfurt-university.de/s/MzxHw2rDRdx5eRA)) herunter und
importieren Sie ihn mit Pandas. Die ersten drei Zeilen sind Kommentare und
müssen daher mit dem Argument `skiprows=3` übersprungen werden. 

1. Lassen Sie die Studierendenzahlen männlich und weiblich visualisieren.
2. Berechne Sie eine Regressionsgerade jeweils für die Studierendenzahlen
   weiblich und männlich. Wächst die Anzahl der männlichen oder der weiblichen
   Studierenden schneller?
3. Lassen Sie die Regressionsgeraden zusammen mit den Studierendenzahlen
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
Der Index kann auf die erste Spalte gesetzt werden, muss aber nicht. Die Visualisierung als Streudiagramm erfolgt mit folgenden Python-Code:
```python
# Extraktion der Daten aus der Tabelle
y_maennlich = studizahlen.loc[:,'männlich']
y_weiblich = studizahlen.loc[:, 'weiblich']
semester = studizahlen.index

# Streudiagramm
plt.figure()
plt.scatter(semester, y_maennlich)
plt.scatter(semester, y_weiblich)
plt.xticks(rotation = 45, ha='right')
plt.xlabel('Semester')
plt.ylabel('Anzahl Studierende')
plt.title('Entwicklung der Studierendenzahlen Frankfurt UAS');
```
Für die Regressionsgeraden brauchen wir Zahlen als Ursache, nicht Semester. Daher basteln wir mit der `range`-Funktion x-Werte von 0 bis zur Anzahl der Semester. Danach wenden wir `polyfit` mit Grad 1 an und lassen die beiden Steigungen ausgeben. 
```python3
anzahl_semester = len(semester)
x = range(anzahl_semester)

p_maennlich = np.polyfit(x, y_maennlich, 1)
p_weiblich  = np.polyfit(x, y_weiblich, 1)

print(f'Steigung bei der Entwicklung Studenten: {p_maennlich[0]:.2f}')
print(f'Steigung bei der Entwicklung Studentinnen: {p_weiblich[0]:.2f}')
```
Die Anzahl der weiblichen Studierenden wächst schneller als die der männlichen Studierenden.

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
plt.title('Entwicklung der Studierendenzahlen Frankfurt UAS');
```
````

```{admonition} Übung 12.3
:class: miniexercise
Laden Sie die Biersteuerstatistik
([Download](https://nextcloud.frankfurt-university.de/s/Ejc2LFEW3Hz3mA9)) herunter.
1. Importieren Sie die Daten mit Pandas (8 Zeilen müssen Úbersprungen werden).
Lassen Sie sich einen Überblick anzeigen. Was enthält die Tabelle?
2. Filtern Sie die Tabelle nach den Jahren 2020, 2021 und 2022 lassen Sie den
Absatz von Bier in Hektolitern pro Monat visualisieren.
3. Stellen Sie eine Vermutung an. Durch welches Regressionspolynom könnte der
Absatz von Bier pro Monat am besten erklärt werden?
4. Stellen Sie das Regressionspolynom für 2022 auf und visualisieren Sie es
   zusammen mit den Messwerten.
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
    daten_pro_jahr = daten.loc[ daten.loc[:, 'Jahr'] == jahr, :]
    x = daten_pro_jahr.loc[:, 'Monat']
    y = daten_pro_jahr.loc[:, 'Absatz von Bier [hl]'] 
    plt.scatter(x,y, label=str(jahr))
plt.legend()
plt.xticks(rotation = 45, ha='right')
plt.xlabel('Monat')
plt.ylabel('Absatz von Bier [hl]')
plt.title('Bierstatistik');
```

Aufgrund der Visualisierung entscheiden wir uns für eine Annäherung durch eine
Regressionsparabel.

```python
import numpy as np

data_2022 = data.loc[data['Jahr'] == 2022, :]

x = range(1, 13)
y = data_2022.loc[:, 'Absatz von Bier [hl]']

p2022 = np.polyfit(x, y, 2)

x_modell = np.linspace(1, 12)
y_modell = np.polyval(p2022, x_modell)

plt.figure()
plt.scatter(x, y)
plt.plot(x_modell, y_modell)
plt.xlabel('Monat')
plt.ylabel('Absatz von Bier [hl]')
plt.title('Bierstatistik für das Jahr 2022');
```
````
