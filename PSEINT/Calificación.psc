Proceso sin_titulo
	Escribir "Ingresa tu calificaci�n en matem�ticas:" //Es para que el usuario sepa que debe poner su calificaci�n.
	Leer calificacion //Para que el usuario ingrese su calificaci�n
	
	Si calificacion < 7 // Si el usuario ingresa menor que 7 significa que reprobo
		Escribir "Reprobado:("
	SiNo //Si el usuario no ingreso algun n�mero menor a 7.
		Si calificacion >= 7 && calificacion < 10 //Si el usuario ingreso un n�mero mayor o igual a 7 o un n�mero menor a 10 
			Escribir "Bien :)"
		SiNo // Si no ingreso un n�mero menor a 10
			Si calificacion = 10 // Si ingreso 10 
				Escribir "Felicidades :D"
				
			FinSi
		FinSi
		
	FinSi
FinProceso
