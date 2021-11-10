"""
prevody2.py
Vytvor algoritmus pro prevod hodnoty zadane v m na dm, cm, mm, km (dle SI).
POuzij vypis cisla v exponencialnim tvaru.

vstup: delka v metrech
vystup: delka v cm, mm, dm, km
"""

m = int(input("Zadej delku v metrech: "))

dm = m * 10
cm = dm * 10
mm = cm * 10
km = m / 1000

print (f"{km:.2e} mm = \n{m} m = \n{dm:.2e} dm = \n{cm:.2e} cm = \n{mm:.2e} mm")
