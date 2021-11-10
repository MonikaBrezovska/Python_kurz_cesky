"""
matematika.py
Na samostatnem algoritmu si vyzkousej funkce knihovny math pro zaokrouhlovani a mocniny.


round, ceil, floor
pow, sqrt
"""

import math

cislo = math.pi
print(cislo)
print(round(cislo, 2))

a = 123456.784
print(round(a, 2))
print(round(a, -2))

# round zaokrouhluje matematicky (od 5 nahoru)
# druhy argument je nepovinny, znamena:
# kladny -> pocet cifer vpravo od desetinne tecky
# zaporny -> pocet cifer vlevo od desetinne tecky

print(math.ceil(a))
print (math.floor(a))

print(math.pow(2, 4))
print(math.sqrt(16))
