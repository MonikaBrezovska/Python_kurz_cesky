"""
captcha.py
Vygeneruj "x" nahodnych petimistnych captcha
kodu slozenych ze znak; a-z, A-Z, 0-9
a uloz je do seznamu.
V cyklu captcha kor vypisuj na monitor 
a po uzivateli vyzaduj, aby je prepisovat.
Pocitej uspesnost opisu.
"""
import random

mala = "abcdefghijklmnopqrstuvwxyz"
velka = mala.upper()
cifry = "0123456789"

x = input("Zadej, kolik captcha kodu chces vygenerovat: ")

while not(x.isdigit()) or int(x) <= 0:
	x = input("Zadej kladne cislo: ")

for i in range(0, int(x)):

	# captcha:_ _ _ _ _

	captcha = ""
	opis = ""
	kontrola = [] #ulozeni, kolikrat se uzivatel ne/spletl

	for j in range(0, 5):
		coToBude = random.randint(1, 3)
		if coToBude == 1:
			captcha += random.choice(mala)
		if coToBude == 2:
			captcha += random.choice(velka)
		if coToBude == 3:
			captcha += random.choice(cifry)

	print(captcha)
	opis = input("Opis captcha kod: ")
	kontrola.append(captcha == opis)

	while captcha != opis:
		#do cyklu se vstoupi, pokud podminka plati (opis neroven captcha)
		opis = input("Opis captcha kod: ")
		kontrola.append(captcha == opis)

print(kontrola)
print(f"Uspesnost: {(sum(kontrola) / len(kontrola)) * 100"} %")





