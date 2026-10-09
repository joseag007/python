from datos import pokemons


pesado = pokemons[0]  
# Cogemos el primer Pokémon como el más pesado de momento

for pokemon in pokemons:  
    # Recorremos todos los Pokémon de la lista
    if pokemon["peso_kg"] > pesado["peso_kg"]:  
        # Comprobamos si pesa más que el que tenemos guardado
        pesado = pokemon  
        # Si pesa más, lo guardamos como el nuevo más pesado

print(pesado["nombre"], pesado["peso_kg"])  
# Mostramos el nombre y el peso