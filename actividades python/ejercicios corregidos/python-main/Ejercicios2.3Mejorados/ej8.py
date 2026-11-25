"""
Muestra la edad media de los personajes humanos.
"""

from personajesfierem import personajes_frieren
"""edadmedia=0
contador=0
for personaje in c:
    if personaje["raza"]=="Humano":
        print(personaje["nombre"],personaje["edad"],personaje["raza"])
        edadmedia=edadmedia+personaje["edad"]
        contador=contador+1

edadmedia=edadmedia/contador"""


edadmedia= sum(personaje["edad"] for personaje in personajes_frieren if personaje["raza"]=="Humano")/len(personaje for personaje in personajes_frieren if personaje["raza"]=="Humano")

print(edadmedia)