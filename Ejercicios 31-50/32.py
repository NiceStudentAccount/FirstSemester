print('---------------PROBLEMA 32---------------')
def toBinary(number):
    #binary = ''
    binary = list()
    while number > 0:
        #binary = f'{binary}{number%2}'
        #binary += str(number%2)
        binary.append(number%2)
        number //= 2
    return ''.join(map(str, binary))

print(toBinary(int(input('Numero entero: '))))
