def es_primo(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Ingrese un número: "))

if es_primo(num):
    print("El número es primo")
else: 
    print("El número no es primo")
    
    
def sumatorio(n : int) -> int:
    sumatorio = 0
    for i in range(1,n+1):
        sumatorio += i
    return sumatorio

print(sumatorio(3))


def calcular_suma_hasta_n(n):
    if n < 0:
        return "Error: el número no puede ser menor que 0"
    else:
        return sum(range(1, n + 1))
    
num1 = int(input("Introduce un número: "))

resultado = calcular_suma_hasta_n(num1)
print("El resultado es ", resultado)