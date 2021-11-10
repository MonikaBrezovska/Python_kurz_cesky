"""
obsahuje.py
Nacti retezec obsahujici cifry a znaky.
Retezec prochazej znak po znaku a znaky rozdeluj do skupin: pismena, cifry, jine znaky.
Vypis, kolik znaku kazda skupina obsahuje.
Program uprav: nacti novy znak, 
kdyz se znak v puvodnim retezci jeste nevyskytuje, 
pridej jej na konec retezce.
"""

s = input("Zadej retezec: ")

delka = len(s)

pocetCisla = 0
pocetZnaky = 0
pocetJine = 0

for i in range(0, delka):
	if s[i].isdigit():
		pocetCisla = pocetCisla + 1
	else: 
		if s[i].isalpha():
			pocetZnaky = pocetZnaky + 1
		else: 
			pocetJine = pocetJine + 1

print(f"Pocet cislic: {pocetCisla}")
print(f"Pocet znaku: {pocetZnaky}")
print(f"Pocet jinych znaku: {pocetJine}")

znak = input("Zadej znak: ")

if znak not in s:
	s = s + znak

print(s)
