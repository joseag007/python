num = int(input("Introduce un número"))

a = 0
b = 1

for i in range(num +1):
    print(b)
    siguiente = a +b
    a = b
    b = siguiente