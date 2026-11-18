num = int(input("Introduce un número: "))
num2 = int(input("Introduce un segundo número: "))


if num > num2:
    print("Error")
else:
    for i in range(num, num2 + 1):
        primo = True

        if i < 2:
            primo = False
        else:
            for j in range(2, i):
                if i % j == 0:
                    primo = False


        if primo:
            print(i)