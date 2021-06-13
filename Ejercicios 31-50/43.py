print('---------------PROBLEMA 43---------------')

#reading functions--------------------------------------------------------------------

def getPolinom():
    raw = str(input('Ingrese un polinomio: '))
    #se separa el string en polinomios
    polinomn = []
    monomial = ''
    for index, x in enumerate(raw):
        monomial += x
        if index > 0:
            if x == '+' or x == '-':
                monomial = monomial[0:-1]
                polinomn.append(monomial)
                if x == '-':
                    monomial = '-'
                else:
                    monomial = ''

        if index == len(raw)-1:
            polinomn.append(monomial)
    
    #se obtiene el coeficiente de los monomios
    for index, x in enumerate(polinomn):
        if index != len(polinomn)-1:
            newMonomial = x[:x.find('x')]
            polinomn[index] = newMonomial
    
    #se convierten los strings en numeros enteros
    polinomn = [int(x) for x in polinomn]

    #each index in the array is converted into an array of two spaces that will contain the coeficient of the monomial, and the degree of the monomial (beause it makes easyer to calculate it later)
    for index, x in enumerate(polinomn):
        polinomn[index] = [x, len(polinomn)-1-index]

    return polinomn

def returnPolinom(polinom):
    x = 0
    x = 

#point functions----------------------------------------------------------------------

def evaluate(number, polinomn):
    exponent = len(polinomn)-1
    answer = 0
    for x in polinomn:
        if exponent != 0:
            answer += x[0]*number**exponent
            exponent -= 1
        else:
            answer += x[0]
    
    return answer

def suma(pol1, pol2):
    polSum = []
    largest = []
    shortest = []

    #the length of the polinoms is matched and also the monomials that have a grater degree are added to the array of the final polinom
    if len(pol2) > len(pol1):
        largest = pol2
        shortest = pol1
    else:
        largest = pol1
        shortest = pol2

    #the equal indexes are added
    x = len(largest)-len(shortest)
    difference = len(largest)-len(shortest)
    while x < len(largest):
        largest[x][0] += shortest[x-difference][0]
        x += 1

    return largest





#Main---------------------------------------------------------------------------------
print('Recuerde que los exponentes tienen que ser descendientes. Los exponentes se representan como numeros normales a la derecha de la x\nEjemplo: 4x3+7x2-9x+3')
point = None

while point != 7:
    point = int(input('\n\nElija una de las siguientes opciones:\n1. Evaluar\n2. Sumar\n3. Restar\n4. Multiplicar\n5. Dividir\n6. Residuo\n7. Salir de la aplicación\n\n'))

    #point 43
    if point == 1:
        num = int(input('Numero a evaluar: '))
        print('Primer polinomio evaluado:', evaluate(num, getPolinom()), '\nSegundo polinomio evaluado:', evaluate(num, getPolinom()))
    
    #point 44
    elif point == 2:
        print(suma(getPolinom(), getPolinom()))

    #point 45
    elif point == 3:
        print()
        
    #point 46
    elif point == 4:
        print()

    #point 47
    elif point == 5:
        print()

    #point 48
    elif point == 6:
        print()

    #point 49
    elif point == 7:
        break
    else: 
        print('Opción invalida')
    
print('\nGracias por usar el programa {0:c}'.format(9996))
