# Larisa Álvarez
def sumatoria(numero):
    suma = 0
    vueltas = 0

    while vueltas < numero:
        suma += numero
        numero -= 1

    return suma

print(sumatoria(4))
