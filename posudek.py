"""
posudek.py
Vytvorte algoritmus pro posouzeni, zdali 
lze dve vlozene celociselne hodnoty 
delit beze zbytku. Vystupem programu bude jeden 
ze dvou stavu: Lze delit beze zbytku, 
nelze delit beze zbytku.

vstup: delenec, delitel
vystup: lze/nelze delit beze zbytku
"""

delenec = int(input("Zadej hodnotu delence: "))
delitel = int(input("Zadej hodnotu delitele: "))

if delitel != 0:
	zbytek = delenec % delitel
	
	if zbytek == 0:
		print("Cisla lze delit beze zbytku.")
	else:
		print("Cisla nelze delit beze zbytku.")
else: 
	print("Nulou nelze delit!")