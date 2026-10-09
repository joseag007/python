from datos import personajes_frieren


for personaje_frieren in personajes_frieren: 
    if "Grupo de los Cuatro Héroes" in personaje_frieren["afiliacion"]:
        print(personaje_frieren["nombre"], personaje_frieren["raza"], personaje_frieren["edad"])