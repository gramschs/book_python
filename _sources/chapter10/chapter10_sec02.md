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

# 10.2 Arbeiten mit Tabellendaten

Eine Tabellenkalkulationssoftware wie LibreOffice Calc, Excel oder Number ist
nicht nur nützlich, um Daten zu sammeln, sondern auch um sie zu bearbeiten. In
diesem Kapitel geht es darum zu lernen, wie mit Pandas auf einzelne Zeilen,
Spalten oder Zellen zugegriffen wird.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können auf ganze Zeilen und Spalten zugreifen:
  * Zugriff auf eine einzelne Zeile oder Spalte, indem ein Index spezifiziert wird
  * Zugriff auf mehrere zusammenhängende Zeilen oder Spalten (Slice) 
  * Zugriff auf mehrere unzusammenhängende Zeilen oder Spalten (Selektion)
* Sie können auf einzelne oder mehrere Zellen der Tabelle zugreifen.
* Sie können ein DataFrame-Objekt nach einer Eigenschaft filtern.
```

## Zugriff auf Spalten

Für die folgenden Demonstrationen wollen wir wiederum die Spielerdaten der
Top7-Fußballvereine der Bundesligasaison 2020/21 verwenden. Importieren Sie
bitte vorab die Daten und verwenden Sie die 1. Spalte (= Namen) als Zeilenindex.

```{code-cell}
import pandas as pd
data = pd.read_csv('bundesliga_top7_offensive.csv', index_col=0)
data.head(10)
```

### Einzelne Spalte

Der Zugriff auf Spalten wird am häufigsten gebraucht, da üblicherweise in den
Spalten die Merkmale der Datenobjekte stehen. Daher bietet Pandas dafür einen
direkten Zugriff über die eckigen Klammern `[ ]` an.

```{figure} pics/tabelle_spalte_einzeln.png
:name: fig08_04
:alt: Einzelne Spalte einer Tabelle
:align: center
:width: 50%

Auf eine einzelne Spalte der Tabelle wird mit `[spaltenindex]` zugegriffen. 
```

Das Alter der Fußballspieler erhalten wir somit mit dem Spaltenindex `Age`.

```{code-cell}
alter = data['Age']
print(alter)
```

### Selektion Spalten per Liste

Wir möchten nun die Anzahl der Spiele (`Matches`) und die Anzahl der gespielten
Minuten in der kompletten Saison (`Mins`) auswerten, um beispielsweise die
durchschnittliche Minutenzahl pro Spiel zu ermitteln. Da die Spalten nicht
nebeneinander liegen, müssen wir eine Liste benutzen, um sie zu selektieren. Die
Auswahl der Spalten wird in der Fachsprache **Selektion** genannt.

```{figure} pics/tabelle_spalte_selektion.png
:name: fig08_06
:alt: Selektion von Spalten einer Tabelle
:align: center
:width: 50%

Auf mehrere unzusammenhängende Spalten der Tabelle wird mit `[list]`
zugegriffen. Das nennt man Selektion.
```

Das folgende Code-Beispiel demonstriert die Selektion zweier Spalten.

```{code-cell}
spiele_minuten = data[['Matches', 'Mins']]
print(spiele_minuten)
```

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie sich die folgenden Spalten anzeigen:
* Nationality
* Nationality, Age und Matches
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
data_spalte = data['Nationality']
data_selektion = data[['Nationality','Age', 'Matches']]

print(data_spalte)
print(data_selektion)
```
````

## Zugriff auf Zeilen

Der Zugriff auf Zeilen erfordert eine Erweiterung der Syntax. Über das Attribut
`loc[]` stellt Pandas nicht nur den Zugriff auf Zeilen zur Verfügung, sondern
ermöglicht auch fortgeschritte Zugriffsmöglichkeiten wie beispielsweise das
Slicing, wie wir später sehen werden. Aber zunächst starten wir mit dem Zugriff
auf einzelne Zeilen.

### Einzelne Zeile

Uns interessieren die Spielerdaten von Thomas Müller näher.

```{figure} pics/tabelle_zeile_einzeln.png
:name: fig08_01
:alt: Eine einzelne Zeile der Tabelle ist markiert.
:align: center
:width: 50%

Auf eine einzelne Zeile der Tabelle wird mit `.loc[zeilenindex]` zugegriffen.
```

Um eine ganze Zeile aus der Tabelle herauszugreifen, verwenden wir das Attribut
`.loc[zeilenindex]` und geben in eckigen Klammern den Index der Zeile an, die
wir betrachten wollen. Da wir beim Import die Namen als Zeileindex gesetzt
haben, lautet der Zugriff also wie folgt:

```{code-cell}
zeile = data.loc['Thomas Müller']
print(zeile)
```

### Selektion Zeilen per Liste

Wenn wir auf mehrere Zeilen zugreifen wollen, die nicht zusammenhängen, so nennt
man das wie bei den Spalten ebenfalls Selektion.

```{figure} pics/tabelle_zeile_selektion.png
:name: fig08_03
:alt: Slicing von Zeilen einer Tabelle
:align: center
:width: 50%

Auf mehrere unzusammenhängende Zeilen der Tabelle wird mit `.loc[list]`
zugegriffen. Das nennt man Selektion.
```

Um mehrere unzusammenhängende Zeilen zu selektieren, übergeben wir `.loc[]` eine
Liste mit den gewünschten Zeilenindizes.

```{code-cell}
zeilen_selektion = data.loc[['Manuel Neuer', 'David Alaba']]
print(zeilen_selektion)
```

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie sich die folgenden Zeilen anzeigen:
* Kingsley Coman
* Kingsley Coman bis Alphonso Davies
* Robert Lewandowski, Kingsley Coman und Serge Gnabry
```

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
data_zeile = data.loc['Kingsley Coman']
data_selektion = data.loc[['Robert Lewandowski','Kingsley Coman', 'Serge Gnabry']]

print(data_zeile)
print(data_selektion)
```
````

## Slicing

Wenn wir auf mehrere Zeilen oder Spalten gleichzeitig zugreifen wollen, gibt es
zwei Möglichkeiten:

1. Zwischen den einzelnen Zeilen/Spalten sind Lücken, wir haben eine
   unzusammenhängende Selektion.
2. Die Zeilen oder Spalten folgen direkt aufeinander, sind also zusammenhängend.

Den ersten Fall haben wir bereits oben dargestellt. Bei Spalten wird die
Selektion über eine Liste und eckige Klammern `[]` realisiert, bei Zeilen über
eine Liste, die in `.loc[]` eingesetzt wird.

Der Zugriff auf zusammenhängende Bereiche wird in der Informatik **Slicing**
genannt. Wir werden uns die beiden Fälle

* Slicing für Zeilen
* Slicing für Spalten

anschauen, aber zunächst betrachten wir das Slicing von Zeilen.

### Slicing von Zeilen

```{figure} pics/tabelle_zeile_slice.png
:name: fig08_02
:alt: Mehrere zusammenhängende Zeilen der Tabelle sind markiert.
:align: center
:width: 50%

Auf mehrere zusammenhängende Zeilen der Tabelle wird mit `.loc[start:stopp]`
zugegriffen. Das nennt man Slicing.
```

Bei der Angabe des Bereiches gibt man den Anfangsindex gefolgt von einem
Doppelpunkt an und dann den Endindex der letzten Zeile, die "herausgeschnitten"
werden soll.

```{code-cell} ipython3
zeilen_slice = data.loc['Thomas Müller' : 'Jérôme Boateng']
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

### Slicing von Spalten

Wenden wir uns nun dem Slicing von Spalten zu. Möchten wir beispielsweise die
Anzahl der Spiele (`Matches`), die ein Spieler in der Saison absolviert hat, mit
der Anzahl der Spiele, in denen er vom Anfang an auf dem Platz stand (`Starts`)
vergleichen, so können wir die beiden aufeinanderfolgenden Spalten 'Matches' und
'Starts' als sogenannten **Slice** ausschneiden. Dazu müssen wir jedoch das
Attribut `.loc[]` verwenden, das uns fortgeschrittene Techniken des Zugriffs
bietet. Allerdings müssen wir Python mitteilen, dass diesmal Spalten und nicht
Zeilen gemeint sind. Die Dokumentation von `loc[]` zeigt uns, dass Spalten nach
einem Komma angegeben werden. Damit alle Zeilen dabei sind, brauchen wir als
erstes Argument den Doppelpunkt.

```{figure} pics/tabelle_spalte_slice.png
:name: fig08_05
:alt: Slice von Spalten einer Tabelle
:align: center
:width: 50%

Auf mehrere zusammenhängende Spalten der Tabelle wird mit `.loc[:, start:stopp]`
zugegriffen. Das nennt man Slicing.
```

Das folgende Beispiel zeigt das Slicing zweier Spalten.

```{code-cell} ipython3
spiele = data.loc[:, 'Matches' : 'Starts']
print(spiele)
```

## Zugriff auf Zellen

Es kann auch vorkommen, dass man gezielt auf eine einzelne Zelle oder einen
Bereich von Zellen zugreifen möchte. Auch dazu benutzen wir das Attribut
`.loc[]`.

Eine Zelle ist ein einzelnes Element der Tabelle, sozusagen der Kreuzungspunkt
zwischen Zeile und Spalte. Die Zelle mit dem Zeilenindex `Thomas Müller` und dem
Spaltenindex `Age` enthält das Alter von Thomas Müller.

```{figure} pics/tabelle_zelle_einzeln.png
:name: fig08_07
:alt: Einzelne Zelle einer Tabelle
:align: center
:width: 50%

Auf ein einzelne Zelle der Tabelle wird mit `.loc[zeilenindex, spaltenindex]` zugegriffen.
```

Der Trick ist nun, die drei Möglichkeiten (einzeln, Slice und Selektion per
Liste) für die Zeilen mit den gleichen drei Möglichkeiten des Zugriffes für
Spalten zu kombinieren.

Wollen wir beispielsweise das Alter von Thomas Müller aus der Tabelle
heraussuchen, so gehen wir folgendermaßen vor.

```{code-cell} ipython3
alter_mueller = data.loc['Thomas Müller', 'Age']
print(f'Thomas Müller ist {alter_mueller} Jahre alt.')
```

Wollen wir Beispielsweise das Alter der Fußballprofis von 'David Alaba' bis
'Robert Lewandowski' wissen, so gehen wir folgendermaßen vor:

```{code-cell} ipython3
alter_slice = data.loc['David Alaba' : 'Robert Lewandowski', 'Age']
print(alter_slice)
```

Und möchten wir von den Herren Thomas Müller und Joshua Kimmich sowhl die
Nationalität als auch das Alter selektieren, so gehen wir wie folgt vor:

```{code-cell} ipython3
spezialauswahl = data.loc[ ['Thomas Müller', 'Joshua Kimmich'], ['Nationality', 'Age'] ]
print(spezialauswahl)
```

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie sich das Alter von Robert Lewandowski und Thomas Müller anzeigen.
```

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
alter = data.loc[['Robert Lewandowski', 'Thomas Müller'], 'Age']
print(alter)
```
````

## Filtern

Vielleicht haben Sie sich schon gefragt, warum wir nur Bayern-Spieler analysiert
haben. Die Antwort ist simpel, Bayern stand im Datensatz oben in den ersten
Zeilen. Tatsächlich sind aber die Spielerdaten von sieben Vereinen im Datensatz
enthalten. Wir können uns die verschiedenen Werte einer Spalte mit der Methode
`.unique()` ansehen.

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
Datensatz gerne nach Eintracht Frankfurt filtern. Dazu benutzen wir einen
Vergleich und speichern das Ergebnis des Vergleichs in einer Variablen.

```{code-cell} ipython3
filter_eintracht = data.loc[:, 'Club'] == 'Eintracht Frankfurt'
print(filter_eintracht)
```

Das Ergebnis des Vergleichs, der in der Variablen `filter_eintracht` gespeichert
ist, ist ein Pandas-Series-Objekt, das für jede Zeile gespeichert hat, ob der
Vergleich wahr (True) oder falsch (False) ist. Ist in einer Zeile der Club
gleich 'Eintracht Frankfurt', so ist in dem booleschen Objekt an dieser Stelle
True eingetragen und ansonsten False. Der Datenyp dtype wird mit `bool`
angegeben.

Wir können nun anstatt einer Liste diesen booleschen Index nutzen, um Zeilen zu
selektieren. Steht in einer Zeile des booleschen Series-Objektes `True`, so wird
diese Zeile ausgewählt. Ansonsten wird die Zeile übersprungen. Damit erhalten
wir alle Spielerdaten, die zu Eintracht Frankfurt gehören.

```{code-cell} ipython3
eintracht_frankfurt = data.loc[filter_eintracht, :]
print(eintracht_frankfurt)
```

Da der print()-Befehl nicht alle Einträge anzeigt, gehen wir jetzt Zeile für
Zeile durch. Den Zeilenindex erhalten wir über das Attribut `.index`:

```{code-cell} ipython3
for zeilenindex in eintracht_frankfurt.index:
    print(zeilenindex)
```

## Zusammenfassung und Ausblick

In diesem Abschnitt konnten wir nur die Basis-Funktionalitäten streifen.
Natürlich ist auch möglich, Bereiche zu sortieren oder gruppieren. Im nächsten
Abschnitt erarbeiten wir uns erste statistische Analysen mit Pandas.
