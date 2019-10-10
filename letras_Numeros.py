#Larisa Alvarez
cambio = ""

palabra = input("Ingrese una palabra: ")

for x in palabra:
    if x == "i":
         cambio += "1"
    elif x == "o":
        cambio += "0"
    elif x == "a":
        cambio += "4"
    elif x == "e":
        cambio += "3"
    else:
        cambio += x

    # if x == "o":
    #     cambio += "0"


print(cambio)
# >>> a = ['a', 'b', 'c', 'd']
# >>> "".join(a)
# 'abcd'


 #string = ''
    #sub_cadenas = []
    #for j in cadena:
         #if j == 'X':
        #     string +=j
         #elif j == 'Y':
        #     string += j
         #else:
        #     sub_cadenas.append(string)
        #     break
