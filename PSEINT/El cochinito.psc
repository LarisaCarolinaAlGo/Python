Proceso sin_titulo
	Escribir "Casa de cambio -el cochinito-"
	
	Escribir "Elige el tipo de cambio:"
	Escribir "1- D�lares a pesos"
	Escribir "2- Pesos a d�lares"
	leer op
	
	Escribir "Cu�nto quieres cambiar?"
	Leer dinero
	
	
	si op = 1
		Escribir "Cu�nto vale un d�lar?"
		Leer cambio
	FinSi
	si op = 2
		Escribir "Cu�nto vale un peso?"
		Leer cambio
	FinSi
	
	total = cambio * dinero
	Escribir total
	
	
	
FinProceso
