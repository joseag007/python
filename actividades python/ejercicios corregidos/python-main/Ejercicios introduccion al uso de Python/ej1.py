#Pedir al usuario una nota numérica entera mediante un input y diga si la calificación
#es Suspenso, Aprobado, Notable, Sobresaliente, o No válida (en caso de que la
#entrada sea diferente a la esperada). Realizar una versión con IF y otra con MATCH.

nota = int(input("cual es tu nota?: "))
# con if
if nota < 5 and nota >= 0:
    print("suspenso")
elif nota >= 5 and nota < 7:
    print ("aprobado")
elif nota >= 7 and nota <9:
    print("notable")
elif nota >=9 and nota <= 10:
    print("sobresaliente")
else :
    print("nota no valida")

# con match
match nota:
    case n if n < 5 and nota >= 0:
        print("suspenso")
    case n if n >= 5 and nota < 7:
        print ("aprobado")
    case n if n >= 7 and nota <9:
        print("notable")
    case n if n >=9 and nota <= 10:
        print("sobresaliente")
    case _:
        print("nota no valida")