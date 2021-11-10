"""
kavarna.py
Vytvor program, ktery vypise nabidku kavarny, 
tedy nazev napoje, jeho objem a cenu.
Vystup formatuj do prehledne tabulky, 
data budou ve sloupcich.
"""

napoj = "kava s mlekem", "capuccino", "dzus", "voda", "smetana"
objem = "200 ml", "180 ml", "250 ml", "100 ml", "50 ml"
cena = "45 Kc", "60 Kc", "30 Kc", "5 Kc", "8 Kc"

pocet = len(napoj)

for i in range(0, pocet):
	print(f"{napoj[i]:<15} {objem[i]:>6} {cena[i]:>6}")
