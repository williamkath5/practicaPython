#Rifa de 1'000.000 de pesos.

b = 30
n = 22
control = 0
cantidad_intentos = 1

while (True):
    num =int(input("Ingrese un número: "))
    if (num == n):
        print (f"¡LO LOGRASTE! Usaste {cantidad_intentos} intentos")
        cantidad_intentos +=1
        exit()
    elif (num > n and num <= b):
        print (f"¡Ups! Te pasaste")
        cantidad_intentos +=1
    elif (num < n and num > control):
        print (f"¡Ups! estás por debajo")
        cantidad_intentos +=1
    elif (num > b):
        print (f"¡Te saliste del intervalo!")
    else:
        print (f"¡Te saliste del intervalo!")