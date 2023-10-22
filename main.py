import requests

url = "https://pokeapi.co/api/v2/pokemon/"
pokemons = []

while url:
    response = requests.get(url)
    data = response.json()
    pokemon_list = data["results"]
    pokemons.extend(pokemon_list)
    url = data["next"]

for pokemon in pokemons:
    print("Pokemon: ", pokemon["name"])