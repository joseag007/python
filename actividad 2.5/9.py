from datos import series

lista = [g for j in series for g in j["generos"]]
print(lista)