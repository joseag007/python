"""
Pedir al usuario la edad de una persona y mostrar si es mayor o menor de edad. Si
la edad es menor a 0 mostrar un mensaje de error, y si es superior a 120 indicar que
es un vampiro.
"""

edad = int(input ("indique su edad: "))
if edad >=0 and edad < 120:
    print("su edad es",edad)
elif edad <0:
    print("error")
elif edad > 120:
    print("VAMPIRO!!, A LA HOGUERA!!!")
