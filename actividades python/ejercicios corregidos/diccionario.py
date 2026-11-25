diccionario = {
    "nombre" : "Pepe",
    "apellidos" : "López",
    "edad" : 18
}
diccionario["edad"] = 20
diccionario["direccion"] = "Calle 1"
del diccionario["edad"]

#print(diccionario["direccion"])
#print(diccionario)


estudiantes = [
    {
        "nombre" : "Joselín",
        "apellido" : "Flores",
        "modulos" : ["Acceso a datos", "Python", "Proyecto"],
    },
    {
            "nombre" : "Camilo",
            "apellido" : "Sesto",
            "modulos" : ["Acceso a datos", "Desarrollo de interfaces"],
        }
]

#print(estudiantes[1]["modulos"][1])
#print(estudiantes[0])

conjunto = {2,1,3,3,4}
conjunto.add(7)
conjunto.remove(3)
#print(conjunto)

def main():
    print("este es mi main")

if __name__=="__main__":
    main()