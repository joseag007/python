def convertir_acciones(compañia : str, cantidad : int, cambio : str) -> float:
    compañia = compañia.upper()
    cambio = cambio.lower()
    valorAcciones: float
    
    if compañia  not in ["NVDA", "SONY", "BMW"]:
        raise ValueError("Las compañias disponibles solo pueden ser NVDA, SONY o BMW")
    
    if cambio  not in ["euro", "dolar", "libra"]:
            raise ValueError("Las divisas disponibles solo son el euro, el dolar y la libra")
        
    if compañia == "NVDA":
        valorAcciones = 156.20 * cantidad
    elif compañia == "SONY":
        valorAcciones = 24.16 * cantidad
    elif compañia == "BMW":
        valorAcciones = 58.12 * cantidad
        
    if cambio == "euro":
        valorAcciones = valorAcciones
    elif cambio == "dolar": 
        valorAcciones = valorAcciones * 1.10
    elif cambio == "libra":
        valorAcciones = valorAcciones * 0.83
    
    return round(valorAcciones,2)

print(convertir_acciones("NVDA", 10, "euro"))
print(convertir_acciones("SONY", 5, "dolar"))
print(convertir_acciones("BMW", 20, "libra"))
print(convertir_acciones("bmw", 20, "LIBRA"))