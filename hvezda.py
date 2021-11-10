"""
hvezda.py
Vytvor funkci, ktera dle zadaneho cisla vykresli obrys hvezdy.
Vstupem bude cele cislo > 2.
Vytvor funkci, ktera dle zadaneho cisla vykresli jednou carou hvezdu. Vstupem bude cele cislo > 2.
"""

from turtle import *

def hvezdaLicha(x):
	for i in range(x):
		forward(100)
		left(180 - (180 / x))
	exitonclick()

def hvezdaSuda(x):
	for i in range(x):
		forward(100)
		left(360 - (360 / x))
		forward(100)
		left(180 - (360 / x))
	exitonclick()

x = int(input("Zadej, kolik cipu chces vykreslit: ")
if x % 2 == 0:
	hvezdaSuda(x)
else:
	hvezdaLicha(x)
