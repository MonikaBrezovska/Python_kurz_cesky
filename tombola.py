"""
tombola.py
K cenam tomboly losuj jmeno osoby, 
ktera cenu vyhrava.
Mej dva seznamy: ceny tomboly
(postupne prochazej ceny od posledni po prvni) 
a seznam osob. K cene tomboly 
nahodne vybirej ze seznamu osob.
"""
import random

ceny = ["auto", "kolo", "popelnice", "poukaz", "vino", "pivo"]
lide = ["Adam", "Bozena", "Cecilie"]

zacatek = len(ceny) - 1
konec = -1
krok = -1

for i in range(zacatek, konec, krok):
	vyherce = random.choice(lide)
	print(f"Cenu {ceny[i]} vyhrava {vyherce}.")








