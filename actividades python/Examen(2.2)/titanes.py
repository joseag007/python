from datos import personajes


def ejercicio1():
    lista = [
        j["nombre"]
        for j in personajes
        if j["vivo"] == True and j["afiliacion"] == "Cuerpo de Exploración"
    ]
    print(lista)


def ejercicio2():
    lista = [
        j["nombre"]
        for j in personajes
        if j["afiliacion"] == "Cuerpo de Exploración"
        and "Supervivencia" in j["habilidades"]
        and "Sigilo" in j["habilidades"]
    ]
    print(lista)


def ejercicio3():
    # El enunciado pide una lista de tuplas: (nombre, afiliacion)
    lista = [
        (j["nombre"], j["afiliacion"])
        for j in personajes
        if j["afiliacion"] != "Cuerpo de Exploración"
    ]
    print(lista)


def ejercicio4():
    lista = [
        f"{j['nombre']} ({j['afiliacion']})"
        for j in personajes
        if j["registro_combate"]["misiones_completadas"] >= 20
    ]
    print(lista)


def ejercicio5():
    # El enunciado pide una lista de tuplas con la altura en centímetros
    lista = [
        (j["nombre"], j["estatura_m"] * 100)
        for j in personajes
        if j["estatura_m"] > 1.70
    ]
    print(lista)


def ejercicio6():
    lista = [s for j in personajes for s in j["habilidades"]]
    print(lista)


def ejercicio7():
    # registro_combate es un diccionario, se accede directamente a sus claves
    lista = [
        j["nombre"]
        for j in personajes
        if j["registro_combate"]["titanes_solo"]
        + j["registro_combate"]["titanes_equipo"]
        >= 5
    ]
    print(lista)


def ejercicio8():
    # El enunciado pide una lista de diccionarios
    lista = [
        {
            "nombre": j["nombre"],
            "titanes_totales": j["registro_combate"]["titanes_solo"]
            + j["registro_combate"]["titanes_equipo"],
        }
        for j in personajes
    ]
    print(lista)


def ejercicio9():
    alturas = [j["estatura_m"] for j in personajes]
    media = sum(alturas) / len(alturas)
    print(media)


def ejercicio10():
    media = sum([j["estatura_m"] for j in personajes]) / len(personajes)
    lista = [
        (j["nombre"], j["estatura_m"])
        for j in personajes
        if j["estatura_m"] > media
    ]
    print(lista)