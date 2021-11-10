"""
znamky.py
Vytvor program pro postupne zadavani znamek, 
tzn, celych cisel v rozsahu 1-5. Pokud uzivatel
zada cislo mimo rozsah, cyklus bude ukoncen.
Vypis, kolik znamek uzivatel zadal.
"""

znamka = int(input("Zadej 1. znamku: "))

i = 0
suma = 0
seznam = []

while znamka in range(1, 6):
	seznam.append(znamka) 
	i = i + 1
	suma = suma + znamka
	znamka = int(input(f"Zadej {i + 1}. znamku: "))

if i > 0:
	print(f"Bylo zadano {i} znamek.")
	print(f"Prumerna znamka je {suma / i:.2f}.")

if len(seznam) > 0:
	print(f"{sum(seznam)}, {len(seznam)}, {min(seznam)}, {max(seznam)}")
	print(seznam)