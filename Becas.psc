Proceso sin_
	
	Escribir "Becas -El puerquito-"
	//input
	
	Escribir "�Hola! qui�n eres?"
	Leer nombre
	Escribir "Cu�l fue tu calificaci�n en:"
	Escribir "Matem�ticas"
	Leer calificacionMatematicas
	Escribir "Espa�ol"
	Leer calificacionEspa�ol
	Escribir "Biolog�a"
	Leer calificacionBiologia
	Escribir "Religi�n"
	Leer calificacionReligion
	Escribir "Formaci�n C�vica"
	Leer calificacionCivica
	
	//proceso 
	
	Promedio = (calificacionBiologia + calificacionCivica + calificacionEspa�ol + calificacionMatematicas + calificacionReligion) / 5
	Si Promedio >= 85
		Escribir "A�n tienes beca ", nombre
	SiNo
		Escribir "Expulsado ", nombre
	FinSi
	//output
FinProceso
