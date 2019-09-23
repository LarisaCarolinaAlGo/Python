Proceso sin_titulo
	Escribir "cuántos kilos de tortilla compraste en la semana?" // lo puse para que el usuario sepa que debe ingresar.
	dia = 1 
	semana = 1
	acumulador = 0

	mientras dia <=7
		Escribir "Día ", dia
		Leer kilos
		dia = dia + 1
		acumulador = acumulador + kilos 
	FinMientras
	kilosTotal = (acumulador * 11) / 7
	
	Escribir "El promedio de lo que gastaste fue de: $", kilosTotal
	
FinProceso
