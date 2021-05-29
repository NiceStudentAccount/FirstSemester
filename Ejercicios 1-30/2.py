print('---------------PROBLEMA 2---------------')

#FUNCION: calcula el numero de huevos mensuales
#AARGUMENTOS: nAves en la granja
def produccionMensual(aves):
    huevosMensuales = aves*(1/6)*10
    huevosMensuales += aves*(1/6)*6
    return int(huevosMensuales)

#FUNCION: se imprime la respuesta, se llama la funcion produccionMensual y se pide el numero de aves
print('La prodccion mensual de huevos es de:', produccionMensual(float(input('Ingrese la cantidad de aves en la granja: '))))