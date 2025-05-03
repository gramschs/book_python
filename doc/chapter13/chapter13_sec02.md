---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 13.2 Überwachtes, unüberwachtes und verstärkendes Lernen

Nachdem im letzten Kapitel erklärt wurde, was machinelles Lernen überhaupt
ist, betrachten wir in diesem Kapitel die drei großen Kategorien von
ML-Modellen: überwachtes Lernen (Supervised Learning), unüberwachtes Lernen
(Unsupervised Learning) und verstärkendes Lernen (Reinforcement Learning).

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können anhand eines Beispiels erklären, was die Fachbegriffe
  * **überwachtes Lernen (Supervised Learning)**,
  * **unüberwachtes Lernen (Unsupervised Learning)** und
  * **verstärkendes Lernen (Reinforcement Learning)** bedeuten.
* Sie können beim überwachten Lernen zwischen **Regression** und
  **Klassifikation** unterscheiden.
```

## Überwachtes Lernen (Supervised Learning)

Im letzten Kapitel haben wir im Video [»So lernen Maschinen:
Algorithmen«](https://youtu.be/HmUzceKCI9I) die Aufgabenstellung kennengelernt,
auf Fotos Hunde von Katzen zu unterscheiden. Diese Art von Problemstellung ist
typisch für **überwachtes Lernen**. Die Daten werden vorab gekennzeichnet, sie
erhalten ein **Label**. So lernen auch Kinder. Stellen Sie sich vor, in einem
Korb liegen Äpfel und Bananen und ein Kind soll den Unterschied erlernen. Jedes
Stück Obst wird aus dem Korb genommen und dem Kind gezeigt. Dazu sagen wir dann
entweder »Apfel« oder »Banane«. Das Kind hat also einen Lehrer oder Trainer. Mit
der Zeit wird das Kind zwischen beiden Obstsorten unterscheiden können.

```{admonition} Was ist ... überwachtes Lernen?
:class: note
Überwachtes Lernen ist eine Kategorie des maschinellen Lernens. Beim überwachten
Lernen liegen die Daten als Eingabe- und Ausgabedaten mit Labels vor. Ein
maschineller Lernalgorithmus versucht ein Modell zu finden, das bestmöglich den
Eingabedaten die Ausgabedaten zuordnet.
```

Beim überwachten Lernen können die Prognosen des Modells für bekannte Daten mit
den korrekten Ergebnissen (Labels) verglichen werden. Das Modell wird also
überwacht.

Prinzipiell werden dabei wiederum zwei Arten von Labels unterschieden:

* kontinuierliche Labels und
* diskrete Labels.

Bei dem Beispiel mit den Hunde- und Katzenfotos sind die Labels diskret. Mit
**diskreten Labels** ist gemeint, dass nur wenige verschiedene Labels existieren.
In diesem Fall sind es genau zwei verschiedene Labels, nämlich zum einen das
Label »Hund« und zum anderen das Label »Katze«. Ein anderes Beispiel für
diskrete Labels sind die Schulnoten sehr gut, gut, befriedigend, ausreichend,
mangelhaft und ungenügend. Es gibt nur sechs verschiedene Noten, die eine
Schülerin oder ein Schüler in einem Test erreichen kann. Dabei müssen die
diskreten Labels keine Texte sein. Die Schulnoten könnten wir auch mit den Labels
1, 2, 3, 4, 5 und 6 kennzeichnen.

Bei den **kontinuierlichen Labels** gibt es sehr viele, normalerweise unendliche
viele verschiedene Labels. Textbezeichnungen sind dann nicht mehr sinnvoll, so
dass kontinuierliche Labels durch Zahlen repräsentiert werden. Ein Beispiel für
kontinuierliche Ausgabedaten ist der Verkaufspreis eines Autos abhängig vom
Kilometerstand. Normalerweise kosten Neuwagen mit einem Kilometerstand von 0 km
am meisten und der Preis sinkt, je mehr Kilometer das Auto bereits gefahren
wurde. Die Verkaufspreise könnte man nun als ganze Zahlen darstellen, wenn man
sie in ganzen Euros angibt, oder als Fließkommazahl, wenn der Preis auf den Cent
genau angegeben wird. Es gibt nicht unendlich viele Verkaufspreise, aber sehr
viele verschiedene mögliche Werte.

Viele ML-Modelle funktionieren sowohl für diskrete als auch kontinuierliche
Daten, aber nicht alle. Daher ist es notwendig, bereits zu Beginn zu
entscheiden, ob das Modell für diskrete oder kontinuierliche Ausgabedaten
eingesetzt werden soll.

Das überwachte Lernen wird daher wiederum in zwei Arten unterteilt:

* **Regression** für kontinuierliche Ausgabedaten und
* **Klassifikation**  für diskrete Ausgabedaten.

Auf beide Problemstellungen gehen die nächsten Videos ein.

```{dropdown} Video zu "ML Tutorial - #3 Supervised Learning" von CodingWithMagga
<iframe width="560" height="315" src="https://www.youtube.com/embed/gaYYJAEt0zI?si=AvndIfnXrjUNiBbf" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

### Regression

```{admonition} Was ist ... Regression?
:class: note
Regression ist das Teilgebiet des überwachten maschinellen Lernens, bei dem
Modelle den Zusammenhang zwischen Eingabedaten und *kontinuierlichen* Ausgabedaten
prognostizieren sollen.
```

```{dropdown} Video zu "Überwachtes Lernen – Regression" von Plattform Lernende Systeme
<iframe width="560" height="315" src="https://www.youtube.com/embed/NCCctUdfA3E" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

### Klassifikation

```{admonition} Was ist ... Klassifikation?
:class: note
Klassifikation ist das Teilgebiet des überwachten maschinellen Lernens, bei dem
Modelle den Zusammenhang zwischen Eingabedaten und *diskreten* Ausgabedaten
prognostizieren sollen.
```

```{dropdown} Video zu "Überwachtes Lernen – Klassifikation" von Plattform Lernende Systeme
<iframe width="560" height="315" src="https://www.youtube.com/embed/g6zuVEDlAzo" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Unüberwachtes Lernen (Unsupervised Learning)

Beim überwachten Lernen liegen Eingabedaten und Ausgabedaten mit Labels vor. Die
Prognosen eines Modells können für bekannte Paare von Eingabe- und Ausgabedaten
überwacht werden. Das ist beim unüberwachten Lernen nicht der Fall. Beim
**unüberwachten Lernen (Unsupervised Learning)** gibt es keine Ausgabedaten,
also keine Labels. Stattdessen soll der maschinelle Lernalgorithmus eigenständig
Muster erlernen und Strukturen in den Daten finden.

```{admonition} Was ist ... unüberwachtes Lernen (Unsupervised Learning)?
:class: note
Unüberwachtes Lernen ist ein Teilgebiet des maschinellen Lernens, bei dem ein
Algorithmus versucht, Muster und Strukturen in Daten zu finden. Dabei sind die
Daten nicht vorab in Eingabe- und Ausgabedaten aufgeteilt bzw. mit Labels
gekennzeichnet.
```

Ein Kind könnte auch selbstständig einen Obstkorb erkunden. Vielleicht würde das
Kind mit der Zeit lernen, dass es Obst gibt, das ihm schmeckt, wohingegen
anderes Obst dem Kind nicht schmeckt. Vielleicht würde das Kind das Obst auch in
großes Obst und kleines Obst unterteilen oder nach Farbe sortieren. Das Kind
gruppiert also Obst nach selbst gewählten Eigenschaften. Es bildet Cluster,
dementsprechend heißt dieser Vorgang **Clustering**.

```{dropdown} Video zu "Unüberwachtes Lernen: Clustering" von Plattform Lernende Systeme
<iframe width="560" height="315" src="https://www.youtube.com/embed/P2Qwc63iCVQ" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video zu "ML Tutorial - #4 Unsupervised Learning" von CodingWithMagga
<iframe width="560" height="315" src="https://www.youtube.com/embed/yKcGVt3xfiE?si=t0UP-8h12bFBjhyr" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Verstärkendes Lernen (Reinforcement Learning)

Wir schließen unsere Übersicht der maschinellen Lernverfahren mit dem
verstärkendem Lernen ab.

```{admonition} Was ist ... verstärkendes Lernen (Reinforcement Learning)?
:class: note
 **Verstärkendes Lernen (Reinforcement Learning)** ist eine Art des maschinellen
Lernens, bei dem ein ML-Algorithmus durch versuch und Irrtum erlernt, was das
optimale Verhalten ist, um ein bestimmtes Ziel zu erreichen. Es werden Aktionen
ausgeführt und entweder bestraft oder belohnt, je nachdem, ob durch diese
Aktionen das Ziel besser oder schlechter erreicht wird.
```

Ein Beispiel aus dem Alltag für verstärkendes Lernen ist das Training eines
Haustieres, eines Hundes beispielsweise. Folgt der Hund dem Befehl »Sitz!«, so
erhält er ein Leckerli. Mit der Zeit wird der Hund auf das Kommando »Sitz!«
reagieren und sich setzen, auch wenn es nicht immer eine Belohnung dafür gibt.

Ein bekanntes Beispiel aus dem Bereich Künstliche Intelligenz für verstärkendes
Lernen sind Schachsysteme. Anfangs kennt das Schachsystem nur die grundlegenden
Schachregeln, aber keinerlei Strategie. Durch das Spielen vieler Spiele, wobei
der Computer bei jedem Sieg eine "Belohnung" erhält und bei jeder Niederlage
eine "Strafe", lernt das Schachsystem allmählich, welche Züge gewinnbringend
sind und welche eher zu Niederlagen führen. Nach Tausenden oder sogar Millionen
von Spielen kann das Schachsystem dann auf einem sehr hohen Niveau spielen -
alles durch verstärkendes Lernen.

```{dropdown} Video zu "Verstärkendes Lernen" von Plattform Lernende Systeme
<iframe width="560" height="315" src="https://www.youtube.com/embed/5HhQgFCQGIY" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

```{dropdown} Vide zu "ML Tutorial - #5 Reinforcement Learning" von CodingWithMagga
<iframe width="560" height="315" src="https://www.youtube.com/embed/EAX12jlMlUw?si=yeV8S4zOT2pMlnBi" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Abschnitt haben Sie die drei wichtigsten Kategorien des maschinellen
Lernens kennengelernt: überwachtes Lernen, unüberwachtes Lernen und
verstärkendes Lernen. Für die Ingenieurwissenschaften ist vor allem das
überwachte Lernen von Bedeutung. Dabei unterscheiden wir zwischen überwachtem
Lernen für diskrete Ausgabedaten (= Klassen, Kategorien), das wir Klassifikation
nennen, und überwachtem Lernen für kontinuierliche Ausgabedaten, das wir
Regression nennen.
