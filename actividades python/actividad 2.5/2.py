from datos import series

lista = [j["titulo"] for j in series if "Fantasía" in j["generos"] or  "Misterio" in j["generos"]]
print(lista)