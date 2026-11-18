from datos import personajes

def ejercicio1():
    lista = [j["nombre"] for j in personajes if j["vivo"]==True and "Cuerpo de Exploracion"in j["afiliacion"]]
    print(lista)

def ejercicio2():
    lista = [j["nombre"] for j in personajes if "Cuerpo de Exploracion" in  j["afiliacion"] and "Sigilo" in j["habilidades"] and "Supervivencia" in j["habilidades"]]           
    print(lista)

def ejercicio3():
    lista = [f"{j['nombre']} {j['afiliacion']}" for j in personajes if j["afiliacion"]!= "Cuerpo de Exploracion"]
    print(lista)

def ejercicio5():
    lista = [f"{j['nombre']} {j['estatura_m']*100}cm" for j in personajes if j["estatura_m"]>1.70]
    print(lista)

def ejercicio6():
    lista = [s for j in personajes for s in j ["habilidades"]]
    print(lista)
    
def ejercicio7():
    lista = [j["nombre"] for j in personajes for s in j["registro_combate"] if s["titanes_solo"]+s["titanes_equipo"]>=5]
    print(lista)
    
def ejercicio8():
    lista = [f"{j["nombre"]} {j["registro_combate"]["titanes_solo"] + j["registro_combate"]["titanes_equipo"]}" for j in personajes]
    print(lista)
