"""
Vamos a crear una función llamada aplicar_funcion que nos permita
ejecutar el cálculo de varios algoritmos matemáticos.
Crea primero una función sumatorio que reciba un número positivo (o cero) y
devuelva el resultado de sumar todos los números desde el 0 hasta dicho
número.
Crea luego una función factorial que reciba un número igual o mayor a 1 y
devuelva el resultado de multiplicar todos los números desde 1 hasta dicho
número.
Por último, crea la función aplicar_funcion, que reciba un valor numérico
entero y un string. Si la cadena de texto introducida es “sumatorio”, ejecutará
la función sumatorio con el valor pasado por parámetro, y si es “factorial”,
ejecutará la función factorial. Así, si por ejemplo introducimos “3” y “factorial”,
se devolverá el resultado “6”.
Además, en caso de introducir un valor numérico no permitido, se mostrará
un mensaje de error (por ejemplo, al introducir “-3” y “factorial”).
"""
def aplicar_funcion(numero:int,funcion:str)-> int:
    if numero <=0:
        raise ValueError(f'error, {numero} no puede ser menor a 0')
    unidades_validas = ["factorial","sumatorio"]
    if funcion not in unidades_validas:
        raise ValueError("no se ha idicado correctamente la funcion (factorial o sumatorio)")
    resultado=0
    if funcion==unidades_validas[0]:
        resultado=fractorial(numero)
    elif funcion==unidades_validas[1]:
         resultado=sumatorio(numero)
    return resultado


def sumatorio(numero:int)->int:
    numFinal=0
    for i in range(1,numero+1):
            numFinal=numFinal+i
    return numFinal

def fractorial(numero:int)->int:
    numFinal =1
    
    
    for i in range(1,numero+1):
        numFinal=numFinal*i

    return numFinal