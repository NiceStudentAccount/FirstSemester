print('---------------PROBLEMA 55---------------')

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

def binary(mat, n):
    x = 0
    while x < len(mat):
        y = 0
        while y < len(mat[0]):
            if mat[x][y] <= n:
                mat[x][y] = 0
            else: 
                mat[x][y] = 1
            y += 1
        x += 1
    
    return mat

#MAIN-------------------------------------------------------    
print('Insert the matrix lines separed with spaces. To finish type ENTER\n')

print(outputMatrix(binary(inputMatrix(1), int(input('Number to evaluate: ')))))
