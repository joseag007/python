num1 = int(input("Introduzca un número entero: "))
resultado = 1

if (num1 < 0):
    print("El número introducio es negativo")
else:
    for i in range(1, num1 + 1):
        resultado = resultado * i
        
    print(resultado)