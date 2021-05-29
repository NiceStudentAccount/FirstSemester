print('---------------PROBLEMA 30---------------')

def reorganize(array):
    counter = 0
    while counter < len(array):
        if array[counter] == 0:
            array.remove(0)
            array.append(0)
        counter += 1
    return array

numbers = list()
for x in range(int(input('Amount of items: '))):
    numbers.append(int(input('Number: ')))

print('The organized array is: ', reorganize(numbers))