"""
Pedir al usuario un número entero y añadir todos los números de la serie de
fibonacci desde 0 hasta ese número (incluido) a una lista. Mostrar dicha lista al
acabar. Si el número introducido es menor que 0, mostrar un mensaje de error.
"""

def fibonacci(num:int)->int:
    fibonacci = [0,1]
    for i in range(3,num+1):
        
        
        nuevoNum=fibonacci[-2]+fibonacci[-1]
        print("Iteración ", i)
        print("Nuevo num: ", nuevoNum)
        print("==========")

        fibonacci.append(nuevoNum)
    
    return fibonacci


numero = int(input("indique numero "))


if numero <=0:
    print('error, el numero no puede ser menor o igual a 0')
elif numero == 1:
    print([0])
else:

    print(fibonacci(numero))