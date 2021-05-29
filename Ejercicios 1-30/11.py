print('---------------PROBLEMA 11---------------')

#FUNCION: devuelve el coeficiente lineal de la derivada del polinomio
#ARGUMENTOS: numero que multiplica el x^2, numero que multiplica la x, termino independiente
def coeficienteLinealDerivada(primerCoeficiente):
    return primerCoeficiente*2

print('Ingrese los coeficientes en la forma: ax^2+bx+cx')
print('El coeficiente lineal de la derivada es: ', coeficienteLinealDerivada(float(input('Primer coeficiente: '))))