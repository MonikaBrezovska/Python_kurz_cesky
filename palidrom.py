"""
palindrom.py
Vytvor program, ktery vyhodnoti, zdali 
je vlozene slovo polichdrom.
Palidrom se slovo, ktere lze cist 
zepredu i zezadu stejne.
"""

slovo = input("Vloz slovo: ")
slovo = slovo.lower()
pozpatku = ""

zacatek = len(slovo) - 1
konec = -1
krok = -1

for i in range(zacatek, konec, krok):
	pozpatku = pozpatku + slovo[i]

print(pozpatku)

if slovo == pozpatku:
		print("Je to palidrom. ")
else:
	print("Neni to polidrom. ")

