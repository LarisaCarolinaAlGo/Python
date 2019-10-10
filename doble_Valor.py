#larisa Carolina
num = 0
numeros = []
dobles = []

while num < 4:
    usuario = int(input("Ingrese un número: "))
    numeros.append(usuario)
    num += 1

for x in numeros:
    doble = x*2
    dobles.append(doble)

print(dobles)
