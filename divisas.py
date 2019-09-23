#Larisa Álvarez

#Inpu
print ("Qué quiere covertir?:")
print ("a) dolares a pesos.")
print ("b) pesos a dolares.")
divisas = input ()

#Proceso
if divisas == "a":
     dolares = float(input("Ingrese la cantidad de dolares "))
     conversion = dolares * 19.29
     print (f"Su dinero vale ${conversion} dolares.")
elif divisas == "b":
    pesos = float(input("Ingrese la cantidad de pesos "))
    conversion = pesos / 19.29
    print (f"Su dinero vale ${conversion} pesos mexicanos.")
else:
    print ("Error")
#Output
