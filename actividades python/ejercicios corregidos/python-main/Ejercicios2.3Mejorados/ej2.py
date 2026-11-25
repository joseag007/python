"""
Muestra la media de altura de todos los pokémons.
"""
from pokemons import pokemons #hay que poner el minsmo nombre del fichero y la variable, sino no funciona

"""media=0
contador=0
for pokemon in pokemons:
    media=media+pokemon['altura_m']
    contador=contador+1
media=media/contador"""

media= sum(pokemon["altura_m"] for pokemon in pokemons)/len(pokemons)
print(media)
