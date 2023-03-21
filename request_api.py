import requests


url_api = "https://pokeapi.co/api/v2/pokemon?limit=150"
res = requests.get(url = url_api)

for pokemon in res.json()["results"]:
    print(pokemon["name"])