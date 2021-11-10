"""
malaNasobilka.py
Vytvor program, ktery vypise malou nasobilku, 
tzn. prvnich 10 nasobku cisel 1 az 10.
Nasobilku formatuj vzhledove do tabulky.
"""

def nasobilka(cislo1, cislo2):
	for i in range(1, cislo1 + 1):
		for j in range(cislo2 + 1):
			print(f"{i * j:>4}", end = "")
		print()

a, b = int(input("Zadej cislo: ")), int(input("Zadej cislo: "))
nasobilka(a, b)

