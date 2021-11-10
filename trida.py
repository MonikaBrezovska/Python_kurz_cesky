"""
trida.py
Ve tride je x divek a y chlapcu; vytvor algoritmus
pro vyjadreni procentualniho podilu divek 
a chlapcu.

vstup: pocet divek, pocet chlapcu
vystup: procentualni podil divek
		procentualni podil chlapcu
"""

divky = int(input("Zadej pocet divek: "))
chlapci = int(input("Zadej pocet chlapcu: "))

if (divky > 0) or (chlapci > 0):
	divkyProcenta = (divky/ (divky + chlapci)) * 100

	print(f"Procentualni podil divek: {divkyProcenta:.2f} %")
	print(f"Procentualni podil chlapcu: {100 - divkyProcenta:.2f} %")
else:
	print("Alespon jedna hodnota musi byt vetsi nez 0.")
