"""
dvojice.py
Losuj dvojice videk a chlapcu do skolnich lavic. 
Jmena se nesmi opakovat. Maruska nemuze sedet 
zaroven s Jenikem a Petou. Mej dva stejne dlouhe 
seznamu, v jednom divky, ve druhem chlapce.
Seznamy nahodne zamichej a vypis dvojice
divka-chlapec (vzdy [0] index z jednoho seznamu 
a k nemu [0] index z druheho atd.)
"""

import random

divky = ["Maruska", "Anicka", "Petra", "Terezka", "Miska"]
chlapci = ["Tom", "Jenik", "Petr", "Kubik", "David"]

random.shuffle(divky)
random.shuffle(chlapci)

for i in range(0, len(divky)):
	print (f"{i + 1}. lavice: {divky[i]} + {chlapci[i]}")





