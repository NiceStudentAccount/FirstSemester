print('---------------PROBLEMA 1---------------')

#FUNCION: calcula la leche producida en la granja.
#ARGUMENTOS: ratio de produccion de leche por vaca, numero de vacas.
def lecheProducida(ratio):
    #se llama la funcion areaCorral y se opera
    lechePosible = (corralLargo * corralAnchor) / ratio
    return lechePosible



#se piden los datos
corralAnchor = float(input('Ingresa el ancho del corral en metros: '))
corralLargo = float(input('Ingresa el largo del corral en metros: '))


#se llama la función lecheProducida y se imprime la respuesta
print('''Asumiendo que la vaca puede producir leche infinita y que las vaca es inmortal,
 la leche que produjo la granja es de: ''', 
 lecheProducida(ratio = float(input('Metros cuadrados necesarios para producir un litro de leche: '))), 'L')