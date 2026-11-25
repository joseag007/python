"""
Inserta al final de la lista un nuevo pokémon que tenga todos los campos con algún
valor con sentido (puedes inventártelos, pero que sean razonables).
"""

from pokemons import pokemons

pokemons.append({
    "nombre": "Giratina",
    "generacion": 4,
    "categoria": "Renegado",
    "tipos": ["Fantasma","Dragón"],
    "peso_kg": 750.0,
    "altura_m": 6.9
})
for pokemon in pokemons:
    print(pokemon)