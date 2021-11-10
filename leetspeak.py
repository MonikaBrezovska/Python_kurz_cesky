"""
leetspeak.py
Zasifruj retezec reci L3375P34K.
Viz simple.wikipedia.org/wiki/leet
Zameny znaku:
A->4	B->8	E->33	G->6	I->1
O->0	S->5	T->7	Z->2	
"""

znaky = "ABEGIOSTZ"
leet = "483610572"

vstup = input("Zadej retezec k zasifrovani: ")
vstup = vstup.upper()
vstup = list(vstup)

for i in range(0, len(vstup)):
	pismenko = vstup[i]
	if pismenko in znaky:
		index = znaky.find(pismenko)
		vstup[i] = leet[index]
		
vstup = "".join(vstup)

print(vstup)
