from datos import series

animacion = [j["titulo"] for j in series if "Animación" in j["generos"]]
print(animacion)