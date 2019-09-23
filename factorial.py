#Larisa
numero = int(input("Ingrese el nùmero del que quiere sacar su factorial: "))
vueltas = 1
multiplicacion = 0
suma = 0
while vueltas < numero:
    numero-=1
    multiplicacion = numero * numero
    suma += multiplicacion
    vueltas += 1 

print(f"El factorial de su número es de {multiplicacion}")
