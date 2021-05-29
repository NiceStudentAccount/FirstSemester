print('---------------PROBLEMA 12---------------')

#FUNCION: evalua la derivada de la función de grado 2
#ARGUMENTOS: primer coeficiente, segundo coeficiente, donde se va a evaluar la x
def evaluarDerivada(coeficiente1, coeficiente2, valorX):
    return coeficiente1*2*valorX+coeficiente2

print(f'El valor de la derivada de la función en x es de: ', 
evaluarDerivada(float(input('Primer coeficiente:')), float(input('Segundo coeficiente: ')), 
float(input('Valor de x: '))))