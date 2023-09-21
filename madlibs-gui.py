#
#  Author / First Contributor: Jack Ruder
#
# Contributors: Jack Ruder , None
#

import tkinter as tk
import customtkinter as ctk
import random
from tkinter import ttk
from tkinter import Grid
from tkinter import random

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
seltxt = None
rds = None

# Madlib listen

def reload():

    global selvar
    global seltxt
    global rds
    global text1
    global text2
    global text3
    global text4
    global text5
    global text6
    global text7
    global text8
    global text9
    global text10
    global text11
    global text12
    global text13
    global var1
    global var2
    global var3
    global var4
    global var5
    global var6
    global var7
    global var8
    global var9
    global var10
    global var11
    global var12
    global var13
    global plhN
    global plhV
    global plhA
    global nomen
    global verb
    global adjektiv
    global plhnrm
    global fplh



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


def save_nomen():
    global nomen
    nomen = nomenscreen_nomen.get()

def save_verb():
    global verb
    verb = verbscreen_verb.get()

def save_adjektiv():
    global adjektiv
    adjektiv = adjektivscreen_adjektiv.get()




# Setup und Debug



# Einstellungen

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

firstscreen = ctk.CTk()
firstscreen.geometry("1280x720")
firstscreen.title("Madlibs")
firstscreen.resizable(False, False)

auswahlshow = ctk.CTk()
auswahlshow.geometry("1280x720")
auswahlshow.title("Madlibs")
auswahlshow.resizable(False, False)

nomenscreen = ctk.CTk()
nomenscreen.geometry("1280x720")
nomenscreen.title("Madlibs --- Nomen")
nomenscreen.resizable(False, False)

verbscreen = ctk.CTk()
verbscreen.geometry("1280x720")
verbscreen.title("Madlibs --- Verb")
verbscreen.resizable(False, False)

adjektivscreen = ctk.CTk()
adjektivscreen.geometry("1280x720")
adjektivscreen.title("Madlibs --- Adjektiv")
adjektivscreen.resizable(False, False)

endscreen = ctk.CTk()
endscreen.geometry("1280x720")
endscreen.title("Madlibs")
endscreen.resizable(False, False)


def reroll():
    global rds
    global auswahlshow
    global nomenscreen
    global verbscreen
    global adjektivscreen
    global endscreen
    global selvar
    global seltxt
    rds = random.randint(0,12)
    reload()
    auswahlshow.update(self=seltxt)
    nomenscreen.update(self=seltxt)
    verbscreen.update(self=seltxt)
    adjektivscreen.update(self=seltxt)
    endscreen.update(self=selvar)
    print(rds)
    print(selvar)
    print(seltxt)

reroll()
print(rds)
print(selvar)
print(seltxt)

#
#    --- UI ---
#

# firstscreen
titel = ctk.CTkLabel(firstscreen, text="Madlibs")

firstscreen_Start = ctk.CTkButton(firstscreen, text="Start", command=lambda: [firstscreen.withdraw(), auswahlshow.deiconify()])
firstscreen_beenden = ctk.CTkButton(firstscreen, text="Beenden", command=lambda: [firstscreen.destroy(), auswahlshow.destroy(), nomenscreen.destroy(), verbscreen.destroy(), adjektivscreen.destroy(), endscreen.destroy()])

# auswahlshow
auswahlshow_Titel = ctk.CTkLabel(auswahlshow, text="Madlibs")
auswahlshow_glhf = ctk.CTkLabel(auswahlshow, text=fplh)
auswahlshow_Reroll = ctk.CTkButton(auswahlshow, text="Reroll", command=lambda: [reroll()])
auswahlshow_text = ctk.CTkLabel(auswahlshow, text=seltxt)
auswahlshow_zurueck = ctk.CTkButton(auswahlshow, text="Zurück", command=lambda: [auswahlshow.withdraw(), firstscreen.deiconify()])
auswahlshow_weiter = ctk.CTkButton(auswahlshow, text="Weiter", command=lambda: [auswahlshow.withdraw(), nomenscreen.deiconify()])

# nomenscreen
nomenscreen_Titel = ctk.CTkLabel(nomenscreen, text="Tippe ein passendes Nomen ein")
nomenscreen_text = ctk.CTkLabel(nomenscreen, text=seltxt)
nomenscreen_nomen = ctk.CTkEntry(nomenscreen, textvariable=nomen)
nomenscreen_zurueck = ctk.CTkButton(nomenscreen, text="Zurück", command=lambda: [nomenscreen.withdraw(), auswahlshow.deiconify()])
nomenscreen_weiter = ctk.CTkButton(nomenscreen, text="Weiter", command=lambda: [nomenscreen.withdraw(), save_nomen(), verbscreen.deiconify()])

verbscreen_Titel = ctk.CTkLabel(verbscreen, text="Tippe ein passendes Verb ein")
verbscreen_text = ctk.CTkLabel(verbscreen, text=seltxt)
verbscreen_verb = ctk.CTkEntry(verbscreen, textvariable=verb)
verbscreen_zurueck = ctk.CTkButton(verbscreen, text="Zurück", command=lambda: [verbscreen.withdraw(), nomenscreen.deiconify()])
verbscreen_weiter = ctk.CTkButton(verbscreen, text="Weiter", command=lambda: [verbscreen.withdraw(), save_verb(), adjektivscreen.deiconify()])

adjektivscreen_Titel = ctk.CTkLabel(adjektivscreen, text="Tippe ein passendes Adjektiv ein")
adjektivscreen_text = ctk.CTkLabel(adjektivscreen, text=seltxt)
adjektivscreen_adjektiv = ctk.CTkEntry(adjektivscreen, textvariable=adjektiv)
adjektivscreen_zurueck = ctk.CTkButton(adjektivscreen, text="Zurück", command=lambda: [adjektivscreen.withdraw(), verbscreen.deiconify()])
adjektivscreen_weiter = ctk.CTkButton(adjektivscreen, text="Weiter", command=lambda: [adjektivscreen.withdraw(), save_adjektiv(), reload(), endscreen.update(), endscreen.deiconify()])

endscreen_Titel = ctk.CTkLabel(endscreen, text="Madlibs")
endscreen_text = ctk.CTkLabel(endscreen, text=selvar)
endscreen_danke = ctk.CTkLabel(endscreen, text="Danke fürs Spielen!")
endscreen_zzstart = ctk.CTkButton(endscreen, text="Zum Start", command=lambda: [endscreen.withdraw(), reroll(), firstscreen.deiconify()])
endscreen_beenden = ctk.CTkButton(endscreen, text="Beenden", command=lambda: [endscreen.destroy(), firstscreen.destroy(), auswahlshow.destroy(), nomenscreen.destroy(), verbscreen.destroy(), adjektivscreen.destroy()])



#
# Verpackung :)
#

titel.pack(pady=10)
firstscreen_Start.pack(pady=10)
firstscreen_beenden.pack(pady=10)

auswahlshow_Titel.grid(row=0, column=2, pady=10)
auswahlshow_glhf.grid(row=1, column=2, pady=10)
auswahlshow_text.grid(row=2, column=2, pady=10)
auswahlshow_zurueck.grid(row=3, column=1, pady=10)
auswahlshow_Reroll.grid(row=3, column=2, pady=10)
auswahlshow_weiter.grid(row=3, column=3, pady=10)

nomenscreen_Titel.grid(row=0, column=2, pady=10)
nomenscreen_text.grid(row=1, column=2, pady=10)
nomenscreen_nomen.grid(row=2, column=2, pady=10)
nomenscreen_zurueck.grid(row=3, column=1, pady=10)
nomenscreen_weiter.grid(row=3, column=3, pady=10)

verbscreen_Titel.grid(row=0, column=2, pady=10)
verbscreen_text.grid(row=1, column=2, pady=10)
verbscreen_verb.grid(row=2, column=2, pady=10)
verbscreen_zurueck.grid(row=3, column=1, pady=10)
verbscreen_weiter.grid(row=3, column=3, pady=10)

adjektivscreen_Titel.grid(row=0, column=2, pady=10)
adjektivscreen_text.grid(row=1, column=2, pady=10)
adjektivscreen_adjektiv.grid(row=2, column=2, pady=10)
adjektivscreen_zurueck.grid(row=3, column=1, pady=10)
adjektivscreen_weiter.grid(row=3, column=3, pady=10)

endscreen_Titel.grid(row=0, column=2, pady=10)
endscreen_text.grid(row=1, column=2, pady=10)
endscreen_danke.grid(row=2, column=2, pady=10)
endscreen_zzstart.grid(row=3, column=1, pady=10)
endscreen_beenden.grid(row=3, column=3, pady=10)

# Mainloop

firstscreen.mainloop()

# Ende

# Copyrigt 2023 by Jack Ruder
