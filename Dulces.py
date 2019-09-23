#Larisa Álvarez

#Inputs
dulces = int(input("Buenos días Miss. Ingrese la cantidad de dulces que repartira: "))

#Proceso
dulcesGuardados = dulces % 11
dulcesAlumnos = dulces // 11

#Output
print(f"Dulces para los alumnos {dulcesAlumnos}, dulces para la maestra: {dulcesGuardados}")
