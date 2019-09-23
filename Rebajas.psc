Proceso Leverpool_titulo
	Escribir "Liverpool, temporada de rebajas"
	Escribir "Cuál fue tu gasto?"
	Leer gasto
	si gasto > 100
		descuento = gasto * 0.24
		total = gasto - descuento
	SiNo 
		total = gasto
	FinSi
	Escribir "Con su compra su total es de: ", total, "pesos"
	
FinProceso
