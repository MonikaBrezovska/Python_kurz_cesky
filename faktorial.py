"""
faktorial.py
Na samostatnem algoritmu si vyzkousej funkci 
pro vypocet faktorialu vlozeneho prirozeneho cisla.
Vstup prirozeneho cisla osetri podminkou.

vstup: prirozene cislo
vystup: faktorial

1.) nacteni hodnoty, kontrola, zdali je cislo 
cele a kladne
2.) vypocet
3.) vystup vysledku
"""

import math

cislo = int(input("Zadej cele kladne cislo: "))

if cislo > 0:
	faktorial = math.factorial(cislo)
	print(str(cislo) + "! = " + str(faktorial))
else:
	print("Nebylo zadano cele kladne cislo.")

