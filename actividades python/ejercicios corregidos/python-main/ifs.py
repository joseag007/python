numero = int(input("introuce un numero: "))

if numero >0:
    print ("el numero es positivo")
elif numero <0:
    print ("el numero es negativo")
else:
    print ("el numero es 0")


# switch case aqui se llama match case

dia = input("introduce dia: ").lower() #el .lower pasa el string a minusculas

match dia:
    case "miercoles" | "viernes": #el or es una barra |, "and" para and
        print("hay clase")

    case "lunes" | "martes" | "jueves": 
            print("no hay clase")

    case _:# el case _: es para el default
        print("finde")


#bucles for

#suelen usarse rangos, usa del primer numero del rango asta el penultimo
for i in range(1,10):
     print (i)
for i in range(10,1,-1):
     print (i)

# for each

juegos = [
     "minecraft",
     "wow",
     "factorio",
     "ultrakill"
]

#ojo cuidado que la primera variable se suele poner un diferente nombre, por lo general se le quita la S del final
for juego in juegos:
     print (juego)

diccionarios =[
     {
          "titulo" : "minecraft",
          "desarrollador" : "mojang",
          "precio" : 25
     },
     {
          "titulo" : "ultrakill",
          "desarrollador" : "newblood",
          "precio" : 15
     },
     {
               "titulo" : "leage of legend",
               "desarrollador" : "satan",
               "precio" : 0
          }
]

for diccionario in diccionarios:
     if diccionario["precio"] == 0:
          print(diccionario["titulo"])


# los Strings son procaticamente listas de char y los identifica como eso
texto = "antonio villalba"

for letra in texto:
     print (letra)