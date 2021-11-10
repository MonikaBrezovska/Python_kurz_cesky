"""
darkomat.py
Blizi se Vanoce a kazdy ve firme prichysta pozornost pro jednoho kolegu.
Nesmi se stat, ze by daval darek sam sobe.
Vypisuj, kdo komu pripravi darek na vanocni vecirek.
Priprav se dva identicke seznamy osob ve firme.
Vyuzivej prikaz pro smazani polozky ze seznamu.
"""

import random

lide = ["Adam", "Bob", "Cirda", "Dana", "Eva", "Fanynka", "Gusta"]
kopie = lide.copy()

for clovek in lide:
	proKoho = random.choice(kopie)
	while proKoho == clovek:
		proKoho = random.choice(kopie)
	print(f"{clovek} pripravi darek pro {proKoho}")
	kopie.remove(proKoho)
	 