print('---------------PROBLEMA 15---------------')

def puntoDeCorte(m, x, y):
    return -m*x + y

x = float(input('Las rectas se intersextan en la ordenada x: '))
y = float(input('Las rectas se intersextan en la ordenada y: '))

print('La primera recta corta al eje y en: ', puntoDeCorte(float(input('Pendiente 1: ')), x, y))
print('La segunda recta corta al eje y en: ', puntoDeCorte(float(input('Pendiente 2: ')), x, y))
