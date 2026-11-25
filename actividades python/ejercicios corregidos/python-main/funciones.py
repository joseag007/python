def suma1(a,b):
    return a+b

def suma2(a:int,b:int):
    return a+b

def suma3(a:int,b:int)-> int:#para obligar que devuelva un int o lo que sea, es necesario la flechita , indicando que tipo de dato antes de los ":"

    return a+b

def suma4(a:int,b:int)-> int:

    return a+b,a,b#se puede devolver varios datos a la vez
num1,num2,num3=suma4(3,4)

print(num1,num2,num3)

def suma5(*numeros):#esto para generar una tupla con los datos que le proporcionen
    return sum(numeros)