"""
kyticky.py
Program vykreslí louku plnou kytiček. Uživatel na začátku zadá, 
kolik okvětních plátků má každá kytička mít, a počet kytiček
na louce. Barvy kytiček budou náhodně generovány. 
"""
     
from turtle import *
import random
     
     
def kyticky(x, y):
        barvy = [
           "pink",
    	   "red",
    	   "blue",
    	   "cyan",
    	   "magenta",
    	   "green"]
    	
        for i in range(y):
    	       pencolor(random.choice(barvy))
    	       pendown()
    	       for j in range(x):
                   circle(10)
       	           left(360 / x)
    	       penup()
    	       setx(random.randint(10, 200))
    	       sety(random.randint(10, 200))
    	
        exitonclick()
     
     
x = int(input("Zadej počet okvětních plátků: "))
y = int(input("Zadej počet květinek: "))
     
if x > 0 and y > 0:
 	    kyticky(x, y)
else:   
   	    print("Nebyla zadána kladná čísla.")