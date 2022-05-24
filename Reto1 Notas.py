print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre = input("Por favor, ingrese su nombre: ")
materia = input("Ingrese el nombre de la materia: ")
nota_acumulada = 0
porcentaje = 0
respuesta = "S"
while respuesta == "S":
    nota = float(input("Ingrese la nota obtenida: "))
    porcentage = int(input("Ingrese el porcentaje de la nota: "))
    porcentaje += porcentage
    if porcentaje > 100.0:
        print("El porcentaje evaluado de una materia no puede ser mayor a 100")
        porcentaje -= porcentage
        nota = float(input("Ingrese la nota obtenida: "))
        porcentage = int(input("Ingrese el porcentaje de la nota: "))
        porcentaje += porcentage
    nota_acumulada += nota * (porcentage/100)
    if nota_acumulada >= 3:
        resultado = "aprobado"
    else:
        resultado = "reprobado"

    if porcentaje < 100.0:
        respuesta = input("¿Falta añadir notas? S/N: ")
    if porcentaje == 100.0:
        break


# nombre = nombre.lower()
# materia = materia.lower()
nota_acumulada = round(nota_acumulada, 2)
print(f"El estudiante {nombre.capitalize()} cursó la materia {materia.capitalize()} y obtuvo {nota_acumulada} resultando en {resultado}")
