"""
Muestra una lista con los nombres de los jugadores que pertenecen al "FC
Barcelona".
"""

from jugadores import jugadores

fcBarsa = [j["nombre"] for j in jugadores if j["equipo"] == "FC Barcelona"]
print (fcBarsa)