#Larisa Alvarez

menoscinco_Cinco = 0
menor_Igual = 0
mayor_Igual = 0
numeros = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for z=0 to 19:
    if numeros[z] >= 5:
        mayor_Igual =+ 1
    elif numeros[z] <= -5:
        menor_Igual =+ 1
    else:
        menoscinco_Cinco =+ 1


print(f"""Numeros entre el -5 y 5: {menoscinco_Cinco}
Numeros menores o iguales a -5: {menor_Igual}
Numeros mayores o iguales a 5: {mayor_Igual}""")
