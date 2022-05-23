"""
NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, 
El equipo de desarrollo de este calificador modificó las funciones 'print' e 'input'.
Esta modificación se hizo con la finalidad de que el sistema pueda calificar tu solución.
Por eso LEER MUY BIEN LO QUE SE SOLICITA Y LAS RESTRICCIONES QUE SE LE IMPUSIERON A ESTAS DOS FUNCIONES.
"""
from student_utilities import input, print


def solucion(b,n):
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    
    
    
    intentos = 0;
   
    cond = True
    while cond:
        
        numero = int(input("𝐼𝑛𝑔𝑟𝑒𝑠𝑒 𝑢𝑛 𝑛ú𝑚𝑒𝑟𝑜: ")); 
        if numero < 0 or numero > b:
            print("¡Te saliste del intervalo!")
        else:
            intentos = intentos + 1
            if numero > n:
                print("¡Ups! Te pasaste")
            if numero < n:
                print("¡Ups! Estás por debajo")

        if n == numero:
            cond = False 

    print(f"¡LO LOGRASTE! Usaste {intentos} intentos")
    
    
    
    
    
    
    
    
    #ACÁ TERMINA LA FUNCIÓN SOLUCIÓN
"""
¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE!
NO AÑADIR CÓDIGO FUERA DE LA FUNCIÓN calcular_promedio_y_cuadro_honor(grupo) .
SOLO AÑADIR CÓDIGO ENTRE EL ESPACIO DONDE DICE: ACÁ INICIA... ACÁ TERMINA
"""