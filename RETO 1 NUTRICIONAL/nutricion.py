"""
NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, SIMULARÁ
LAS FUNCIONES input() y print() DE PYTHON PARA PROBAR
EL FUNCIONAMIENTO DE TU SOLUCIÓN CON BASE EN UNOS
OBJETOS DE PRUEBA. TU SOLUCIÓN DEBE ESTAR CONTENIDA
EN LA REGIÓN DELIMITADA A CONTINUACIÓN.
"""

from student_utilities import input, print

def solucion(edad, peso):
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    import math
    edad=int(input("Indicar la edad del paciente:"))
    peso=float(input("Indicar el peso del paciente en kilogramos:"))
    #clasificacion por peso_edad
    desnutricion="A"
    sobrepeso="B"
    peso_saludable="C"
    # conversor a gramos
    kg=1000

    #PESOS_SALUDABLES
    peso_sal1=22
    peso_sal2=32
    peso_sal3=56
    #pesos minimos
    pesomin1=16
    pesomin2=30
    pesomin3=51
    #pesos maximos
    pesomax1=28
    pesomax2=50
    pesomax3=63
    #complementos diarios 
    complemento_desnut=101.9
    complemento_sobre=(-31.04)
    complemento_salu=2.6
    #LOS DAT1,DAT2,DAT3,ETC... SE REFIEREN A LA FORMULA PARA SACAR LOS DIAS DE DIETA
    #RANGO1
    if edad in range(5,10+1) and peso<pesomin1:
        dat1=math.ceil(((peso_sal1-peso)*kg)/complemento_desnut)
        print("El estado nutricional del paciente es %s y se requieren %d dias de dieta para que alcance un peso saludable" %(desnutricion, dat1))
    elif edad in range(5,10+1)  and peso in range(16,28+1):
        dat2=math.ceil(((pesomax1-peso)*kg)/complemento_salu)
        print("El estado nutricional del paciente es %s y se requieren %d dias de dieta para que alcance el peso maximo" %(peso_saludable, dat2))
    elif edad in range(5,10+1)  and peso>=pesomax1:
        dat3=math.ceil(((peso-24)*kg)/complemento_sobre*-1)
        print("El estado nutricional del paciente es %s y se requieren %d dias de dieta para que alcance un peso saludable" %(sobrepeso, dat3))    
     #RANGO2  
    elif edad in range(11,13+1) and peso<=pesomin2:
        dat4=math.ceil(((peso_sal2-peso)*kg)/complemento_desnut)
        print("El estado nutricional del paciente es %s y se requieren %d dias de dieta para que alcance un peso saludable" %(desnutricion, dat4))
    elif edad in range(11,13+1)  and peso in range(30,50+1):
        dat5=math.ceil(((pesomax2-peso)*kg)/complemento_salu)
        print("El estado nutricional del paciente es %s y se requieren %d dias de dieta para que alcance el peso maximo" %(peso_saludable, dat5))
    elif edad in range(11,13+1)  and peso>pesomax2:
        dat6=math.ceil(((peso-43)*kg)/complemento_sobre*-1)
        print("El estado nutricional del paciente es %s y se requieren %d dias de dieta para que alcance un peso saludable" %(sobrepeso, dat6))
    #RANGO3
    elif edad in range(14,17+1) and peso<=pesomin3:
        dat7=math.ceil(((peso_sal3-peso)*kg)/complemento_desnut)
        print("El estado nutricional del paciente es %s y se requieren %d dias de dieta para que alcance un peso saludable" %(desnutricion, dat7))
    elif edad in range(14,17+1)  and peso >=pesomin3 and peso<=63:
        dat8=math.ceil(((pesomax3-peso)*kg)/complemento_salu)
        print("El estado nutricional del paciente es %s y se requieren %d dias de dieta para que alcance el peso maximo" %(peso_saludable, dat8))
    elif edad in range(14,17+1)  and peso>pesomax3:
        dat9=math.ceil(((peso-58)*kg)/complemento_sobre*-1)
        print("El estado nutricional del paciente es %s y se requieren %d dias de dieta para que alcance un peso saludable" %(sobrepeso, dat9))




    #ACÁ TERMINA LA FUNCIÓN SOLUCIÓN
    """
¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE!
NO AÑADIR CÓDIGO FUERA DE LA FUNCIÓN solucion().
SOLO AÑADIR CÓDIGO ENTRE EL ESPACIO DONDE DICE: ACÁ INICIA... ACÁ TERMINA...
"""