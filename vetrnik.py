"""
vetrnik.py
Vytvor funkci, ktera dle zadaneho cisla vykresli vetrnik.
Vstupem bude cele cislo "x" znacici pocet lopatek.
"""

from turtle import *
import math

def lopatka():
	forward(100)
	left(180 - 45)
	forward(math.sqrt(50 ** 2 + 50 ** 2))
	left(90)
	forward(math.sqrt(50 ** 2 + 50 ** 2))
	left(180 - 45)
	
def vetrnik(x):
	for u in range(x):
		lopatka()
		left(360 / x)
	exitonclick()

x = int(input("Zadej, kolik lopatek chces vykreslit: "))
vetrnik(x)