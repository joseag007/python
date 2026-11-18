num = int(input("Introduzca el número de filas: "))

# Recorremos cada una de las filas
for i in range(num):

    # Creamos una lista vacía para guardar los números 
    # de la fila
    fila = []

    # Cada fila empieza y termina en 1
    for j in range(i + 1):

        # Si estamos en el principio o en el final de la fila,
        # el número siempre es 1
        if j == 0 or j == i:
            fila.append(1)

        # Para los números interiores, sumamos los dos números
        # que están justo encima de ellos
        else:
            fila.append(filas[i - 1][j - 1] + filas[i - 1][j])

    # Guardamos la fila para poder utilizarla en la siguiente
    if i == 0:
        filas = [fila]
    else:
        filas.append(fila)

    # Calculamos los espacios para centrar el triángulo
    espacios = " " * (num - i)

    # Convertimos los números de la fila a texto y los mostramos
    print(espacios + " ".join(map(str, fila)))

# Pero hay un pequeño detalle: filas debe inicializarse antes 
# del primer for. Por tanto, la versión correcta y que debes 
# utilizar es:

num = int(input("Introduzca el número de filas: "))

# Lista donde vamos a guardar todas las filas anteriores
filas = []

# Recorremos cada fila
for i in range(num):

    # Lista que contendrá los números de la fila actual
    fila = []

    # Recorremos las posiciones de la fila
    for j in range(i + 1):

        # El primer y último número de cada fila siempre son 1
        if j == 0 or j == i:
            fila.append(1)

        # Los números del medio se obtienen sumando
        # los dos números que están encima
        else:
            fila.append(filas[i - 1][j - 1] + filas[i - 1][j])

    # Guardamos la fila actual
    filas.append(fila)

    # Añadimos espacios para centrar el triángulo
    espacios = " " * (num - i)

    # Mostramos la fila
    print(espacios + " ".join(map(str, fila)))