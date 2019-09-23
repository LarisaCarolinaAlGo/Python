#Larisa Álvarez

numero = int(input("Ingrese un número: "))
num = 1
while num <= numero:
    print(num)
    num += 2


while num < numero:
    if num % 2 != 0:
        print(num)
