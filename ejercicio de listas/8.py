from datos import personajes_frieren

edad_media =0


for personaje_frieren in personajes_frieren:  #
    # Recorremos todos los Pokémon
    edad_media = edad_media + personaje_frieren["edad"]  
    # Sumamos su altura

edad_media = edad_media / len(personajes_frieren)  
# Dividimos la suma entre la cantidad de Pokémon

print(edad_media)