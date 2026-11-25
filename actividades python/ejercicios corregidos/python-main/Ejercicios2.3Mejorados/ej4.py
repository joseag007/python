"""
Muestra el nombre y los tipos de los pokémons que sean de tipo agua.
"""
from pokemons import pokemons #hay que poner el minsmo nombre del fichero y la variable, sino no funciona

for pokemon in pokemons:
    
    """
    for tipo in pokemon["tipos"]:

        if tipo=="Agua":
            print(pokemon['nombre'],pokemon['tipos'])
    """
    if "Agua" in pokemon["tipos"]:
        print(pokemon['nombre'],pokemon['tipos'])