"""
A partir de 60 mm de lluvia acumulados en 12 horas se declara una alerta amarilla, y
a partir de 120 mm, una alerta roja. Pedir al usuario los milímetros de lluvia
acumulados y mostrar por pantalla si No hay alerta, Hay alerta amarilla o Hay
alerta roja. Realizar una versión con IF y otra con MATCH.
"""

mm = float(input("indique mm: "))

if mm < 60:
    print("no hay alerta")
elif mm >= 60 and mm < 120:
    print ("alerta amarilla")
elif mm >= 120:
    print("alerta roja")
else :
    print("mm no valido")

match mm:
    case n if n < 60 :
        print("no hay alerta")
    case n if n >= 60 and n < 120:
        print ("alerta amarilla")
    case n if n >= 120 :
        print("alerta roja")
    case _:
        print("mm no valida")