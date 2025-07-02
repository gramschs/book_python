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

# 13.1 Was ist maschinelles Lernen?

KI (Künstliche Intelligenz) ist in aller Munde. Etwas seltener wird der Begriff
**maschinelles Lernen** verwendet. Maschinelles Lernen, oft auch **Machine
Learning** genannt, ist ein Teilgebiet der Künstlichen Intelligenz.

Wir kürzen in dieser Vorlesung maschinelles Lernen oft mit **ML** ab. Damit
umgehen wir die Diskussion, warum Künstliche Intelligenz mit einem
Großbuchstaben beginnt und maschinelles Lernen mit einem Kleinbuchstaben.
Gleichzeitig ist das auch die gängige Abkürzung im englischen Sprachgebrauch.
Dieses Kapitel klärt, was maschinelles Lernen ist und führt in die
grundlegenenden Bestandteile eines ML-Systems ein.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, wie langes es das Forschungsgebiet **maschinelles Lernen** gibt
  und warum es sich in den letzten beiden Jahrzehnten so stark entwickelt hat.
* Sie kennen die Bestandteile eines ML-Systems: **Daten**, **Algorithmus** und
  **Modell**. 
```

## Ein wenig Geschichte

Viele glauben, dass die Forschungsgebiete Künstliche Intelligenz und
maschinelles Lernen Neuentwicklungen des 21. Jahrhunderts sind. Doch tatsächlich
hat Arthur L. Samuel bereits 1959 maschinelles Lernen wie folgt definiert:

```{epigraph}
»... ein Forschungsgebiet, das Computer in die Lage versetzen soll, zu lernen,
ohne explizit darauf programmiert zu sein.«

Arthur L. Samuel, 1959
```

[Wikipedia → Maschinelles Lernen](https://de.wikipedia.org/wiki/Maschinelles_Lernen)
bietet eine weitere Definition:

```{epigraph}
»Maschinelles Lernen (ML) ist ein Oberbegriff für die „künstliche“ Generierung
von Wissen aus Erfahrung: Ein künstliches System lernt aus Beispielen und kann
diese nach Beendigung der Lernphase verallgemeinern.«
```

Auch hier wird der Aspekt betont, dass das künstliche System selbst lernt. Aber
was ist mit selbst Lernen gemeint? Ein Kind lernt beispielsweise selbst das
Laufen. Auch wenn Eltern präzise beschreiben könnten, welcher Muskel zu welchem
Zeitpunkt kontrahiert werden muss und mit welcher Geschwindigkeit in welche
Richtung das Bein bewegt werden soll, würde das Kind die Anweisungen nicht
verstehen können. Ein Kind lernt selbst durch Versuch und Irrtum. In der
Anfangszeit der Robotik versuchten Forscherinnen und Forscher, Roboter durch
explizite Befehle zu steuern. Doch bei unvorhergesehenen Hindernissen stießen
solche Roboter an ihre Grenzen. Aus der Notwendigkeit, dass Roboter ähnlich wie
Menschen lernen, entwickelte sich das Teilgebiet maschinelles Lernen innerhalb
der Künstlichen Intelligenz.

Doch nicht nur in der Robotik spielt maschinelles Lernen eine wichtige Rolle.
Auch bei der Datenanalyse kann es hilfreich sein, wenn ein Computersystem
eigenständig Muster in den Daten erkennt. Ein Klassiker dafür ist die
Spam-Erkennung. Natürlich ist es möglich, den Spam-Filter mit expliziten Regeln
zu programmieren. Schon nach kurzer Zeit ändern jedoch Spammer die E-Mail-Texte
und schon greifen die expliziten Regeln nicht mehr. Hier helfen maschinell
gelernte Regeln. Durch die Markierung von E-Mails als Spam lernt das
E-Mail-Programm nach und nach selbst Regeln, um Spam-E-Mails zu identifizieren.

Die exponentiell wachsende Datenmenge der letzten beiden Jahrzehnte hat das
Interesse an maschinellen Lernverfahren stark erhöht. Es gibt aber auch noch
andere Gründe, die zum aktuellen Boom des maschinellen Lernens beigetragen
haben.

````{admonition} Mini-Übung
:class: miniexercise
Schauen Sie sich das folgende Video an. Welche drei Gründe werden dort genannt,
warum maschinelles Lernen zuletzt so stark nachgefragt wurde? 

<iframe width="560" height="315" src="https://www.youtube.com/embed/l_HSWmxMRlU" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
````

```{admonition} Lösung
:class: miniexercise, toggle
Jannik nennt bei Zeitindex 2:44 min drei Gründe, warum in den letzten zwei Jahrzehnten maschinelles Lernen an Bedeutung gewonnen hat:

1. mehr Daten
2. schnellere Computer
3. Forschung
```

Es gibt einige Gründe, warum ML in den letzten zwei Jahrzehnten so stark an
Bedeutung gewonnen hat. Im Folgenden werden die wichtigsten Gründe für den
Bedeutungsgewinn erläutert.

**Datenverfügbarkeit**: Die Produktion von Daten hat mit der Digitalisierung
massiv zugenommen. Mit der Einführung der Smartphones ist auch die Anzahl der
Bilder und Videos deutlich gewachsen, die täglich aufgenommen werden. Das
Kaufverhalten von Kunden in Online-Shops wird beobachtet, Fußballspiele werden
statistisch analysiert oder Maschinen mit Messsensoren bestückt. Das
Beratungsunternehmen IDC (International Data Corporation) prognostiziert, dass
sich die Datenmenge von 33 Zettabytes im Jahr 2018 auf 175 Zettebytes im Jahr
2025 mehr als verfünffachen wird.

**Rechenleistung**: Der rasante Fortschritt in der Computertechnologie hat die
Rechenleistung, die für maschinelles Lernen erforderlich ist, drastisch erhöht.
Speziell für die Entwicklung sogenannter neuronaler Netze werden sogar häufig
Grafikkarten (GPUs) anstatt eines Prozessors (CPU) bevorzugt.

**Algorithmen und Modelle**: Natürlich ist auch die Erforschung neuer
Algorithmen und Modelle nicht stehengeblieben. Ein Durchbruch in der Forschung
war dabei die Entwicklung von den sogenannten Deep-Learning-Modellen, einer
Variante der neuronalen Netze.

**Software und Tools**: Es gibt jetzt eine Vielzahl von Softwarebibliotheken und
Tools (z.B. [TensorFlow](https://www.tensorflow.org),
[PyTorch](https://pytorch.org),
[Scikit-learn](https://scikit-learn.org/stable/index.html) usw.), die es
ermöglichen, auch ohne tiefergehende Mathematik- und Programmierkenntnissen
maschinelles Lernen in der Praxis einzusetzen. Daher werden immer mehr
Anwendungen mit maschinellem Lernen analysiert und optimiert.

Bisher haben wir nicht besprochen, was es mit Künstlicher Intelligenz und Deep
Learning auf sich hat. Beide Begriffe werden oft in einem Atemzug mit ML
genannt. Das folgende Video gibt eine Einführung dazu.

```{dropdown} Video zu "ML Tutorial - #1 Einführung in ML" von CodingWithMagga
<iframe width="560" height="315" src="https://www.youtube.com/embed/tCApwsdijDk?si=Qf6x6MhoAuEBZv7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Was sind Algorithmen und Modelle?

Ein notwendiger Baustein des maschinellen Lernens sind Daten, am besten ganz,
ganz viele! Aber selbst ein riesiger Haufen an Daten ist alleine wertlos. Erst
durch Algorithmen, die in diesen Daten Muster finden, gewinnen wir neues Wissen,
können Prozesse analysieren und Entscheidungen treffen.

Aber was ist nun ein Algorithmus? In dem folgenden Video wird zuerst erklärt,
was ein Algorithmus ist. Danach werden die ersten grundlegenden Fachbegriffe des
maschinellen Lernens eingeführt.

```{admonition} Mini-Übung
:class: miniexercise
Schauen Sie sich das folgende Video an und beantworten Sie die folgenden Fragen:

1. Welche drei Beispiele für Algorithmen werden aufgezählt?
2. In dem Video werden die Fachbegriff »Feature« und »Label« eingeführt. Was bedeuten die
  Begriffe? 
3. Was bedeutet »überwachtes Lernen«?

<iframe width="560" height="315" src="https://www.youtube.com/embed/HmUzceKCI9I" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{admonition} Lösung
:class: miniexercise, toggle
1. Bei Zeitindex 0:28 min wird erklärt, dass ein Algorithmus eine exakte
   Handlungsvorschrift zum Lösen eines Problems ist. Als erstes Beispiel wird
   die Anweisung, wie ein mathematisches Problem zu lösen ist, genannt. Als
   weitere Beispiele werden ein Kochrezept oder eine Spieleanleitung aufgezählt.
   Ab Zeitindex 0:38 min wird Tic-Tac-Toe als Algorithmus formuliert.
2. Ab Zeitindex 3:19 min werden die Begriffe Feature und Label eingeführt. Die
   Eingangsdaten (z.B. Bilder von Hunden und Katzen), die wir dem Computer zum
   Lernen geben, werden Features genannt. Daraus soll der Computer lernen, Hunde
   von Katzen zu unterscheiden. Dazu müssen zuerst die Bilder, die einen Hund
   zeigen, als »Hundebild« gekennzeichnet werden und die anderen als
   »Katzenbild«. Die Kennzeichnung wird Label genannt. Die Zielgröße bzw. Ziel ist die
   Einordnung Hund/Katze.
3. Überwachtes Lernen ist das Lernen aus Beispielen (Zeitindex 4:03 min). Bevor
   der Computer lernt, auf Bildern Hunde und Katzen zu unterscheiden, müssen die
   Bilder mit den Labels Hund/Katze versehen werden.
```

Ein **Algorithmus** ist also eine Anleitung, wie ein Problem zu lösen ist.
Typisch für einen Algorithmus ist, das in sehr kleinen Schritten detailliert
Anweisungen formuliert werden, um das Problem zu lösen. In der Informatik sind
Algorithmen besonders wichtig, da durch sie festgelegt wird, wie der Computer
Daten verarbeiten und ein Problem lösen soll. Jeder einzelne Schritt zur
Problemlösung muss eindeutig und konkret beschrieben werden. Wird der
Algorithmus in einer Programmiersprache formuliert, verwendet man den Begriff
**Computerprogramm**.

```{admonition} Was ist ... ein Algorithmus?
:class: note
Ein Algorithmus ist eine spezifische Anleitung mit einzelnen Anweisungen, wie ein
bestimmtes Problem gelöst werden soll.
```

Der Begriff **Modell** hat viele verschiedenen Bedeutungen (siehe [Wikipedia →
Modell
(Begriffsklärung)](https://de.wikipedia.org/wiki/Modell_(Begriffsklärung))).
Zunächst einmal bedeutet Modell, das ein Original vereinfacht beschrieben wird.
Vereinfacht heißt, dass beispielsweise Details weggelassen werden oder die
Abmessungen geändert werden. In der Architektur wird beispielsweise ein Haus in
kleinem Maßstab gebaut, um potentiellen Kunden durch das Modell einen besseren
Eindruck zu vermitteln, wie das Haus in echt aussehen wird. Im Maschinenbau wird
das Modell eines Flugzeugs in einen Windkanal gehalten, um die Flugzeuggeometrie
zu optimieren. In manchen naturwissenschaftlichen Museen gibt es begehbare
Modelle von Organen wie beispielsweise dem Darm, um den Aufbau des Darms
begreifbar zu machen. Es gibt auch auch virtuelle Modelle wie  das
[Vier-Ohren-Modell](https://de.wikipedia.org/wiki/Vier-Seiten-Modell) des
Kommunikationswissenschaftlers Friedemann Schulz von Thun, das das
Kommunikationsverhalten von Menschen beschreibt.

In der Welt des maschinellen Lernens bezieht sich der begriff Modell darauf,
Daten zu interpretieren und basierend auf diesen Daten Vorhersagen oder
Entscheidungen zu treffen.

```{admonition} Was ist ... ein Modell?
:class: note
Ein Modell ist ein vereinfachtes Abbild der Wirklichkeit. Im Kontext das
maschinellen Lernens ist das ML-Modell eine abstrake Beschreibung eines Systems,
das unbekannte Daten interpretieren kann oder basierend auf diesen Daten
Vorhersagen oder Entscheidungen treffen kann.
```

## Maschinelles Lernen ist wie Kuchenbacken

Damit kommen beim maschinellen Lernen drei Dinge zusammen: Daten, Algorithmus
und Modell. Um das Verhältnis zwischen den drei Konzepten zu verdeutlichen,
vergleichen wir die Konzepte mit dem Kuchenbacken. Die Daten sind die Zutaten,
aus denen ein Kuchen gebacken werden soll. Der Algorithmus ist das Rezept mit
einer detaillierten Schritt-für-Schritt-Anleitung, wie der Kuchen gebacken
werden soll. Das Modell hingegen ist der fertige Kuchen, der aus dem Prozess
herauskommt. Es ist somit das Endprodukt, das erstellt wird, indem man den
Anweisungen des Rezepts (dem Algorithmus) folgt und die Zutaten zusammenfügt.

Sobald das Modell bzw. der Kuchen fertig ist, wird dieses Modell
dann verwendet, um Vorhersagen zu treffen oder Entscheidungen zu treffen, genau
wie man einen Kuchen essen würde, nachdem er gebacken ist.

```{figure} pics/ml_as_baking.png
:name: fig_ml_as_baking

Analogie zwischen dem ML-Workflow und dem Kuchenbacken (Quelle: eigene Darstellung)
```

Allerdings ist es damit nicht getan. Je nachdem, wie viele und welche Gäste
erwartet werden, benötigen wir einen anderen Kuchen. Bei einer großen
Geburtstagsparty brauchen wir einen Blechkuchen, damit jeder Gast ein Stückchen
Kuchen bekommt. Haben wir Diabetiker eingeladen, sollten wir keine
Schokoladentorte anbieten. Auch beim maschinellen Lernen ist es daher sehr
wichtig, je nach Einsatzzweck das passende Modell bzw. den passenden Algorithmus
zu wählen.

Natürlich hängt die Wahl des Kuchens auch von den vorhandenen Zutaten ab. Fehlt
die Schokolade, so kann ich keinen Schokoladenkuchen backen. Entweder backen wir
dann einen anderen Kuchen oder wir entscheiden uns, noch schnell zum Supermarkt
zu gehen und Schokolade einzukaufen. Vielleicht stellen wir auch fest, dass die
Milch abgelaufen ist und nicht mehr genießbar ist. Dann ist unser Plan nicht
durchführbar. Und auch hier können wir uns entscheiden, einen anderen Kuchen zu
backen oder die Zutaten zu erneuern. Diese Analogie passt auch zu maschinellem
Lernen. Fehlen Daten oder sind die Daten nicht qualititativ hochwertig, können
wir die Datenlage verbessern, indem wir beispielsweise mehr Experimente
durchführen oder offensichtlich schiefgelaufene Experimente wiederholen. Diese
Phase des maschinellen Lernen wird auch **Datenerkundung** oder
**Datenexploration** genannt. Sollten wir die Daten jedoch nicht verbessern
können (oder wollen, weil zu teuer oder die Abgabefrist der Bachelorarbeit
ansteht), dann müssen wir die Auswahl des Modells an die vorhandenen Daten
anpassen.

Zutaten komplett, Rezept ausgewählt, Kuchen gebacken, der Gast beißt in den
Kuchen und verzieht das Gesicht ... Zucker und Salz verwechselt. Hätten wir den
Kuchen lieber einmal vor dem Servieren probiert. Auch beim maschinellen Lernen
ist es mit dem "Backen" des Modells nicht getan. Ist ein Modell erstellt, so
muss es auch bewertet werden. Der Prozess des maschinellen Lernens wird mit der
**Validierung** abgeschlossen, bevor das Modell dann produktiv eingesetzt wird.
Die Erstellung und Verwendung von Modellen im maschinellen Lernen ist ein
fortlaufender Prozess. Modelle werden oft mehrfach getestet und angepasst, um
ihre Leistung zu verbessern. Beim Kuchenbacken könnte der Bäcker auf die Idee
kommen, den Kuchen nicht bei 160 °C, sondern bei 162 °C zu backen, weil dann der
Kuchen noch besser schmeckt. Solche Parameter zum Finetunen eines Modells werden
**Hyperparameter** genannt. Hyperparameter haben nichts mit den vorhanden Daten
zu tun, sondern gehören zum ML-Modell. Aber auch wenn sich Daten verändern und
neue Daten hinzukommen, muss das Modell aktualisiert werden, um mit den sich
ändernden Bedingungen zurechtzukommen.

Die folgende Skizze zeigt den schematischen Ablauf eines typischen ML-Projektes.
Dabei benutzen wir das sogenannte
[QUA3CK-Modell](https://www.researchgate.net/publication/339830240_The_QUACK_Machine_Learning_Development_Process_and_the_Laboratory_for_Applied_Machine_Learning_Approaches_LAMA).
Das QUA3CK-Modell zeigt den typischen Ablauf eines ML-Projektes von der
wissenschaftlichen Fragestellung (Q -- Question) bis zu deren Beantwortung (K --
Knowledge Transfer). Dazu gehört das Sammeln und Erkunden der Daten (U --
Understanding the data), mit Hilfe derer die Frage beantwortet werden soll. Die
Phase der ML-Modellbildung wird mehrfach durchlaufen und besteht aus der Auswahl
und dem Training des Algorithmus bzw. des Modells (A -- Algorithm selection and
training), dazu passend der Auswahl und Anpassung der Daten (A -- Adaption of
the data) sowie der Anpassung der Hyperparamter (A -- Adjustement of the
hyperparameter). Die Modelle, die durch diese Schleife erstellt werden, werden
letztendlich miteinander verglichen und bewertet (C -- Comparison and
Conclusion), bevor sie produktiv eingesetzt werden.

```{figure} pics/qua3ck_process.png
:name: fig_qua3ck_process
:width: 60%

Typischer Ablauf eines ML-Projektes als QUA<sup>3</sup>CK-Prozess dargestellt
(Quelle: in Anlehnung an [The QUA³CK Machine Learning Development Process and the Laboratory for Applied Machine Learning Approaches (LAMA)](https://www.researchgate.net/publication/339830240_The_QUACK_Machine_Learning_Development_Process_and_the_Laboratory_for_Applied_Machine_Learning_Approaches_LAMA))
```

Das folgende Video erklärt den ML-Workflow etwas detaillierter, als wir es mit
der Kuchenbacken-Analogie getan haben. Als Ausblick auf die weitere Vorlesung
bietet dieses Video dennoch eine sehr gute Übersicht über die Vorgehenweise in
einem ML-Projekt und ist daher sehr empfehlenswert.

```{dropdown} Video zu "ML Tutorial - #2 ML-Workflow" von CodingWithMagga
<iframe width="560" height="315" src="https://www.youtube.com/embed/f9QT2dqeW04?si=ScwgvnYzsCvbicb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir zwar die drei grundlegenden Bestandteile eines
ML-Systems (Daten, Algorithmus und Modell) kennengelernt, aber entscheidend ist
auch die Anwendung, welche Art von Daten vorliegen. Im nächsten Kapitel werden
wir die drei großen Kategorien betrachten, in die ML-Modelle eingeteilt werden:

* Überwachtes Lernen (Supervised Learning),
* Unüberwachtes Lernen (Unsupervised Learning) und
* Verstärkendes Lernen (Reinforcement Learning).
