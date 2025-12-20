import requests as rq
import json

url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
data = rq.get(url).json()
names = []

for pokemon in data["results"]:
    names.append(pokemon["name"])
    
print(names)

