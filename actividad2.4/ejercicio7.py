from datos import jugadores

nombre_equipo = ['{j["nombre"]} ({j["equipo"]})' for j in jugadores]
print(nombre_equipo)