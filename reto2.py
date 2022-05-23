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

# Bloque de Librerias
import os, time
# Bloque de constantes y variables
empleados = {"1": ["a","Ing", 500]}

# Bloque de las funciones
def menu():
  os.system("clear")
  print("""
      Informacion del Empleado
        1) Carga de datos de empleados.
        2) Listado empleados
        3) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
        4) Mostrar todos los datos de empleados que tienen una profesión
        5) Salir
  """)

def ingresar_empleados():
  
  cant_emp = int(input("Indique cantidad de empleados:  "))
  for i in range(cant_emp):
    codigo = input("Codigo empleado: ")
    nombre = input("Nombre empleado: ")
    profesion = input("Profesion empleado: ")
    sueldo = int(input("Sueldo empleado: "))

    empleados[codigo] = [nombre, profesion, sueldo]


  

def modificar_sueldo_empleados(cod_empl,sueldo):
  empleados[cod_empl][2] = sueldo
  print("Registro modificado")

def listado_empleado():
    print(" ! Listado Empleados !")
    for empleado in e
