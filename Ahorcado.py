#Larisa Álvarez

#regresa el número en el que se encuentra un elemento de la lista
import os
import random


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def palabras():

    palabras = ["orrnitorrinco", "alive", "electroencefalografista", "otorrinolaringologo", "pistache"]
    usadas = random.randint(0,len(palabras)-1)
    palabra = palabras[usadas]

    return palabra

def esconde(palabras):
    lista = []
    for x in palabras:
        lista.append("*")

    return lista

def revisar(palabra, letra, escondida):
    if letra in palabra:
        for z in range(0, len(escondida)):
            if palabra[z] == letra:
                escondida[z] = letra
        return True
    else:
        return False

def obtener_letra(utilizadas):

    condicion = 1
    while condicion != 0:

        abc = "abcdefghijklmnñopqrstuvwxyz"
        letra = input("\nDame la letra que quieras usar: ")
        letra = letra.lower()

        if letra in utilizadas:
            print("Esa letra ya la uso, ingrese otra letra ")
        elif letra not in abc:
            print("Tiene que ser una letra")
        elif len(letra) != 1:
            print("Solo una letra")
        else:
            condicion = 0
    return letra

def dibuja_ahorcado(numero_error):
    dibujos=['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']
    return dibujos[numero_error]

def estado_actual (escondida, errores, utilizadas):
    clear()
    print("Palabra:", end=" ")
    print("  ".join(escondida))
    print(dibuja_ahorcado(errores))
    print("Letras usadas:", end=" ")
    print(", ".join(utilizadas))
    print(f"Errores:  {errores}")
def juego(palabra):
    errores = 0
    utilizadas = []
    palabraEscondida = esconde(palabra)
    print("Palabra escondida ", end = " ")

    for x in palabraEscondida:
        print (x, end = " " )

    while errores < 6:
        letra = obtener_letra(utilizadas)
        utilizadas.append(letra)
        if revisar(palabra, letra, palabraEscondida):
            esc = "".join(palabraEscondida)
            estado_actual(palabraEscondida, errores, utilizadas)

            if palabra == esc:
                return True

        else:
            errores += 1
            estado_actual(palabraEscondida, errores, utilizadas)

    return False


print("""Bienvenido al juego de ahorcado

  ____________________
 /    __       __     \.
|                      |
|                      |
|    \ /       \ /     |
|    / \       / \     |
|          o           |
|        _____         |
|          U           |
 \____________________/

Presione enter para continuar: """)
input()
clear()
gano = juego(palabras())
if gano:
    print("""Felicidades, has ganado.
     ___            ___
    /   \          /   \.
    |   |          |   |
    |   |          |   |
    |   | ________ |   |
    |   |/        \|   |
    |    __       __   |
    |   |  |     |  |  |
    |   |__|     |__|  |
    |        \_/       |
    \      \__|__/     /
     \________________/""")
else:
    print("""Lo siento, suerte para la próxima.
      ____________________
     /    __       __     \.
    |                      |
    |                      |
    |    ____      ____    |
    |   /    \    /    \   |
    |    ()    oo    ()    |
    |        _____         |
    |       /______\       |
     \____________________/""")
