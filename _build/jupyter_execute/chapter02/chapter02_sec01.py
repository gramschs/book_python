#!/usr/bin/env python
# coding: utf-8

# # Listen
# 
# Bisher haben wir drei verschiedene Datentypen kennengelernt:
# * Integer (ganze Zahlen),
# * Floats (Fließkommazahlen) und
# * Strings (Zeichenketten).
# 
# Damit können wir einzelne Objekte der realen Welt ganz gut abbilden. Mit einem
# String können wir den Namen einer Person erfassen, mit einem Integer das Alter
# der Person und mit einem Float die Körpergröße der Person gemessen in Meter. Was
# uns aber bisher fehlt ist, eine Sammlung von Namen oder eine Sammlung von
# Körpergrößen verwalten zu können. Daher werden wir uns in diesem Jupyter
# Notebook mit Listen beschäftigen.
# 
# ```{admonition} Lernziele
# :class: hint
# * Sie wissen, dass **Container** Datentypen sind, die andere Objekte als Sammlung verwalten.
# * Sie können eine **Liste** erzeugen.
# * Sie wissen, was der Fachbegriff **Index** bedeutet.
# * Sie können lesend und schreibend auf die Elemente einer Liste zugreifen, beherrschen also
#     * **Lesezugriff** und 
#     * **Schreibzugriff**.
# * Sie können mit dem Plus-Operator + Listen **verketten**.
# * Sie können Strings als Container interpretieren.
# ```
# 

# ## Container für Sammlungen
# 
# In der Mathematik gibt es den Begriff des Vektors. Einen Vektor kann man als
# eine Sammlung von Zahlen interpretieren. Dabei müssen Vektoren nicht immer eine
# geometrische Interpretation haben. Beispielsweise steht der Vektor
# 
# (116, 144, 199)
# 
# für ein sehr schönes Blau, wenn die drei Komponenten als die Intensität der
# Farbanteile Rot - Grün und Blau interpretiert werden. Diese Art Farben zu
# beschreiben, wird RGB-Wert genannt (siehe auch [Wikipedia →
# RGB-Farbraum](https://de.wikipedia.org/wiki/RGB-Farbraum)). Die Internetseite
# [https://www.color-hex.com](https://www.color-hex.com/) ermöglicht es, die
# RGB-Werte verschiedener Farbtöne zu ermitteln.
# 
# Wir könnten aber auch eine Namensliste mit den Mitgliedern einer WG führen
# wollen, z.B. [“Alice”, “Bob”, “Charlie”]. Damit verlassen wir die mathematische
# Welt der Zahlen und damit des Vektors. Aber auch für diese Anwendungsszenarien
# wäre es schön, Daten gemeinsam zu sammeln und zu verwalten. 
# 
# Der Fachbegriff für
# Datentypen, die daür gedacht sind, Daten als Sammlung zu verwalten, ist
# **Container**. In Python gibt es verschiedene Container:
# 
# * Listen: list
# * Tupel: tuple
# * Dictionaries: dict
# * Mengen: set
# 
# Wir behandeln in diesem Abschnitt die Listen.
# 

# ## Listen erzeugen mit []
# 
# Eine Liste wird in Python durch eckige Klammern [  ] erzeugt. Sie finden das
# Zeichen für die eckige Klammer auf der Taste mit der 8, das Zeichen für die
# eckige Klammer auf der Taste mit der 9. Zusätzlich müssen Sie die Taste Alt Gr
# drücken, um die eckigen Klammern auf der Tastatur einzugeben.
# 
# Betrachten wir ein Beispiel. Hier wird eine Liste mit den Elementen 1, 2, 3, 4,
# 5 erzeugt und dann anschließend in der Variablen `liste_beispiel` gespeichert.
# Mit der Funktion `print()` lassen wir den Inhalt der Liste ausgeben.

# In[1]:


liste_beispiel = [1, 2, 3, 4, 5]
print(liste_beispiel)


# ```{admonition} Mini-Übung
# :class: miniexercise
# Erzeugen Sie eine Liste mit Ihrem Vornamen, Ihrem Nachnamen und Ihrer Körpergröße in m. Welche Datentypen brauchen Sie für diese drei Objekte? Lassen Sie Ihre Liste auch ausgeben.
# ```

# In[2]:


# Hier Ihr Code


# ````{admonition} Lösung
# :class: minisolution, toggle
# ```python
# ich = ['Simone', 'Gramsch', 1.61]
# print(ich)
# ```
# Vor- und Nachname werden durch Strings repräsentiert, die Körpergröße als Float.
# ````

# ## Elemente aus einer Liste herausholen: Zugriff
# 
# Jede Liste hat einen Index. Man kann sich eine Liste wie eine Straße mit einer
# Sammlung von Häusern vorstellen. Um ein Haus in der Straße zu finden, hat es
# eine Hausnummer. Und das ist in der Informatik der **Index**, also die Position
# in der Liste, an der ein Element zu finden ist.
# 
# In jeder Programmiersprache gibt es Container mit einem Index, wobei der Index
# in der Regel durch Integer repräsentiert wird. Allerdings gibt es Unterschiede,
# bei welcher Zahl die Nummerierung beginnt. In Python fangen wir mit der Null an.
# Dann können wir mit dem Index sozusagen nachsehen, welches Element an dieser
# Index-Position gespeichert ist. Das nennt man in der Informatik **Lesezugriff**.
# Oder wir können das Element an einer bestimmten Index-Position gegen ein neues
# Element austauschen. Das nennt man dann **Schreibzugriff**.
# 
# Um auf ein Element einer Liste zugreifen zu können (egal ob lesend oder
# schreibend), verwenden wir eckige Klammern und den Index. Wenn wir also
# beispielsweise das erste Element nachschlagen, also lesen wollen, dann sieht der
# Lesezugriff also so aus:

# In[3]:


# Erzeugung einer Liste
meine_liste = ['rot', 'grün', 'blau', 'gelb', 'weiß', 'schwarz']

# Lesezugriff mit Position 1, also Index 0
erstes_objekt = meine_liste[0]
print(erstes_objekt)


# ```{admonition} Mini-Übung
# :class: miniexercise
# Speichern Sie das 4. Element der Liste `meine_liste = ['rot', 'grün', 'blau', 'gelb', 'weiß', 'schwarz']` in der Variable `vier` ab und lassen Sie es ausgeben.
# ```

# In[4]:


# Hier Ihr Code


# ````{admonition} Lösung
# :class: minisolution, toggle
# ```python
# meine_liste = ['rot', 'grün', 'blau', 'gelb', 'weiß', 'schwarz']
# 
# vier = meine_liste[3]
# print(vier)
# ```
# ````

# Für den Schreibzugriff benutzen wir ebenfalls die Schreibweise mit den eckigen
# Klammern und dem Index.
# 
# Um in unserer Liste die Farbe weiß durch lila zu ersetzen, benutzen wir
# folgenden Code:

# In[5]:


# Erzeugung Liste
meine_liste = ['rot', 'grün', 'blau', 'gelb', 'weiß', 'schwarz']

# Schreibzugriff
meine_liste[4] = 'lila'
print(meine_liste)


# ## Liste + Liste = verkettete Liste
# 
# Auch wenn es im ersten Moment verrückt erscheint, in Python können wir Listen
# addieren. Am besten schauen wir uns ein Beispiel an:

# In[6]:


liste_de = ['rot', 'grün', 'blau']
liste_en = ['red', 'green', 'blue']

# Verkettung zweier Listen durch +
liste_de_en = liste_de + liste_en
print(liste_de_en)


# Das Aneinanderhängen von Elementen zweier Container nennen wir in der Informatik
# **Verkettung**. Oft wird auch der englische Begriff **Concatenation** verwendet.

# ## Strings sind auch nur Container
# 
# Tatsächlich sind Strings eine Sammlung von einzelnen Zeichen. Im Deutschen
# werden Strings auch Zeichenketten genannt. Wir können auf einzelne Zeichen eines
# Strings ebenfalls mit eckigen Klammern und dem Index zugreifen.
# 
# Beispielsweise können wir so die Initialen ermitteln: 

# In[7]:


vorname = 'Alice'
nachname = 'Wunderland'

print('Initialen:')
print(vorname[0])
print(nachname[0])


# Die beiden Buchstaben können erneut verkettet werden, damit die Initialen zusammen sind.

# In[8]:


vorname = 'Alice'
nachname = 'Wunderland'

initialen = vorname[0] + nachname[0]

print('Initialen:')
print(initialen)


# Dadurch lassen sich Ausgaben auch schöner gestalten. Beispielsweise können wir
# jetzt auch Strings erst verketten, bevor wir sie anzeigen lassen.

# In[9]:


name = 'Alice'
print('Hallo ' + name)

