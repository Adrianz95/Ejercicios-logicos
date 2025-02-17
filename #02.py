# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

# Función que hace un split de la palabra y lo almacena en una lista
def listaLetrasPalabra(palabra):
    listaLetras = []

    for i in palabra:
        listaLetras.append(i)

    return listaLetras

def esAnagrama():
    palabra_1 = input("Palabra 1: ").lower()
    palabra_2 = input("Palabra 2: ").lower()

    letrasPalabra1 = listaLetrasPalabra(palabra_1)
    letrasPalabra2 = listaLetrasPalabra(palabra_2)

    letrasPalabra1.sort()
    letrasPalabra2.sort()

    if letrasPalabra1 == letrasPalabra2:
        print("Es anagrama")
    else:
        print("No son anagramas")


esAnagrama()