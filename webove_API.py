import requests

# stažení stránky
stranka = requests.get('https://github.com')

# ověření, že dotaz proběhl v pořádku
stranka.raise_for_status()

# vypsání obsahu
print(stranka.text)

with open('token.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

stranka = requests.get('https://api.github.com/user', headers=headers)
stranka.raise_for_status()
print(stranka.text)

data = json.loads(stranka.text)
print(json.dumps(data, ensure_ascii=True, indent=2))
print(data['avatar_url'])



