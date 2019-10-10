#Larisa
contador = ""
palabras = ["vestir", "vestidor"]

palabra1 = palabras[0]
palabra2 = palabras[1]

for palabra in palabras:
    if palabra1[0] == palabra2[0]:
        contador += palabras[0][0]
        if palabra1[1] == palabra2[1]:
            contador += palabras[0][1]
            if palabra1[2] == palabra2[2]:
                contador += palabras[0][2]
                if palabra1[3] == palabra2[3]:
                    contador += palabras[0][3]
    else:




print(contador)
