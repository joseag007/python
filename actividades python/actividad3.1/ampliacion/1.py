def sumatorio(num1 : int) -> int:
    
    if num1 < 0:
        raise ValueError("El número no puede ser negativo")

    resultado = 0
    for i in range(1, num1 + 1):
        resultado += i

    if (num1>=0):
        return resultado
    elif (num1<0):
        resultado = ValueError
        return resultado

def factorial(num2 : int) -> int:
    
    if num2 < 1:
        raise ValueError("El número no puede ser negativo")

    resultado = 1
    for i in range(1, num2 + 1):
        resultado = resultado * i

    if (num2>=1):
        return resultado
    elif (num2<1):
        resultado = ValueError
        return resultado

def aplicar_funcion(num1 : int, num2 : int, funcion=str) -> int:
    
    if funcion not in ["C", "F", "K"]:
            raise ValueError("Las unidades posibles solo pueden ser C, F o K")
    
    
    if num1 < 1:
        raise ValueError("El número no puede ser negativo")

    resultado = 1
    for i in range(1, num1 + 1):
        resultado = resultado * i

    return resultado