print('---------------PROBLEMA 9---------------')

#FUNCION: determina si un número es múltiplo de la suma do otros dos números.
#ARGUMENTOS: numero producto, sumando 1, sumando2
def esMultiplo(multiplo, sumando1, sumando2):
    #se suman los sumandos y si no son divisibles por el primer numero, este no es multiplo
    if (sumando1 + sumando2) % multiplo == 0:
        return True
    else:
        return False


#Se analiza el resultado de la funcion esMultiplo y dependiendo de esta,
#se imprime la respuesta
if esMultiplo(int(input('Ingrese el \"multiplo\": ')), float(input('Ingrese el primer sumando: ')), float(input('Ingrese el segundo sumando:'))) == True:
    print('El primer numero es multiplo de la suma de los otros dos')
else:
    print('El primer numero no es multiplo de la suma de los otros dos')
    