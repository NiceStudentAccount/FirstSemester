print('---------------PROBLEMA 21---------------')

def lego(n):
    if n == 0:
        return 0 
    a = 0
    b = 1
    c = 1
    for x in range(1, n):
        a = b
        b = c
        c = a + b
    return c

def amarillo(n):
    contador = 0
    n -= 3
    if n == 0:
        return 1
    y = n
    for x in range(0, n+1):
        if x == 0:
            contador +=  lego(y)
        if y == 0:
            contador += lego(x)
        else:
            contador += lego(x) * lego(y)
        y -= 1
    return contador


base = int(input('Pai que pex: '))
print('La conmbinación de fichas azules y rojas es ', lego(base), ' y si le añadimos una ficha amarilla sería ', amarillo(base))



'''def lego(n):
    if n==1:
        return 1
    if n == 0:
        return 0
    if n == 2:
        return 2
    else:
        return lego(n-1) + lego(n-2)

numero = 0
while numero != -1:
    mumero = int(input('Longitud de la base: '))
    print('Hay ', lego(numero), ' posibilidades')'''