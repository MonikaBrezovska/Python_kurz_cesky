"""
prirozenaCisla.py
Vytvoř program, který vypíše, 
z kolika jednotek, desítek, stovek 
s tisíců se skládá číslo na vstupu.

vstup: přirozené číslo
výstupy: počet jednotek, desítek, stovek, tisíců

1.) načtení vstupní hodnoty
2.) výpočty (celčíselné dělení)
3.) průběžné výstupy
"""

vstup = int(input("Zadej přirozené číslo: "))
cislo = vstup

tisice = cislo // 1000
# print("Tisíce:", tisice)
cislo = cislo % 1000

stovky = cislo // 100
# print("Stovky:", stovky)
cislo = cislo % 100

desitky = cislo // 10
# print("Počet desítek:", desitky)
cislo = cislo % 10

jednotky = cislo // 1
# print("Počet jednotek:", jednotky)
cislo = cislo % 1

print(cislo, "=", tisice, "* 1000 +", stovky, "* 100 +", desitky, "* 10 +", jednotky "* 1")
