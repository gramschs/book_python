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

# 10.1 Series und DataFrame

Einfache Listen reichen nicht aus, um größere Datenmengen oder Tabellen
effizient zu speichern. Dazu benutzen Data Scientists die Datentypen `Series`
oder `DataFrame` aus dem Modul Pandas. Daher werden wir uns in diesem Kapitel
mit diesen beiden Datentypen beschäftigen. Darüber hinaus lernen wir das häufig
verwendete Datenformat `csv` kennen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können **Pandas** mit der üblichen Abkürzung pd importieren.
* Sie können aus einer Liste das Datenobjekt **Series** erzeugen.
* Sie kennen das **csv-Dateiformat**.
* Sie können eine csv-Datei mit **read_csv()** einlesen.
* Sie konnen mit **.info()** sich einen Überblick über die importierten Daten verschaffen.
```

## Import von pandas

Pandas ist eine Bibliothek zur Verarbeitung und Analyse von Daten in Form von
Datenreihen und Tabellen. Die beiden grundlegenden Datenstrukturen sind Series
und DataFrame. Dabei wird **Series** für Datenreihen genommen, also sozusagen
die Verallgemeinerung von Vektoren bzw. eindimensionalen Arrays. Der Datentyp
**DataFrame** repräsentiert Tabellen, also sozusagen Matrizen bzw.
verallgemeinerte zweidimensionale Arrays.

Um das Modul pandas benutzen zu können, müssen wir es zunächst importieren. Es
ist üblich, dabei dem Modul die Abkürzung **pd** zu geben, damit wir nicht immer
pandas schreiben müssen, wenn wir eine Funktion aus dem pandas-Modul benutzen.

```{code-cell} ipython3
import pandas as pd # kürze das Modul pandas als pd ab, um Schreibarbeit zu sparen
```

## Series aus Liste erzeugen

Der Datentyp Series speichert Datenreihen. Liegt beispielsweise eine Reihe von
Daten vor, die in einer Variable vom Datentyp Liste gespeichert ist, so wird
über die Methode `pd.Series(liste)` ein neues Series-Objekt erzeugt, dass die
Listenelemente enthält. Im folgenden Beispiel haben wir Altersangaben in einer
Liste, also `[25, 22, 43, 37]` und initialisieren über `pd.Series()` die
Variable `alter`:

```{code-cell} ipython3
alter = pd.Series([25, 22, 43, 37])
print(alter)
```

Was ist aber jetzt der Vorteil von Pandas? Warum nicht einfach bei der Liste
bleiben oder aber, wenn Performance wichtig sein sollte, ein eindimensionales
Numpy-Array nehmen? Der wichtigste Unterschied ist der **Index**.

Bei einer Liste oder einem Numpy-Array ist der Index implizit definiert. Damit
ist gemeint, dass bei der Initialisierung automatisch ein Index 0, 1, 2, 3, ...
angelegt wird. Wenn bei einer Liste `l = [25, 22, 43, 37]` auf das zweite
Element zugegriffen werden soll, dann verwenden wir den Index 1 (zur Erinnerung:
Python zählt ab 0) und schreiben

```{code-cell} ipython3
l = [25, 22, 43, 37]
print("2. Element der Liste: ", l[1])
```

Die Datenstruktur Series ermöglich es aber, einen *expliziten Index* zu setzen.
Über den optionalen Parameter `index=` speichern wir als Zusatzinformation noch
ab, von welcher Person das Alter abgefragt wurde. In dem Fall sind es die vier
Personen Alice, Bob, Charlie und Dora.

```{code-cell} ipython3
alter = pd.Series([25, 22, 43, 30], index=["Alice", "Bob", "Charlie", "Dora"])
print(alter)
```

Jetzt ist auch klar, warum beim ersten Mal, als wir `print(alter)` ausgeführt
haben, die Zahlen 0, 1, 2, 3 ausgegeben wurden. Zu dem Zeitpunkt hatte das
Series-Objekt noch einen impliziten Index wie eine Liste. Was noch an
Informationen ausgegeben wird, ist das Attribut `dtype`. Darin gespeichert ist
der Datentyp der gespeicherten Werte. Auf dieses Attribut kann auch direkt mit
dem Punktoperator zugegegriffen werden.

```{code-cell} ipython3
print(alter.dtype)
```

Offensichtlich sind die gespeicherten Werte Integer.

```{admonition} Mini-Übung
:class: miniexercise 
Erzeugen Sie ein Series-Objekt mit den Wochentagen als Index und der Anzahl der
Vorlesungs/Übungs-Stunden an diesem Wochentag.
```

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
stundenplan = pd.Series([4, 0, 4, 6, 8], index=["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"])
print(stundenplan)
```
````

+++

## DataFrame für Tabellen

Bei Auswertung von Messungen ist aber der häufigste Fall der, dass Daten in Form
einer Tabelle vorliegen. Ein DataFrame-Objekt entspricht einer Tabelle, wie man
sie beispielsweise von Excel, LibreOffice oder Numbers kennt. Sowohl Zeile als
auch Spalten sind indiziert. Typischerweise werden die Daten in der Tabelle
zeilenweise angeordnet. Damit ist gemeint, dass jede Zeile einen Datensatz
darstellt und die Spalten die Eigenschaften speichern.

Ein DataFrame kann direkt über mehrere Pandas-Series-Objekte oder verschachtelte
Listen erzeugt werden. Da es in der Praxis nur selten vorkommt und nur für sehr
kleine Datenmengen praktikabel ist, Daten händisch zu erfassen, fokussieren wir
gleich auf die Erzeugung von DataFrame-Objekten aus einer Datei.

## Import von Tabellen

Tabellen werden oft in demjenigen Dateiformat abgespeichert, das die jeweilige
Tabellenkalkulationssoftware Excel, Numbers oder OpenOfficeCalc als Standard
vorgibt. Wir betrachten in dieser Vorlesung aber primär Tabellen, die in einem
offenen Datenformat vorliegen und damit unabhängig von der verwendeten Software
und dem verwendeten Betriebssystem sind. Der Import von Excel wird kurz
gestreift.

### Import von Tabellen im csv-Format

Das **Dateiformat csv** speichert Daten zeilenweise ab. Dabei steht csv für
"comma-separated values". Die Trennung der Spalten erfolgt durch ein
Trennzeichen, normalerweise durch das Komma. Im deutschsprachigen Raum wird
gelegentlich ein Semikolon verwendet, weil Dezimalzahlen das Komma zum Abtrennen
der Nachkommastellen verwenden.

Um Tabellen im csv-Format einzulesen, bietet Pandas eine eigene Funktion namens
`read_csv` an (siehe
[Dokumentation/read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)).
Wird diese Funktion verwendet, um die Daten zu importieren, so wird automatisch
ein DataFrame-Objekt erzeugt. Beim Aufruf der Funktion wird der Dateiname
übergeben, aber beispielweise könnte auch ein anderes Trennzeichen eingestellt werden.

Am besten sehen wir uns die Funktionsweise von `read_csv` an einem Beispiel an.
Sollten Sie mit einem lokalen JupyterNotebook arbeiten, laden Sie bitte die
Datei
[`bundesliga_top7_offensive.csv`](https://nextcloud.frankfurt-university.de/s/yJjkkMSkWqcSxGL)
herunter und speichern Sie sie in denselben Ordner, in dem auch dieses
JupyterNotebook liegt. Die csv-Datei stammt von
[Kaggle](https://www.kaggle.com/rajatrc1705/bundesliga-top-7-teams-offensive-stats?select=bundesliga_top7_offensive.csv).
Wie der Name schon verrät, sind darin Spielerdaten zu den Top7-Fußballvereinen
der Bundesligasaison 2020/21 enthalten.

Führen Sie dann anschließend die folgende Code-Zelle aus.

```{code-cell} ipython3
import pandas as pd
data = pd.read_csv('bundesliga_top7_offensive.csv')
```

Es erscheint keine Fehlermeldung, aber den Inhalt der geladenen Datei sehen wir
trotzdem nicht. Dazu verwenden wir die Methode `.head()`.

```{code-cell} ipython3
data.head()
```

Die Methode `.head()` zeigt uns die ersten fünf Zeilen der Tabelle an. Wenn wir
beispielsweise die ersten 10 Zeilen anzeigen lassen wollen, so verwenden wir die
Methode `.head(10)`mit dem Argument 10.

```{code-cell} ipython3
data.head(10)
```

Offensichtlich wurde beim Import der Daten wieder ein impliziter Index 0, 1, 2,
usw. gesetzt. Das ist nicht weiter verwunderlich, denn Pandas kann nicht wissen,
welche Spalte wir als Index vorgesehen haben. Und manchmal ist ein automatisch
erzeugter impliziter Index auch nicht schlecht. In diesem Fall würden wir aber
gerne als Zeilenindex die Namen der Spieler verwenden. Daher modifizieren wir
den Befehl mit `index_col=`. Die Namen stehen in der 1. Spalte, was in
Python-Zählweise einer 0 entspricht.

```{code-cell} ipython3
data = pd.read_csv('bundesliga_top7_offensive.csv', index_col=0)
data.head(10)
```

### Import von Tabellen im xlsx-Format

Eine sehr bekannte Tabellenkalkulationssoftware ist Excel von Microsoft. Excel
bringt sein eigenens proprietäres Datenformat mit, in der Regel erkennbar an der
Dateiendung `.xlsx`. Laden Sie sich den Datensatz zu den Top7-Bundesligavereinen
als Excel-Datei
[bundesliga_top7_offensive.xlsx](https://nextcloud.frankfurt-university.de/s/wogabyEQbkSTtpm)
herunter.

```{code-cell} ipython3
data = pd.read_excel('bundesliga_top7_offensive.xlsx', index_col=0)
data.head(5)
```

Vermutlich erhalten Sie zunächst eine Fehlermeldung: `Missing optional
dependency 'openpyxl'.  Use pip or conda to install openpyxl.` Falls das der
Fall sein sollte und Sie interessiert daran sind, Excel-Dateien lesen und
schreiben zu können, installieren Sie bitte das Modul `openpyxl` mit `!conda
install openpyxl` oder `!pip install openpyxl` nach. In dieser Vorlesung
verwenden wir nur csv-Dateien, so dass ein Nachinstallieren für die
Vorlesung/Übung nicht notwendig ist.

## Übersicht verschaffen mit info

Das obige Beispiel zeigt uns zwar nun die ersten 10 Zeilen des importierten
Datensatzes, aber wie viele Daten insgesamt enthalten sind oder welche Vereine
noch kommen, können wir mit der `.head()`-Methode nicht erfassen. Dafür stellt
Pandas die Methode `.info()` zur Verfügung. Probieren wir es einfach aus.

```{code-cell} ipython3
data.info()
```

Mit `.info()` erhalten wir eine Übersicht, wie viele Spalten es gibt und auch
die Spaltenüberschriften werden aufgelistet. Dabei sind Überschriften wie `Name`
selbsterklärend, aber was `xG` bedeutet, erschließt sich nicht von selbst. Dazu
brauchen wir mehr Informationen von den Autor:innen der Daten.

Weiterhin entnehmen wir der Ausgabe von `.info()`, dass in jeder Spalte 177
Einträge sind, die 'non-null' sind. Damit ist gemeint, dass diese Zellen beim
Import nicht leer waren. Zudem wird bei jeder Spalte noch der Datentyp
angegeben. Für die Namen, die als Strings gespeichert sind, wird der allgemeine
Datentyp 'object' angegeben. Beim Alter/Age wurden korrektweise Integer erkannt
und die mittlere erwartete Anzahl von Toren pro Spiel 'xG' (= expected number of
goals from the player in a match) wird als Float angegeben.
