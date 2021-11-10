"""
hexadec.py
S pomoci lektora vytvor program, ktery v cyklu vypise 0. az 15. hodnotu 
hexadecimalni ciselne soustavy.
Bude se jednat o cisla 0-9
a pismena A-F, tedy obsazenost 4 bitu (24 = 16, tzn. 16 moznosti 
variant, tj. hodnoty 0 az 15).
"""

for i in range (0, 16):
	print("%X " % i, end = "")
	
