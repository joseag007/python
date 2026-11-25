"""
Pedir al usuario un número y mostrar el triángulo de pascal de ese número de filas.
En caso de que el número sea inferior a 1, mostrar un mensaje de error.
"""

numero = int(input("indique numero "))
pirLay=(1)


if numero <=1:
    print('error, el numero no puede ser menor a 1')
else:
    for i in range (1,numero):
        print(pirLay)
        