Proceso sin_titulo
	Escribir "Ingresa 4 de tus calificaciones:"
	Leer calificacion1
	Leer calificacion2
	Leer calificacion3
	Leer calificacion4
	Si  calificacion1 < calificacion2 && calificacion1 < calificacion3 && calificacion1 < calificacion4
		promedio1 = (calificacion2 + calificacion3 + calificacion4) / 3
		Escribir "Su promedio fue de un total de ", promedio1
		Escribir "Se ha eliminado la calificación ", calificacion1
	SiNo
		si calificacion2 < calificacion1 && calificacion2 < calificacion3 && calificacion2 < calificacion4
			promedio2 = (calificacion1 + calificacion3 + calificacion4) / 3 
			Escribir "Su promedio fue de un total de ", promedio2
			Escribir "Se ha eliminado la calificación ", calificacion2
		Sino
			Si calificacion3 < calificacion1 && calificacion3 < calificacion2 && calificacion3 < calificacion4
				promedio3 =(calificacion1 + calificacion2 + calificacion4) / 3
				Escribir "Su promedio fue de un total de ", promedio3
				Escribir "Se ha eliminado la calificación ", calificacion3 
			SiNo
				Si calificacion4 < calificacion1 && calificacion4 < calificacion2 && calificacion4 < calificacion3
					promedio4 = (calificacion1 + calificacion2 + calificacion3) / 3
					Escribir  "Su promedio fue de un total de ", promedio4
					Escribir "Se ha eliminado la calificación ", calificacion4
				SiNo
					Si calificacion1 == calificacion2 && calificacion1 == calificacion3 && calificacion1 == calificacion4
						Escribir "Su promedio fue de un total de ", calificacion1
						Escribir "son iguales"
						
					FinSi
					
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
