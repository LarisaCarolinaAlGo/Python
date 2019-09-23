#Larisa Álvarez

dias = int(input("Ingrese el número de días: "))
vueltas = 1
acumulador = 0

while vueltas <= dias:
    ingresos = int(input(f"Escribe la cantidad del día {vueltas}: "))
    acumulador += ingresos
    vueltas += 1

print(f"los ingresos acumulados durante {dias} días fueron de ${acumulador}")
