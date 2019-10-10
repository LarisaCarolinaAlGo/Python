#Larisa Alvarez
contador_palabras = 0

palabras = ["avestruz","jirafa","koala","pinguino","abeja","limon","kiosko", "karaoke"]

letra = input("Ingrese la letra: ")





for palabra in palabras:

    if palabra[0] == letra:
        contador_palabras += 1

print(f"{contador_palabras} palabras de la lista inician con su letra")
