"""
pyramida.py
Vytvor program, ktery dle vlozeneho 
prirozeneho cisla vykresli pyramidu.
pr.:	vstup = 3
		vystup:

o
oo
ooo

"""

def pyramida(cislo):
	for i in range(1, cislo + 1):
		print("o" * i)

a = int(input("Zadej prirozene cislo: "))

if a > 0:
	pyramida(a)
else: 
	print("Nebylo zadano prirozene cislo. ")

