"""
zamena.py
Vytvor priklad pro zamenu obsahu dvou promennych.
Vstupem jsou dve celociselne hodnoty, vystupem totez.
Reseni: s vyuzitim pomocne promenne, 
nebo postupnym odecitanim.

vstup: a = 5, b = 2
vystup: a = 2, b = 5
"""

a = int(input("Zadej hotnotu promenne \"a\": "))
b = int(input("Zadej hotnotu promenne \"b\": "))
print(f"a = {a}, b = {b}")

# s uzitim pomocne promenne:
c = a
a = b
b = c

print(f"a = {a}, b = {b}")

#metodou postupneho odecitani:
a = a + b # a = 3 + 8 = 11
b = a - b # b = 11 - 8 = 3
a = a - b # a =  11 - 3 = 8

print(f"a = {a}, b = {b}")