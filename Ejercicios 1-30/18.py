import math
print('---------------PROBLEMA 18---------------')

#FUNCION: devuelve el area del triangulo equilatero que circunscirbe un circulo con radio r
#ARGUMENTOS: radio del circulo
def cantidadTelaraña(radio):
    #se asume que la araña se gasta al menos 6 en los extramos externos de la telaraña que se adhieren a las paredes
    telarañaTotal = 6.0
    radio = int(radio)
    for x in range(radio, 0, -1):
        hexagonoActual = 12*math.sin(math.radians(30))*x
        #se le suman las telaraña que une los hexagonos
        hexagonoActual += 6
        telarañaTotal += hexagonoActual
    
    return telarañaTotal
    
print('La telaraña necesaria es: ', cantidadTelaraña(int(input('Radio de la telaraña: ')))) 