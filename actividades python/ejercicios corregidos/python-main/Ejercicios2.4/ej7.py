"""
Crea una lista de cadenas de texto con la forma "Nombre (Equipo)" para cada
jugador. Muéstrala.
"""
from jugadores import jugadores

nombreJugador = [j["nombre"] for j in jugadores]
print (nombreJugador)