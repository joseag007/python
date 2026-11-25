"""
Extrae en una única lista todas las filigranas de todos los jugadores (no importa si
hay duplicadas) y muéstrala.
"""

from jugadores import jugadores


"""filigranas = [j["filigranas"] for j in jugadores]"""
filigranas=[f for j in jugadores for f in j["filigranas"]]
print(filigranas)
