"""
Crea una función llamada calcularValorBruto, que reciba un número con
decimales (el precio de un producto) y una cadena de caracteres (que
representará el tipo de IVA aplicable). Las cadenas de caracteres posibles
serán GENERAL, REDUCIDO y SUPERREDUCIDO. La función devolverá el
resultado de sumar el IVA aplicable al valor neto del producto. Por ejemplo,
calcularValorBruto(10,”GENERAL”) devolvería el resultado de sumar a los
10€ de valor neto, el porcentaje de IVA del tipo general (que es un 21%), lo
que daría 12,1€. Devuelve el resultado con dos decimales, redondeando
hacia arriba.
"""


import math


def calcularValorBruto(precio: float, iva: str) -> float:
    unidades_validas = ("GENERAL", "REDUCIDO", "SUPERREDUCIDO")
    aux = 0.0
    porcentaje = 0
    if iva not in unidades_validas:
        return aux

    if iva == "GENERAL":
        porcentaje = 21
    elif iva == "REDUCIDO":
        porcentaje = 10
    elif iva == "SUPERREDUCIDO":
        porcentaje = 4

    bruto = ((porcentaje * precio) / 100) + precio

    return math.ceil(bruto * 100) / 100