print('---------------PROBLEMA 33---------------')
def mcd(numbers):
    numbers = set(map(int, numbers.split()))
    maximum  = max(numbers)

    while True:
        theOne = True
        for x in numbers:
            if x % maximum != 0:
                theOne = False
                break
        if theOne == True:
            return maximum
        else: 
            maximum -= 1 
                
print(mcd(str(input('Numeros separados por un espacio: '))))