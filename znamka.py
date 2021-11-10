"""
znamka.py
Uzivatel zada cele cislo.
Program bude vyhodnocovat, zdali se 
jedna/nejedna o skolni znamku.
(tzn. o cislo v rozsahu 1 az 5).
Vyuzij co nejvice moznosti reseni:
	slozene podminky, 
	logicke spojky, 
	rozsahy.
"""

x = int(input("Zadej cele cislo: "))

# slozene podminky
if x < 1: 
	print("Neni znamka.")
elif x <= 5:
	print("Je znamka.")
else:
	print("Neni znamka.")

# logicke spojky (spojka AND)
if x >= 1 and x <= 5:
	print("Je znamka.")
else:
	print("Neni znamka.")

# logicke spojky (spojka OR) 
if x < 1 or x > 5: 
	print("Neni znamka.")
else:
	print("Je znamka.")

# rozsahy
if x in range(1, 6):
	print("Je znamka.")
else:
	print("Neni znamka.")

if x not in range(1, 6):
	print("Neni znamka.")
else: 
	print("Je znamka.")
	