"""
uceni.py
Vytvoř program, který načte uživatelovu 
odpověď (pouze 0 = ne či 1 = ano) 
na dotaz: „Učíš se nyní Python?“. 
Odpověď přetypuj do logické hodnoty 
a adekvátně reaguj (např.  „Ano, máš pravdu.“ 
či  „Ne, lžeš.“).
     
vstup: odpověď na otázku (0, nebo 1)
výstup: reakce na odpověď
     
1.) načti vstup
2.) když je vstup 1 (pravda), 
tak výpis "Ano, máš pravdu."
jinak výpis "Ne, lžeš."
"""
     
odpoved = int(input("Učíš se nyní Python? Zadej 0 či 1: "))
     
if odpoved in range(0, 2):
 	odpoved = bool(odpoved)
 	if odpoved:
  		print("Ano, máš pravdu.")
    else:
  		print("Ne, lžeš!")
else:
    print("Nebyla zadána 0 či 1.")