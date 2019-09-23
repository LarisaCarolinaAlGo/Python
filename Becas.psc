Proceso sin_
	
	Escribir "Becas -El puerquito-"
	//input
	
	Escribir "¡Hola! quién eres?"
	Leer nombre
	Escribir "Cuál fue tu calificación en:"
	Escribir "Matemáticas"
	Leer calificacionMatematicas
	Escribir "Español"
	Leer calificacionEspañol
	Escribir "Biología"
	Leer calificacionBiologia
	Escribir "Religión"
	Leer calificacionReligion
	Escribir "Formación Cívica"
	Leer calificacionCivica
	
	//proceso 
	
	Promedio = (calificacionBiologia + calificacionCivica + calificacionEspañol + calificacionMatematicas + calificacionReligion) / 5
	Si Promedio >= 85
		Escribir "Aún tienes beca ", nombre
	SiNo
		Escribir "Expulsado ", nombre
	FinSi
	//output
FinProceso
