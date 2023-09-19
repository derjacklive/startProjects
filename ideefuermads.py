#
# Copyright Jack Ruder
#
import random
import os
import time


global vocde
global voclat
global vocmax
global vocindex
global answer

vocde =["Herreszug", "Kathager", "Rede", "Reise"]
voclat = ["agmen", "poneos", "oratio", "iter"]
vocmax = 3
vocmin =0
vocindex = 0
answer = "Herreszug"


def standartlists():
    vocde = ["Herreszug", "Kathager", "Rede", "Reise"]
    voclat = ["agmen", "poneos", "oratio", "iter"]
    # Die erste vokabel ist immer index 0

def calclist():
    vocmax = len(vocde) - 1
    vocmin = 0


def startup():
    os.system("cls")
    print("Vokabeltrainer\n\n\nWählen sie aus\n(1) Lernen sie eine Bestimmte Vokabel\n(2) Lernen sie eine zufällige Vokabel\n(3) Lernen sie alle Vokabeln\n(4) Fügen sie eine Vokabel hinzu\n(5) Löschen sie eine Vokabel")
    mainmauswahl = input("Ihre Auswahl: ")
    if (mainmauswahl == "1"):
        vocselect()
    elif (mainmauswahl == "2"):
        vocrandom()
    elif (mainmauswahl == "3"):
        vocall()
    elif (mainmauswahl == "4"):
        vocadd()
    elif (mainmauswahl == "5"):
        vocdel()
    else:
        print("Sie haben eine ungültige Auswahl getroffen\nBitte achten sie das sie nur Zahlen angeben")
        startup()

def learnloop():
    os.system("cls")
    print(f"Vokabeltrainer\n\n\nFrage\n\nWas ist {voclat[vocindex]} auf Deutsch?")
    answer = input("Antwort: ")
    if (answer == vocde[vocindex]):
        print("Richtig")
        time.sleep(5)
    else:
        print("Falsch")
        print(f"Die richtige Antwort wäre {vocde[vocindex]} gewesen")
        time.sleep(5)


def vocselect():
    os.system("cls")
    calclist()
    print(f"Vokabeltrainer\n\n\nAktuelle Vokabeln\n")
    for i in range(vocmin, vocmax):
        print(f"{i} {vocde[i]} {voclat[i]}")
    print(f"\nGeben sie einen Index zwischen {vocmin} und {vocmax} ein")
    vocindex = input("Ihre Auswahl: ")
    learnloop()
    startup()

def vocrandom():
    os.system("cls")
    calclist()
    vocindex = random.randint(vocmin, vocmax)
    learnloop()
    startup()

def vocall():
    os.system("cls")
    calclist()
    for i in range(vocmin, vocmax):
        vocindex = i
        learnloop()
    startup()

def vocadd():
    os.system("cls")
    calclist()
    print(f"Vokabeltrainer\n\n\nAktuelle Vokabeln\n")
    for i in range(vocmin, vocmax):
        print(f"{i} {vocde[i]} {voclat[i]}")
    print("\nGeben sie eine Deutsche Vokabel ein die sie hinzufügen wollen")
    vocde.append(input("Deutsche Vokabel: "))
    print("Geben diese Vokabel auf Latein ein")
    voclat.append(input("Lateinische Vokabel: "))
    startup()

def vocdel():
    os.system("cls")
    calclist()
    print(f"Vokabeltrainer\n\n\nAktuelle Vokabeln\n")
    for i in range(vocmin, vocmax):
        print(f"{i} {vocde[i]} {voclat[i]}")
    print("\nGeben sie den Index der Vokabel ein die sie löschen wollen")
    vocindex = input("Ihre Auswahl: ")
    vocde.pop(vocindex)
    voclat.pop(vocindex)

standartlists()
startup()
