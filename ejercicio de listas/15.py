from datos import personajes_frieren


for personaje_frieren in personajes_frieren:
    if personaje_frieren["raza"] == "Humano" and personaje_frieren["edad"] >= 100:
        personaje_frieren["raza"] = "Zombie"