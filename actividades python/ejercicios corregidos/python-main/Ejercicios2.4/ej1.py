"""
Muestra una lista solo con los nombres de todos los futbolistas.
"""
from jugadores import jugadores

nombres = [j["nombre"]for j in jugadores]
print (nombres)