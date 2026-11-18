from datos import jugadores

pase_alto = [j["nombre"] for j in jugadores if j["atributos"]["pase"] >= 9]
print(pase_alto)