"""
Pedir al usuario dos números enteros (base y potencia). Calcular el resultado de
elevar la base al exponente. Mostrar un error en caso de que la base sea menor que
1 o que la potencia sea menor que 0.
"""
def potencia(num1:int,num2:int)->int:

    numFinal=num1
    for i in range(1,num2):
        numFinal=numFinal*num1
    return numFinal

numero1 = int(input("indique numero "))
numero2 = int(input("indique potencia "))
numFinal =0

if (numero1 <=0) or (numero2 < 0):
    print('error, el numero no puede ser menor a 1 ni la potencia menor a 0')
else:
    

    print(potencia(numero1,numero2))