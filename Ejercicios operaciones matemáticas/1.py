num1 = int(input("Introduzca un entero: "))
resultado = 0

if (num1 < 0):
    print("El número introducio es negativo")
else:
    for i in range(1, num1 + 1):
        resultado += i
        
    print(resultado)