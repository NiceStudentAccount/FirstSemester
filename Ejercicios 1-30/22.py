print('---------------PROBLEMA 22---------------')

def cribe(n): 
    numbers = list()
    for x in range(2, n+1):
        numbers.append(x)
    y = 0
    while y < len(numbers):
        for x in numbers:
            if x % numbers[y] == 0 and x != numbers[y]:
                numbers.remove(x)
        y += 1
    return numbers

print(cribe(int(input('Numero hasta el cual implementar la criba: '))))