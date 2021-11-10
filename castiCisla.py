"""
castiCisla.py
Vytvor algoritmus, ktery dle zadaneho desetinneho 
cisla vypise jeho celou a desetinnou cast.
Pouzij dve reseni - s a bez fenkce knihovny math.

vstup: desetinne cislo
vystup: cela a desetinna cast cisla

1.) vstup, pr. 6.2
2.) vypocet bez funkce:
		6 = int(6.2)
		0.2 = 6.2 - 6
	vypocet s funkci:
		math.modf()
3.) vypis vysledku, pr. 6.2 = 6 + 0.2
"""

import math

cislo = float(input("Zadej desetinne cislo: "))
cele1 = int(cislo)
desetinne1 = cislo - cele1
print(cislo, "=", cele1, "+", round(desetinne1, 2))

desetinne2, cele2 = math.modf(cislo)
# ulozeni hodnot do vice promennych
# vzniksji tim n-tice (datovy typ tuple)
desetinne2 = round(desetinne2, 2)
print(cislo, "=", cele2, "+", desetinne2)

