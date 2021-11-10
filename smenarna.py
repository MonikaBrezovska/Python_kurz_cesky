"""
smenarna.py
Priklad pro vypocet poplatku za smenu
z CZK na EUR. Poplatek cini 1 % ze 
smenovane castky, minimalni vyse polatku je 50 Kc. 
Stanovte pevny kurz pro prevod. Vystupem bude 
vyse poplatku a pocet EUR.

Vstup: castka ke smene
Vystup> poplatek, castka ke smene
"""
castka = int(input("Zadejte castku v CZK: "))
kurz = 25
eur = castka/ kurz

print(f"{castka} CZK = {eur} E")

poplatek = castka * 0.01
if poplatek < 50:
	poplatek = 50
	
print(f"Poplatek cini: {poplatek} CZK")
