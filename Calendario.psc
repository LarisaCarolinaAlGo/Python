Proceso sin_titulo
	Escribir "Ingresa un n�mero del 1 al 12"
	Leer num
	
	si num < 1
		Escribir "error"
	SiNo
		Si num == 1
			Escribir "Enero tiene 31 d�as"
		SiNo
			si num  == 2
				Escribir "Febrero tiene 28 d�as, pero si es a�o bisiesto tiene 29 d�as"
			SiNo
				Si num == 3
					Escribir "Marzo tiene 31 d�as"
				SiNo
					Si num == 4
						Escribir "Abril tiene 30 d�as"
					SiNo
						Si num == 5
							Escribir "Mayo tiene 31 d�as"
						SiNo
							si num == 6
								Escribir "Junio tiene 30 d�as"
							SiNo
								Si num == 7
									Escribir "Julio tiene 31 d�as"
								SiNo
									Si num == 8
										Escribir "Agosto tiene 31 d�as"
									Sino 
										Si num == 9
											Escribir "Septiembre tiene 30 d�as"
										SiNo
											Si num == 10
												Escribir "Octubre tiene 31 d�as"
											SiNo
												Si num == 11
													Escribir "Novbiembre tiene 30 d�as"
												SiNo 
													Si num == 12
														Escribir "Diciembre tiene 31 d�as"
													SiNo
														Escribir "Error"
													FinSi
												FinSi
											FinSi
										FinSi
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
