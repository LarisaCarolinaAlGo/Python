
def calculadora(x, y):

    mult =  x * y
    return mult
    dividir = x / y
    return div
    suma = x + y
    return suma
    resta = x - y
    return resta

print('1. Caja')
print('2. Calculadora')
print('3. Listas')

opcion = int(input('Elige una opcion del menu: '))

if opcion == 1:
    print('Entraste a la opcion de caja')
    print("Cuál es el tipo de paquete?")
    print("Caja")
    print("Carta")
    paquete = input()

    print("Cuál es la prioridad?")
    print("""
    prioridad (a)
    carta = $120/ gramo
    caja = $4,575 * kilo

    prioridad (b)
    carta = $101 / gramo
    caja = $3,550.00 kilo

    prioridad (c)
    carta = $85 / gramo
    caja = $1,775 * gramo
    """)
    input (prioridad)
elif opcion == 2:
    print('Entraste a la calculadora')
    print ("Bienvenido a calculadora")

    print("""a) multiplicar
    b) dividir
    c) sumar
    d) resta """)
    oper = input("Eliga la opción que quiera ejecutar:")
    if oper == "a":
        y = input("Escribe el número que quieres multiplicar: ")
        x = input("Ingrese el número por el cual lo quiere multiplicar: ")

elif opcion == 3:
    print('Entraste a la opcion de lista')
