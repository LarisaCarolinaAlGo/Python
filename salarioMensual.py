#Larisa Álvarez

#Inputs
salario = float(input("Ingrese el salario mensual: "))
v1 = float(input("Ingrese la venta 1: "))
v2 = float(input("Ingrese la venta 2: "))
v3 = float(input("Ingrese la venta 3: "))

#Proceso
comision = (v1 + v2 + v3) * 0.1
salario += comision

#Output
print(f"El salario final de su empleado es de: {salario}")
