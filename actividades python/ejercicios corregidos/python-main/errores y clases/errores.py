def convertirTemperatura(num: float, str1: str, str2: str) -> float:
    unidades_validas = ("C", "K", "F")
    str1=str1.upper
    str2=str2.upper
    if str1 not in unidades_validas or str2 not in unidades_validas:
        #return 0.0
        raise ValueError("no se ha idicado correctamente la medida (C,K o F)")

    if str1 == str2:
        #return round(num, 2)
        raise ValueError("las dos medidas son iguales, por favor indique dos medidas diferentes")

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