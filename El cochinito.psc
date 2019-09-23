Proceso sin_titulo
	Escribir "Casa de cambio -el cochinito-"
	
	Escribir "Elige el tipo de cambio:"
	Escribir "1- Dólares a pesos"
	Escribir "2- Pesos a dólares"
	leer op
	
	Escribir "Cuánto quieres cambiar?"
	Leer dinero
	
	
	si op = 1
		Escribir "Cuánto vale un dólar?"
		Leer cambio
	FinSi
	si op = 2
		Escribir "Cuánto vale un peso?"
		Leer cambio
	FinSi
	
	total = cambio * dinero
	Escribir total
	
	
	
FinProceso
