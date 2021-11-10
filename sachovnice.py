"""
sachovnice.py
Vytvor program, ktery vykresli sachovnici 
8x8 znaku naplnenou stridave znaky B a W
(jako black a white)
"""

def sachovnice():
	for i in range(1, 9):
		for j in range(1, 9):
			if (i + j) % 2 == 0:
				print("B ", end = "")
			else: 
				print("W ", end = "")

		print()
odpoved = input("Chces vykreslit sachovnice? Ano/ne ")
odpoved = odpoved.lower()

while odpoved == "ano":
	sachovnice()
	print()
	odpoved = input("Chces vykreslit sachovnice? Ano/ne ")
	odpoved = odpoved.lower()


