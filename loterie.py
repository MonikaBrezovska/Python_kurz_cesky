"""
loterie.py
Vytvor program, ktery vygeneruje "x"
unikatnich cisel v rozsahu 1-80. Cisla ukladej do seznamu.
"""

import random

x = int(input("Zadej pocet cisel ke generovani: "))
seznam = []
i = 0

if x in range(1, 81):
	while i < x:
		cislo = random.randint(1, 80)
		if cislo not in seznam:
			seznam.append(cislo)
			i = i + 1
	print(seznam)
else: 
	print("Pocet musi byt v rozsahu 1--80.")


