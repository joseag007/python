from datos import pokemons

altura_media = 0  # Empezamos la suma en 0

for pokemon in pokemons:  #
    # Recorremos todos los Pokémon
    altura_media = altura_media + pokemon["altura_m"]  
    # Sumamos su altura

altura_media = altura_media / len(pokemons)  
# Dividimos la suma entre la cantidad de Pokémon

for pokemon in pokemons:
    if pokemon["altura_m"] < altura_media: 

        print(pokemon["nombre"],pokemon["altura_m"])