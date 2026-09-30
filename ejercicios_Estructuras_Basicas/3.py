edad = int(input("Introduce su edad: "))

if edad>= 18 and edad <= 120:
    print("Mayor de edad")
elif edad >= 0 and edad < 18:
    print("Menor de edad")
elif edad < 0:
    print("Error, edad no valida")
else:
    print("Eres un vampiro")

