"""
matFunkce.py
Vytvoř program, který načte vložené číslo 
a dle volby uživatele vypíše: druhou mocninu 
(volba 1), druhou odmocninu (volba 2), 
faktoriál (volba 3).
     
vstup: číslo, volba
výstup: druhá mocnina, druhá odmocnina, nebo faktoriál
     
1.) načtení vstupů
2.) když volba je 1, tak
    	výpočet druhé mocniny
    když volba je 2, tak
    	výpočet druhé odmocniny
    když volba je 3, tak
    	výpočet faktoriálu
    """
     
import math
     
cislo = int(input("Zadej číslo: "))
volba = int(input("Zadej volbu \n(1: mocnina, \n 2: odmocnina, \n 3: faktorial): "))

if volba == 1:
    print("Druha mocnina je", pow(cislo, 2))
else:
    if volba == 2:
        print("Druha odmocnina je", math.sqrt(cislo))
    else:     
        if volba == 3:
            print("Fakorial je", math.factorial(cislo))
        else:
            print("Volba neni na vyber.")

