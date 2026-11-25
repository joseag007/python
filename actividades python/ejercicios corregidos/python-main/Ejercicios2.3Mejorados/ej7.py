"""
Elimina todos los pokémons de tipo normal.
"""

#pobres tipos normales, que han hecho para merecerse esto?

from pokemons import pokemons

for pokemon in pokemons[:]:#al eliminar un objeto, el numero de la lista se reduce en uno, y cuando pasa el bucle, al siguente sesion, si coincide un parametro del IF, este no lo recorrera ya que se lo ha pasado, al poner [:]este le hace una copia temoral para evitar este
    """for tipo in pokemon["tipos"]:
        
        if tipo=="Normal":
            
            
            pokemons.remove(pokemon)"""
    if "Normal" in pokemon["tipos"]:
         pokemons.remove(pokemon)
        
        

for pokemon in pokemons:
     print(pokemon["nombre"])