"""
sibenice.py
Vytvor hru sibenice.
Do promenne si uloz "tajne" slovo a pomocnou promennou
si napln treba hvezdickami (jako mista pro pismena).
Uzivatel pak bude zadavat pismena, pokus bude pismeno
v tajnem slove, prepis hvezdicku na dane pismeno.
Pocitej trestne body.
"""

slovo = "listopad"
sifra = "*" * len(slovo)
trestneBody = 0 

while sifra != slovo:
	print(sifra)
	znak = input("Zadej znak: ")
	sifra = list(sifra)
	if znak in slovo:
		for i in range(0, len(slovo)):
			if slovo[i] == znak:
				sifra[i] = znak
	else: 
		print("Hadej dal...")
		trestneBody += 1
	sifra = "".join(sifra)

print(sifra)
print(f"Pocet trestnych bodu: {trestneBody}. ")