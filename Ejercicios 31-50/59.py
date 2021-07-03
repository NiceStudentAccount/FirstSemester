import math
import sys
print('---------------PROBLEMA 59---------------')

#READING FUNCTIONS--------------------------------------------
def inputArray(string):
    return string.split()

def outputMatrix(mat):
    matrix = ''
    try: 
        for x in mat:
            for y in x:
                matrix += str(f'{y} ')
            matrix += '\n'
    except: 
        return mat
    return matrix

#PROGRAM FUNCTIONS--------------------------------------------
def espiral(array):
    #variables 
    matLenght = math.sqrt(len(array))
    mat = list()

    line = 0
    column = 0
    case = 1
    n = 0
    difference = 1

    #check if the array can be turned into a squared matrix
    if matLenght % 1 != 0:
        print('Error: Lenght of the array doesn\'t have a square root')
        sys.exit()
    else:
        matLenght = int(matLenght)


    #create the empty array
    for x in range(matLenght):
        mat.append([])
        for y in range(matLenght):
            mat[x].append(0)

    #transform the empty array into spiral one
    #first line
    while column < matLenght-difference:
        mat[line][column] = array[n]
        n += 1
        column += 1

    #spiral
    while n < len(array)-1:
        if case == 1:
            while line < matLenght-difference:
                mat[line][column] = array[n]
                line += 1
                n += 1
        elif case == 2:
            while column >= difference:
                mat[line][column] = array[n]
                column -= 1
                n += 1
        elif case == 3:
            while line >= difference:
                mat[line][column] = array[n]
                line -= 1
                n += 1
        elif case == 4:
            while column < matLenght-difference:
                mat[line][column] = array[n]
                column += 1
                n += 1

        #cases
        if case == 2: 
            difference += 1

        if case == 4:
            case = 1
        else: 
            case += 1

    #last square
    if matLenght % 2 == 0:
        mat[line][column] = array[-1]
    else:
        mat[line][column] = array[-1]

    return mat



#MAIN---------------------------------------------------------
option = int(input('HOW ARE YOU GOING TO FORM THE ARRAY?\n1. Range\n2. Array\n\nOption: '))
matrix = None

if option == 1:
    array = list()
    for x in range(1, int(input('\nMAX RANGE NUMBER: '))+1):
        array.append(x)
    matrix = espiral(array)
elif option == 2:
    matrix = espiral(inputArray(str(input('ARRAY: '))))


print('SPIRAL MATRIX\n' + outputMatrix(matrix))