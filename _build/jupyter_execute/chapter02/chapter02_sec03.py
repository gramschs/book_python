#!/usr/bin/env python
# coding: utf-8

# # Das Modul Turtle
# 
# ```{admonition} Lernziele
# :class: hint
# * TODO
# ```

# ## Virtuelle Roboter zeichnen mit dem Modul Turtle
# 
# In der Informatik nennt man Grafiken, die dadurch entstehen, dass ein Roboter
# Linien auf eine Leinwand zeichnet, Turtle-Grafiken. Der Roboter wird dabei mit
# einfachen Kommandos gesteuert. Beschrieben wird er durch seine Position (x- und
# y-Koordinaten in einem kartesischen Koordinatensystem) und seine Ausrichtung.
# Der "Stift" des Roboters kann von seinen Eigenschaften her ebenfalls variieren.
# So können beispielsweise verschiedenfarbige Stifte verwendet werden oder die
# Linienstärke kann verändert werden.
# 
# Der Kern von Python enthält bereit ein Modul, um eine solche Turtle-Grafik zu erzeugen. Da wir in dieser Vorlesung mit Jupyter Notebooks arbeiten, verwenden wir jedoch das Modul `ipyturtle3`, das das Turtle-Modul mit Funktionalitäten für Jupyter Notebooks erweitert.
# 
# **Achtung:
# Bitte verwenden Sie kein JupyterLab, sondern die klassische Software Jupyter Notebook.**

# Als erstes importieren wir aus dem `ipyturtle3`-Modul die Kommandos Canvas, TurtleScreen und Turtle. Wir erzeugen mit dem Befehl
# 
# ```python3
# Canvas(width=500, height=250)
# ``` 
# 
# eine leere Leinwand, die 500 Bildpunkte breit ist und 250 Bildpunkte hoch ist. Bildpunkte werden normalerweise als Pixel bezeichnet, was wiederum mit px abgekürzt wird. Damit wir mit der Leinwand weiter arbeiten können, speichern wir dieses Objekt in der Variablen `leinwand`. Zuletzt lassen wir uns die Leinwand mit dem Befehl `display()` anzeigen.
# 
# Zusammengesetzt lautet der Code zur Erzeugung einer Leinwand also wie folgt:

# In[1]:


from ipyturtle3 import Canvas, TurtleScreen, Turtle

leinwand = Canvas(width=500, height=250)
display(leinwand)


# Damit der Computer weiß, dass auf dieser Leinwand eine Turtle-Grafik gezeichnet
# werden soll, platzieren wir über die Leinwand ein Turtle-Feld. Dazu erzeugen wir
# mit dem Befehl `TurtleScreen()` das Feld und speichern es zur weiteren
# Verwendung in der Variablen `feld`. Damit das Turtle-Feld auf der Leinwand
# platziert wird, müssen wir der Erzeugung des Turtle-Feldes die Leinwand als
# Zusatzinformation hinzufügen.

# In[2]:


feld = TurtleScreen(leinwand)


# Nun können wir endlich einen Roboter erzeugen und in die Mitte des Feldes setzen
# lassen.

# In[3]:


robo = Turtle(feld)


# Um jetzt den kompletten Code zusammen zu haben, wiederholen wir die bisherigen Code-Zeilen in der folgenden Code-Zelle und experimentieren dann in der übernächsten Code-Zelle mit der Steuerung des Roboters. Mit dem Befehl
# 
# ```python3
# robo.forward(schritte)
# ````
# 
# wird der Roboter vorwärts bewegt und legt insgesamt `schritte` (gemessen in Pixeln) zurück.
# 
# Mit den Befehlen 
# 
# ```python3
# robo.left(winkel)
# ```
# 
# und 
# 
# ```python3
# robo.right(winkel)
# ````
# 
# wird der Roboter nach links (gegen den Uhrzeigersinn) oder rechts (im
# Uhrzeigersinn) gedreht. Der Drehwinkel wird durch die Variable `winkel`
# bestimmt.
# 
# Wenn Sie das Turtle-Feld wieder auf seinen Ausgangszustand zurücksetzen möchten,
# führen Sie erneut die Code-Zelle mit der Erzeugung und Initialisierung aus.

# In[4]:


# Import der benötigten Module
from ipyturtle3 import Canvas, TurtleScreen, Turtle

# Erzeugung und Anzeige der Leinwand
leinwand = Canvas(width=500, height=250)
display(leinwand)

# Initialisierung des Turtle-Feldes
feld = TurtleScreen(leinwand)

# Erzeugung eines Roboters mit Namen robo und Platzierung auf dem Feld
robo = Turtle(feld)


# In[5]:


robo.forward(100)
robo.left(120)
robo.forward(50)


# ```{admonition} Mini-Übung
# :class: miniexercise
# Erzeugen Sie ein Rechteck der Länge 200 px und Höhe 100 px. Am Ende soll der Roboter in die ursprüngliche Richtung hin ausgerichtet sein, also nach Osten bzw. rechts.
# ```

# ````{admonition} Lösung
# :class: minisolution, toggle
# ```python
# robo.forward(200)
# robo.left(90)
# robo.forward(100)
# robo.left(90)
# robo.forward(200)
# robo.left(90)
# robo.forward(100)
# robo.left(90)
# ```
# Anmerkung: natürlich hätten wir den Roboter auch viermal nach rechts drehen lassen können.
# ````
