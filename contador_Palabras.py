#larisa Álvarez

contador_Letras = 0

palabras = ["orrnitorrinco", "alive", "electroencefalografista", "otorrinolaringologo", "pistache", "hola", "solllllllllllllllllllllllllly"]

for x in palabras:

    if len(x) >= 5:
        contador_Letras += 1

print(f"{contador_Letras} de estas palabras tienen 5 o más letras.")
