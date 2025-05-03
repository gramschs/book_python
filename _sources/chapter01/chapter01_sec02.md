---
jupytext:
  cell_metadata_filter: -all
  formats: ipynb,md:myst
  main_language: python
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 1.2 Programmieren

Es gibt viele Gründe, warum es sich lohnt, Programmieren zu lernen. Die
Nachfrage nach Ingenieurinnen und Ingenieuren, die zusätzlich Programmieren
können, wächst aufgrund der Digitalisierung der Industrie rasant. Programmieren
fördert kritisches Denken und Problemlösungsfähigkeiten. Umgekehrt werden durch
Programmieren diese Fähigkeiten weiter entwickelt. Zudem fördert Programmieren
das Verständnis von Technologie und Computersystemen. Es kann helfen, die
Funktionsweise von Software und Hardware besser zu verstehen und Einblicke in
die Arbeitsweise von Websites, Anwendungen und anderen Technologien zu gewinnen.
Programmierung kann auch dabei helfen, Routineaufgaben zu automatisieren und
Zeit zu sparen. Dies kann Fehler minimieren und die Effizienz steigern.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können erklären, was ein **Algorithmus** ist.
* Sie wissen, was eine **Programmiersprache** ist.
* Sie kennen den Unterschied zwischen **höheren Prorgammiersprachen** und
  **Maschinensprache**.
* Sie wissen, was der Unterschied zwischen einer **kompilierten
  Programmiersprache** und einer **interpretierten Programmiersprache** ist. Sie
  können für beide Kategorien Beispiele benennen.
```

## Programmieren ist wie Kochen

Programmieren bedeutet, dem Computer eine Reihe von Anweisungen zu geben. Es
geht darum, mit Hilfe einer Abfolge von Anweisungen ein Problem zu lösen. Ein
wichtiger Aspekt des Programmierens ist die Fähigkeit, komplexe Probleme in
kleinere, leichter zu lösende Aufgaben zu unterteilen. Diese Aufgaben können
dann einzeln gelöst und in einem größeren Programm kombiniert werden, um das
Problem als Ganzes zu lösen.

Diese schrittweise Beschreibung der Lösung eines Problems nennt man
**Algorithmus**. Ein Algorithmus ist ein klar definierter Satz von Anweisungen
oder Regeln, die von einem Computer (oder auch von einem Menschen) ausgeführt
werden können, um ein bestimmtes Ergebnis zu erzielen.

```{admonition} Mini-Übung
:class: miniexercise
Nehmen Sie sich 5 min Zeit, um einen Algorithmus aufzuschreiben, wie Ihr
Lieblingsgericht zubereitet wird.
```

```{admonition} Lösung
:class: miniexercise, toggle
Zuerst werden 1 Apfel, 1 Banane, 1 Orange und 2 Kiwis kleingeschnitten und in
eine Schüssel gefüllt. Danach werden 3 EL Joghurt mit 1 TL Honig und einer Prise
Zimt verrührt. Zuletzt wird das Joghurt-Dressing mit den Obststücken gemischt
und angerichtet.
```

Kochanweisungen sind nicht immer verständlich. Es kommt auf das
Hintergrundwissen der Person an, die versucht, ein Gericht nachzukochen, ob die
Kochanweisung verständlich ist. In dem obigen Beispiel wurde beispielsweise
vorausgesetzt, dass die Abkürzungen EL für Esslöffel und TL für Teelöffel
bekannt sind. Es hätten aber auch Formulierungen vorkommen können wie Mehl
anschwitzen, Sauce binden, Masse stocken lassen oder Zwiebeln glasig werden
lassen. Falls solche Formulierungen unverständlich sind, liegt es oft daran,
dass sich dahinter ein eigener Kochprozess verbirgt, den man kennen muss, um das
Rezept insgesamt nachzukochen.

[Chefkoch](https://www.chefkoch.de/) bietet eine riesige Anzahl an Rezepten wie
z.B. das folgende Rezept eines
[Rosenkohl-Auflaufs](https://www.chefkoch.de/rezepte/1717121280428611/Rosenkohlauflauf.html):

> Die Kartoffeln und den Rosenkohl bissfest garen. Das Hackfleisch anbraten
und nach Belieben eine Zwiebel zugeben. Die Sahne und den Schmand verrühren und
etwas geriebenen Käse zugeben, mit Knoblauchpulver und Muskat würzen. Eine
Auflaufform fetten und abwechselnd Kartoffeln, Rosenkohl, Gehacktes, Toastkäse
und Sahne-Schmandmischung schichten. Anschließend den restlichen Reibekäse über
den Auflauf geben. Für eine halbe Stunde in den auf 200 Grad vorgeheizten
Backofen geben.

Könnten Sie dieses Rezept nachkochen? Was müsste aus Ihrer Sicht detaillierter
beschrieben werden?

```{admonition} Mini-Übung
:class: miniexercise
Listen Sie die Details auf, die dem obigen Rezept des Rosenkohl-Auflaufs
zugefügt werden müssten, um auch Kochanfängern eine Möglichkeit zu bieten, das
Rezept nachzukochen.
```

```{admonition} Lösung
:class: miniexercise, toggle
* Die Garzeiten der Kartoffeln und des Rosenkohls sind normalerweise
  unterschiedlich und müssten spezifiziert werden. 
* Wie wird Hackfleisch angebraten? Erläuterungen zum Anbraten fehlen komplett.
* Angaben zur Würzung der Sahne-Schmand-Mischung fehlen.
* Soll der Backofen 200 Grad bei Umluft oder Ober-/Unterhitze haben? Mittlere
* Schiene oder eine andere?
```

Auf die Idee, einen Algorithmus mit dem Kochen zu vergleichen, werden wir in
späteren Kapiteln noch zurückkehren. Als nächstes beschäftigen wir uns damit, wie
den Computer Anweisungen erteilt werden.

## Programmiersprachen

Eine **Programmiersprache** ist die formale Sprache zur Formulierung von
Datenstrukturen und Algorithmen (= Abfolge von Anweisungen), die von einem
Computer ausgeführt werden können.

Es gibt nicht die wichtigste oder beste Programmiersprache, sondern die Auswahl
der Programmiersprache sollte sich stets nach der anvisierten Anwendung richten.
Der sogenannte Tiobe-Index zeigt die Beliebtheit der 50 wichtigsten
Programmiersprachen:

<https://www.tiobe.com/tiobe-index/>

```{admonition} Mini-Übung
:class: miniexercise
Recherchieren Sie im Tiobe-Index nach den Programmiersprachen MATLAB und Python.
Auf welchem Platz stehen die beiden Programmiersprachen aktuell?
```

In der Anfangszeit der Computer waren Programmiersprachen noch sehr nahe am
Computern ausgerichtet. Hier sehen Sie ein Beispiel, wie in der
Programmiersprache Assembler die Meldung "Hallo Welt" auf dem Monitor angezeigt
wird:

```{figure} pics/fig_chap00_sec01_assembler.png
:name: fig_chap00_sec01

"Hallo Welt" in Assembler (Quelle: [Wikipedia → Assemblersprache](https://de.wikipedia.org/wiki/Assemblersprache))
```

In Python ist dieser Programmcode wesentlich kürzer:

```{code-cell}
print('Hallo Welt')
```

Heute werden nur noch die sogenannten **höheren Programmiersprachen** verwendet
(wie Python, MATLAB oder C++), die für Menschen leichter verständlich sind.
Dafür müssen dann Programme, die in höheren Programmiersprachen geschrieben
sind, in **Maschinensprache** übersetzt werden. Verschiedene Programmiersprachen
verwenden dazu unterschiedliche Prinzipien. Die beiden wichtigsten Vertreter
sind

* **Compiler-Programmiersprachen** und
* **Interpreter-Programmiersprachen**.

Bei Compiler-Programmiersprachen wird der Programmcode vorab in Maschinensprache
übersetzt und der Anwender erhält die Anwendungssoftware in Maschinensprache
(bei Windows beispielsweise als exe-Datei). Den Vorgang des Übersetzens nennt
man **kompilieren**. Bei Interpreter-Sprachen wird der Code in dem Moment in
Maschinensprache übersetzt, in dem das Programm läuft bzw. ausgeführt wird.
Während also das Programm läuft, muss gleichzeitig ⎼ quasi im Hintergrund ⎼ der
Übersetzer arbeiten und die höhere Programmiersprache in Maschinensprache
**interpretieren**. Daher der Name Interpreter-Sprache. Manchmal wird Code, der
kompiliert wurde und dann eigenständig lauffähig ist, als **Programm**
bezeichnet. Dahingegen wird Code, der interpretiert wird und dringend auf einen
gerade laufenden Interpreter angewiesen ist, oft als Skript bezeichnet. Im
Alltag geht diese Unterscheidung meist unter und wir verwenden den Begriff
Programm auch für Python-Skripte.

```{admonition} Mini-Übung
:class: miniexercise
Recherchieren Sie im Internet. Sind die folgenden Programmiersprachen
kompilierte oder interpretierte Programmiersprachen?

* C bzw. C++
* Java
* C# (ausgesprochen: C Sharp)
* Visual Basic
* JavaScript
```

```{admonition} Lösung
:class: miniexercise, toggle
Recherchieren Sie im Internet. Sind die folgenden Programmiersprachen
kompilierte oder interpretierte Programmiersprachen?

* C bzw. C++ --> kompiliert
* Java --> kompiliert (wird manchmal auch zu den interpretierten Sprachen
  gezählt, weil der kompilierte Bytecode anschließend von der Java Virtual
  Machine interpretiert wird und nicht vom Betriebsystem direkt ausgeführt wird)
* C# --> kompliliert
* Visual Basic --> kompiliert
* JavaScript --> interpretiert
```

Insgesamt ist der Unterschied zwischen kompilierten und interpretierten Sprachen
vor allem eine Frage der Geschwindigkeit und Flexibilität. Kompilierte Programme
sind in der Regel schneller als interpretierte Programme, da der Maschinencode
direkt vom Betriebssystem ausgeführt werden kann. Umgekehrt können Änderungen
des Programms bei interpretierten Programmen schneller durchgeführt werden, da
diese ja ohnehin Zeile für Zeile abgearbeitet und interpretiert werden. Dies
bedeutet, dass Änderungen am Code sofort wirksam werden, ohne dass eine erneute
Kompilierung erforderlich ist.

Letztendlich hängt die Wahl der Programmiersprache von den Anforderungen des
Projekts ab und davon, welche Kompromisse zwischen Geschwindigkeit und
Flexibilität akzeptabel sind.

## Warum Python?

Was ist überhaupt Python? Wikipedia erklärt Python folgendermaßen:

> "Python ([ˈpʰaɪθn̩], [ˈpʰaɪθɑn], auf Deutsch auch [ˈpʰyːtɔn]) ist eine
  universelle, üblicherweise interpretierte, höhere Programmiersprache. Sie hat
  den Anspruch, einen gut lesbaren, knappen Programmierstil zu fördern. So
  werden beispielsweise Blöcke nicht durch geschweifte Klammern, sondern durch
  Einrückungen strukturiert."
  (Quelle: [Wikipedia](https://de.wikipedia.org/wiki/Python_(Programmiersprache))

In dieser Vorlesung verwenden wir Python als Programmiersprache, da Python viele
Vorteile bietet, die das Erlernen der Programmierung erleichtern und Spaß
machen:

1. Einfache Syntax: Python hat eine klare und leicht verständliche Syntax, die
   es leicht macht, die Grundlagen der Programmierung zu erlernen. Die Syntax
   ist lesbar und ähnelt der englischen Sprache, was das Verständnis
   erleichtert.
2. Vielseitigkeit: Python ist eine sehr vielseitige Programmiersprache, die in
   vielen verschiedenen Bereichen eingesetzt werden kann. Sie wird oft für
   Datenanalyse, künstliche Intelligenz, Webentwicklung und wissenschaftliches
   Rechnen verwendet.
3. Große Community: Python hat eine große Community von Entwicklern, die aktiv
   an der Weiterentwicklung der Sprache und an der Bereitstellung von
   Hilfestellung und Ressourcen für Anfänger beteiligt sind. Es gibt viele
   Online-Foren, Kurse und Tutorials, die das Erlernen der Sprache erleichtern.
4. Interaktiver Modus: Python bietet einen interaktiven Modus, der es Anfängern
   ermöglicht, Code Zeile für Zeile auszuführen und das Ergebnis sofort zu
   sehen. Dies macht das Experimentieren und die Suche nach Fehlern im Code sehr
   einfach und effektiv.
5. Plattformunabhängigkeit: Python kann auf verschiedenen Betriebssystemen wie
   Windows, Mac und Linux ausgeführt werden. Dies macht es für Anfänger leicht,
   die Sprache auf ihrem bevorzugten Betriebssystem zu erlernen.

Ansonsten ist es ein wenig wie mit dem Erlernen einer Fremdsprache. Die erste
Fremdsprache ist die schwerste! Sprich, wenn Sie eine Programmiersprache erlernt
haben und wissen, wie ein komplexes Problem in Teilaufgaben zerlegt wird, können
Sie das schnell auf andere Programmiersprachen übertragen.

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir die Vorteile des Programmierens für Ingenieure
diskutiert, den Begriff des Algorithmus anhand von Kochrezepten erklärt und die
Unterschiede zwischen verschiedenen Programmiersprachen sowie die Vorteile von
Python hervorgehoben. Im nächsten Kapitel beschäftigen wir uns mit den
technischen Voraussetzungen, um Python-Programme zu schreiben und auszuführen.
