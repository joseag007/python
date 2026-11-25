"""si quieres importar una cariable de otro sitio, se hace asi (se utiliza pokemones.py)"""

from pokemones import pokemones #hay que poner el minsmo nombre del fichero y la variable, sino no funciona

for pokemon in pokemones:
    print(pokemon['nombre'])