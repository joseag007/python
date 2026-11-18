from datos import personajes_frieren


for personaje_frieren in personajes_frieren: 
    if "Magos de Primera Clase" in personaje_frieren["afiliacion"]:
        print(personaje_frieren["nombre"], personaje_frieren["raza"])