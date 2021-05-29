import math
print('---------------PROBLEMA 16---------------')

#FUNCION: devuelve el area del triangulo equilatero que circunscirbe un circulo con radio r
#ARGUMENTOS: radio del circulo
def areaTriangulo(radio):
    #se remplaza el radio en la formula para calcular el area del triangulo y se devuelve
    lado = math.tan(math.radians(60))*radio*2
    return  (lado * 3 * lado)/2
    
print('El area del triangulo equilatero es: ', areaTriangulo(float(input('Radio del circulo circumscrito: '))))