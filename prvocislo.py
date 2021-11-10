"""
prvocislo.py
Vytvor program, ktery vyhodnoti, zdali je 
vlozene cislo prvocislo.
Prvocisla maji prave dva delitele, 
jsou delitelna pouze 1 a sami sebou.


cislo = input("Vloz cislo: ")

if cislo.isdigit() and int(cislo) > 0:
	cislo = int(cislo)
	delitele = []
	for i in range(1, cislo + 1):
		if cislo % i == 0:
			delitele.append(i)
	print(f"Delitele: {delitele}")
	if len(delitele) == 2:
		print(f"Cislo {cislo} je prvocislo.")
	else:
		print(f"Cislo {cislo} neni prvocislo.")
else: 
	print("Nebylo zadano kladne cislo.:")
"""
"""
Vytvor program, ktery vyhodnoti prvnich "x" prvocisel.
Prvocisla ukladej do seznamu a na konci jej vypis.
"""

x = int(input("Zadej, kolik prvocisel chces vypsat: "))

cislo = 1
prvocisla = []

while len(prvocisla) < x:
	delitele = []
	for i in range(1, cislo + 1):
		if cislo % i == 0:
			delitele.append(cislo)
	if len(delitele) == 2:
		prvocisla.append(cislo)
	cislo = cislo + 1

print(f"Prvnich {x} prvocisel je {prvocisla}.")

