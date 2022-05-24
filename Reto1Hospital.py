import math

carbohidrato = 60.1
fruta_verdura = 24.4
proteina = 30.5
A = "A"
B = "B"
C = "C"
porc_desnutricion = (carbohidrato * 2) + (proteina - (fruta_verdura * 2))
porc_sobrepeso = (carbohidrato * 0.6) + (proteina - (fruta_verdura * 4))
porc_saludable = (carbohidrato * 0.5) + ((proteina * 0.7) - (fruta_verdura * 2))
dias = 0
while True:
    edad = int(input("Indicar la edad del paciente: "))
    peso = float(input("Indicar el peso del paciente en Kilogramos: "))

    if 5 <= edad <= 10 and peso < 16:
        dias = math.ceil((22 - peso) / (porc_desnutricion/1000))
        print(f"El estado nutricional del paciente es {A} y se requieren {dias} días de dieta para que alcance el peso saludable")
    elif 5 <= edad <= 10 and peso > 28:
        dias = math.ceil((24-peso) / (porc_sobrepeso/1000))
        print(f"El estado nutricional del paciente es {B} y se requieren {dias} días de dieta para que alcance el peso saludable")
    elif 5 <= edad <= 10 and 16 <= peso <= 28:
        dias = math.ceil((28 - peso) / (porc_saludable/1000))
        print(f"El estado nutricional del paciente es {C} y se requieren {dias} días de dieta para que alcance el peso maximo")

    if 10 < edad <= 13 and peso < 30:
        dias = math.ceil((32 - peso) / (porc_desnutricion / 1000))
        print(f"El estado nutricional del paciente es {A} y se requieren {dias} días de dieta para que alcance el peso saludable")
    elif 10 < edad <= 13 and peso >= 50:
        dias = math.ceil((43 - peso) / (porc_sobrepeso / 1000))
        print(f"El estado nutricional del paciente es {B} y se requieren {dias} días de dieta para que alcance el peso saludable")
    elif 10 < edad <= 13 and 30 <= peso < 50:
        dias = math.ceil((50 - peso) / (porc_saludable / 1000))
        print(f"El estado nutricional del paciente es {C} y se requieren {dias} días de dieta para que alcance el peso maximo")

    if 13 < edad <= 17 and peso < 51:
        dias = math.ceil((56 - peso) / (porc_desnutricion / 1000))
        print(f"El estado nutricional del paciente es {A} y se requieren {dias} días de dieta para que alcance el peso saludable")
    elif 13 < edad <= 17 and peso >= 63:
        dias = math.ceil((58 - peso) / (porc_sobrepeso / 1000))
        print(f"El estado nutricional del paciente es {B} y se requieren {dias} días de dieta para que alcance el peso saludable")
    elif 13 < edad <= 17 and 51 <= peso < 63:
        dias = math.ceil((63 - peso) / (porc_saludable / 1000))
        print(f"El estado nutricional del paciente es {C} y se requieren {dias} días de dieta para que alcance el peso maximo")

