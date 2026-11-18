from datos import personajes_frieren


for personaje_frieren in personajes_frieren:
    if "Demonio" in personaje_frieren["raza"]:
        personajes_frieren.remove(personaje_frieren)

