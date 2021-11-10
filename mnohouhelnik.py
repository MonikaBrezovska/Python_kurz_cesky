"""
mnohouhelnik.py
Vytvor funkci , ktera bude vykreslovat mnohouhelnik. 
Uzivatel na zacatku zada cislo >2, program pak vykresli 
patricny mnohouhelnik (rovnostranny trojuhelnik, ctverec, 
petiuhelnik atd.)
"""

import turtle

def mnohouhelnik(x):
	for i in range(x):
		turtle.forward(100)
		turtle.left(360 / x)
	turtle.done()


x = int(input("Zadej, kolikatiuhelnik chcecs nakreslit: "))
mnohouhelnik(x)


