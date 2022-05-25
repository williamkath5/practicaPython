# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN.
# NO ELIMINAR LAS IMPORTACIONES A CONTINUACIÓN. SU SOLUCIÓN
# DEBE BASARSE EN EL USO DE ELLAS. SE RECOMIENDA ENSAYAR POR
# APARTE SU PROPUESTA DE SOLUCIÓN USANDO LOS DATOS DE APOYO

import numpy as np

def clima(datos):
    datos = np.array(datos)
    datos = datos.reshape(int(len(datos)/7),-1)
    
    
    
    
    valores = np.array(datos[:,1:datos[1].size], dtype='f')
    fechas = datos[:, 0]
    
    
    temp_min_prom = valores[:, 0]
    temp_max_prom = valores[:, 1]
    precip_total = valores[:, 2]
    num_dias_sol = valores[:, -1]
    
    temp_min =np.amin(temp_min_prom)
    temp_max = np.amax(temp_max_prom)
    precip_min = np.amin(precip_total)
    precip_max = np.amax(precip_total)
    max_dias_sol = np.amax(num_dias_sol)
    
    
    fechas_temp_min = list()
    fechas_temp_max = list()
    fechas_precip_min = list()
    fechas_precip_max = list()
    fechas_max_dias_sol = list()
    
    for i in range(fechas.size):
        if temp_min == temp_min_prom[i]:
            fechas_temp_min.append(fechas[i])
        if temp_max == temp_max_prom[i]:
            fechas_temp_max.append(fechas[i])
        if precip_min == precip_total[i]:
            fechas_precip_min.append(fechas[i])
        if precip_max == precip_total[i]:
            fechas_precip_max.append(fechas[i])
        if max_dias_sol == num_dias_sol[i]:
            fechas_max_dias_sol.append(fechas[i])
            
    print(fechas_max_dias_sol,fechas_temp_min,fechas_temp_max,fechas_precip_min,fechas_precip_max)
    #ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA HALLAR LAS
    #FECHAS DE LOS EVENTOS DEL TIEMPO MENCIONADOS EN EL ENUNCIADO.
    #ATÉNGASE AL USO DE LOS RETORNOS PUESTOS AL FINAL DE ESTA FUNCIÓN

    return fechas_temp_min, fechas_temp_max, fechas_precip_min, fechas_precip_max, fechas_max_dias_sol