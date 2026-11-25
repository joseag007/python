"""Crea una clase llamada Punto y otra llamada Segmento.
Un punto representará a un punto matemático, y un segmento a un segmento
matemático. Las especificaciones son las siguientes:
● Punto
    ○ Atributos:
        ■ coordenadaX : int
        ■ coordenadaY : int
        ○ Constructor:
        ■ Crea por defecto un punto con ambas coordenadas a 0. En
        caso contrario, lo crea con las coordenadas especificadas. Si
        una de las coordenadas tiene un valor que exceda a 100 o -100,
        lanzará una excepción.

    ○ Métodos:
        ■ __str__ : Imprime el punto con el formato Punto(coordenadaX,
        coordenadaY)

        ■ __eq__ : Recibe como parámetro otro punto y devolverá True si
        para ambos la coordenadaX es igual y la coordenadaY es igual.

● Segmento
    ○ Atributos:
        ■ puntoA : Punto
        ■ puntoB : Punto
    ○ Constructor:
        ■ Crea por defecto un segmento con puntoA = Punto(0,0) y
        puntoB = Punto(1,1).

    ○ Métodos:
        ■ __str__ : Imprime el punto con el formato Segmento[puntoA,
        puntoB]
        ■ longitud : Devuelve la longitud del segmento, que se calcula con
        la siguiente fórmula:

        ■ __eq__ : Recibe como parámetro otro Segmento y devolverá
        True si para ambos el puntoA es igual y el puntoB es igual."""

import math


class Punto:
    def __init__ (self,coordX:float=0,coordY:float=0):

        if coordX>100 or coordY>100 or coordX<-100 or coordY<-100:
            raise ValueError("el valor de las coordenadas deve estar entre -100 y 100")
            
        self.coordX=coordX
        self.coordY=coordY

    def __str__(self)->str:
        return f"({self.coordx},{self.coordY})"

    def __eq__(self,punto:Punto)->bool:
        isEqual:bool=False
        if punto.coordX==self.coordX and punto.coordY==self.coordY:
            isEqual=True

        return isEqual
class Segmento:
    def __init__ (self,punto1:Punto=Punto(),punto2:Punto=Punto(1,1)):
    
        
            
        self.punto2=punto2
        self.punto1=punto1
    def __str__ (self)->str:
        return (f"[{self.punto1.__str__},{self.punto2.__str__}]")
    def longitud(self)->float:
        return math.sqrt(((self.punto1.coordX-self.punto1.coordX)**2)+(self.punto2.coordX-self.punto2.coordX)**2)
    def __eq__ (self, segmento:Segmento)->bool:
        isEqual:bool=False
        if segmento.punto1.__eq__(self.punto1) and segmento.punto2.__eq__(self.punto2):
            isEqual=True
        return isEqual
