# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

numerosPrimos = []

for i in range(2, 101):
    if es_primo(i):
        numerosPrimos.append(i)

print(numerosPrimos)