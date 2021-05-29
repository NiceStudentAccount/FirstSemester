print('---------------PROBLEMA 26---------------')

def smallest(array):
    smallest_number = array[0]
    for x in array:
        if x < smallest_number:
            smallest_number = x
    return smallest_number

numbers = list()
for x in range(int(input('Lenght of the array: '))):
    numbers.append(int(input('Number: ')))

print('The smallest number of the array is: ', smallest(numbers))