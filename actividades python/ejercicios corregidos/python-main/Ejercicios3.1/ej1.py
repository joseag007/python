"""
Crea una función llamada comprobarLetraDNI que reciba una cadena de caracteres que representará al DNI de una persona y devuelva True si el DNI
es correcto y False si no lo es. Un DNI es correcto si tiene 8 dígitos enteros seguidos de una letra (mayúscula o minúscula), y la letra es correcta. Para
conocer si la letra es correcta puedes consultar la web del Ministerio del Interior.
"""

valido=False
DNI=input("Introduce DNI: ")
if len(DNI) != 9:
        print( False)

num = DNI[:8]
letra = DNI[8].upper()

if not num.isdigit():
    print( False)
if not letra.isalpha():
    print( False)

num = int(num)
letras = "TRWAGMYFPDXBNJZSQVHLCKE"
resto = letras[num % 23]

print( letra == resto)

            
