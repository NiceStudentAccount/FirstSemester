print('---------------PROBLEMA 19---------------')


def nArbolesPodados(hojasObjetivo, hojasPorRama, ramasPorarbol):
    return hojasObjetivo/(hojasPorRama * ramasPorarbol)

print('En numero de arboles que se necesitan podar es de: %.2f' % nArbolesPodados(int(input('Hojas que se desean podar: ')), int(input('Hojas por rama: ')), int(input('Ramas a podar por arbol: '))))