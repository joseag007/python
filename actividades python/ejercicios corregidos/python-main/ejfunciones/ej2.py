"""
Pedir al usuario un número entero y calcular el factorial desde 1 hasta dicho número
(incluido). Si el número introducido es menor que 1, mostrar un mensaje de error.
"""

def factorial(num:int)->int:
    numFinal =1
    for i in range(1,num+1):
            numFinal=numFinal*i

    return numFinal

numero = int(input("indique numero "))



if numero <=0:
    print('error, el numero no puede ser menor a 0')
else:

    

    print(factorial(numero))