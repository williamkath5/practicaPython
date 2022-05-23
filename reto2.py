def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN modificar_materia (En este espacio debes 
    # poner el código necesario para implementar esta funcionalidad)
    
    if semestre < 1 or semestre > 3: #validacion de semestre
        mensaje = "Ingrese un semestre válido"
        
    elif len(pensum[semestre-1]) == 0:
        mensaje = "El semestre no tiene materias"
        
    #si el codigo de la materia no esta en el semestre
    elif materia != (pensum[semestre-1]):
        mensaje = "La materia no existe"
        
    else:
        pensum[semestre-1][materia] = {"nombre": nombre, "creditos": creditos}
        mensaje = "Modificada con éxito"
        print(pensum)
    
    
    # ACÁ TERMINA LA FUNCIÓN modificar_materia
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return mensaje
