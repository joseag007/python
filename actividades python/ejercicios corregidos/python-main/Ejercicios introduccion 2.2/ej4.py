"""
Pedir al usuario un número entero y añadir todos los números de la serie de
fibonacci desde 0 hasta ese número (incluido) a una lista. Mostrar dicha lista al
acabar. Si el número introducido es menor que 0, mostrar un mensaje de error.
"""

numero = int(input("indique numero "))
fibonacci = [0,1]

if numero <=0:
    print('error, el numero no puede ser menor a 0')
else:
    for i in range(3,numero+1):
       
        nuevoNum=fibonacci[-2]+fibonacci[-1]
        print("Iteración ", i)
        print("Nuevo num: ", nuevoNum)
        print("==========")

        fibonacci.append(nuevoNum)

print(fibonacci)