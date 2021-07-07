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
    #VARIABLES 
    matLenght = math.sqrt(len(array))
    mat = list()

    line = 0
    column = 0
    case = 1
    n = 0
    difference = 1

    #CHECK IF THE ARRAY CAN BE TURNED INTO A MATRIX 
    if matLenght % 1 != 0:
        print('Error: Lenght of the array doesn\'t have a square root')
        sys.exit()
    else:
        matLenght = int(matLenght)

    #create the empty array
    mat = [[0 for x in range(matLenght)] for y in range(matLenght)]

    #TRANSFORM THE EMPTY ARRAY INTO A SPIRAL ONE
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


print('\nSPIRAL MATRIX\n' + outputMatrix(matrix))