"""
Muestra una lista de tuplas (titulo_serie, nota_dada) de las reseñas dejadas por el
usuario Elena.
"""

from series import series

#lista = [(s["titulo"],e["nota"]) for s in series  if s["reseñas"]["usuario"]=="Elena"]

lista=[(s["titulo"],r["nota"]) for s in series for r in s["reseñas"] if r["usuario"]=="Elena"]
print (lista)