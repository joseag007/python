"""
Pedir al usuario un número entero y calcular el sumatorio desde 1 hasta dicho
número (incluido). Si el número introducido es menor que 1, mostrar un mensaje de
error.
"""

numero = int(input("indique numero "))
numFinal =0

if numero <=0:
    print('error, el numero no puede ser menor a 0')
else:
    for i in range(1,numero+1):
        numFinal=numFinal+i

print(numFinal)