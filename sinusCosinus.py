"""
sinusCosinus.py
Na samostatnem algoritmu si vyzkousej funkce sinus
a cosinus pro hodnoty uhlu ve stupnich, ktere zada
uzivatel na vstupu.

vstup: uhel ve stupnich
vystup: sinus a cosinus

1.) vstup
2.) vypocty
3.) vystup
"""

import math

uhel = float(input("Zadej uhel ve stupnich: "))

# trigonometricke funkce pracuji s uhly v radianech
uhelRadiany = math.radians(uhel)
print("Uhel v radianech:", uhelRadiany)
sinus = math.sin(uhelRadiany)
cosinus = math.cos(uhelRadiany)

print("Sinus:", sinus)
print("Cosinus:", round(cosinus, 2))
