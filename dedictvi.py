"""
dedictvi.py
Vytvor algoritmus pro rozdeleni majetku 
mezi libovolny pocet potomku. Hodnota
majetku bude zadana v CZK, Vystupem progamu 
bude celociselna castka v CZK pripadajici na 1 potomka, 
a nerozdeleny zbytek v CZK.

Vstup: majetek v CZK, pocet potomku
vystup: podil, zbytek po rozdeleni
"""
majetek = int(input("Zadej castku pro rozdeleni: "))
deti = int(input("Zadej pocet deti: "))

if (deti > 0) and (majetek > 0):
	podil = majetek // deti
	zbytek = majetek % deti

	print(f"Podil: {podil} CZK")
	print(f"Zbytek: {zbytek} CZK")
else: 
	if deti <= 0:
		print("Nemas deti, nema kdo dedit.")
	else:
		print("Nemas majetek, neni co rozdelit.")

