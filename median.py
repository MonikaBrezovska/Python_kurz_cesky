"""
median.py
Vytvor program, ktery na vstupu ziska pole cisel a na vystupu vrati jeho median. Wikipedia: ... staci hodnoty seradit podle velikost a vzit hodnotu, ktera se naleza uprostred seznamu.
Pokud ma soubor sudy pocet prvk;, obvykle se za median oznacuje aritmeticky prumer hodnot na mistech n/2 a n/2+1.
"""

def median(seznam):
	seznam.sort()
	pocetPrvku = len(seznam)
	if pocetPrvku % 2 != 0:
		# [1, 2, 3, 4, 5], pocetPrvku = 5, median = [2], 2 = 5 // 2
		# [1, 2, 3], pocetPrvku = 3, median = [1], 1 = 3 // 2
		median = seznam[pocetPrvku // 2]
	else: 
		# [1, 2, 3, 4], pocetPrvku = 4, median = ([1] + [2]) / 2
		# [2] = 4 // 2, [1] = [2] - 1
		x = pocetPrvku // 2
		median = (seznam[x] + seznam[x - 1]) / 2
	return median

seznam = []

pocet = int(input("Zadej pocet prvk; seznamu: "))

for i in range(0, pocet):
	seznam.append(int(input(f"{i + 1}. prvek seznamu: ")))

print(median(seznam))