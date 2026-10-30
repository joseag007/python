from datos import series

lista = [r["comentario"] for j in series for r in j["reseñas"] if len(r["comentario"]) > 40]
print(lista)