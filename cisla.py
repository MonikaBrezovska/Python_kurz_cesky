"""
cisla.py
Vytvor program pro postupne nacitani cisel
a vyhodnot jejich soucet, minimum a maximum.
Radu cisel ukonci cislice 0.
"""

cislo = int(input("Zadej cislo: "))
suma = 0
i = 0 

while cislo != 0:
	i = i + 1
	suma = suma + cislo
	if i == 1:
		min = cislo
		max = cislo
	else:
		if cislo < min:
			min = cislo
		elif cislo > max:
			max = cislo
	cislo = int(input("Zadej cislo: "))

if i > 0:
	print(f"\nSoucet je: {suma}.")
	print(f"Prumer je: {suma / i:.2f}.")
	print(f"Minimum je: {min}.")
	print(f"Maximum je: {max}.")

