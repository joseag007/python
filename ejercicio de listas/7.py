from datos import pokemons


for pokemon in pokemons:
    for tipo in pokemon["tipos"]:
        if "Normal" in tipo:
            pokemons.remove(pokemon)