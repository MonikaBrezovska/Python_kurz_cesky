""" 
cykly.py
S uzitim cyklu "for" a "while" vypis vzestupnou
radu celych cisel v rozsahu od "a" do "b".
Krajni hodnoty rozsah; budou na4teny na vstupu
od uzivatele.

Rozsireni:
cisla spravne serad, tzn. cyklus bude zacinat 
na mensim z cisel a koncit na vetsim z cisel, 
vyhodnocuj pocet sudych a lichych cisel v rozsahu, 
vyhodnot prumer vypsanych cisel.

vstup: a, b
vystup: vzestupna rada cisel od "a" do "b"
"""
a, b = int(input("Zadej hodnotu \"a\":")), int(input("Zadej hodnotu \"b\":"))

zacatek = 0
konec = 0 

if a < b:
	zacatek = a
	konec = b
elif b < a:
	zacatek = b
	konec = a
else:
	print("Nebyla zadana ruzna cisla, cyklus se neprovede. ")

if zacatek != konec:
	suma = 0
	licha = 0
	for i in range(zacatek, konec + 1):
		print(i)
		suma = suma + i
		if i %2 != 0:
			licha = licha + 1

	print(f"Prumer je {suma / (konec - zacatek + 1)}.")
	print(f"Pocet lichych cisel: {licha}.") 
	print(f"Pocet sudych cisel: {konec - zacatek + 1 - licha}.")

	print("------")

	i = zacatek
	while i <= konec:
		print(i)
		i = i + 1