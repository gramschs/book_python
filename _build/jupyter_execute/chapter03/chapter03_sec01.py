#!/usr/bin/env python
# coding: utf-8

# # for-Schleifen mit Liste
# 
# In der Praxis kommt es oft vor, dass wir von vornherein wissen, wie oft wir eine
# Handlung wiederholen wollen. Beispielsweise soll in einem Verein darüber
# abgestimmt werde, ob Anna oder Bob zukünftig die Kasse verwalten soll. Alle
# Vereinsmitglieder schreiben einen der beiden Namen auf einen Zettel und werfen
# ihn in die Wahlurne. Jetzt beginnt die Wiederholung. Charlie greift in die Urne,
# zieht einen Zettel heraus, liest den Namen vor und macht dann entweder bei Anna
# oder bei Bob einen Strich auf dem Flipboard. Solange Zettel in der Urne sind,
# wird diese Prozedur wiederholt. Wenn wir aber bereits vorher wissen, dass 12
# Vereinsmitglieder abgestimmt haben, so wird Charlie 12 x diese Prozedur
# wiederholen. In diesem Fall bietet sich die Umsetzung als sogenannte
# Zählschleife an.
# 
# In Python gibt es zwei Varianten von Zählschleifen. Zum einen die Zählschleife,
# bei der Elemente einer Liste abgearbeitet werden. Zum anderen die Zählschleife
# mit einem Zahlenbereich. In diesem Abschnitt behandeln wir Zählschleife mit
# einer Liste.
# 
# ```{admonition} Lernziele
# :class: hint
# * TODO
# ```
# 

# ## Grammatik der for-Schleife mit Liste
# 
# Die for-Schleife mit Liste hat folgende Syntax (= Grammatik einer Programmiersprache):
# 
# ```python3
# for element in liste:
#     anweisungsblock
# ```
# 
# Eine Schleife beginnt mit dem Schlüsselwort **for**. Danach kommt der Name der sogenannten **Schleifenvariable**, in diesem Fall also `element`. Als nächstes folgt wieder ein Schlüsselwort, nämlich **in** und zuletzt die Liste.
# 
# Python muss wissen, welche Kommandos für jeden Schleifendurchgang ausgeführt werden sollen. Daher wird die Kopfzeile der Schleife mit einem Doppelpunkt `:` beendet. Danach werden alle Kommandos aufgelistet, die ausgeführt werden sollen. Damit Python weiß, wann es wieder mit dem normalen Programm weitergehen soll, müssen wir dem Python-Interpreter das Ende der Schleife signalisieren. In vielen Programmiersprachen wird das mit dem Schlüsselwort `end` gemacht oder es werden Klammern gesetzt. In Python wird stattdessen mit **Einrückung** gearbeitet. Alle Zeilen, die eingerückt sind, werden in der Schleife wiederholt.
# 
# Probieren wir es mit einem einfachen Beispiel:
# 
# 

# In[1]:


for i in [2, 4, 6, 8, 10]:
    print(i)


# 
# Es werden nacheinander die Elemente der Menge `[2, 4, 6, 8, 10]` auf dem Bildschirm ausgegeben.
# 
# Meistens geht es nicht darum, nur etwas einzeln anzuzeigen, sondern die Elemente der Menge zu verarbeiten. Im nächsten Beispiel soll jedes Element der Liste `[4,5,7,11,21` um 2 erhöht und dann angezeigt werden.

# In[2]:


for zahl in [4,5,7,11,21]:
    zahl2 = zahl + 2
    print(zahl2)

print('Ich bin fertig!')

