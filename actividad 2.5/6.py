from datos import series

lista = [f"La serie {j['titulo']} tiene {len(j['reseñas'])} reseñas" for j in series]
print(lista)