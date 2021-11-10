"""
pozpatku.py
Vytvor program, ktery nacte retezec a vypise
ho pozpatku od posledniho zanku po prvni.
Program uprav tak, ze nactes celou vetu, kterou 
rozsekas po slovech a ta vypises pozpatku.
pr.: 	Dnes je ale krasny den!
		!ned ynsark ela ej sedD
"""

veta = "Ahoj svete!"

delka = len(veta)
zacatek = delka - 1
konec = -1
krok = -1

for i in range(zacatek, konec, krok):
	print(veta[i], end = "") 

print("\n-----------------")

seznam = list(veta.split(" "))
for slovo in seznam: 
	# print(slovo)
	delka = len(slovo)
	zacatek = delka - 1
	konec = -1
	krok = -1

	for i in range(zacatek, konec, krok):
		print(slovo[i], end = "")
	print()