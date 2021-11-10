"""
jazykC.py
Vyzkousej si ruzne moznosti formatovani
hodnoty pi.
S pomoci lektora vytvor program, ktery v cyklu vypise 0. az 10. mocninu cisla 10 formatovane zarovnanou vpravo.
"""

import math
"""
pi = math.pi

print("%f" % pi)
print("%.2f" % pi)
print("%10.2f" % pi)
print("%10.3f" % pi)
print("%10.4f" % pi)
"""
for i in range(0, 11):
	mocnina = pow(10, i)
	print("%012.0f" % mocnina)
