"""
Muestra la lista de los jugadores que llevan el dorsal número 10.
"""
from jugadores import jugadores

numero10 = [j for j in jugadores if j["dorsal"] is 10]
print (numero10)