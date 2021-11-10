"""
ctverecObvod.py
Vytvor program, ktery na vstupu ziska prirozene cislo, a na vystupu hvezdickami vykresli obvod tohoto ctverce.
pr.:
vstup = 5
vystup:

* * * * *
*       *
*       *
*       *
* * * * *


"""
def ctverecObvod(delka):
	vnitrek = delka + (delka - 3) 
	# 5 + (5 - 3) = 7 4 + (4 - 3) = 5  6 + (6 - 3) = 9
	for i in range(1, delka + 1):
		if (i == 1) or (i == delka):
			print("* " * delka)
		else:
			print("*" + " " * vnitrek + "*")

a = int(input("Zadej delku strany ctverce: "))
ctverecObvod(a)

