def main():


if __name__ == "__main__":
    main()

frutas = ["Manzana","Pera","Melocotón"]

frutas_2 = ["kiwi","sandía","Melón"]

frutas.extend(frutas_2)

print(frutas[5])

tupla = (3,5,7)

print("primer elemento ", tupla[0])


inicio = int(input("Inicio:"))
fin = int(input("Fin:"))
salto = int(input("Salto:"))
rango = range(inicio, fin, salto)


print(rango)

