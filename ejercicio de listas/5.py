from datos import pokemons


for pokemon in pokemons:
    for tipo in pokemon["tipos"]:
        if tipo.endswith("a"):
            print(pokemon["nombre"], pokemon["tipos"])