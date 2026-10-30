from datos import series

lista = [
    (j["titulo"], "Obra maestra" if sum(r["nota"] for r in j["reseñas"])
    / len(j["reseñas"]) >= 9 else "Gran serie") for j in series
]

print(lista)