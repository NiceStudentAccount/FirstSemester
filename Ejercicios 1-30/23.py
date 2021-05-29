print('---------------PROBLEMA 23---------------')

def sumatory(array):
    result = 0
    for x in array:
        result += x
    return result

array = list()
for x in range(int(input('Number of elements: '))):
    array.append(int(input('Number: ')))
print ('The result is: ', sumatory(array))

