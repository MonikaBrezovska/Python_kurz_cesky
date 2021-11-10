"""
faktorialPodminka.py
Vytvoř program pro výpis faktoriálu 
vloženého přirozeného čísla. 
Vstup ošetři podmínkou.
Výpis faktoriálu formátuj se zarovnáním 
doprava, např.: 
00005! = 00120
"""
     
import math
     
cislo = int(input("Zadej přirozené číslo: "))
     
if cislo > 0:
    faktorial = math.factorial(cislo)
    print(f"{cislo:>05}! = {faktorial:>05}")
else:
	print("Nebylo zadáno přirozené číslo.")

    