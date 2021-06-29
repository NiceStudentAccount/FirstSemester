print('---------------PROBLEMA 58---------------')

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

#PROGRAM FUNCTIONS----------------------------------------------------
def inverse(mat):
    #we check if the matrix is squared
    if len(mat[0]) != len(mat):
        return None

    #variables
    mult = 0
    inverse = list()
    
    #create the inverse matrix
    for x in range(len(mat)):
        currentLine = list()
        for y in range(len(mat)):
            if y == x:
                currentLine.append(1)
            else:
                currentLine.append(0)
        inverse.append(currentLine)

    #we convert the lower triangle values in 0 
    x = 0
    while x < len(mat[0])-1:
        y = x
        while y < len(mat)-1:
            if mat[y+1][x] == 0 or mat[x][x] == 0:
                mult = 0
            else:
                mult = -mat[y+1][x]/mat[x][x]
            z = 0
            while z < len(mat[0]):
                mat[y+1][z] += mat[x][z] * mult
                inverse[y+1][z] += inverse[x][z] * mult
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
            z = len(mat)-1
            while z >= 0:
                mat[y-1][z] += mat[x][z] * mult
                inverse[y-1][z] += inverse[x][z] * mult
                z -= 1
            y -= 1
        x -= 1

    #divide de diagonals by them selves
    x = 0
    while x < len(mat):
        current = mat[x][x]
        y = 0
        while y < len(mat):
            inverse[x][y] /= current
            y += 1

        mat[x][x] /= current

        x += 1
    

    print(outputMatrix(mat))
    return inverse

#MAIN-----------------------------------------------------------------
print('Insert the matrix lines separated with spaces. To finish type ENTER')

inve = inverse(inputMatrix(1))
if inve == None:
    print('The matrix is not square-shaped')
else:
    print('\nMATRIX INVERSE:\n', outputMatrix(inve))