print('---------------PROBLEMA 3---------------')

#FUNCION: Se calcula el peso a vender
#ARGUMENTOS: nEscorpiones grandes, nEscorpiones medianos y nEscorpiones pequeños
def soldWeight(x,y,z):
    soldScorpions : int = 0 
    maximumSale : int = (x+y+z)//3
    soldWeight : float = 0
    flag = True
    while flag or soldScorpions < maximumSale:
        flag = False
        if 0 < x:
            x -= 1
            soldScorpions += 1
            soldWeight += 0.05
        elif 0 < y:
            y -= 1
            soldWeight += 0.03
            soldScorpions += 1
        elif 0 < z:
            z -= 1
            soldScorpions += 1
            soldWeight += 0.02
    return soldWeight

#FUNCION: se imrime la respuesta, se piden los datos y se llama la función soldWeight
print('El peso total vendido es de: ', soldWeight(int(input('Ingrese el numero de escorpiones grandes: ')), int(input('Ingrese el numero de escorpiones medianos: ')),int(input('Ingrese el numero de escorpiones pequeños: '))), 'Kg')