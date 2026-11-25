"""
Pedir al usuario dos números enteros y mostrar los números pares dentro de dicho
intervalo. Si el primer número es mayor que el primero se mostrará por pantalla un
mensaje de error. Realizar una versión con FOR y otra con WHILE.
"""

num1 = int(input("indique numero 1 "))
num2 = int(input("indique numero 2 "))



for i in range (num1,num2):
    if (i % 2 == 0):
        print (i)

for i in range (num2,num1):
    if (i % 2 == 0):
        print (i)
