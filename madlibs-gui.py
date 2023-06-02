#
#  Author / First Contributor: Jack Ruder
#
# Contributors: Jack Ruder , None
#

import tkinter as tk
import customtkinter as ctk
import random
import time

# PLaceholder wortarten für übersicht

nomen = None
verb = None
adjektiv = None

# Platzhalter Listen + vlgtext 

fplh = "Fülle die Lücken mit den Jeweiligen Adjektiven, Verben und Nomen.  Viel Glück!"
plhN = "_Ein Nomen_"
plhV = "_Ein Verb_"
plhA = "_Ein Adjektiv_"
plhnrm = ""
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
selvar = None
seltext = None


# Zufallszahl für die Auswahl des Textes

rds = random.randint(1,13)

# Madlib listen

def reload():
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

    alltext = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13]

    seltxt = alltext[rds]
    allvar = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13]
    selvar = allvar[rds]

    return selvar, seltxt

#Reload Funktion
#
#selvar, seltxt = reload()
#print(rds)
#print(selvar)
#print(seltxt)

# Einstellungen

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

gui = ctk.CTk()
gui.geometry("780x420")
gui.title("Madlibs")
gui.resizable(False, False)

gui.mainloop()




#print(values["nomen"])
#print(values["verb"])
#print(values["adjektiv"])
