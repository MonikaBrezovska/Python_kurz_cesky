"""
bodovani.py
Vytvor program, ktery postupne projde 
bodove vysledky 5 osob
a spolu se jmenem osoby vypise, kolik
bodu a jake hodnocene osoba ziskala.
Rozsahy bodovani urci podle vlastniho uvazeni.
"""

osoby = "Jan", "Tom", "Nela", "Eva", "Martina"
body = 20, 60, 85, 75, 90

pocet = len(osoby)

for i in range(0, pocet):
	print(f"{osoby[i]:>10} : {body[i]:>5} ", end = "")
	if body[i] <= 35:
		print("C")
	elif body[i] <= 85:
		print("B")
	else:
		print("A")
		
