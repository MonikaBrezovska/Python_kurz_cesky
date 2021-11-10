"""
mozek.py
Vytvor hru pro trening mozku. 
Poznas, co znamena slovo "Ketven" ci "Creevn"?
Lidksemu mozku staci znat prvni a posledni pismeno, 
ostatni pismena mohou byt prehazena a presto text 
dokaze precist.
"""
import random

slova = [
	"leden", 
	"unor",
	"brezen",
	"duben", 
	"kveten"
	"cerven"
	"cervenec"
	"srpen"
	"zari", 
	"rijen", 
	"listopad", 
	"prosinec"
] 

def zamichejSlovo(slovo):
	hadejSlovo = []
	hadejSlovo.append(slovo[0])
	prostredek = slovo[1:len(slovo) - 1]
	random.shuffle(prostredek)
	hadejSlovo.extend(prostredek)
	hadejSlovo.append(slovo[len(slovo) -1])
	return hadejSlovo

slovo = random.choice(slova)
slovo = list(slovo)
hadejSlovo = zamichejSlovo (slovo)

while slovo == zamichejSlovo:
	hadejSlovo = zamichejSlovo (slovo)

hadejSlovo = "".join(hadejSlovo)
slovo = "".join(slovo)
print(hadejSlovo)

tipy = []

uzivatel = input("Napis slovo: ")
tipy.append(slovo == uzivatel)

while slovo != uzivatel:
	print("Neuhodl/a jsi!")
	uzivatel = input("Mas dalsi pokus: ")
	tipy.append(slovo == uzivatel)

print("\n------------\nStatistika pokusu\n")
print(f"Spravne:\t{sum(tipy)}")
print(f"Spatne:\t\t{len(tipy) - sum(tipy)}")


