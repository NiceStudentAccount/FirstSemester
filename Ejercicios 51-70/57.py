print('---------------PROBLEMA 57---------------')

#INPUT FUNCTIONS
def inputMatrix(n):
    print('\nMATRIX', n)
    matrix = list()
    currentLine = ''

    counter = 1
    while True: 
        #convert the input into a list
        currentLine = str(input(f'Line {counter}: '))
        if currentLine == '':
            break
        else:
            currentLine = currentLine.split()

        currentLine = [int(x) for x in currentLine]

        #modify to match the matrix width
        if counter != 1:
            if len(currentLine) < len(matrix[0]):
                while len(currentLine) < len(matrix[0]):
                    currentLine.append(0)
            elif len(currentLine) > len(matrix[0]):
                while len(currentLine) > len(matrix[0]):
                    currentLine.pop(-1)
        
        #append all the current line to the matrix 20947699
        matrix.append(currentLine)   
        counter += 1

    return matrix

def outputMatrix(mat):
    matrix = ''
    for x in mat:
        for y in x:
            matrix += str(f'{y} ')
        matrix += '\n'
    
    return matrix

def inputArray():
    array = input('\nINDEPENDENT VALUES: ').split()
    array = [int(x) for x in array]
    return array

#PROGRAM FUNCTIONS----------------------------------------------------
def solve(mat, array):
    #we check if the matrix is squared and if the amount of independent values are the same as the matrix lenght
    if len(mat[0]) != len(mat) or len(array) != len(mat):
        return None

    #variables
    mult = 0

    #we convert the lower triangle values in 0 
    x = 0
    while x < len(mat[0])-1:
        y = x
        while y < len(mat)-1:
            if mat[y+1][x] == 0 or mat[x][x] == 0:
                mult = 0
            else:
                mult = -mat[y+1][x]/mat[x][x]
            array[y+1] += array[x] * mult
            z = 0
            while z < len(mat[0]):
                mat[y+1][z] += mat[x][z] * mult
                z += 1
            y += 1
        x += 1
    
    #convert the higher triangle values in 0 
    x = len(mat)-1
    while x > 0:
        y = x
        while y > 0:
            if mat[x][x] == 0 or mat[y-1][x] == 0 :
                mult = 0
            else: 
                mult = -mat[y-1][x]/mat[x][x]
            array[y-1] += array[x] * mult
            z = len(mat)-1
            while z >= 0:
                mat[y-1][z] += mat[x][z] * mult
                z -= 1
            y -= 1
        x -= 1

    #divide the first independent value by the coeficient of the "x"
    array[0] = array[0]/mat[0][0]
    
    return array[0]

#MAIN-----------------------------------------------------------------
print('Insert the matrix lines separated with spaces. To finish type ENTER')

xSol = solve(inputMatrix(1), inputArray())
if xSol == None:
    print('The matrix is not square-shaped or the amount of independent values is different')
else:
    print('\nSOLUTION FOR X:', xSol)