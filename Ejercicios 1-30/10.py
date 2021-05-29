print('---------------PROBLEMA 10---------------')

#FUNCION: evalua un polinomio de grado 2 en x
#ARGUMENTOS: numero que multiplica el x^2, numero que multiplica la x, termino independiente
#valor por el cual se quiere reemplazar la x
def evaluar(primerCoeficiente, segundoCoeficiente, tercerCoeficiente, valorX):
    return primerCoeficiente*(valorX**2) + segundoCoeficiente*valorX + tercerCoeficiente

#imprime la respuesta de la funcion, llama a la funcion evaluar y hace la recepción de datos
print('Ingrese los coeficientes en la forma: ax^2+bx+cx')
print(f'El polinomio es igual a ', evaluar(float(input('Primer coeficiente: ')), float(input('Segundo coeficiente: ')), float(input('Tercer coeficiente: ')), float(input('Valor de X: '))))