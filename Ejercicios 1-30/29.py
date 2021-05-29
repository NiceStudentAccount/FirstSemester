print('---------------PROBLEMA 29---------------')

def median(array):
    if len(array) % 2 != 0:
        return array[int(len(array)/2)]
    else: 
        n1 = array[int(len(array)/2)]
        n2 = array[int(len(array)/2-1)]
        return (n1 + n2)/2

numbers = list()sdf
for x in range(int(input('Amount of items: '))):
    numbers.append(int(input('Number: ')))

print('The median number is: ', median(numbers))
