"""
Muestra la lista de los jugadores que saben hacer la filigrana "ruleta".
"""
from jugadores import jugadores

ruleteros = [j["nombre"] for j in jugadores if "ruleta" in j["filigranas"]]
print (ruleteros)