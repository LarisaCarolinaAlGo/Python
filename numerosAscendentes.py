#Larisa Álvarez
inicio = int(input("Ingrese el número desde el cual quiere iniciar: "))
final = int(input("Ingrese el número desde el cual quiere terminar: "))
contador = 1
while inicio <= final :
    if contador <= 5:
        print(inicio, end=" ")

        contador += 1

    elif contador == 6:

        print("")
        contador = 1
    inicio += 2
