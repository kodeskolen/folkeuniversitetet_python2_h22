import json

with open("pokedex.json") as f:
    pokedex = json.load(f)
    
#print(pokedex)

#print(type(pokedex))
#print(pokedex[0])

print(len(pokedex))

def finn_pokemon(pokemon):
    return int(pokemon["Capture Rate"]) < 10

resultat = list(filter(finn_pokemon, pokedex))
for pokemon in resultat:
    print(pokemon["Name"])

for pokemon in resultat:
    print(pokemon["Type 1"])

print(len(resultat))

def fjern_drage(pokemon):
    if pokemon["Type 1"] == "Dragon":
        pokemon["Type 1"] = "Rock"
    
    return pokemon

for pokemon in map(fjern_drage, pokedex):
    print(pokemon["Type 1"])

def finn_drage(pokemon):
    return pokemon["Type 1"] == "Dragon"

print(len(list(filter(lambda pokemon: pokemon["Type 1"] == "Dragon", pokedex))))









