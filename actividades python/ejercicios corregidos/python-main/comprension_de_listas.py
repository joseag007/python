notas = [4, 8, 3, 9, 5]

resultados = ["Aprobado" if nota >= 5 else "Suspenso" for nota in notas]
print(resultados)

numeros = range(1,11)
pares = [n for n in numeros if n % 2 == 0]
print(pares)

numeros = [1,2,6,7,10]

if 7 in numeros:
    print("El 7 está")