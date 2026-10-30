from datos import series

lista = [(j["titulo"], r["nota"]) for j in series for r in j["reseñas"] if r["usuario"] == "Elena"]

print(lista)