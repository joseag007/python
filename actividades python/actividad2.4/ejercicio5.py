from datos import jugadores

ruleta = [j for j in jugadores if "ruleta" in j["filigranas"]]
print("5.", ruleta)