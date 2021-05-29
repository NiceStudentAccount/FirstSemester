print('---------------PROBLEMA 7---------------')

#FUNCION: divide el numero por todos los numeros menores que el y si el resultado
#es 0, se devuelve primo, de lo contrario se devuelve compuesto
#ARGUMENTOS: numero
def esPrimo(numero):
    if numero == 2:
        return True
    for x in range(2, numero):
        return False if numero % x == 0 else True
    
if esPrimo(int(input('Ingrese el numero: '))) == True:
    print('El numero ingresado es primo')
else: 
    print('El numero ingresadono es compuesto')