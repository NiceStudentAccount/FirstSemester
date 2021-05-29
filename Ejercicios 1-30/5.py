print('---------------PROBLEMA 5---------------')

#FUNCION: calcula la potencia de un numero entero elevado a un numero entero
#ARGUMENTOS: base, exponente
def potenciaDeEnteros(base, exponente):
    return base**exponente

#Imprime el resultado, llama la funcion potenciaDeEnteros y pide los datos
print('La potencia de los numeros es:', potenciaDeEnteros(int(input('Ingrese la base (numero entero): ')), int(input('Ingrese el exponente (numero entero): '))))