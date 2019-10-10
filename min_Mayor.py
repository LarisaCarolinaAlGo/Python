#Larisa

cambio = ""
palabra = input("Ingrese una palabra: ")

for x in palabra:
    if x == "a":
        cambio += x.upper()
    elif x == "e":
        cambio += x.upper()
    elif x == "i":
        cambio += x.upper()
    elif x == "o":
        cambio += x.upper()
    elif x == "u":
        cambio += x.upper()
    else:
        cambio += x
print(cambio)
