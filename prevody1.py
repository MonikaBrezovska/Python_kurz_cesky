"""
prevody1.py
Vytvoř algoritmus pro převod hodnoty zadané v GB na MB, KB, B 
a bity (dle SI).
vstup: velikost v GB
vystup: velikost v MB, KB, B a bitech

1.) vstup GB
2.) vypocet a vystup
	1 GB = 2^10 MB = 2^20 KB = 2^30 B = 2^30 * 8 b
"""

GB = int(input("Zadej velikost v gigabyte (GB): "))

MB = GB * pow(2, 10)
KB = MB * pow(2, 10)
B = KB * pow(2, 10)
b = B * 8

print(f"{GB} GB = \n{MB:,} MB = \n{KB:,} KB = \n{B:,} B = \n{b} b")
