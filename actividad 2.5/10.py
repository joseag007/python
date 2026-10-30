from datos import series

lista = [r["usuario"] for j in series if "Drama" for r in j["reseñas"] in j["generos"]]
print(lista)