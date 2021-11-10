"""
nahoda.py
Vytvor program, ve kterem si vyzkousis
nektere funkce knihovny random.
Program zkombinuj s cykly a seznamy.
Napr.:
 - generovani cisla;
 - vyber nahodneho znaku/prvku z/ze retezce/seznamu;
 - promichavani polozek seznamu;
 - generovani nahodnych "x" polozek seznamu.
 """

import random
"""
for i in range(0, 5):
 	cislo = random.random()
 	print(cislo)
"""
seznam = []
"""
for i in range(0, 10):
 	seznam.append(random.randint(1, 10))


i = 0
while i < 10:
	cislo = random.randint(1, 10)
	if cislo not in seznam:
		seznam.append(cislo)
		i = i + 1

seznam.sort()
for polozka in seznam:
	print(polozka)

random.shuffle(seznam)
for polozka in seznam:
	print(polozka)

print(f"Nahodna polozka: {random.choice(seznam)}")


s = "ABCDEF"
print(random.choice(s))

seznam = list(s)
print(seznam)
random.shuffle(seznam)
print(seznam)
"""

x = int(input("Zadej pocet polozek seznamu: "))

for i in range(0, x):
	seznam.append(random.randint(1, 10))

print(seznam)










