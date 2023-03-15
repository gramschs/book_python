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

# 9.2 Arbeiten mit Tabellendaten

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie können auf ganze Zeilen und Spalten zugreifen:
  * Zugriff auf eine einzelne Zeile oder Spalte, indem ein Index spezifiziert wird
  * Zugriff auf mehrere zusammenhängende Zeilen oder Spalten (Slice) 
  * Zugriff auf mehrere unzusammenhängende Zeilen oder Spalten (Selektion)
* Sie können auf einzelne oder mehrere Zellen der Tabelle zugreifen.
* Sie können ein DataFrame-Objekt nach einer Eigenschaft filtern.
```

## Zugriff auf Zeilen

Als erstes möchten wir ganze Zeilen der Tabelle lesen. Dazu verwenden wir das
Attribut `.loc` mit passenden Indizes. 

Für die folgenden Demonstrationen wollen wir wiederum die Spielerdaten der
Top7-Fußballvereine der Bundesligasaison 2020/21 verwenden. Importieren Sie
bitte vorab die Daten und verwenden Sie die 1. Spalte (= Namen) als Zeilenindex. 

```{code-cell} ipython3
import pandas as pd
data = pd.read_csv('bundesliga_top7_offensive.csv', index_col=0)
data.head(10)
```

### Einzelne Zeile

Uns interessieren die Spielerdaten von Joshua Kimmich näher. Um eine ganze Zeile
aus der Tabelle herauszugreifen, verwenden wir das Attribut `.loc[zeilenindex]`
und geben in eckigen Klammern den Index der Zeile an, die wir betrachten wollen.
Da wir beim Import die Namen als Zeileindex gesetzt haben, lautet der Zugriff
also wie folgt:

```{code-cell} ipython3
zeile = data.loc['Joshua Kimmich']
print(zeile)
```

### Zusammenhängende Zeilen: Slicing

Wenn wir auf mehrere Zeilen gleichzeitig zugreifen wollen, gibt es zwei
Möglichkeiten:

1. Die Zeilen folgen direkt aufeinander, sind also zusammenhängend.
2. Zwischen den einzelnen Zeilen sind Lücken. 

Als erstes betrachten wir zusammenhängende Zeilen. Der Zugriff auf
zusammenhängende Bereiche wird in der Informatik **Slicing** genannt. Bei der
Angabe des Bereiches gibt man den Anfangsindex gefolgt von einem Doppelpunkt an
und dann den Endindex der letzten Zeile, die "herausgeschnitten" werden soll.

```{code-cell} ipython3
zeilen_slice = data.loc['Joshua Kimmich' : 'Alphonso Davies']
print(zeilen_slice)
```

Beim Slicing können wir den Angangsindex oder den Endindex oder sogar beides
weglassen. Wenn wir den Anfangsindex weglassen, fängt Pandas bei der ersten
Zeile an. Lassen wir den Endindex weg, geht der Slice automatisch bis zum Ende. 

Im folgenden Beispiel startet der Slice bei 'Robert Lewandowski'und geht bis zur
letzten Zeile. Obwohl nicht alle Zeilendargestellt werden, erkennen wir das an
der Anzahl der Zeilen: 173 rows (und 15 Spalten columns). Zur Erinnerung, es
sind insgesamt 177 Zeilen.

```{code-cell} ipython3
data_slice_from_lewandowski = data.loc['Robert Lewandowski': ]
print(data_slice_from_lewandowski)
```

### Selektion unzusammenhängender Zeilen per Liste

Soll auf mehrere Zeilen zugegriffen werdenn, die nicht zusammenhängen, so können
wir eine Liste mit den Zeilenindizes übergeben. 

```{code-cell} ipython3
zeilen_multiple = data.loc[ ['Manuel Neuer', 'Robert Lewandowski', 'Alphonso Davies'] ]
print(zeilen_multiple)
```

## Zugriff auf Spalten

Auf Spalten können wir zugreifen, indem wir `.loc` mit zwei Argumenten benutzen.
Dann steht das 1. Argument für den Zeilenindex und das 2. Argument für den
Spaltenindex. Wenn wir die komplette Spalte betrachten wollen, setzen wir für
den Zeilenindex einfach einen Doppelpunkt `:`. Damit werden automatisch als
Anfangsindex die erste Zeile und als Endindex die letzte Zeile gewählt.
Ansonsten erfolgen die Zugriffe auf Spalten analog zu den Zugriffen auf Zeilen
über die drei Möglichkeiten

* einzelne Spalte,
* zusammenhängende Spalten (Slicing) und
* unzusammenhängende Spalten als Liste.

### Einzelne Spalte

Alle Minuten, die die Spieler auf dem Platz standen, erhalten wir somit als

```{code-cell} ipython3
data_minuten = data.loc[:, 'Mins']
print(data_minuten)
```

### Zusammenhängende Spalten: Slicing

Wenn wir beispielsweise die verwandelten Elfmeter mit den versuchten Elfmetern
vergleichen wollen, so können wir die beiden aufeinanderfolgenden Spalten
'Penalty_Goals' und 'Penalty_Attempted' als Slice ausschneiden:  

```{code-cell} ipython3
data_elfmeter = data.loc[:, 'Penalty_Goals' : 'Penalty_Attempted']
print(data_elfmeter)
```

### Selektion unzusammenhängender Spalten per Liste

Die Anzahl der Tore ('Goals'), die Anzahl der Spiele ('Matches') und die
durchschnittliche Anzahl erwarteter Tore pro Spiel ('xG') miteinander zu
vergleichen, könnte aufschlussreich sein. Da die Spalten nicht nebeneinander
liegen, müssen wir eine Liste benutzen, um sie zu selektieren. 

```{code-cell} ipython3
data_tore = data.loc[:, ['Goals', 'Matches', 'xG'] ]
print(data_tore)
```

## Zugriff auf Zellen

Es kann auch vorkommen, dass man gezielt auf eine einzelne Zelle oder einen
Bereich von Zellen zugreifen möchte. Auch dazu benutzen wir das Attribut
`.loc[]`. 

Der Trick ist nun, die drei Möglichkeiten (einzeln, Slice und Selektion per
Liste) für die Zeilen mit den gleichen drei Möglichkeiten des Zugriffes für
Spalten zu kombinieren.

Wollen wir Beispielsweise das Alter der Fußballprofis von 'David Alaba'bis
'Serge Gnabry' wissen, so gehen wir folgendermaßen vor:

```{code-cell} ipython3
alter = data.loc['David Alaba' : 'Serge Gnabry', 'Age']
print(alter)
```

Und möchten wir von den Herrn Thomas Müller, Kingsley Coman und Alphonso Davies
sowhl die Nationalität als auch das Alter selektieren, so gehen wir wie folgt
vor:

```{code-cell} ipython3
data_special = data.loc[ ['Thomas Müller', 'Kingsley Coman', 'Alphonso Davies'], ['Nationality', 'Age'] ]
print(data_special)
```

## Filtern

Vielleicht haben Sie sich schon gefragt, warum wir nur Bayern-Spieler analysiert
haben. Die Antwort ist simpel, Bayern stand im Datensatz oben in den ersten
Zeilen. Tatsächlich sind aber die Spielerdaten von sieben Vereinen im Datensatz
enthalten. Wir können uns die verschiedenen Werte einer Spalte mit der Methode
`.unique()`ansehen.

In einem ersten Schritt lesen wir die Spalte mit den Vereinen aus (Spalte
'Club'). Dann wenden wir auf das Ergnis die Methode `.unique()` an.

```{code-cell} ipython3
vereine = data.loc[:, 'Club']
vereinsnamen = vereine.unique()
print(vereinsnamen)
```

Wenn man möchte, kann man auch beide Schritte in einem Schritt ausführen:

```{code-cell} ipython3
vereinsnamen = data.loc[:, 'Club'].unique()
print(vereinsnamen)
```

Jetzt wo wir wissen, dass auch Eintracht Frankfurt dabei ist, würden wir den
Datensatz gerne nach Eintracht Frankfurt filter. Dazu benutzen wir einen
Vergleich und speichern das Ergebnis des Vergleichs in einer Variablen.

```{code-cell} ipython3
filter = data.loc[:, 'Club'] == 'Eintracht Frankfurt'
print(filter)
```

Das Ergebnis des Vergleichs, der in der Variablen `filter` gespeichert ist, ist
ein Pandas-Series-Objekt, das für jede Zeile gespeichert hat, ob der Vergleich
wahr (True) oder falsch (False) ist. Ist in einer Zeile der Club gleich
'Eintracht Frankfurt', so ist in dem booleschen Objekt an dieser Stelle True
eingetragen und ansonsten False. Der Datenyp dtype wird mit `bool` angegeben. 

Wir können nun anstatt einer Liste diesen booleschen Index nutzen, um Zeilen zu
selektieren. Steht in einer Zeile des booleschen Series-Objektes `True`, so wird
diese Zeile ausgewählt. Ansonsten wird die Zeile übersprungen. Damit erhalten
wir alle Spielerdaten, die zu Eintracht Frankfurt gehören.

```{code-cell} ipython3
eintracht_frankfurt = data.loc[ filter, :]
print(eintracht_frankfurt)
```

Da der print()-Befehl nicht alle Einträge anzeigt, gehen wir jetzt Zeile für
Zeile durch. Den Zeilenindex erhalten wir über das Attribut `.index`: 

```{code-cell} ipython3
for zeilenindex in eintracht_frankfurt.index:
    print(zeilenindex)
```

## Zusammenfassung

In diesem Abschnitt konnten wir nur die Basis-Funktionalitäten streifen.
Natürlich ist auch möglich, Bereiche zu sortieren oder gruppieren. Im nächsten
Abschnitt erarbeiten wir uns erste statistische Analysen mit Pandas.
