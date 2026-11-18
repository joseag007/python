from datos import personajes
lista = [f"{j['nombre']} {j['afiliacion']}" for j in personajes if j["afiliacion"]!= "Cuerpo de Exploracion"]
print(lista)