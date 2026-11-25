class CuentaBancaria:
    def __init__ (self,titular,saldo=0):
        if saldo <0:
            raise ValueError("el saldo no puede ser 0 o inffferior")
        self.titular=titular
        self.saldo=saldo

    def depositar (self, cantidad):
        if cantidad <0:
            raise ValueError("la cantidad no puede ser 0 o menor")
        self.saldo +=cantidad
    def retirar (self, cantidad):
        if cantidad <0:
            raise ValueError("la cantidad no puede ser 0 o menor")
        elif cantidad>self.saldo:
            raise ValueError("la cantidad no puede ser superior al saldo")
        self.saldo -=cantidad
    def __str__(self):
        return f"Cuenta de {self.titular} | Saldo = {self.saldo}"
