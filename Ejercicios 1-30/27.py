print('---------------PROBLEMA 27---------------')

def biggest(array):
    biggest_number = array[0]
    for x in array:
        if x > biggest_number:
            biggest_number = x
    return biggest_number

numbers = list()
for x in range(int(input('Lenght of the array: '))):
    numbers.append(int(input('Number: ')))

print('The biggest number of the array is: ', biggest(numbers))