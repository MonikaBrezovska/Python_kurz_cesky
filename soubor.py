soubor = open('basnicka.txt', encoding='utf-8')
obsah = soubor.read()
soubor.close()

print(obsah)

with open('basnicka.txt', encoding='utf-8') as soubor:
    obsah = soubor.read()

print(obsah)

