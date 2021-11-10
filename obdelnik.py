"""
obdelnik.py
Vytvoř program pro výpočet obvodu a obsahu obdélníka.
Dély stran obdélníka zadá uživatel na začátku programu.

vstupy: délka stran obdélníka (a, b)
výstup: obvod a obsah obdélníka

1.) načtení dat za vstupu
2.) výpočet
3.) výpis dat na monitor
"""

a = float(input("Zadej délku strany a: "))
b = float(input("Zadej délku strany b: "))

o = 2 * (a + b)
S = a * b

print("Obvod:", o, "\tObsah:", S)

# zalomení řádku: \n
# tabulátor: \t


