print('---------------PROBLEMA 14---------------')
'''En realidad no hace falta saber el punto de corte de las rectas, con la pendiente
se puede resolver todo el ejercicio'''

#FUNCION: devuelve True si el numero hace parte de la secuencia de fibonacci
#ARGUMENTOS: mumero a evaluar
def interseccion(pendiente1, pendiente2):
    if pendiente1 * pendiente2 == -1:
        return 'son perpendiculares'
    elif pendiente1 == pendiente2:
        return 'son paralelas'
    else:
        return 'no son paralelas o perpendiculares'

print('Las pendientes', interseccion(float(input('Pendiente 1: ')), float(input('Pendiente 2: '))))