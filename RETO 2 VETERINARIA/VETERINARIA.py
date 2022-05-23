# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# NO MODIFICAR LOS NOMBRES, PARÁMETROS DE ENTRADA NI RETORNOS DE LAS FUNCIONES
# USE LOS MISMOS NOMBRES DE LOS RETORNOS PARA NOMBRAR LOS RESULTADOS QUE SU FUNCIÓN DEBE GENERAR

def veterinaria(nombres, tipos, edades, pesos):
    # ACÁ INICIA LA FUNCIÓN VETERINARIA
    # (En este espacio debe poner el código necesario para crear los diccionarios y promedios pedidos)
      #declara el diccionario vacio
    diccionario= {}

    #diccionario 1

    #recorre todos los indice de la lista
    for j in range(0,len(nombres)):

        #guarda en una lista los primeros indice de las 5 lista
        lista = [nombres[j] , tipos[j] , edades[j] , pesos[j]  ]  

        #se inserta los datos de la lista creada anteriormente
        diccionario[str(j+1)] = lista
 
    #diccionario 2

    beneficiarios_can_fel = {}
    contador = 0

    diccionario2 = {}

    for j in range(0,len(nombres)):
        
        #guarda en una lista los primeros indice de las 5 lista
        lista = [nombres[j] , tipos[j] , pesos[j]  ]  
        lista1= [edades[j]]

        if edades[j] >= 9 and tipos[j] == 'canino' or edades[j] >= 9 and tipos[j] == 'felino':
            contador +=1 
            #se inserta los datos de la lista creada anteriormente
            beneficiarios_can_fel[str(contador)] = lista
            
            diccionario2[str(contador)] = lista1



    #diccionario 3

    beneficiarios_equ_bov = {}

    for j in range(0,len(nombres)):
        
        #guarda en una lista los primeros indice de las 5 lista
        lista = [nombres[j] , tipos[j] , edades[j] , pesos[j]  ]  

        if edades[j] >= 16 and tipos[j] == 'Equino' or edades[j] >= 16 and tipos[j] == 'bovino':
            #se inserta los datos de la lista creada anteriormente
            beneficiarios_equ_bov[str(j+1)] = lista


    #print(diccionario2)

    #promedio 1
    promedio_can_fel = 0;
    cont = 0;

    
    if len(beneficiarios_can_fel)==0:
        promedio_can_fel = None
    else:
        for item in diccionario2:
            cont+=1
            promedio_can_fel += diccionario2[item][0]
            
        promedio_can_fel = promedio_can_fel/cont
        #promedio_can_fel = int(promedio_can_fel)
    #promedio 2
    cont=0
    promedio_equ_bov = 0

    if len(beneficiarios_equ_bov)==0:
        promedio_equ_bov = None
    else:
        for item in beneficiarios_equ_bov:
            cont+=1
            promedio_equ_bov += beneficiarios_equ_bov[item][2]
            
        promedio_equ_bov = promedio_equ_bov/cont
        #promedio_equ_bov = int(promedio_equ_bov)
    
    
    # ACÁ TERMINA LA FUNCIÓN VETERINARIA
    # NO MODIFIQUE LA SIGUIENTE LÍNEA
    return diccionario, beneficiarios_can_fel, beneficiarios_equ_bov, promedio_can_fel, promedio_equ_bov