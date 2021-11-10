ja = {'jmeno': 'Anna', 'mesto': 'Brno', 'cisla': [3, 7]}

print(ja['jmeno'])
#print(ja['vek'])

ja['cisla'] = [3, 7, 42]
print(ja)
ja['jazyk'] = 'Python'
print(ja)

del ja['cisla']
print(ja)

cisla = {
    'Maruška': '153 85283',
    'Terka': '237 26505',
    'Renata': '385 11223',
    'Michal': '491 88047',
}

barvy = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}

popisy_funkci = {'len': 'delka', 'str': 'retezec', 'dict': 'slovnik'}
for klic in popisy_funkci:
    print(klic)

for hodnota in popisy_funkci.values():
    print(hodnota)

for klic, hodnota in popisy_funkci.items():
    print('{}: {}'.format(klic, hodnota))

for klic, hodnota in popisy_funkci.items():
    print('{}: {}'.format(klic, hodnota))

for klic, hodnota in popisy_funkci.items():
    print('{}: {}'.format(klic, hodnota))

barvy_po_tydnu = dict(barvy)
for klic in barvy_po_tydnu:
    barvy_po_tydnu[klic] = 'cerno-hnedo-' + barvy_po_tydnu[klic]
print(barvy['jablko'])
print(barvy_po_tydnu['jablko'])

data = [(1, 'jedna'), (2, 'dva'), (3, 'tři')]
nazvy_cisel = dict(data)
print(data)
print(nazvy_cisel)

popisy_funkci = dict(len='délka', str='řetězec', dict='slovník')
print(popisy_funkci['len'])
print(popisy_funkci['str'])

