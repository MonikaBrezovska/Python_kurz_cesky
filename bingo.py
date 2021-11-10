"""
bingo.py
Zahrajeme si zjednodusene bingo.
Hraci pole 5 x 5 napln cisly 1-75
(vzdy po peti cislech ze skupin:
1-15, 16-30, 31-45, 46-60 a 61-75);
bud je zada uzivate nebo je nahodne vygeneruj.
Vylosuj 25 nahodnych cisel 1-75, 
kontroluj, zdali se tvuj tip shoduje s losovanymi cisly.
Nakonec vypis pocet shodnych cisel.
"""

import random

zacatek = 1
konec = 15

hrac = []

for i in range(0, 5):
	for j in range(0, 5):
		cislo = random.randint(zacatek, konec)
		while cislo in hrac:
			cislo = random.randint(zacatek, konec)
		hrac.append(cislo)
		print(f"{cislo:>4}", end = "")
	zacatek = zacatek + 15
	konec = konec + 15
	print()

print("\n-------------------------------\n")

bingo = []
for i in range(0, 25):
	cislo = random.randint(1, 75)
	while cislo in bingo:
		cislo = random.randint(1, 75)
	bingo.append(cislo)
	print(f"{cislo:>4}", end = "")
	if (i + 1) % 5 == 0:
		print()


print("\n-------------------------------\n")

shoda = []
for cislo in bingo:
	if cislo in hrac:
		shoda.append(cislo)

if len(shoda) > 0:
	print("Gratulujeme k vyhre!")
	print(f"Shoda v {len(shoda)} cislech.")
	print(f"Vypis: {shoda}.")
else:
	print("Bohuzel jsi nevyhral/a.")