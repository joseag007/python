"""
Pedir al usuario un número y mostrar el triángulo de pascal de ese número de filas.
En caso de que el número sea inferior a 1, mostrar un mensaje de error.
"""

def triangulo(num:int):

    pascal = []

    for i in range(x):
        if i == 0:
            pascal.append([1])
        else:
            last_row = pascal[-1]
            new_row = [1]

            for j in range(len(last_row) - 1):
                new_row.append(last_row[j] + last_row[j + 1])

            new_row.append(1)
            pascal.append(new_row)
    for row in pascal:
        print(row)
x = int(input("Introduce un número entero: "))

if x < 1:
    print("Error: Introduce un número mayor o igual que 1.")
else:
    triangulo(x)



