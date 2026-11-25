"""
Supongamos que la contraseña para acceder es “12345”. Pedir al usuario la
contraseña por pantalla y, si es la correcta, mostrar un mensaje de bienvenida. Si la
contraseña introducida es incorrecta, volver a pedirla hasta que se introduzca
correctamente.
"""

contrasena = '12345'
contrIncorr = False

while(contrIncorr):
    teclado = input('indique contraseña')
    if teclado==contrasena :
        conIncorr=True
print('bienvenid@ usuario')