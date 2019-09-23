#Larisa Álvarez
#Inputs
consumo = float(input("Ingrese el consumo:")) #Ingresa el consumo, lo lee, lo convierte en float y lo guarda en la variable "consumo"
propina = float(input("Escriba el porcentaje a dar de propina:")) # Ingresa el porcentaje de propina, lo lee, lo convierte a float y lo guarda en la variable "propina"
#Proceso
propina2 = (consumo*propina)/100 #Estamos sacando el porcentaje, la cantidad de propina que le van a dar.
total = (propina2+consumo) #Se suma la cantidad de propina y la cantidad de lo que se consumio
#Output
print ("Su total a pagar es de: " + str(total)) #Lo converti a string para que se pueda sumar.
