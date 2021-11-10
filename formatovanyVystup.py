"""
formatovanyVystup.py
Využij dnešní znalosti formátovaného 
výstupu a cyklu, abys vytvořil/a program,
který vypíše 0. až 10. mocninu vloženého
jednociferného přirozeného čísla (tzn. 
v úvahu připadá číslo 1 až 9; prozatím 
nemusíš ošetřit podmínkou) formátovanou 
některým z pythonních způsobů 
(tzn. f, nebo format) zarovnané doprava 
a s předřazenými nulami.
 
vstup: přirozené číslo (1 až 9)
výstup: 0. až 10. mocnina čísla
 
1.) načteme hodnotu
2.) výpočet v cyklu
	pro mocniny od 0. do 10. vypisuj mocninu čísla
"""
 
cislo = int(input("Zadej přirozené číslo: "))
if cislo in range(1, 10):
	for i in range(0, 11):
		mocnina = pow(cislo, i)
		print(f"{i>2}: {mocnina:>010}")
else:
	print("Nebylo zadáno přirozené číslo.")
