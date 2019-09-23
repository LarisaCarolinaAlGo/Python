def revisar(palabra, letra, escondida):
    if letra in palabra:
        for z in range(0, len(escondida)):
            if palabra[z] == letra:
                escondida[z] = letra
        return True
    else:
        return False
