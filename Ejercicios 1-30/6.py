print('---------------PROBLEMA 6---------------')

#FUNCION: calcula la potencia de un numero entero elevado a un numero entero
#ARGUMENTOS: base, exponente
def divisible(dividendo, divisor):
    return True if dividendo % divisor == 0 else False

if divisible(int(input('Primer numero: ')), int(input('Segundo Numero: '))) == True:
    print('El primer numero es divisible por el segundo')
else:
    print('El primer numero es indivisible por el segundo')