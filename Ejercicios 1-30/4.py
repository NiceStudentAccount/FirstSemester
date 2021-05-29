print('---------------PROBLEMA 4---------------')

#FUNCION: Determina el cerramiento mas económico
#ARGUMENTOS: ancho del corral, largo del corral, precio del metro de madera, 
#precio del metro de alambre y precio del metro de varilla.
def materialMasEconomico(precio_madera, precio_alambre, precio_varillas):
   
    corral_madera = 4*precio_madera
    corral_varillas = 8*precio_varillas
    corral_alambre = 5*precio_alambre
    if corral_madera < corral_varillas and corral_madera < corral_alambre:
        return 'madera'
    elif corral_varillas < corral_madera and corral_varillas < corral_alambre:
        return 'varillas'
    else:
        return 'alambre'
    
    
#Imprime la respuesta, pide los datos y llama la funcion materialMasEconomico
print('El cerramiento mas económico es el de', materialMasEconomico(float(input('Precio del metro de madera: ')), float(input('Precio del metro de alambre: ')), float(input('Precio del metro de varilla: '))))