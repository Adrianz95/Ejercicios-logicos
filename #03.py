# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
#   la que el siguiente siempre es la suma de los dos anteriores.
#   0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(listaSumaFibo):

    for i in range(2, 50):
        resultado = listaSumaFibo[(i + 1) - 2] + listaSumaFibo[(i + 1) - 1]
        listaSumaFibo.append(resultado)
    
    return listaSumaFibo


sumaFibo = [1, 1, 2]

print(fibonacci(sumaFibo))