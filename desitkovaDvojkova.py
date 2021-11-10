"""
desitkovaDvojkova.py
Vytvor program pro prevod cisla
z desitkove soustavy do dvojkove soustavy.
"""
cislo = int(input("Zadej cislo: "))
x = cislo
seznam = []

while x > 0:
	zbytek = x % 2
	seznam.append(zbytek)
	x = x // 2

start = len(seznam) - 1
stop = -1
krok = -1

for i in range(start, stop, krok):
	print(seznam[i], end = "")
