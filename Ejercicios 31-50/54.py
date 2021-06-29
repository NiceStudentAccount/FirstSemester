print('---------------PROBLEMA 54---------------')

def inputMatrix():
    print('\nMATRIX')
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

def magic(mat):
    #we check if the matrix is squared-shaped
    if len(mat) != len(mat[0]):
        return False
    elif len(mat) == 1 or len(mat[0]) == 1:
        return True

    magicNum = sum(mat[0])
    
   #check lines
    x = 0
    while x < len(mat):
        if sum(mat[x]) != magicNum:
            return False
        x += 1

    #check columns
    x = 0
    while x < len(mat[0]):
        y = 0 
        current = 0
        while y < len(mat):
            current += mat[x][y]
            y += 1
        if current != magicNum:
            return False
        x += 1

    #check diagonal 1
    x = 0
    current = 0
    while x < len(mat):
        current += mat[x][x]
        x += 1
    if current != magicNum:
        return False

    #check diagonal 2
    x = 0
    y = len(mat)-1
    current = 0
    while x < len(mat):
        current += mat[x][y]
        x += 1
        y -= 1
    if current != magicNum:
        return False

    return True

#MAIN-------------------------------------------------------    
print('Insert the matrix lines separed with spaces. To finish type ENTER\n')
if magic(inputMatrix()):
    print('The square is magic')
else: 
    print('The square isn\'t magic')


