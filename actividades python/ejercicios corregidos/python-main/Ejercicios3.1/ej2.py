"""
Crea una función llamada convertirTemperatura que reciba un número con decimales y dos cadenas de caracteres. Las cadenas de caracteres posibles
serán “C”, “K” y “F”, que representan unidades de temperatura (Celsius, Kelvin y Fahrenheit). La función devolverá, como número con decimales, el
resultado de convertir de la primera unidad que reciba la función a la segunda. Por ejemplo, convertirTemperatura(10,”F”,”C”) devolvería el
resultado de pasar 10 Fahrenheit a Celsius. Devuelve el resultado con dos decimales, redondeando al valor más cercano.
"""
def convertirTemperatura(num: float, str1: str, str2: str) -> float:
    unidades_validas = ("C", "K", "F")
    if str1 not in unidades_validas or str2 not in unidades_validas:
        return 0.0

    if str1 == str2:
        return round(num, 2)

    aux = 0.0
    if str1 == "C":
        if str2 == "F":
            aux = num * (9 / 5) + 32
        elif str2 == "K":
            aux = num + 273.15
    if str1 == "F":
        if str2 == "C":
            aux = (num - 32) * (5 / 9)
        elif str2 == "K":
            aux = (num - 32) * (5 / 9) + 273.15
    if str1 == "K":
        if str2 == "C":
            aux = num - 273.15
        elif str2 == "F":
            aux = (num - 273.15) * (9 / 5) + 32

    return round(aux, 2)