"""
Crea una clase llamada Jarra que tenga los siguientes atributos:
● capacidad (int)
● contenido (int), por defecto cero
La clase tendrá un constructor con las siguientes especificaciones:
● Si la capacidad es cero o menos, se lanzará una excepción.
● Si el contenido es menor que cero, se lanzará una excepción.
● Si el contenido es superior a la capacidad, se modificará para que sea igual a
la misma.
Asimismo, tendrá los siguientes métodos:
● llenar: Llena la jarra.
● vaciar: Vacía la jarra.
● servir: Extrae una cantidad concreta de la jarra. Si la cantidad solicitada es
superior al contenido de la jarra, lanzará una excepción.
● llenar_desde: Sirve el contenido de otra jarra en la nuestra hasta que se
llene o la otra jarra se vacíe.
Una vez creada la clase, realiza las siguientes acciones en otro fichero:
    1. Crea dos jarras, ambas vacías y con 500 y 1000 de capacidad.
    2. Llena ambas jarras.
    3. Vacía la segunda jarra.
    4. Sirve 200 de la primera jarra.
    5. Llena la segunda jarra desde la primera.
"""
class Jarra:
    def __init__ (self,capacidad:float,contenido:float=0):
        if contenido <0 or capacidad<0:
            raise ValueError("el contenido ni la capacidad no puede ser 0 o inferior")
        self.capacidad=capacidad
        self.contenido=contenido
        self.desborda()

    def desborda(self):
        if self.capacidad<self.contenido:
            self.contenido=self.capacidad

    def llenar(self):
        self.contenido=self.capacidad

    def vaciar(self):
        self.contenido=0

    def llenarDesde(self,jarra:Jarra):
        capacidadDisponible=self.capacidad-self.contenido
        if jarra.contenido<=capacidadDisponible:
            self.depositar(jarra.contenido)
            jarra.vaciar()
        else:
            self.depositar(capacidadDisponible)
            jarra.servir(capacidadDisponible)

    def depositar (self, cantidad:int):
        if cantidad <0:
            raise ValueError("la cantidad no puede ser 0 o menor")
        self.contenido +=cantidad
        self.desborda()

    def servir (self, cantidad:int):
        if cantidad <0:
            raise ValueError("la cantidad no puede ser 0 o menor")
        elif cantidad>self.contenido:
            raise ValueError("la cantidad no puede ser mas que su contenido actual")
        else:
            self.contenido -=cantidad

    def __str__(self):
        return f"esta a {self.contenido}ml de {self.capacidad}ml"
jarra1=Jarra(500)
jarra2=Jarra(1000)
jarra1.llenar()
jarra2.llenar()
jarra2.vaciar()
jarra1.servir(200)
print(jarra1)
jarra2.llenarDesde(jarra1)
print(jarra1)
print(jarra2)