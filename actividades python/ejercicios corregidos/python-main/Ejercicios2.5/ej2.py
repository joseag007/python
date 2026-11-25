"""
Muestra los títulos de las series que sean de Fantasía o Misterio.
"""

from series import series

fansterio = [s["titulo"] for s in series if "Fantasía" or "Misterio" in s["generos"] ]
print (fansterio)