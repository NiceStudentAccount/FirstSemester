print('---------------PROBLEMA 20---------------')

def interesSimple(prestamo, interes):
    return prestamo * (1 + (interes/100 * 7)) + prestamo

def interesCompuesto(prestamo, interes):
    return prestamo * (1 + interes/100)**7

prestamo = float(input('Valor del prestamo: '))
interes = float(input('Porcentaje de interes: '))
print('El interes simple es de: ', interesSimple(prestamo, interes))
print('El interes compuesto es de: ', interesCompuesto(prestamo, interes))