Proceso sin_titulo
	contador = 0
	acumulador = 0
	Escribir "Cuántos alumnos tiene?"
	Leer alumnos
	mientras contador < alumnos
		Escribir "calificacion:"
		leer calificacion
		contador = contador + 1
		acumulador =  acumulador + calificacion
	FinMientras
	
	promedio = acumulador / alumnos
	Escribir promedio
	
FinProceso
