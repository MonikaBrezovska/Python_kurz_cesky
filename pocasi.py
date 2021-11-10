"""
pocasi.py
Vytvor program, dle zadane teploty
vypise, jaky je pocitovy stav
(napr. je teplo, je obstojne, je zima).
"""

teplota = int(input("Zadej teplotu ve st.C: "))

if teplota < 5:
	print("Je zima.")
elif teplota in range (5, 16):
	print("Je chladno.")
elif teplota in range(16, 21):
	print("Je tepleji.")
else:
	print("Je vedro.")
