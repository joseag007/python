precio = float(input("Introduce una nota numérica: "))
iva = input("Tipo de IVA: ").lower()
precioFinal

if iva == "general":
    precioFinal = precio + (precio * 0.21)
elif iva == "reducido":
    precioFinal = precio + (precio * 0.1)
elif iva == "superreducido":
    precioFinal = precio + (precio * 0.04)