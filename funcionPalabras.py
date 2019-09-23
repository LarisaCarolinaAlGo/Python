import random
def palabras():

    palabras = ["cacahuate", "kayak", "rainbow", "mickey", "fredy"]
    usadas = random.randint(0,len(palabras)-1)
    palabra = palabras[usadas]

    return palabra

print(palabras())
