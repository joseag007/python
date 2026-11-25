from datos import personajes

def ejercicio1():
    lista=[p["nombre"] for p in personajes if ("Cuerpo de Exploracion" in p["afiliacion"]) and p["vivo"]]
    print(lista)

def ejercicio2():
    lista=[p["nombre"] for p in personajes if ("Cuerpo de Exploracion" in p["afiliacion"]) and ("Supervivencia" in p["habilidades"]) or ("Sigilo" in p["habilidades"])]
    print(lista)

def ejercicio3():
    lista=[(p["nombre"],p["afiliacion"]) for p in personajes if ("Cuerpo de Exploracion" not in p["afiliacion"])]
    print(lista)

def ejercicio4():
    lista=[(p["nombre"]+" "+p["afiliacion"]) for p in personajes if p["registro_combate"]["misiones_completadas"]>=20]
    print(lista)

def ejercicio5():
    lista=[(p["nombre"],{p["estatura_m"]*100}) for p in personajes if p["estatura_m"]>1.7]
    print(lista)

def ejercicio6():
    lista=[h for p in personajes for h in p["habilidades"]]
    print(lista)
########

def ejercicio7():
    lista=[p["nombre"] for p in personajes for r in p["registro_combate"] if r["titanes_solo"]+r["titanes_equipo"]>=5]
    print(lista)



def ejercicio8():
    lista=[(p["nombre"],{r["titanes_solo"]+r["titanes_equipo"]}) for p in personajes for r in p["registro_combate"] ]
    print(lista)
#######


def ejercicio9():
    mediaaltura=(sum(p["estatura_m"] for p in personajes)/len(personajes))
    print(mediaaltura)

def ejercicio10():
    mediaaltura=(sum(p["estatura_m"] for p in personajes)/3)
    lista=[(p["nombre"],p["estatura_m"]) for p in personajes if p["estatura_m"]>mediaaltura]
    print(lista)


