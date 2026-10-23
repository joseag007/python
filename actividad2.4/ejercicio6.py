from datos import jugadores

tiro_regate = [j for j in jugadores if j["atributos"]["tiro"] >= 8 
    and j["atributos"]["regate"] >= 9]
print(tiro_regate)