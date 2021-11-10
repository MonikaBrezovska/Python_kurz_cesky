"""
vypisCisel.py
Pomoci cyklu vypis cisla od -x" do "+x", 
pricemz hodnotu "x" zada uzivatel na vstupu.
Cisla budou formatovana nasledovne:
zaporna cisla se dvema desetinnymi misty;
nula a kladna zarovnana doprava a s predrazenymi nulami.

vstup: x
vystup: cisla od -x do +x

1.) nacteni "x" 
2.) opakovani vypisu cisel od -x do +x
	potrebuji vypo49tat +x (tzn. x * (-1))
"""

x = int(input("Zadejte cislo x: "))

zacatek = x * (-1)
konec = x

for i in range(zacatek, konec + 1):
	if i < 0:
		print(f"{i:0.2f}")
	else: 
		print(f"{i:>10}")		

