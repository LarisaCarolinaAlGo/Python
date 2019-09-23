#Larisa Álvarez

calificacion = 0.0
acumulador = 0.0
ronda = 1
alumno = int(input("Cuál es el número de  alumnos en su grupo? "))
while ronda <= alumno:
    calificacion = float(input(f"Calificación alumno {ronda}: " ))
    acumulador += calificacion
    ronda += 1
print(acumulador / alumno)
