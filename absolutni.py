"""
absolutni.py
Vytvor algoritmus pro vyhodnoceni absolutni hodnoty.
Vstupem algoritmu bude celocielna hodnota.
Absolutni hodnotu vyhodnocuj bez uziti funkce knihovny math.

vstup: cislo
vystup: absolutni hodnota cisla
"""

cislo = int(input("Zadej cislo: "))

if cislo < 0:
	absolutni = cislo * (-1)
else:
	absolutni = cislo
	
print(f"|{cislo}| = {absolutni}")

