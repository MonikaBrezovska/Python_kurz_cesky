"""
sudaLicha.py
Vytvor program, ktery dle zadaneho 
cisla vyhodnoti, zdali je sude ci liche.

vstup: cislo
vystup: suda/licha

suda cisla jsou delitelna 2 beze zbytku, tzn. 
zbytek po deleni cislem 2 je roven nule

zbytek = cislo % 2
kdyz zbytek == 0, tak cislo je sude
jinak je cislo liche
"""

cislo = int(input("Zadej cele cislo: "))

if cislo % 2 == 0:
	print("Cislo je sude.")
else: 
	print("Cislo je liche.")
	