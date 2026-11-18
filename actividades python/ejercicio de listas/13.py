from datos import personajes_frieren


for personaje_frieren in personajes_frieren:
    if personaje_frieren["raza"] == "Elfo":
        personaje_frieren["afiliacion"].append("Elfos Supervivientes del Examen de Python")