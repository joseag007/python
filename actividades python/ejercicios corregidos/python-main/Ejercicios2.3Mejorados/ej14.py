"""
A todos los personajes que pertenezcan a la Asociación Continental de Magia,
quítales esa afiliación.
"""
from personajesfierem import personajes_frieren

for personaje in personajes_frieren[:]:
    for afiliacionindi in personaje["afiliacion"]:
        if afiliacionindi=="Asociación Continental de Magia":
            personaje["afiliacion"].remove(afiliacionindi)
    print(personaje)