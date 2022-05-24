# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# NO MODIFICAR EL NOMBRE, PARÁMETROS O RETORNO DE LA FUNCIÓN
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN modificar_materia (En este espacio debes 
    # poner el código necesario para implementar esta funcionalidad)
    contador=True
    if (semestre==0 or (semestre >(len(pensum)))):
        mensaje='Ingrese un semestre válido'
    else:
        semestre=semestre-1
        if len(pensum[semestre])==0:
            mensaje='El semestre no tiene materias'
        else:
            for values in pensum[semestre]:
                if values!=materia and contador==True:
                    mensaje='La materia no existe'
                else:
                    contador=False
                    pensum[semestre][materia]['nombre']=nombre
                    pensum[semestre][materia]['créditos']=creditos
                    mensaje='Modificada con éxito'
    
    
    # ACÁ TERMINA LA FUNCIÓN modificar_materia
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return mensaje