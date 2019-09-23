#Carolina Álvarez

calificacion = 0.0
acumulador = 0.0
alumno = 1
while alumno <= 20:
    calificacion = float(input(f"Calificación alumno {alumno}: " ))
    acumulador += calificacion
    alumno += 1
print(acumulador / 20)
