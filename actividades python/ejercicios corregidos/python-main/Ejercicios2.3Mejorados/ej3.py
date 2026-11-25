"""
Muestra el nombre y la altura de todos los pokémons que midan menos que la
media.
"""
from pokemons import pokemons #hay que poner el minsmo nombre del fichero y la variable, sino no funciona
"""
media=0
contador=0
for pokemon in pokemons:
    media=media+pokemon['altura_m']
    contador=contador+1
media=media/contador
"""
from ej2 import media

"""for pokemon in pokemons:
    if pokemon['altura_m']<media:
        print(pokemon["nombre"],pokemon["altura_m"])
"""
sup_media = [p for p in pokemons if media >p["altura_m"]]
print(sup_media)