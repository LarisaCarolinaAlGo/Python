Proceso sin_titulo
	Escribir "Ingresa tu calificación en matemáticas:" //Es para que el usuario sepa que debe poner su calificación.
	Leer calificacion //Para que el usuario ingrese su calificación
	
	Si calificacion < 7 // Si el usuario ingresa menor que 7 significa que reprobo
		Escribir "Reprobado:("
	SiNo //Si el usuario no ingreso algun número menor a 7.
		Si calificacion >= 7 && calificacion < 10 //Si el usuario ingreso un número mayor o igual a 7 o un número menor a 10 
			Escribir "Bien :)"
		SiNo // Si no ingreso un número menor a 10
			Si calificacion = 10 // Si ingreso 10 
				Escribir "Felicidades :D"
				
			FinSi
		FinSi
		
	FinSi
FinProceso
