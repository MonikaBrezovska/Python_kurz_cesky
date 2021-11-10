"""
retezce.py
Uloz do promenne retezec, zjisti jeho delku,
vypis jeho prvni a posledni znak.
"""
import time

s = "retezec"

delka = len(s)
print(f"Delka retezce je {delka} znaku.")

print(f"Prvni znak retezce: {s[0]}")
print(f"Druhy znak retezce: {s[1]}")
print(f"Treti znak retezce: {s[2]}")
print(f"Posledni znak retezce: {s[delka - 1]}")

for i in range(0, delka):
	print(s[i])
	time.sleep(1)