#Larisa
contador_er = 0
contador_ir = 0
contador_ar = 0

terminaciones = ["barrer", "jugar", "columpio", "bailar", "ir", "suplir", "cantar" ]


# for palabra in terminaciones:
for palabra in terminaciones:
    if palabra[0:6][-2:] == "er":
        contador_er += 1
    elif palabra[0:6][-2:] == "ar":
        contador_ar += 1
    elif palabra[0:6][-2:] == "ir":
        contador_ir += 1


print(f"""{contador_ar} palabras terminan en ar
{contador_ir} palabras terminan en ir
{contador_er} palabras terminan en er""")
