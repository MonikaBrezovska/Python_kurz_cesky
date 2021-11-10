"""
trideniASCII.py
Vytvor priklad, ktery roztridi vsechny 
znaky 7bitove ASCII tabulky na pismena, 
cifry a jine znaky.
Jednotlive skupiny ukladej do novych
promennych, nakonec vypis jejich obsah 
a pocet za kazdou skupinu.
"""

znaky = ""
cifry = ""
jine = ""

for i in range(0, 128):
	znak = chr(i)
	if znak.isalpha():
		znaky += znak
	else: 
		if znak.isdigit():
			cifry += znak
		else: 
			jine += znak

print(f"Znaky: {znaky} (pocet {len(znaky)})")
print(f"Cifry: {cifry} (pocet {len(cifry)})")
print(f"Jine: {jine} (pocet {len(jine)})")
print(f"Kontrola: {len(znaky) + len(cifry) + len(jine)}")
