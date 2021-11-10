"""
vazenyPrumer.py
Vytvor program, ktery na vstupu ziska dve stejne velka
pole -- hodnoty a k nim odpovidajici vahy. Na vystupu vypise 
hodnotu vazeneho prumeru.
"""
def vazenyPrumer(hodnoty, vahy):
	suma = 0
	for i in range(0, len(hodnoty)):
		suma += hodnoty[i] * vahy[i]
	prumer = suma / sum(vahy)
	return prumer

hodnoty = []
vahy = []

pocet = int(input("Kolik hodnot chces zadat? Napis: "))
for i in range(0, pocet):
	print(f"\n{i + 1}.dvojice: ")
	hodnoty.append(int(input("Zadej hodnotu: ")))
	vahy.append(int(input("Zadej vahu: ")))

# hodnoty = [1, 2, 3, 4, 5]
# vahy = [1, 1, 1, 1, 1, 10]

print(f"Vazeny prumer je: {vazenyPrumer(hodnoty, vahy)}")

