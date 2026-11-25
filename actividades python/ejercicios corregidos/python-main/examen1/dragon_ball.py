from datos import personajes
def ejercicio1():
    personajes.append({
        "nombre": "Saitama",
        "raza": "Humano",
        "nivel_pelea": 900000001,
        "tecnicas": ["Nomral Punch", "Serious punch","Consecutive Soft Punchs"],
        "atributos": {
            "fuerza":100,
            "defensa":100,
            "velocidad":99}
    })
    print (personajes)


def ejercicio2():
    for personaje in personajes:
       
        media=(personaje["atributos"]["fuerza"]+personaje["atributos"]["defensa"]+personaje["atributos"]["velocidad"])/3
        
        print (media)
        if media>80:
            print(personaje)
        

def ejercicio3():
    media=0
    contador=0
    for personaje in personajes:
           
        media=media+personaje["atributos"]["velocidad"]
        contador=contador+1
        print (media)
    media=media/contador
    for personaje in personajes:
        if personaje["atributos"]["velocidad"]>media:
            print(personaje)




def ejercicio4():
    for personaje in personajes:
               
            for tecnica in personaje["tecnicas"]:
                if tecnica=="Big Bang Attack":
                    personaje["atributos"]["fuerza"]=personaje["atributos"]["fuerza"]+10
                    if personaje["atributos"]["fuerza"]>100:
                        personaje["atributos"]["fuerza"]=100
            print (personaje)




def ejercicio5():

    print("quien gana a vegeta")



def ejercicio6():
    print("personajes eliminados:")
    for personaje in personajes[:]:
                   
                if personaje["raza"]=="Saiyan":
                     print (personaje)
                     personajes.remove(personaje)

