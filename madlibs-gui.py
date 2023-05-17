#
#Author: Jack Ruder
#

import tkinter as tk
import PySimpleGUI as sg
import random
import time

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

text2 = f"Ich habe gestern ein {plhN} gesehen, der {plhV} konnte. Es war wirklich {plhA}."
var2 = f"Ich habe gestern einen {nomen} gesehen, der {verb} konnte. Es war wirklich {adjektiv}."

text3 = f"Mein Lieblingshobby ist es, {plhN} zu {plhV}. Es macht mich immer {plhA}."
var3 = f"Mein Lieblingshobby ist es, {nomen} zu {verb}. Es macht mich immer {adjektiv}."

text4 = f"Mein Lieblingsessen ist {plhN} mit {plhV}. Es schmeckt {plhA}."
var4 = f"Mein Lieblingsessen ist {nomen} mit {verb}. Es schmeckt {adjektiv}."

text5 = f"Der {plhN} nebenan ist wirklich {plhA}. Er/sie {plhV} den ganzen Tag."
var5 = f"Der {nomen} nebenan ist wirklich {adjektiv}. Er/sie {verb} den ganzen Tag."

text6 = f"Wenn ich könnte, würde ich gerne {plhN} mit einem {plhA} {plhV}."
var6 = f"Wenn ich könnte, würde ich gerne {nomen} mit einem {adjektiv} {verb}."

text7 = f"Ich liebe es, {plhN} zu {plhV}. Es gibt mir ein Gefühl von {plhA}."
var7 = f"Ich liebe es, {nomen} zu {verb}. Es gibt mir ein Gefühl von {adjektiv}."

text8 = f"Gestern habe ich {plhN} getroffen, der/die {plhV} und {plhA} ist."
var8 = f"Gestern habe ich {nomen} getroffen, der/die {verb} und {adjektiv} ist."

text9 = f"Mein Lieblingsfilm ist {plhN}. Es ist so {plhA} und {plhV}."
var9 = f"Mein Lieblingsfilm ist {nomen}. Es ist so {adjektiv} und {verb}."

text10 = f"Das Beste am Sommer ist, {plhN} zu {plhV}. Es ist so {plhA}."
var10 = f"Das Beste am Sommer ist, {nomen} zu {verb}. Es ist so {adjektiv}."

text11 = f"Gestern habe ich {plhN} getroffen, der/die {plhV} und {plhA} ist."
var11 = f"Gestern habe ich {nomen} getroffen, der/die {verb} und {adjektiv} ist."

text12 = f"Mein größter Traum ist es, {plhN} zu {plhV}. Es wäre so {plhA}."
var12 = f"Mein größter Traum ist es, {nomen} zu {verb}. Es wäre so {adjektiv}."

text13 = f"Jedes Mal, wenn ich {plhN} trage, fühle ich mich {plhA}. Es ist so ähnlich wie z.b.: {plhV}."
var13 = f"Jedes Mal, wenn ich {nomen} trage, fühle ich mich {adjektiv}. Es ist so ähnlich wie z.b: {verb}."

# listen mit allen texten

allvar = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13]

alltext = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13]


# Zufallszahl für die Auswahl des Textes

rds = random.randint(1,13)

# Auswahl des Textes

selvar = allvar[rds]
seltxt = alltext[rds]

#def nextword():
def reload(
    
    text1 = f"Heute war ein {plhA} Tag, und ich habe mich entschieden, {plhN} zu {plhV}.",
    var1 = f"Heute war ein {adjektiv} Tag, und ich habe mich entschieden, {nomen} zu {verb}.",

    text2 = f"Ich habe gestern ein {plhN} gesehen, der {plhV} konnte. Es war wirklich {plhA}.",
    var2 = f"Ich habe gestern einen {nomen} gesehen, der {verb} konnte. Es war wirklich {adjektiv}.",

    text3 = f"Mein Lieblingshobby ist es, {plhN} zu {plhV}. Es macht mich immer {plhA}.",
    var3 = f"Mein Lieblingshobby ist es, {nomen} zu {verb}. Es macht mich immer {adjektiv}.",

    text4 = f"Mein Lieblingsessen ist {plhN} mit {plhV}. Es schmeckt {plhA}.",
    var4 = f"Mein Lieblingsessen ist {nomen} mit {verb}. Es schmeckt {adjektiv}.",

    text5 = f"Der {plhN} nebenan ist wirklich {plhA}. Er/sie {plhV} den ganzen Tag.",
    var5 = f"Der {nomen} nebenan ist wirklich {adjektiv}. Er/sie {verb} den ganzen Tag.",

    text6 = f"Wenn ich könnte, würde ich gerne {plhN} mit einem {plhA} {plhV}.",
    var6 = f"Wenn ich könnte, würde ich gerne {nomen} mit einem {adjektiv} {verb}.",

    text7 = f"Ich liebe es, {plhN} zu {plhV}. Es gibt mir ein Gefühl von {plhA}.",
    var7 = f"Ich liebe es, {nomen} zu {verb}. Es gibt mir ein Gefühl von {adjektiv}.",

    text8 = f"Gestern habe ich {plhN} getroffen, der/die {plhV} und {plhA} ist.",
    var8 = f"Gestern habe ich {nomen} getroffen, der/die {verb} und {adjektiv} ist.",

    text9 = f"Mein Lieblingsfilm ist {plhN}. Es ist so {plhA} und {plhV}.",
    var9 = f"Mein Lieblingsfilm ist {nomen}. Es ist so {adjektiv} und {verb}.",

    text10 = f"Das Beste am Sommer ist, {plhN} zu {plhV}. Es ist so {plhA}.",
    var10 = f"Das Beste am Sommer ist, {nomen} zu {verb}. Es ist so {adjektiv}.",

    text11 = f"Gestern habe ich {plhN} getroffen, der/die {plhV} und {plhA} ist.",
    var11 = f"Gestern habe ich {nomen} getroffen, der/die {verb} und {adjektiv} ist.",

    text12 = f"Mein größter Traum ist es, {plhN} zu {plhV}. Es wäre so {plhA}.",
    var12 = f"Mein größter Traum ist es, {nomen} zu {verb}. Es wäre so {adjektiv}.",

    text13 = f"Jedes Mal, wenn ich {plhN} trage, fühle ich mich {plhA}. Es ist so ähnlich wie z.b.: {plhV}.",
    var13 = f"Jedes Mal, wenn ich {nomen} trage, fühle ich mich {adjektiv}. Es ist so ähnlich wie z.b: {verb}.",

    # listen mit allen texten

    allvar = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13],

    alltext = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13],

    selvar = allvar[rds],
    seltxt = alltext[rds],
):


# Debugg Test ausgabe

#print(selvar)
#print(seltxt)


# GUI - Layouts

layout_s = [
    [sg.Text(fplh)],
    [sg.HorizontalSeparator()],
    [sg.Text(seltxt, background_color='gray', justification='center', size=(200, 1))],
    [sg.HorizontalSeparator()],
    [sg.Button("Ready?")]
]

layout_n = [
    [sg.Text(fplh)],
    [sg.HorizontalSeparator()],
    [sg.Text(seltxt, background_color='gray', justification='center', size=(200, 1))],
    [sg.HorizontalSeparator()],
    [sg.Text("Nomen: "), sg.InputText(key="nomen")],
    [sg.Button("Nächstes Wort")],
]

layout_v = [
    [sg.Text(fplh)],
    [sg.HorizontalSeparator()],
    [sg.Text(seltxt, background_color='gray', justification='center', size=(200, 1))],
    [sg.HorizontalSeparator()],
    [sg.Text("Verb: "), sg.InputText(key="verb")],
    [sg.Button("Weiter")],
]

layout_a = [
    [sg.Text(fplh)],
    [sg.HorizontalSeparator()],
    [sg.Text(seltxt, background_color='gray', justification='center', size=(200, 1))],
    [sg.HorizontalSeparator()],
    [sg.Text("Adjektiv: "), sg.InputText(key="adjektiv")],
    [sg.Button("Bestätigen")],
]

layout_f = [
    [sg.Text(fplh)],
    [sg.HorizontalSeparator()],
    [sg.Text(seltxt, background_color='gray', justification='center', size=(200, 1))],
    [sg.HorizontalSeparator()],
    [sg.Text(selvar, background_color='gray', justification='center', size=(200, 1))],
    [sg.Button("Fertig!")],
]
# GUI - Fenster

window_s = sg.Window("Madlibs by Jack Version 0.1", layout_s)
window_n = sg.Window("Madlibs by Jack Version 0.1", layout_n)
window_v = sg.Window("Madlibs by Jack Version 0.1", layout_v)
window_a = sg.Window("Madlibs by Jack Version 0.1", layout_a)
window_f = sg.Window("Madlibs by Jack Version 0.1", layout_f)

# GUI - Loop

while True:
    event, values = window_s.read()  
    if event == "Ready?":
        window_s.hide()
        event, values = window_n.read()  
    if event == "Nächstes Wort":
        window_n.hide()
        event, values = window_v.read()  
    if event == "Weiter":
        window_v.hide()
        event, values = window_a.read()  
    if event == "Bestätigen":
        window_a.hide()
        reload()
        event, values = window_f.read()  
    if event == "Fertig!":
        window_f.hide()
        break
    if event is None:  # Überprüfung auf Fensterschließung
        break

# GUI - Loop Ende

sg.popup("Danke fürs Spielen!")

# Debugg Test ausgabe

#print(values["nomen"])
#print(values["verb"])
#print(values["adjektiv"])
