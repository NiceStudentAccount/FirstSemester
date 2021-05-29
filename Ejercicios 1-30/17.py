import math
print('---------------PROBLEMA 17---------------')

def inscritos(radio):
    #PERIMETRO Y AREA CUADRADO
    perimetro_cuadrado = 4*2*math.sin(math.radians(45))*radio
    area_cuadrado = (perimetro_cuadrado * math.cos(math.radians(40))*radio)/2

    #PERIMETRO Y AREA PENTAGONO
    perimetro_pentagono = 5*2*math.sin(math.radians(36))*radio
    area_pentagono = (perimetro_pentagono * math.cos(math.radians(36))*radio)/2

    #PERIMETRO Y AREA HEXAGONO
    perimetro_hexagono = 6*2*math.sin(math.radians(30))*radio
    area_hexagono = (perimetro_hexagono * math.cos(math.radians(30))*radio)/2

    mensaje = f'Cuadrado:   Area = {area_cuadrado}   Perimetro = {perimetro_cuadrado}\nPentagono:   Area = {area_pentagono}   Perimetro = {perimetro_pentagono}\nHexagono:   Area = {area_hexagono}   Perimetro = {perimetro_hexagono}\n'
    return mensaje

def circunscritos(radio):
    #PERIMETRO Y AREA CUADRADO
    perimetro_cuadrado = 4*2*math.tan(math.radians(45))*radio
    area_cuadrado = (perimetro_cuadrado * radio)/2

    #PERIMETRO Y AREA PENTAGONO
    perimetro_pentagono = 5*2*math.tan(math.radians(36))*radio
    area_pentagono = (perimetro_pentagono * radio)/2

    #PERIMETRO Y AREA HEXAGONO
    perimetro_hexagono = 6*2*math.tan(math.radians(30))*radio
    area_hexagono = (perimetro_hexagono * radio)/2

    mensaje = f'Cuadrado:   Area = {area_cuadrado}   Perimetro = {perimetro_cuadrado}\nPentagono:   Area = {area_pentagono}   Perimetro = {perimetro_pentagono}\nHexagono:   Area = {area_hexagono}   Perimetro = {perimetro_hexagono}\n'
    return mensaje

radio = float(input('Radio: '))

print(f'POLIGONOS INSCRITOS:\n {inscritos(radio)}\nPOLIGONOS CIRCUNSCRITOS\n{circunscritos(radio)}')