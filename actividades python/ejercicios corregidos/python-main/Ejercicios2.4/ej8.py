"""
Crea una lista de tuplas con el nombre del jugador y el texto "Goleador" si su atributo
de tiro es mayor o igual a 9, o "Asistente" en caso contrario. Muéstrala.
"""

from jugadores import jugadores

"""goleadores = [j["nombre"]+" goleador" for j in jugadores if (j["atributos"]["tiro"] >=9)]
print (goleadores)"""

lista=[(j["nombre"],"goleador") if j["atributos"]["tiro"] >=9 else (j["nombre"],"Asistente") for j in jugadores]
print (lista)