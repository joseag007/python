"""
Muestra el nombre, la raza y la edad de los personajes del grupo de los cuatro
héroes.
"""

from personajesfierem import personajes_frieren

for personaje in personajes_frieren:
    for alfiliacionindi in personaje["afiliacion"]:
        if alfiliacionindi=="Grupo de los Cuatro Héroes":
            print(personaje["nombre"],personaje["raza"])