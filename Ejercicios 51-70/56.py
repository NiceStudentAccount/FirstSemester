print('---------------PROBLEMA 56---------------')

#INPUT FUNCTIONS------------------------------------------------------
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
        
        #append all the current line to the matrix 
        matrix.append(currentLine)   
        counter += 1

    return matrix

def outputMatrix(mat):
    matrix = '\nFINAL MATRIX:\n'
    for x in mat:
        for y in x:
            matrix += str(f'{y} ')
        matrix += '\n'
    
    return matrix

#PROGRAM FUNCTIONS----------------------------------------------------
def determinant(mat):
    deter : float
    mult = 0

    #we check if the matrix is squared
    if len(mat[0]) != len(mat):
        return None
    
    #we convert the lower triangle values in 0 
    x = 0
    while x < len(mat[0])-1:
        y = x + 0
        while y < len(mat)-1:
            if mat[y+1][x] == 0 or mat[x][x] == 0:
                mult = 0
            else:
                mult = -mat[y+1][x]/mat[x][x]
            z = x + 0 
            while z < len(mat[0]):
                mat[y+1][z] += mat[x][z] * mult
                z += 1
            y += 1
        x += 1

    #we multiply so we can find the determinant
    x = 0
    while x < len(mat):
        if x == 0:
            deter = mat[x][x]
        else:
            deter *= mat[x][x]
        x += 1
    
    #convert to integer if posible
    if deter % 1 == 0:
        deter = int(deter)

    print(outputMatrix(mat))
    return deter

#MAIN-----------------------------------------------------------------
print('Insert the matrix lines separated with spaces. To finish type ENTER\n')

det = determinant(inputMatrix(1))
if det == None:
    print('The matrix is not square-shaped')
else:
    print('\nMATRIX DETERMINANT:', det)

