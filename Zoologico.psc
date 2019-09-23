Proceso sin_titulo
	Escribir "Bienvenido al zoologico"
	Escribir "Ingrese su edad:"
	Leer edad
	Si edad < 0 
		Escribir "error"
	SiNo
		Si edad <= 12 || edad >= 65
			Escribir "Tiene que pagar la tarifa -economica-"
		Sino
			Si edad >= 13 && edad <= 21
				Escribir "Tiene que pagar tarifa -estudiante-"
			SiNo
				Escribir "Tiene que pagar tarifa adulto"
			FinSi
		FinSi
	FinSi
	
FinProceso
