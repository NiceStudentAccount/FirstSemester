print('---------------PROBLEMA 52---------------')

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

def addColumn(mat, n):
    addition = 0
    for x in mat:
        addition += x[n-1]
    return addition

#MAIN-------------------------------------------------------    
print('Insert the matrix lines separed with spaces. To finish type ENTER\n')
print('Suma de la columna: ', addColumn(inputMatrix(1),int(input('Columna a sumar: '))))
