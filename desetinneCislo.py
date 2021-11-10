"""
desetinneCislo.py
Vytvoř program, který rozdělí desetinné číslo 
na celou a desetinnou část.

vstup: desetinné číslo (např. 3.14)
výstup: celá a desetinná část čísla

1.) vstup
2.) výpočet
	3.14 = 3 + 0.14
	jak udělám z čísla 3.14.číslo 3?
	přetypování float -> int :-)
	jak dostanu desetinnou část?
	rozdíll 3.14 - 3 = 0.14 :-)
3.) výstup
"""

cislo = float(input("Zadej desetinné číslo: "))

celaCast = int(cislo)
# desetinnaCast = cislo - celaCast
# timto zapisem ulozis posledni hodnotu vpravo (celaCast)
# do vsech promennych vlevo (desetinnaCast, cislo)

# desetinnaCast = cislo - celaCast

print(cislo, "=", celaCast, "+", desetinnaCast)
