"""
Muestra los pokémons que tengan un tipo que acabe en “a”.
"""

from pokemons import pokemons #hay que poner el minsmo nombre del fichero y la variable, sino no funciona

for pokemon in pokemons:
    
    for tipo in pokemon["tipos"]:


        if tipo[-1]=="a":# al ser los arrays strings, puedes aprobechar que en la posicion 0 lo hagas como un charat
            print(pokemon['nombre'],pokemon['tipos'])
            
    