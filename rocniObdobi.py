"""
rocniObdobi.py
Vytvor program, ktery dle zadaneho mesice
cislem vypise, jako rocni obdobi momentalne je.

1,2		zima
3,4,5	jaro
6,7,8,	leto
9,10,11	podzim
12		zima
"""
import datetime

dnes = datetime.date.today()
mesic = dnes.month

print(f"Dnes je: {dnes} ({type(dnes)}")
print(f"Mesic je: {mesic} ({type(mesic)}")
# mesic = int(input("Zadej mesic cislem: "))

if mesic >= 1 and mesic <= 12:
 	# jedna se o spravne zadany mesic
 	if mesic <= 2:
 		print("zima")
 	elif mesic <= 5:
 		print("jaro")
 	elif mesic <= 8:
 		print("leto")
 	elif mesic <= 11:
 		print("podzim")
 	else: 
 		print("zima")

else:
	print("Byla vlozena nevhodna hodnota.")
