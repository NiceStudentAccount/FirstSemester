print('---------------PROBLEMA 35---------------')
#----------------FUNCIONES DE LECTURA-----------------

#función que revisa si se ejecutó el programa por segunda vez y recibe los conjuntos o conserva los
#los conjuntos anteriores
def recheckArray(isFirst, conj1, conj2):
    if isFirst == False:
        if int(input('\n1. Usar los mismos conjuntos\n2. Usar conjuntos diferentes\n')) == 1:
            return conj1, conj2

    return getArray(1), getArray(2)

#Función que recoje un arreglo de numeros enteros y para cuando el usuario ingresa "p"
def getArray(n):
    print('\nCONJUNTO', n)
    array = set()
    dato = ''
    contador = 1
    while dato != 'p':
        dato = input(f'Numero {contador}: ')
        if dato == 'p':
            break
        array.add(int(dato))
        contador += 1
    return array


#----------------FUNCIONES DE PUNTOS-----------------
def union(con1, con2):
    newSet = set()
    for x, y in zip(con2, con1):
        newSet.add(x)
        newSet.add(y)
    if len(con1) == 0:
        return 'vacio'
    '''an other way of doing it is by methods:
    con1.union(con2)'''
    return newSet

def intersection(con1, con2):
    newSet = set()
    for x in con2:
        for y in con1:
            if x == y:
                newSet.add(x)
    if len(newSet) == 0:
        return 'vacio'
    '''an other way of doing it is by methods:
    con1.intersection(con2)'''
    return newSet

def diferencia(con1, con2):
    newSet = set()
    for x in con1:
        for y in con2:
            itsin = False
            if x == y:
                itsin == True
            if itsin == False:
                newSet.add(x)
    '''newSet.update(con1)
    for y in con2:
        for x in con1:
            if y == x:
                newSet.remove(x)'''
    if len(newSet) == 0:
        return 'vacio'
    return newSet

def diferenciaSimetrica(con1, con2):
    newSet = diferencia(union(con1, con2), intersection(con1, con2))
    if len(newSet) == 0:
        return 'vacio'
    return newSet

def pertenece(con1, con2, number):
    var1 = 'no pertenece'
    var2 = 'no pertenece'
    for x in con1:
        if number == x:
            var1 = 'pertenece'
    for x in con2:
        if number == x:
            var2 = 'pertenece'
    return var1, var2

def contenido(con1, con2):
    itsIn = 'está contenido'
    counter = 0
    for x in con1:
        for y in con2:
            if x == y:
                counter += 1

    if counter != len(con1):
        itsIn = 'no está contenido'
    return itsIn

#------------------------MAIN-------------------------
option = int()
conj1 = set()
conj2 = set()
isFirst = True

print('(A la hora de ingresar los conjuntos recuerde oprimir "p" para parar)\n')
#while que se encarga de ejecutar todas las funciones infinitamente
while option != 7:
    
    print('SELECCIONE UNA DE LAS SIGUIENTES OPCIONES:\n'+
    '1. Union\n2. Intersección\n3. Diferencia\n4. Diferencia simétrica\n5. Pertenece\n6. Contenido\n7. Salir del programa') 

    option = int(input())
          
    #(Punto 35: Unión)
    if option == 1:
        conj1, conj2 = recheckArray(isFirst, conj1, conj2)
        print('\nLa union de los conjuntos es: \n', union(conj1,conj2), '\n\n')
    #(Punto 36: Intersección)
    elif option == 2:
        conj1, conj2 = recheckArray(isFirst, conj1, conj2)
        print('\nLa intersection de los conjuntos es: \n', intersection(conj1,conj2), '\n\n')
    #(Punto 37: Diferencia)
    elif option == 3:
        conj1, conj2 = recheckArray(isFirst, conj1, conj2)
        print('\nLa diferencia de los conjuntos es: \n', diferencia(conj1,conj2), '\n\n')
    #(Punto 38: Diferencia simétrica)
    elif option == 4:
        conj1, conj2 = recheckArray(isFirst, conj1, conj2)
        print('\nLa diferencia simetrica de los conjuntos es: \n', diferenciaSimetrica(conj1,conj2), '\n\n')
    #(Punto 39: Pertenece)
    elif option == 5:
        conj1, conj2 = recheckArray(isFirst, conj1, conj2)
        number = int(input('\nNumero a verificar: '))
        respuesta1, respuesta2 = pertenece(conj1, conj2, number)
        print(f'El numero {respuesta1} en el primer conjunto\nEl numero {respuesta2} en el segundo conjunto\n\n')
    #(Punto 40: Contenido)
    elif option == 6:
        conj1, conj2 = recheckArray(isFirst, conj1, conj2)
        print(f'\nEl primer conjunto {contenido(conj1,conj2)} en el segundo\n\n')
    #(Punto 41: Salir)
    elif option == 7:
        break

    #En caso de que no se elija una opción valida    
    else: 
        print('\n{0:c}OPCIÓN INVALIDA{0:c}\n'.format(10060))

    isFirst = False


print('MUCHAS GRACIAS {0:c}, VUELVA PRONTO {1:c}'.format(9996, 128293))