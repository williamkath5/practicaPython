# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# INSERTE SU IMPORTACIÓN
# from <LIBRERÍA> import <FUNCIÓN>

def balotera(balotas):
    # ACÁ INICIA LA FUNCIÓN
    import random
    
    #desordena la lista
    random.shuffle(balotas)
    
    
    contb = 0
    conti = 0
    contn = 0
    contg = 0
    conto = 0
    
    lista = []
    
    #recorrer balotas
    for item in balotas:
        
        if list(item)[0] =='B':
            contb +=1
        if list(item)[0] =='I':
            conti +=1
        if list(item)[0] =='N':
            contn +=1
        if list(item)[0] =='G':
            contg +=1
        if list(item)[0] =='O':
            conto +=1
    
        lista.append(item)
        if contb >= 5 and conti >= 5 and contn >= 4 and contg >= 5 and conto >= 5:
            break
    
    
    
    balotas_revueltas = tuple(lista) 

    
    return balotas_revueltas