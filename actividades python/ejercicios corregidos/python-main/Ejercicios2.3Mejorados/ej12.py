"""
Elimina todos los personajes cuya raza sea demonio.
"""
#no me he visto el anime, pero se que es referencia

from personajesfierem import personajes_frieren

for personaje in personajes_frieren[:]:
    #print(personaje)
    if personaje["raza"]=="Demonio":
        personajes_frieren.remove(personaje)
print("-----------------------------------")
for personaje in personajes_frieren:
    print(personaje)