def es_primo(n):
    if n  <2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True
    
num = int(input("Ingrese un número: "))

if es_primo(num):
    print("El número es primo")
else :
    print("El número no es primo")