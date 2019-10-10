Proceso sin_titulo
	Escribir "Escriba el total de su compra hasta ahora:"
	Leer compra
	si compra <= 0 
		Escribir "Error"
	Sino
		Si compra <= 100
			Escribir "Su pago debe ser en efectivo"
		SiNo
			si compra < 300
				
				Escribir "Su pago debe ser con tarjeta de débito"
			SiNo
				Escribir "Su pago debe ser con tarjeta de credito"
				
			FinSi
		FinSi
	FinSi
FinProceso
