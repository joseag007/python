from datos import series

lista = [j["titulo"] for j in series if j["nota"] >= 9 and len(j["generos"]) >= 3]
print(lista)