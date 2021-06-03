print('---------------PROBLEMA 34---------------')
def askArray():
    numbers = input('Numeros separados por un espacio: ').split()
    numbers = set(map(int, numbers))
    return numbers

def mcm(numbers):
    num = max(numbers)
    print(numbers)
    print(num)
    while True:
        flag = True
        
        for x in numbers:
            if num%x != 0:
                flag = False
                break
        print(flag)
        if flag == True:
            return num 
        else:
            num += max(numbers)

print(mcm(askArray()))