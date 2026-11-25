"""
Muestra una lista de tuplas que incluya el título de la serie y “Obra maestra” si las
notas medias dadas en las reseñas es igual o superior a 9, y “Gran serie” en caso
contrario.
"""

from series import series

#lista = [((s["titulo"], "obra maestra") for s in series for r in s["reseñas"]) if sum(r["nota"])/len(r["nota"])>=9 else (s["titulo"], "gran serie") for s in series]
#lista = [(s["titulo"], "obra maestra") if (sum(r["nota"]) for r in s["reseñas"]) / len(s["reseñas"]) >=9 else (s["titulo"], "gran serie") for s in series]
lista = [(s["titulo"],"obra maestra" if sum(r["nota"] for r in s["reseñas"]) / len(s["reseñas"]) >=9 else "Gran Serie") for s in series]

print (lista)