import time
import sys
from time import sleep

goed = ("goed") or ("Goed") or ("lekker") or ("Lekker") or ("Prima") or ("prima")
slecht = ("slecht") or ("Slecht") or ("kut") or ("Kut") or ("Niet zo goed") or ("niet zo goed") or ("ruk")

print("Welkom!")

naam = input("Wat is je naam? ")
time.sleep(0.5)
print("Hallo " + naam + ",")
time.sleep(0.5)
feel = input("Hoe gaat het met jou?  ")

if feel == goed:
    print("Dat is fijn om te horen")
else:
    print("Dat is dan mooi kut voor je, maar niet echt mijn probleem, vind je wel " + naam + "?")
