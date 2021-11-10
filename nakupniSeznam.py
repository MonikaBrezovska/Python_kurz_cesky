"""
nakupniSeznam.py
Vytvor algoritmus, ktery do seznamu
ulozi "x" polozek seznamu pro nakup.
Kontroluj, aby se polozky v seznamu neopakovaly.
Polozky seznamu vypis pred a po setrideni.
"""

x = int(input("Zadej pocet polozek seznamu: "))

if x > 0:
	seznam = []
	i = 0
	while i < x:
		polozka = input(f"Zadej {i + 1}. polozku:")
		polozka = polozka.lower()
		if i == 0:
		 	seznam.append(polozka)
		 	i = i + 1
		else:
		 	if polozka in seznam:
		 		print(f"{polozka} uz v seznamu mas!")
		 	else:
		 		seznam.append(polozka)
		 		i = i + 1

for abc in seznam:
	print(abc)

seznam.sort()

for abc in seznam:
	print(abc)

		 		