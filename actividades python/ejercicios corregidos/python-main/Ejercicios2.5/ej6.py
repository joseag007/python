"""
Muestra una lista de cadenas con el formato “La serie {titulo} tiene {n} reseñas”, para
todas las series.
"""

from series import series

#resenas = [("La serie",s["titulo"],"tiene",len(s["reseñas"]),"reseñas") for s in series for r in s["reseñas"]]
resenas = [(f"La serie {s["titulo"]} tiene {len(r)} reseñas") for s in series for r in s["reseñas"]]
print (resenas)
