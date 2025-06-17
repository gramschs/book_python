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

# 10.3 Statistik mit Pandas

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können sich mit **describe** eine Übersicht über statistische Kennzahlen
  verschaffen.
* Sie wissen, wie Sie die Anzahl der gültigen Einträge mit **count** ermitteln.
* Sie kennen die statistischen Kennzahlen Mittelwert und Standardabweichung und
  wissen, wie diese mit **mean** und **std** berechnet werden.
* Sie können das Minimum und das Maximum mit **min** und **max** bestimmen.
* Sie wissen wie ein Quantil interpretiert wird und wie es mit **quantile**
  berechnet wird.
```

## Schnelle Übersicht mit .describe()

So wie die Methode `.info()` uns einen schnellen Überblick über die Daten eines
DataFrame-Objektes gibt, so liefert die Methode `.describe()` eine schnelle
Übersicht über statistische Kennzahlen. Wir bleiben bei unserem Beispiel der
Spielerdaten der Top7-Fußballvereine der Bundesligasaison 2020/21.

```{code-cell} ipython3
import pandas as pd

data = pd.read_csv('bundesliga_top7_offensive.csv', index_col=0)
data.head(10)
```

Die Anwendung der `.describe()`-Methode liefert folgende Ausgabe:

```{code-cell} ipython3
data.describe()
```

Da es sich eingebürgert hat, Daten zeilenweise abzuspeichern und die Eigenschaft
pro einzelnem Datensatz in den Spalten zu speichern, wertet `.describe()` jede
Spalte für sich aus. Für jede Eigenschaft werden dann die statistischen
Kennzahlen

* count
* mean
* std
* min
* max
* Quantile 25 %, 50 % und 75 %
* max

ausgegeben.

Die Bedeutung der Kennzahlen wird in der
[Pandas-Dokumentation/DataFrame.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
erläutert. Wir gehen dennoch jede Kennzahl einzeln durch.

## Anzahl count

Mit `.count()` wird die Anzahl der Einträge bestimmt, die *nicht* 'NA' sind. Der
Begriff 'NA' stammt dabei aus dem Bereich Data Science. Gemeint sind fehlende
Einträge, wobei die fehlenden Einträge verschiedene Ursachen haben können:

* NA = not available (der Messsensor hat versagt)
* NA = not applicable (es ist sinnlos bei einem Mann nachzufragen, ob er
  schwanger ist)
* NA = no answer (eine Person hat bei dem Umfrage nichts angegeben)

Wir können auch direkt auf diesen Wert zugreifen, wenn wir beispielsweise wissen
wollen, bei wie vielen Fußballspielern ein Alter eingetragen ist. Wird die
Methode `.count()` direkt auf den kompletten DataFrame angewendet, so erhalten
wir ein Pandas-Series-Objekt.

```{code-cell} ipython3
print(data.count())
```

Um jetzt an die Anzahl gültiger Altersangaben zu kommen, können wir entweder
erst die Spalte mit dem Alter heraussgreifen und darauf `.count()` anwenden.

```{code-cell} ipython3
methode01 = data.loc[:, 'Age'].count()
print(methode01)
```

Oder wir wenden zuerst `.count()`an und wählen dann im Series-Objekt das Alter
'Age' aus.

```{code-cell} ipython3
methode02 = data.count().loc['Age']
print(methode02)
```

## Mittelwert mean

Mittelwert heißt auf Englisch mean. Daher ist es nicht verwunderlich, dass die Methode `.mean()` den Mittelwert der Einträge in jeder Spalte berechnet.

```{code-cell} ipython3
mittelwert = data.mean(numeric_only=True)
print(mittelwert)
```

An der Stelle ist es wichtig, die Option `numeric_only=True` zu setzen, damit
nur von numerischen Werten, also Zahlen, der Mittelwert gebildet wird.

Wir entnehmen der Statistik, dass Fußballer der Top7-Vereine im Mittel 24.9
Jahre alt sind und 1321.6 Minuten im Einsatz waren.

Falls Sie prinzipiell nochmal die Berechnung des Mittelwertes wiederholen
wollen, können Sie folgendes Video ansehen.

```{dropdown} Video "Mittelwert" von Datatab
<iframe width="560" height="315" src="https://www.youtube.com/embed/IKfsGPwACnU"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Standardabweichung std

Das 'st' in `.std()` steht für Standard. Der dritte Buchstabe 'd' kommt von
'deviation', also Abweichung. Somit ist wiederum die Methode nach dem englischen
Fachbegriff 'standard deviation' benannt.  Welche Standardabweichung erhalten
wir beim Alter?

```{code-cell} ipython3
standardabweichung = data.std(numeric_only=True)
print(standardabweichung)
```

Es sind 4.3 Jahre. Das haben wir jetzt der Ausgabe abgelesen. Wenn wir den Wert
extrahieren wollen, gibt es wieder die beiden Methoden. Entweder erst Spalte und
dann `.std()` oder erst `.std()` und dann Selektion nach 'Age'. Probieren wir es
aus.

```{code-cell} ipython3
alter_std = data.loc[:, 'Age'].std()
print(alter_std) 
```

Was war eigentlich nochmal die Standardabweichung? Falls Sie dazu eine kurze
Wiederholung der Theorie benötigen, empfehle ich Ihnen dieses Video.

```{dropdown} Video "Standardabweichung" von Datatab
<iframe width="560" height="315" src="https://www.youtube.com/embed/QNNt7BvmUJM"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Minimum und Maximum mit min und max

Die Namen der Methoden `.min()` und `max()` sind fast schon wieder
selbsterklärend. Die Methode `.min()` liefert den kleinsten Werte zurück, der in
einer Spalte gefunden wird. Umgekehrt liefert `.max()` den größten Eintrag, der
in jeder Spalte gefunden wird. Wie häufig die minimalen und maximalen Werte
vorkommen, ist dabei egal.

Schauen wir uns an, was die minimale Anzahl von Toren ist, die geschossen wurden
(haben Sie eine Vermutung). Und dann schauen wir gleich nach, was die maximale
Anzahl von Toren ist.

```{code-cell} ipython3
tore_min = data.loc[:, 'Goals'].min()
print(tore_min)

tore_max = data.loc[:, 'Goals'].max()
print(tore_max)
```

Wenig verwunderlich ist die minimale Anzahl an Toren 0. Die maximale Anzahl an
Toren, die ein oder mehrere Spieler der Top7 in der Saison 2020/21 geschossen
haben, war 41\. (Wahrscheinlich wissen Sie aber, dass nur ein Spieler 41 Tore
geschafft hat, natürlich Lewandowski).

Von Verteidigern wird nicht erwartet, Tore zu schießen, sondern von Stürmern.
Was ist denn das Minimum an Toren bei den Stürmern? Die Positionen sind in der
Spalte 'Position'. Dabei bedeutet FW = forward = Stürmer, MF = mid field =
Mittelfeld, DF = defensive = Verteidigung und GK = goalkeeper = Torwart. Bei
manchen Spielern stehen zwei Positionen, konzentrieren wir uns auf diejenigen,
bei denen nur 'FW' eingetragen ist.  

```{code-cell} ipython3
filter = data.loc[:, 'Position'] == 'FW'
stuermer = data.loc[filter, 'Goals']

print('Stürmer')
print(stuermer)

print('==============')
print(f'Minimale Tore: {stuermer.min()}')
```

## Quantil mit quantile

Das Quantil $p \%$ ist der Wert, bei dem $p %$ der Einträge kleiner oder gleich
als diese Zahl sind und $100 \% - p \%$ sind größer. Meist werden nicht
Prozentzahlen verwendet, sondern p ist zwischen 0 und 1, wobei die 1 für 100 %
steht.

Angenommen, wir würden gerne das 0.5-Quantil (auch Median genannt) der gelben
Karten wissen. Mit der Methode `.quantile()` können wir diesen Wert leicht aus
den Daten holen.

```{code-cell} ipython3
gelbe_karten_50prozent_quantil = data.loc[:, 'Yellow_Cards'].quantile(0.5)
print(gelbe_karten_50prozent_quantil)
```

Das 50 % -Quantil liegt bei 2 gelben Karten. 50 % aller Spieler haben also
weniger als 2 gelbe Karten oder genau 2 gelbe Karten kassiert. Und 50 % aller
Spieler haben 2 oder mehr gelbe Karten kassiert. Wir schauen uns jetzt das 75 %
Quantil an.

```{code-cell} ipython3
gelbe_karten_75prozent_quantil = data.loc[:, 'Yellow_Cards'].quantile(0.75)
print(gelbe_karten_75prozent_quantil)
```

75 % aller Spieler haben weniger als 4 gelbe Karten bekommen. Schauen wir uns
die Gelbkarten-Spieler an. Ob da vielleicht mehrheitlich Defensivspieler dabei
sind?

```{code-cell} ipython3
filter = data.loc[:, 'Yellow_Cards'] > 4.0
gelbkarten_spieler = data.loc[filter, ['Position', 'Yellow_Cards']]
print(gelbkarten_spieler.sort_values(by='Yellow_Cards', ascending=False))
```

## Zusammenfassung und Ausblick

In diesem Abschnitt haben wir uns mit einfachen statistischen Kennzahlen
beschäftigt, die Pandas mit der Methode `.describe()` zusammenfasst, die aber
auch einzeln über

* `.count()`
* `.mean()`
* `.std()`
* `.min()` und `.max()`
* `.quantile()`

berechnet und ausgegeben werden können. Im nächsten Kapitel werden wir lernen,
die Daten zu visualisieren.
