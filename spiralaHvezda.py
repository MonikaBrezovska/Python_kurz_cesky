"""
spiralaHvezda.py
Vytvor program, ktery jednim tahem vykresli spiralu hvezdy.
Hvezda musi mit lichy pocet cipu (aby sla vykreslit jednim tahem).
"""
from turtle import *

def hvezda(x):
	pocetCar = x * 5
	for i in range(pocetCar):
		forward(i * 10)
		left(180 - (180 / x))
	exitonclick()

x = int(input("Zadej, kolik cipu chces vykreslit: "))

if x > 2 and x % 2 == 1:
	hvezda(x)
else:
	print("Nebylo zadano liche cislo > 2.")