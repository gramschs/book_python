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
effizient zu speichern. Dazu benutzen Data Scientists Pandas. Pandas ist eine
Bibliothek zur Verarbeitung und Analyse von Daten in Form von Datenreihen und
Tabellen. Die beiden grundlegenden Datenstrukturen sind Series und DataFrame.
Dabei wird **Series** für Datenreihen genommen und ist damit die
Verallgemeinerung von Vektoren bzw. eindimensionalen Arrays. Die Datenstruktur
**DataFrame** repräsentiert Tabellen, also sozusagen Matrizen bzw.
verallgemeinerte zweidimensionale Arrays.

Daher werden wir uns in diesem Kapitel mit diesen beiden Datenstrukturen
beschäftigen. Darüber hinaus lernen wir das häufig verwendete Datenformat `csv`
kennen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können **Pandas** mit der üblichen Abkürzung **pd** importieren.
* Sie können aus einer Liste das Datenobjekt **Series** erzeugen.
* Sie kennen das **csv-Dateiformat**.
* Sie können eine csv-Datei mit **read_csv()** einlesen.
* Sie können mit **.info()** sich einen Überblick über die importierten Daten
  verschaffen.
```

## Series aus Liste erzeugen

Um das Modul pandas benutzen zu können, müssen wir es zunächst importieren. Es
ist üblich, dabei dem Modul die Abkürzung **pd** zu geben, damit wir nicht immer
pandas schreiben müssen, wenn wir eine Funktion aus dem pandas-Modul benutzen.

```{code-cell} ipython3
import pandas as pd # kürze das Modul pandas als pd ab, um Schreibarbeit zu sparen
```

Die Datenstruktur Series speichert Datenreihen. Liegt beispielsweise eine Reihe von
Daten vor, die in einer Variable vom Datentyp Liste gespeichert ist, so wird
über die Methode `pd.Series(liste)` ein neues Series-Objekt erzeugt, das die
Listenelemente enthält. Im folgenden Beispiel haben wir Altersangaben in einer
Liste, also `[25, 22, 43, 37]` und initialisieren über `pd.Series()` die
Variable `alter`:

```{code-cell} ipython3
alter = pd.Series([25, 22, 43, 37])
print(alter)
```

Was ist aber jetzt der Vorteil von Pandas? Warum nicht einfach bei der Liste
bleiben oder aber, wenn Performance wichtig sein sollte, ein eindimensionales
Numpy-Array nehmen? Der wichtigste Unterschied zwischen der Datenstruktur Series
und einer Liste ist der **Index**.

Bei einer Liste oder einem Numpy-Array ist der Index *implizit* definiert. Damit
ist gemeint, dass bei der Initialisierung automatisch ein Index 0, 1, 2, 3, ...
angelegt wird. Wenn bei einer Liste `liste = [25, 22, 43, 37]` auf das zweite
Element zugegriffen werden soll, dann verwenden wir den Index 1 (zur Erinnerung:
Python zählt ab 0) und schreiben

```{code-cell}
liste = [25, 22, 43, 37]
print(f'2. Element der Liste: {liste[1]}')
```

Die Datenstruktur Series ermöglich es aber, einen *expliziten Index* zu setzen.
Über den optionalen Parameter `index=` speichern wir als Zusatzinformation noch
ab, von welcher Person das Alter abgefragt wurde. In dem Fall sind es die vier
Personen Alice, Bob, Charlie und Dora.

```{code-cell}
alter = pd.Series([25, 22, 43, 30], index=["Alice", "Bob", "Charlie", "Dora"])
print(alter)
```

Jetzt ist auch klar, warum beim ersten Mal, als wir `print(alter)` ausgeführt
haben, die Zahlen 0, 1, 2, 3 ausgegeben wurden. Zu dem Zeitpunkt hatte das
Series-Objekt noch einen impliziten Index wie eine Liste.

Wenden wir uns nun der letzten Zeile der Ausgabe zu: `dtype: int64`. Für das
Series-Objekt `alter` wird automatisch der Datentyp der enthaltenen Werte
ermittelt. In unserem Fall haben wir das Alter als vier Integers gespeichert,
weshalb `int64` als Attribut `dtype` gespeichert wird. Auf dieses Attribut kann
auch direkt mit dem Punktoperator zugegegriffen werden.

```{code-cell}
print(alter.dtype)
```

```{admonition} Mini-Übung
:class: miniexercise 
Erzeugen Sie ein Series-Objekt mit den Wochentagen als Index und der Anzahl der
Vorlesungs/Übungs-Stunden an diesem Wochentag.
```

```{code-cell}
# Hier Ihr Code:
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
stundenplan = pd.Series([4, 0, 4, 6, 8], index=["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"])
print(stundenplan)
```
````

## DataFrames für Tabellen erzeugen

Bei Auswertung von Messungen kommt es häufig vor, dass die Daten in Form einer
Tabelle vorliegen. Ein DataFrame-Objekt entspricht einer Tabelle, wie man sie
beispielsweise von Excel, LibreOffice oder Numbers kennt. Sowohl die Zeilen als
auch die Spalten haben einen Index. Typischerweise werden die Daten in der
Tabelle zeilenweise angeordnet. Damit ist gemeint, dass jede Zeile einen
Datensatz darstellt und die Eigenschaften der Daten als Spalte gespeichert
werden.

Bevor wir uns dem Import von Tabellen widmen, schauen wir uns kurz an, wie ein
DataFrame-Objekt direkt erstellt werden kann. Dies ist besonders nützlich, wenn
Sie kleinere Datensätze aus Berechnungen oder Messreihen zusammenstellen
möchten.

Die einfachste Methode ist die Erstellung aus einem Dictionary. Dabei entspricht
jeder Schlüssel einer Spaltenüberschrift und die zugehörigen Werte bilden die
Spalteninhalte:

```{code-cell}
# Messdaten von Zugversuchen verschiedener Materialien
messdaten = {
    'Material': ['Stahl', 'Aluminium', 'Kupfer', 'Messing'],
    'Zugfestigkeit_MPa': [400, 310, 220, 380],
    'Streckgrenze_MPa': [250, 280, 70, 200],
    'Bruchdehnung_Prozent': [25, 12, 45, 15]
}

daten_zugversuch = pd.DataFrame(messdaten)
print(daten_zugversuch)
```

Sie können auch explizit einen Index festlegen, beispielsweise die
Probennummern:

```{code-cell}
daten_zugversuch = pd.DataFrame(messdaten, index=['Probe_01', 'Probe_02', 'Probe_03', 'Probe_04'])
print(daten_zugversuch)
```

Alternativ können Sie ein DataFrame aus mehreren Series-Objekten erstellen:

```{code-cell}
materialien = pd.Series(['Stahl', 'Aluminium', 'Kupfer'], name='Material')
zugfestigkeit = pd.Series([400, 310, 220], name='Zugfestigkeit_MPa')

df_aus_series = pd.DataFrame({'Material': materialien, 'Zugfestigkeit': zugfestigkeit})
print(df_aus_series)
```

In der Praxis werden wir DataFrames jedoch meist aus Dateien importieren, da
größere Datensätze selten manuell erfasst werden. Dies betrachten wir im
nächsten Abschnitt.

## Import von Tabellen aus csv-Dateien

Tabellen werden oft in demjenigen Dateiformat abgespeichert, das die jeweilige
Tabellenkalkulationssoftware Excel, Numbers oder OpenOfficeCalc als Standard
vorgibt. Wir betrachten in dieser Vorlesung aber primär Tabellen, die in einem
offenen Datenformat vorliegen und damit unabhängig von der verwendeten Software
und dem verwendeten Betriebssystem sind.

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

Betrachten wir die Funktionsweise von `read_csv` mit einem Beispiel. Sollten Sie
mit einem lokalen JupyterNotebook arbeiten, laden Sie bitte die Datei
{download}`Download bundesliga_top7_offensive.csv
<https://nextcloud.frankfurt-university.de/s/yJjkkMSkWqcSxGL>` herunter und
speichern Sie sie in denselben Ordner, in dem auch dieses JupyterNotebook liegt.
Die csv-Datei stammt von
[Kaggle](https://www.kaggle.com/rajatrc1705/bundesliga-top-7-teams-offensive-stats?select=bundesliga_top7_offensive.csv).
Wie der Name schon verrät, sind darin Spielerdaten zu den Top7-Fußballvereinen
der Bundesligasaison 2020/21 enthalten.

Führen Sie dann anschließend die folgende Code-Zelle aus.

```{code-cell}
import pandas as pd
data = pd.read_csv('bundesliga_top7_offensive.csv')
```

Es erscheint keine Fehlermeldung, aber den Inhalt der geladenen Datei sehen wir
trotzdem nicht. Dazu verwenden wir die Methode `.head()`.

```{code-cell}
data.head()
```

Die Methode `.head()` zeigt uns die ersten fünf Zeilen der Tabelle an. Wenn wir
beispielsweise die ersten 10 Zeilen anzeigen lassen wollen, so verwenden wir die
Methode `.head(10)`mit dem Argument 10.

```{code-cell}
data.head(10)
```

Offensichtlich wurde beim Import der Daten wieder ein impliziter Index 0, 1, 2,
usw. gesetzt. Das ist nicht weiter verwunderlich, denn Pandas kann nicht wissen,
welche Spalte wir als Index vorgesehen haben. Und manchmal ist ein automatisch
erzeugter impliziter Index auch nicht schlecht. In diesem Fall würden wir aber
gerne als Zeilenindex die Namen der Spieler verwenden. Daher modifizieren wir
den Befehl mit `index_col=0`. Die Namen stehen in der 1. Spalte, was in
Python-Zählweise einer 0 entspricht.

```{code-cell}
data = pd.read_csv('bundesliga_top7_offensive.csv', index_col=0)
data.head(10)
```

````{admonition} Import von Tabellen im xlsx-Format
:class: warning
Eine sehr bekannte Tabellenkalkulationssoftware ist Excel von Microsoft. Excel
bringt sein eigenens proprietäres Datenformat mit, in der Regel erkennbar an der
Dateiendung `.xlsx`. Der Befehl zum Import einer Excel-Datei {download}`Download bundesliga_top7_offensive.xlsx
<https://nextcloud.frankfurt-university.de/s/wogabyEQbkSTtpm>` lautet:

```python
data = pd.read_excel('bundesliga_top7_offensive.xlsx', index_col=0)
data.head(5)
```

Vermutlich erhalten Sie zunächst eine Fehlermeldung: `Missing optional
dependency 'openpyxl'.  Use pip or conda to install openpyxl.` Falls das der
Fall sein sollte und Sie interessiert daran sind, Excel-Dateien lesen und
schreiben zu können, installieren Sie bitte das Modul `openpyxl` mit `!conda
install openpyxl` oder `!pip install openpyxl` nach.
````

## Übersicht verschaffen mit info

Das obige Beispiel zeigt uns zwar nun die ersten 10 Zeilen des importierten
Datensatzes an, aber wie viele Daten insgesamt enthalten sind oder welche
Vereine noch kommen, können wir mit der `.head()`-Methode nicht erfassen. Dafür
stellt Pandas die Methode `.info()` zur Verfügung. Probieren wir es einfach aus.

```{code-cell}
data.info()
```

Mit `.info()` erhalten wir eine Übersicht, wie viele Spalten es gibt und auch
die Spaltenüberschriften werden aufgelistet. Dabei sind Überschriften wie `Name`
selbsterklärend, aber was `xG` bedeutet, erschließt sich nicht von selbst. Dazu
brauchen wir mehr Informationen von den Autor:innen der Daten.

Weiterhin entnehmen wir der Ausgabe von `.info()`, dass in jeder Spalte 177
Einträge sind, die `non-null` sind. Damit ist gemeint, dass diese Zellen beim
Import nicht leer waren. Zudem wird bei jeder Spalte noch der Datentyp
angegeben. Für die Namen, die als Strings gespeichert sind, wird der allgemeine
Datentyp `object` angegeben. Beim Alter/Age wurden korrektweise Integers erkannt
und die mittlere erwartete Anzahl von Toren pro Spiel 'xG' (= expected number of
goals from the player in a match) wird als Float angegeben.

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir die beiden wichtigsten Pandas-Datenstrukturen
kennengelernt: Series und DataFrame. Darüber hinaus haben wir uns damit
beschäftigt, wie wir mir `.info()` und `.head()` uns einen ersten Überblick über
die Daten verschaffen können. Wie wir auf Zeilen und Spalten zugreifen, lernen
wir im nächsten Kapitel.
