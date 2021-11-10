"""
ctverecVypln.py
Vytvor program, ktery na vstupu ziska prirozene cislo 
a znak pro vykresleni, a na vystupu vykresli ctverec, 
jehoz strana bude obsahovat prave tolik znaku, 
jaka bude hodnota na vstupu.
Ctverec bude vykresleny s vyplni.
"""

def ctverecVypln(delka, znak):
	for i in range(1, delka + 1):
		print((znak + " ") * delka)

a = int(input("Zadej delku ctverce: "))
znak = input("Zadej znak pro vykresleni: ")
ctverecVypln(a, znak)
