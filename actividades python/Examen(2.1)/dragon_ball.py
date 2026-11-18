from datos import personajes

def ejercicio1():
    personajes.append({
    "nombre": "Goku",
    "raza": "Saiyan",
    "nivel_pelea": 140000000,
    "tecnicas": ["Galick Ho", "Big Bang Attack"],
    "atributos": {"fuerza": 93, "defensa": 90, "velocidad": 89}
    })

def ejercicio2():

    for personaje in personajes:
        fuerza = personaje["atributos"]["fuerza"]
        velocidad = personaje["atributos"]["fuerza"]
        defensa = personaje["atributos"]["fuerza"]

        if fuerza> 80:
            if velocidad>80:
                if defensa>80:
                    print(personaje)


def ejercicio3():

    velocidad_media = 0

    for personaje in personajes:
            
            velocidad = personaje["atributos"]["fuerza"]
            velocidad_media = velocidad_media + velocidad

    for personaje in personajes:
         if velocidad > velocidad_media:
              print(personaje)

def ejercicio4():
      
    for personaje in personajes:
            fuerza = personaje["atributos"]["fuerza"]

            if "Big Bang Attack" in personaje["tecnicas"]:
                 fuerza= fuerza + 10
                 if fuerza > 100:
                      fuerza = 100
print(personajes["nombre"], personajes["atributos"]["fuerza"])

def ejercicio6():
    for personaje in personajes:
        if "Saiyan" in personaje["raza"]:
            personaje.remove[personaje]

    for personaje in personajes:
         print[personaje]



        