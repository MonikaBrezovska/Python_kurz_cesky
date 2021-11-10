"""
tabulka.py
Vytvor program, ktery vygeneruje tabulku o poctu radku a sloupcu
"a" x "b" naplnenou nahodnymi znaky A-Z.

a....radky
b....sloupce
"""

import random

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a = int(input("Zadej pocet radku: "))
b = int(input("Zadej pocet sloucu: "))

if a > 0 and b > 0:
	for i in range(0, a):
		for j in range(0, b): 
			print(random.choice(abc) + " ", end = "")
		print()
else: 
	print("Nebyla zadana kladna cisla.")