#Larisa Alvarez

menoscinco_Cinco = 0
menor_Igual = 0
mayor_Igual = 0
numeros = [3,6,98,2,5,9,5,-2,2,-2,-1,-8,-32,23,6,8,9,3,2,4,46,45,7654,-35347]

for x in numeros:
    if x >= 5:
        mayor_Igual += 1

    elif x <= -5:
        menor_Igual += 1
    else:
        menoscinco_Cinco += 1




print(f"""Numeros entre el -5 y 5: {menoscinco_Cinco}
Numeros menores o iguales a -5: {menor_Igual}
Numeros mayores o iguales a 5: {mayor_Igual}""")
