"""
nakup.py
Napis program, ktery nacte nazvy komodit, 
ktere uzivatel nakoupil. Dale nacte mnozstvi, 
ktere za kazdou komoditu nakoupil.
Nakonec do prehledne tabulky vypise ucet, 
napr.: 
mleko		2 * 20.00 = 	40.00
brambory	0.5 * 15.00 =	7.50
pivo		10 * 8.50 = 	85.00
"""

zbozi = input("Zadej zbozi: "), input("Zadej zbozi: "), input("Zadej zbozi: ")
mnozstvi = int(input("Zadej mnozstvi: ")), int(input("Zadej mnozstvi: ")), int(input("Zadej mnozstvi: "))
cena = 20, 30, 40 

pocet = len(zbozi)

for i in range(0, pocet):
	print(f"{zbozi[i]:<10} {mnozstvi[i]:>4} * {cena[i]:>4} = {cena[i] * mnozstvi[i]:>6}")