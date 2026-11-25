contador = 0 

while contador <=10:
    print(contador)
    contador += 1

animales = ["lince iberico","quebrantahuesos","cabra montesa"]

while animales:
    animal = animales.pop(0)
    #.pop lo que hace eliminar el hueco especificado, y devuelve ese mismo animal
    print (animal)