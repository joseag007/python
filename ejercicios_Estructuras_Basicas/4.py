Lluvia_acumulada = float(input("Milimetros de lluvia en 12 horas"))
if Lluvia_acumulada < 60:
    print("No hay alerta roja")
elif Lluvia_acumulada >= 60 and Lluvia_acumulada < 120:
    print("Alerta amarilla")
else:
    print("Alerta roja")

match Lluvia_acumulada:
    case x if x <60:
        print("No hay alerta")
    case x if x >= 60 and x < 120:
        print("Alerta amarilla")
    case _:
        print("Alerta roja")

