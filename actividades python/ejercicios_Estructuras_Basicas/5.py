num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca un segundo número: "))

if num1 > num2:
    print("Error")
else:
    for i in range(num1,num2):
        if i % 2 == 0:
            print(i)

if num1> num2:
    print("Error")
else:
    i = num1
    while i <= num2:
        if i % 2 == 0:
            print(i)
            i = i +i