print('---------------PROBLEMA 13---------------')

#FUNCION: devuelve True si el numero hace parte de la secuencia de fibonacci
#ARGUMENTOS: mumero a evaluar
def esAureo(numero):
    n1 = 0
    n2 = 1
    n3 = 1
    for x in range(numero+1):
        n1 = n2
        n2 = n3
        n3 = n1+n2

        if numero == n3:
            return True

    return False

if esAureo(int(input('Numero entero: '))) == True:
    print('El numero es aureo')
else:
    print('El numero no es aureo')