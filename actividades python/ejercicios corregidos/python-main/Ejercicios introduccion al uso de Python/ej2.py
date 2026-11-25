"""
Pedir al usuario dos valores por pantalla: el precio de un producto (float) y el tipo de
IVA (General, Reducido, Superreducido). Calcular el precio final del producto fruto
de sumarle el IVA en función de su tipo. Realizar una versión con IF y otra con
MATCH.
"""

precio = float(input("indique el precio del producto:"))
iva = input("indique el tipo de iva (1=general, 2=reducido, 3=superreducido)")

if iva == "1":
    print("el precio total es :", ((precio*20/100)+precio))
elif iva == "2":
    print("el precio total es :", ((precio*10/100)+precio))
elif iva == "3":
    print("el precio total es :", ((precio*5/100)+precio))
else :
    print("valor no permitido")

#con match

match iva:
    case "1":
        print("el precio total es :", ((precio*20/100)+precio))
    case "2":
        print("el precio total es :", ((precio*10/100)+precio))
    case "3":
        print("el precio total es :", ((precio*5/100)+precio))
    case _:
        print("valor no permitido")

