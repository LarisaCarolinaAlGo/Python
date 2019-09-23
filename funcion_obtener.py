def obtener_letra(utilizadas):

    condicion = 1
    while condicion != 0:

        abc = "abcdefghijklmnñopqrstuvwxyz"
        letra = input("Dame la letra que quieras usar: ")
        letra = letra.lower()

        if letra in utilizadas:
            print("Esa letra ya la uso, ingrese otra letra ")
        elif letra not in abc:
            print("tiene que ser una letra:")
        elif len(letra) != 1:
            print("Solo una letra")
        else:
            condicion = 0
    return letra
