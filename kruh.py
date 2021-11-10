"""
kruh.py
Vytvoř program pro výpočet obvodu a obsahu kruhu.
Délku poloměru kruhu zadá uživatel na začátku programu.

vstupy: délka poloměru
výstupy: obvod, obsah

1.) načíst vstup
výpočet
výpis výsledků
"""

r = float(input("Zadej délku poloměru: "))

o = 2 * 3.14 * r
S = 3.14 * r ** 2

print("Obvod:", o, "\nObsah:", S)

#operator ** je mocnina

cislo = float(input("Zadej libovolné číslo: "))
print("Třetí mocnina je:", pow(cislo, 3))