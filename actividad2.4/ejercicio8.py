from datos import jugadores 

tupla = [j for j in jugadores if j["atributos"]["tiro"] >= 8 
    and j["atributos"]["regate"] >= 9]