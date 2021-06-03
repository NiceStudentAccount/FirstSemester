print('---------------PROBLEMA 31---------------')
def toDecimal(array):
    result = 0 
    counter = 0
    while len(array) > 0:
        result += 2**counter * array.pop()
        counter += 1
    return result


array = list(input('Ingrese el numero binario: '))
array = [int(x) for x in array]
print(toDecimal(array))