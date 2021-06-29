print('---------------PROBLEMA 43-49---------------')

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
    #we check if all the coeficients are equal to 0
    flag = True
    for x in polinom:
        if x[0] != 0: 
            flag = False
    if flag:
        return 0
        

    for x in polinom:
        if x[0] == 0:
            polinom.remove(x)

    counter = 0
    poliString = ''
    while counter < len(polinom):

        if counter != 0 and polinom[counter][0] > 0:
            poliString += '+'

        if polinom[counter][1] == 0:
            poliString += str(polinom[counter][0])
            break

        if polinom[counter][1] == 1:
            poliString += f'{polinom[counter][0]}x'
            counter += 1
            continue

        poliString += f'{polinom[counter][0]}x{polinom[counter][1]}'
        counter += 1
    
    return poliString


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

def substract(pol1, pol2):
    polFinal = []

    #monoms with coeficient 0 are added at the begining so the polinoms are equal in lenght
    difference = len(pol1)-len(pol2)
    if difference < 0:
        lenght = len(pol1)
        x = 0
        while x > difference: 
            pol1.insert(0, [0, lenght-x])
            x -= 1
    elif difference > 0:
        lenght = len(pol2)
        x = 0
        while x < difference: 
            pol2.insert(0, [0, len(pol2)+x])
            x += 1

    #the substraction between the coeficients is applied
    x = 0
    while x < len(pol1):
        polFinal.append([pol1[x][0]-pol2[x][0], pol1[x][1]])
        if polFinal[-1][0] == 0:
            polFinal.pop()
        x += 1
    

    return polFinal

def multiply(pol1, pol2):
    polMult = []
    polFinal = []

    #the polinoms are multiplyed
    for x in pol1:
        for y in pol2:
            polMult.append([x[0]*y[0], x[1]+y[1]])

    #the final polinom is simplifyed and the semejant terms are added
    x = len(pol1)+len(pol2)-2
    while x >= 0:
        current = list()
        for y in polMult:
            if x == y[1]:
                current.append(y[0])

        coeficient = 0
        for y in current:
            coeficient += y

        polFinal.append([coeficient, x])
        x -= 1

    return polFinal

def division(pol1, pol2):
    #variables
    cotient = list()
    rest = list()
    polRep = list()

    while True:
        #1. the length of polRep is determined
        monomial = len(polRep)
        while monomial < len(pol2):
            try:
                polRep.append(pol1.pop(0))
                monomial += 1
            except:
                break

        #if the recidue is 0, then the program finishes
        if len(polRep) == 0:
            break

        #if the exponent of the dividend is higher than the residue, then the program finishes
        if pol2[0][1] > polRep[0][1]:
            break

        #2. find the factor
        cotient.append([polRep[0][0]/pol2[0][0], polRep[0][1]-pol2[0][1]])

        #3. multiply
        rest = list()
        for x in pol2:
            rest.append([cotient[-1][0]*x[0], cotient[-1][1]+x[1]])

        #4. substract
        polRep = substract(polRep, rest)



    x = 0
    while x < len(cotient):
        if cotient[x][0] % 1 == 0:
            cotient[x][0] = int(cotient[x][0])
        x += 1
    
    return cotient

def residue(pol1, pol2):
   #variables
    cotient = list()
    rest = list()
    polRep = list()

    while True:
        #1. the length of polRep is determined 20814410
        monomial = len(polRep)
        while monomial < len(pol2):
            try:
                polRep.append(pol1.pop(0))
                monomial += 1
            except:
                break

        #if the recidue is 0, then the program finishes
        if len(polRep) == 0:
            break

        #if the exponent of the dividend is higher than the residue, then the program finishes
        if pol2[0][1] > polRep[0][1]:
            break

        #2. find the factor
        cotient.append([polRep[0][0]/pol2[0][0], polRep[0][1]-pol2[0][1]])

        #3. multiply
        rest = list()
        for x in pol2:
            rest.append([cotient[-1][0]*x[0], cotient[-1][1]+x[1]])

        #4. substract
        polRep = substract(polRep, rest)

    x = 0
    while x < len(polRep):
        if polRep[x][0] % 1 == 0:
            polRep[x][0] = int(polRep[x][0])
        x += 1
    
    return polRep


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
        print('Suma de los polinomios:', returnPolinom(suma(getPolinom(), getPolinom())))

    #point 45
    elif point == 3:
        print('Resta de los polinomios:', returnPolinom(substract(getPolinom(), getPolinom())))
        
    #point 46
    elif point == 4:
        print('Producto de los polinomios:', returnPolinom(multiply(getPolinom(), getPolinom())))

    #point 47
    elif point == 5:
        print('Cociente de los polinomios:', returnPolinom(division(getPolinom(), getPolinom())))

    #point 48
    elif point == 6:
        print('Residuo de los polinomios:', returnPolinom(residue(getPolinom(), getPolinom())))

    #point 49
    elif point == 7:
        break
    else: 
        print('Opción invalida')
    
print('\nGracias por usar el programa {0:c}'.format(9996))