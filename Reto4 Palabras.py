# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN.
#RECUERDE QUE SU SOLUCIÓN DEBE REQUERIR DE POR LO MENOS OTRA
#FUNCIÓN MÁS APARTE DE LA FUNCIÓN main



def main(lista_texto):
    # ACÁ INICIA LA FUNCIÓN main

    #convertir todas las palabras de la lista a la primer letra en mayúsculas
    for i in range(len(lista_texto)):
        lista_texto[i] = lista_texto[i]#.lower()
    
    #Quitar caracteres especiales '-¿?.,¡!:"–'
    
    Caracteres_especiales = '-¿?.,¡!:"–'
    def quitCaracters(lista_texto, caracteres_a_quitar):
        """
        elimina los caracteres de los strings dentro de una lista
        entrada:
            lista_texto -> list: lista compuesta por str de palabras con caracteres para quitar.
            caracteres_a_quitar -> str: todos los caracteres que se desean eliminar de la lista.
        salida:
            nueva_lista_texto -> list: lista con las nuevas palabras sin los caracteres quitados. 
        """
            
        nueva_lista_texto = list()
        for l in lista_texto:
            for c in range(len(Caracteres_especiales)):
                l  = l.replace(Caracteres_especiales[c],"")
            nueva_lista_texto.append(l)
        return nueva_lista_texto
    
    def palabrasFrecuentes(lista_texto, cantidad=1):
        """
        Encuentra la cantidad de palabras mas frecuentes deseadas en una lista.
        
        Entrada:
            lista_texto -> list: lista que contiene todas las palabras a analizar.
            cantidad -> int: Cantidad de palabras frecuentes que se desean.
        Salida:
            lista_conteo -> list: lista que contiene las listas ['palabra', 'cantidad de recurrencias']
        """
        
        dicc = dict()
        contador = []
        for l in lista_texto:
            dicc[l] = lista_texto.count(l)
            contador.append(lista_texto.count(l))
        contador = sorted(list(set(contador)),reverse=True)
    
        lista_conteo = list()
    
        #bucle para añadir las 20 palabras mas frecuentes a lista_conteo
        for i in contador:
            if len(lista_conteo) <= cantidad: #si lista_conteo tiene menos de 20 palabras 
                for k,v in dicc.items():
                    if k != "":
                        if v == i and len(lista_conteo) < cantidad:
                            lista_conteo.append([k,v])
            else:
                break
        return lista_conteo

    nueva_lista = list(quitCaracters(lista_texto, Caracteres_especiales))
    lista_conteo =palabrasFrecuentes(nueva_lista,20)
    # lista_conteo =list()

    # ACÁ TERMINA LA FUNCIÓN main
    # NO MODIFICAR LA SIGUIENTE LÍNEA
    return lista_conteo