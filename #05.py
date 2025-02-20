# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def areaTriangulo(base, altura):
    area = (base * altura) / 2
    return f'El área de un triángulo es: {area}'

def areaCuadrado(lado):
    area = lado * lado
    return f'El área de un cuadrado es: {area}'

def areaRectangulo(base, altura):
    area = base * altura
    return f'El área de un rectangulo es: {area}'

def areaPoligono(area):
    return area

print(areaPoligono(areaTriangulo(10, 2)))
print(areaPoligono(areaCuadrado(4)))
print(areaPoligono(areaRectangulo(10, 2)))