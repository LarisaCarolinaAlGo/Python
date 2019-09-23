#Larisa Álvarez
print  ("Bienvenido a -Becas la abeja-")
#Inputs
materia1 = float(input("Ingrese su primera calificación: "))
materia2 = float(input("Ingrese su segunda calificación: "))
materia3 = float(input("Ingrese su tercera calificación: "))
materia4 = float(input("Ingrese su cuarta calificación: "))
materia5 = float(input("Ingrese su quinta calificación: "))
materia6 = float(input("Ingrese su sexta calificación: "))

promedio = (materia1 + materia2 + materia3 + materia4 + materia5 + materia6) / 6
#Proceso
if promedio >= 85.00:
    print ("Sigues con tu beca, felicidades.")
else:
    print ("Has perdido tu beca. Eres una desonrra para este instituto, estudia más.")
#Output
