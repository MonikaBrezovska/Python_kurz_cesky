"""
trojuhelnik.py
Vytvor program, ktery na vstupu ziska prirozene cislo, a na vystupu vuykresli tvar rovnostranneho trojuhelniku.
Pr. 	vstup = 4
		vystup: 

   o
  o o 
 o o o
o o o o 

"""

def trojuhelnik(delka):
	for i in range(1, delka + 1):
		print(" " * (delka - i) + "o " * i)

a = int(input("Zadej delku podstavy: "))
trojuhelnik(a)
