print('---------------PROBLEMA 25---------------')

def listsProduct(array1, array2):
    product = 0
    for x in range(len(array1)):
        product += array1[x]*array2[x]
    return product

def newList(n):
    numbers = list()
    for x in range(n):
        numbers.append(int(input('Number: ')))
    return numbers

lenght = int(input('Groups lenghts: '))
print('\nFIRST ARRAY')
array1 = newList(lenght)
print('\nSECCOND ARRAY')
array2 = newList(lenght)
print('The point product of the two arrays is:', listsProduct(array1, array2))
        
