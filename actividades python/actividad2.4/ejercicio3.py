from datos import jugadores

barcelona = [j["nombre"] for j in jugadores if j["equipo"] == "FC Barcelona"]
print("3.", barcelona)