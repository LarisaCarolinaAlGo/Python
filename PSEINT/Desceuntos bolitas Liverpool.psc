Proceso sin_titulo
	Escribir "Ingrese su gasto"
	Leer cantidad
	
	Escribir "Ingrese el número del color de la bolita que saco"
	Escribir "1. Blanco"
	Escribir "2. Verde"
	Escribir "3. Amarilla"
	Escribir "4. Azul"
	Escribir "5. Roja"
	Leer bolita
	
	
	
	si bolita < 1
		Escribir "Error"
	SiNo
		Si bolita == 1
			blanco = 0
			Escribir blanco, "%"
		SiNo
			Si bolita == 2
				verde = cantidad - (cantidad * 0.20)
				
			FinSi
		FinSi
	FinSi
FinProceso
