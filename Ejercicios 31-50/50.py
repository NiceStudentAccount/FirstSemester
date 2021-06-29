print('---------------PROBLEMA 50---------------')

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

def add(mat1, mat2):
    #checks if the matrixes are of the same dimesions 
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print('Invalid matrixes')
        return None
    
    x = 0
    while x < len(mat1):
        y = 0 
        while y < len(mat1[0]):
            mat1[x][y] += mat2[x][y]
            y += 1
        x += 1

    return mat1


#MAIN------------------------------------------------------------
print('Insert the matrix lines separed with spaces. To finish type ENTER\n(The matrixes have to be of the same dimensions)\n\n')
print(outputMatrix(add(inputMatrix(1), inputMatrix(2))))