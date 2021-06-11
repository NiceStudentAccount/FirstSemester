print('---------------PROBLEMA 43---------------')

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

    return polinomn


def evaluate(number, polinomn):
    exponent = len(polinomn)-1
    answer = 0
    for x in polinomn:
        if exponent != 0:
            answer += x*number**exponent   
            exponent -= 1
        else:
            answer += x
    
    return answer
    
print('Recuerde que los exponentes tienen que ser descendientes. Los exponentes se representan como numeros normales a la derecha de la x\nEjemplo: 4x3+7x2-9x+3\n\n')
num = int(input('Numero a evaluar: '))
print('Primer polinomio:', evaluate(num, getPolinom()), '\nSegundo polinomio:', evaluate(num, getPolinom()))