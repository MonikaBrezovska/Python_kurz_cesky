"""
ascii.py
Vypi3 na monior znaky standardni
7 bitove ASCII tabulky; vedle cisla 
pozice bude znak.
Tip: vypis bez zalomeni radku:
print(a, end = '')
"""

for i in range(0, 128):
	#print(f"{i}: {chr(i)}\t", end = "")
	print(f"{i}: {chr(i)}\t", end = "\n")
	print(f"{i}: {chr(i)}\t")

