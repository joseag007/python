"""
Muestra el nombre y la raza de todos los personajes que sean magos de primera
clase.
"""

from personajesfierem import personajes_frieren

for personaje in personajes_frieren:
    for alfiliacionindi in personaje["afiliacion"]:
        if alfiliacionindi=="Magos de Primera Clase":
            print(personaje["nombre"],personaje["raza"])