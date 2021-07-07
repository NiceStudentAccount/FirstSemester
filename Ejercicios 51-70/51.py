print('---------------PROBLEMA 51---------------')

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

def multiplication(mat1, mat2):
    #it is veirfied if the columns of mat1 are the same as the lines of mat2
    if len(mat1[0]) != len(mat2):
        return None
    
    #multiply everithing
    multMat = list()
    x = 0
    while x < len(mat1):
        multMat.append(list())
        y = 0 
        while y < len(mat2[0]):
            current = 0
            z = 0 
            while z < len(mat2):
                current += mat1[x][z] * mat2[z][y]
                z += 1
            multMat[x].append(current)
            y += 1
        x += 1

    return multMat

#MAIN-------------------------------------------------------    
print('Insert the matrix lines separed with spaces. To finish type ENTER\n')
print(outputMatrix(multiplication(inputMatrix(1), inputMatrix(2))))
