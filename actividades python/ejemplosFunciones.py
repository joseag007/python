def suma2(a:int, b:int) -> int:
    return a+b

def suma3(a,b):
    return a +b, a,b

def suma4 (*numeros):
    for n in numeros:
        suma += n
        return suma
    #return sum(numeros)

s = suma4(1,2,3,4)
print(s)