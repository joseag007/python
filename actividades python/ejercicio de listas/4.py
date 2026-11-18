from datos import pokemons


for pokemon in pokemons:
    for tipo in pokemon["tipos"]:
        if "Agua" in tipo:
            print(pokemon["nombre"], pokemon["tipos"])