#Larisa Álvarez

#Inputs
dineroGastado = float(input("Ingrese la cantidad de dinero gastado: "))
#Proceso

operacion = dineroGastado * .24
gastoTotal = dineroGastado - operacion
if dineroGastado > 100:
    print(f"Su descuento es de ${operacion}, su gasto sera de un total de {gastoTotal}")
else:
    print(f"Su descuento es de un total de $0, su gasto sera de un total de {dineroGastado} ")
#Output
