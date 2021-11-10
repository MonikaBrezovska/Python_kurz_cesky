"""
automat.py
Vytvor program, ktery bude simulovat
hraci automat. Ze sady znaku (srdce, kary, krize, piky) bude generovat tri nahodne znaky.
Dopln bodovani, pokud se vygeneruji tri stejne znaky, 
prictou se body.
Po vypisu tri znaku se program uzivatele zepta, zdali chce pokracovat.
Na konec vypis pocet bodu.
"""

import random

seznam = ["srdce", "kary", "krize", "piky"]

body = 0
kola = 0
pokracovani = "ANO"

while pokracovani == "ANO":
	los = []
	kola = kola + 1
	for i in range(0, 3):
		los.append(random.choice(seznam))

	print(los)
	if los[0] == los [1] == los[2]:
		print("Shoda 3 znaku.")
		body = body + 1
	else:
		print("Neni shoda.")

	pokracovani = input("Pro pokracovani napis \"ano\": ")
	pokracovani = pokracovani.upper()

if kola > 0:
	print(f"Hral/a jsi {kola} kol.")
	print(f"Ziskala jsi {body} bodu.")
	
