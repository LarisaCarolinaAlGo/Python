#Larisa Álvarez
nombre = input("Hola, cuál es tu nombre? ")

#Input
genero = input("Eres hombre o mujer? ")
edad = int(input(f"Qué edad tienes {nombre}? "))

#Proceso
mujer = (220 - edad) / 10
hombre = (210 - edad) / 10
if genero == "mujer" or genero == "Mujer":
    print (f"Tu número de pulsaciones en 10 segundos es de {mujer}")
else:
    print (f"Tu número de pulsaciones en 10 segundos es de {hombre}")

#Output
