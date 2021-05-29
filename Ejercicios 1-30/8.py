print('---------------PROBLEMA 8---------------')

#FUNCION: si los numeros son primos relativos, se devuelve True, de lo contrario, 
#se devuelve False
#ARGUMENTOS: numero 1, numero 2
def sonPrimosRelativos(n1, n2):
    #si los numeros son iguales y alguno es iferente de 1 entonces no son relativos
    if n1 == n2 and (n1 != 1 or n2 != 1):
        return False

    #son relativos si un numero es 0 y el otro es 1. Si los dos son 0 entonces no son relativos
    if (n1 == 0 and n2 == 1) or (n1==1 and n2 == 0):
        return True
    elif n1 == 0 or n2 == 0:
        return False
        
    x = 2
    while x < min(n1, n2):
        #si los dos numeros son divisibles por el mismo numero, no son primos relativos
        if n1 % x == 0 and n2 % x == 0:
            return False
        else:
            x += 1
    #si dentro del while no se probó que no fueran primos relativos entonces 
    #son primos relativos
    return True



#Se analiza el resultado de la funcion primosRelativos y dependiendo de esta,
#se imprime la respuesta
if sonPrimosRelativos(int(input('Primer numero: ')), int(input('Segundo numero: '))) == False:
    print('Los numeros no son primos relativos')
else: 
    print('Los numeros si son primos relativos')