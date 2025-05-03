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

# 1.1 Hardware und Software

Bevor wir mit der Programmierung in Python beginnen, machen wir uns zunächst mit
einigen grundlegenden Begriffen der Informatik vertraut. In diesem Kapitel geht
es darum, was zu Hardware und was zu Software zählt. Darüber hinaus lernen wir
die Einteilung der Computerprogramme in verschiedene Software-Kategorien wie
Betriebssystem, Anwendungssoftware und Bibliothek kennen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie kennen die Definition von **Hardware** und **Software**. 
* Sie können häufige Hardware-Komponenten benennen und den verschiedenen
  Kategorien (Eingabe, Verarbeitung, Ausgabe, Speicher) zuordnen.
* Sie kennen die verschiedenen Software-Kategorien **Betriebssystem**,
  **Anwendungssoftware** und **Bibliothek** und können Beispiele für jede
  Kategorie benennen.
```

## Hardware

Computer, mobile Geräte wie Smartphones oder technische Systeme wie
Anlagensteuerungen bestehen aus zwei Komponenten: Hardware und Software.
**Hardware** bezeichnet alle physischen Komponenten eines Systems, also die
elektronischen und mechanischen Bauteile. **Software** umfasst die Programme und
deren Dokumentation sowie Daten. Man könnte auch sagen, dass Hardware die
materiellen Teile eines Computersystems bezeichnet, während Software die
nicht-materiellen Teile zusammenfasst.

```{admonition} Mini-Übung
:class: miniexercise
Bitte schauen Sie sich jetzt kurz um. Welche Hardware fällt Ihnen auf, wenn Sie
den Blick schweifen lassen? Nennen Sie mindestens fünf Hardware-Komponenten.
```

```{admonition} Lösung
:class: miniexercise, toggle
Beispiele für Hardware sind:
* Prozessor (CPU = central processing unit = zentrale Recheneinheit zur
  Verarbeitung von Befehlen)
* Grafikprozessor (GPU = graphics processing unit = auf die Berechnung von
  Grafiken spezialisierter Prozessor)
* interner Speicher: 
    * RAM (Random Access Memory: Arbeitsspeicher für den Prozessor)
    * ROM (Read Only Memory: dient zum Start des Computers)
* externer Speicher: 
    * magnetische Speichermedien: Festplatte (HDD)
    * optische Speichermedien: CD, DVD, BlueRay
    * Flash-Speicher: SSD, USB-Stick, SD-Karte 
* Eingabegeräte wie Tastatur, Maus, Touchpad, Webcam, Mikrofon, Scanner,
  Grafiktablett
* Ausgabegeräte wie Monitor, Display, Lautsprecher, Beamer, Drucker
```

Bei Wikipedia können Sie den Begriff
[Hardware](https://de.wikipedia.org/wiki/Hardware) noch einmal nachlesen.
Wikibooks bietet auch ein passendes Buch zu
[Computerhardware](https://de.wikibooks.org/wiki/Computerhardware) an.

## Software

Software umfasst die nicht-materiellen Komponenten eines Computersystems.
Wikipedia listet hier gleich drei verschiedene ISO-Normen zur Definition von
[Software](https://de.wikipedia.org/wiki/Software) auf.

Wir verwenden im Folgenden die weitreichendste Definition von Software, wonach
Software

* Programme
* Dokumentation und
* Daten

umfasst.

Die letzteren beiden Begriffe sind am einfachsten zu erklären. Mit
**Dokumentation** sind Bedienungsanleitungen und Handbücher gemeint, aber auch
die technische Dokumentation, die für andere Informatikerinnen und Informatiker
gedacht ist und in die Benutzer:innen eines Computersystems in der Regel keinen
Einblick haben. **Daten** wiederum sind alle Beobachtungen oder Messungen. In
der digitalisierten Form werden sie normalerweise durch Zahlenwerte
repräsentiert.

```{admonition} Mini-Übung
:class: miniexercise
Nennen Sie eine Software. Gibt es eine Dokumentation dazu? Welche Daten werden
mit dieser Software verarbeitet?
```

```{admonition} Lösung
:class: miniexercise, toggle
Bekannte Softwaretools zur Erstellung von Folien für eine Präsentation sind
* Microsoft Powerpoint (vor allem für das Windows-Betriebssystem, auch MacOS)
* LibreOffice Impress (kostenlos, alle Betriebssysteme, insbesondere auch Linux)
* Keynote (MacOS)

Die Dokumentation der jeweiligen Programme findet sich im Internet:
* [Dokumentation Powerpoint](https://support.microsoft.com/de-de/powerpoint), 
* [Dokumentation LibreOffice Impress](https://de.libreoffice.org/discover/impress/), 
* [Dokumentation Keynote](https://support.apple.com/de-de/keynote)). 

Da LibreOffice ein Open-Source-Projekt von Freiwilligen ist, können Sie den
Programmcode und die technische Dokumentation auf den [LibreOffice →
Developer](https://www.libreoffice.org/community/developers/) Seiten einsehen.

Die Daten in allen drei Präsentationsprogrammen sind natürlich die Folien mit
den Texten, Bildern, Videos und Animationen.

Die Präsentationsprogramme gehören übrigens zur Kategorie der
Anwendungssoftware.
```

Was die Programme anbelangt, gibt es mehrere Kategorien, die im nächsten
Abschnitt erklärt werden.

## Betriebssystem, Anwendungssoftware und Bibliothek

Die wichtigste Software eines jeden Computersystems ist das **Betriebssystem**.
Das Betriebssystem umfasst alle Computerprogramme, die notwendig sind, um den
Computer zu betreiben, zu starten oder zu benutzen. Das
[Betriebssystem](https://de.wikipedia.org/wiki/Betriebssystem) hat laut
Wikipedia folgende Aufgaben:

> ... Benutzerkommunikation; Laden, Ausführen, Unterbrechen und Beenden von
  Programmen; Verwaltung und Zuteilung der Prozessorzeit; Verwaltung des
  internen Speicherplatzes für Anwendungen; Verwaltung und Betrieb der
  angeschlossenen Geräte; Schutzfunktionen z. B. durch Zugriffsbeschränkungen."

Bekannte Betriebssysteme für Computer sind Linux, macOS und Windows. Bei
Smartphones und Tablets kommen häufig die Betriebssysteme Android und iOS zum
Einsatz.

Viele Menschen denken bei Software zuerst an **Anwendungssoftware** (siehe
[Wikipedia →
Anwendungssoftware](https://de.wikipedia.org/wiki/Anwendungssoftware)). Das sind
Computerprogramme, die einen speziellen Zweck erfüllen sollen und den Benutzer
oder die Benutzerin bei Aufgaben unterstützen. Im Englischen werden solche auch
als **Application** (= Anwendung, Verwendung, Einsatz) bezeichnet. 2008 hat die
Firma Apple den »iOS App Store« gegründet, um Anwendungssoftware für das iPhone
zu vertreiben. Seitdem wird immer häufiger auch im deutschen Sprachraum der Name
Application oder App für verwendet. Vielfach steht »Application« eher für
PC-Anwendungssoftware und der Kurzname »App« für Anwendungssoftware für Tablets
und Smartphones.  

Für Softwareentwickler sind — neben der Programmiersprache und den
Software-Entwicklungswerkzeugen — vor allem Bibliotheken wichtig. Eine
**Bibliothek** (siehe [Wikipedia →
Bibliothek](https://de.wikipedia.org/wiki/Programmbibliothek)) ist eine Sammlung
von Programmen, die zwar einen bestimmten Zweck haben, aber eigenständig nicht
lauffähig sind. Diese Programmbibiotheken werden von Programmiererinnen und
Programmieren genutzt, um nicht ständig neu das Rad erfinden zu müssen.
Beispielsweise würde es den Software-Entwicklungsprozess verlangsamen, wenn
jedesmal neu ein Programm geschrieben werden müsste, das die Wurzel einer Zahl
berechnet oder ein Ergebnis einer Berechnung in eine Datei auf die Festplatte
schreibt. Diese Spezialaufgaben wurden bereits von anderen Software-Entwicklern
implementiert und werden dann über Bibliotheken der Gemeinschaft zur Verfügung
gestellt.

```{admonition} Mini-Übung
:class: miniexercise
Recherchieren Sie nach Python-Bibliotheken im Internet. Nennen Sie drei
Bibliotheken zusammen mit ihrem Einsatzzweck.
```

```{admonition} Lösung
:class: miniexercise, toggle
Bekannte Bibliotheken sind
* PyTorch, Scikit-Learn, TensorFlow: maschinelles Lernen
* NumPy: numerisches Python (Matrizen, lineare Gleichungssysteme, ...)
* Pandas: Tabellenverarbeitung für Python
* Matplotlib: Visualisierung von Daten
* SciPy: wissenschaftliches Rechnen mit Python (Regression, Interpolation, Differentialgleichungen)
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir die Unterschiede zwischen Hardware und Software
kennengelernt. Wir haben gesehen, dass Hardware die physischen Komponenten eines
Computersystems umfasst, während Software die Programme, Dokumentation und Daten
beinhaltet. Software wurde in Betriebssysteme, Anwendungssoftware und
Bibliotheken unterteilt. Im nächsten Kapitel werden wir uns mit Programmieren
beschäftigen.
