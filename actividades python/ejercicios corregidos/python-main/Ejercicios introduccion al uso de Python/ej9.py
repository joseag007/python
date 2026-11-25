"""
Pedir al usuario un número entero y mostrar por pantalla si el número es primo o no.
"""
esprimo=True
numero=int(input("indique numero "))

if numero<2:
    es_primo=False
else:
    for i in range(2,int(numero/2)+1):
        print(numero,"/",i," - Resto = ",numero%i)
        if numero % i ==0:
            esprimo=False
            break

print(esprimo)







"""


numero = int(input("indique numero"))
primos = (2,3,5,7)
esprimo = False
salida = False

while (salida):
    #antes de esto hay que hacer algo para añadir primos en la variable primos
   # for 

    for primo in primos:
        if(numero==primo):
            esprimo==True
        
        elif(numero%primo==0):
            esprimo=False
        
"""