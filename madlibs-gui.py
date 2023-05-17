#
#Author: Jack Ruder
#

import tkinter as tk
import PySimpleGUI as sg
import random

# Platzhalter Listen + vlgtext 

fplh = "Fülle die Lücken mit den Jeweiligen Adjektiven, Verben und Nomen.  Viel Glück!"
plhN = "_Ein Nomen_"
plhV = "_Ein Verb_"
plhA = "_Ein Adjektiv_"
plhnrm = ""

# PLaceholder wortarten für übersicht

nomen = ""
verb = ""
adjektiv = ""

# Madlib listen

text1 = f"Heute war ein {plhA} Tag, und ich habe mich entschieden, {plhN} zu {plhV}."
var1 = f"Heute war ein {adjektiv} Tag, und ich habe mich entschieden, {nomen} zu {verb}."

print(text1)