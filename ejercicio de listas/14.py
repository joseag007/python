from datos import personajes_frieren

for personaje_frieren in personajes_frieren:
    if "Asociación Continental de Magia" in personaje_frieren["afiliacion"]:
        personaje_frieren["afiliacion"].remove("Asociación Continental de Magia")