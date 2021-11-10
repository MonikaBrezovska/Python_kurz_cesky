"""
spirala.py
Vytvor program, ktery jednim tahem vykresli spiralu n-uhelniku. 
N-uhelnik musi byt cislo > 2.
"""

from turtle import *
import random

def spirala(x):
	barvy = ["red", "green", "blue", "cyan", "magenta"]
	shape("turtle")
	pocetCar = x * 5
	posun = 20 / x
	for i in range(pocetCar):
		pencolor(random.choice(barvy))
		forward(i * posun)
		left(360 / x)
	done()

x = int(input("Zadej kolikatiuhelnik chces vykreslit: "))
spirala(x) 