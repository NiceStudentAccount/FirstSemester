print('---------------PROBLEMA 24---------------')

def sumatory(array):
    result = 0
    for x in array:
        result += x
    return result/len(array)

array = list()
for x in range(int(input('Number of elements: '))):
    array.append(int(input('Number: ')))
print ('The result is: ', sumatory(array))