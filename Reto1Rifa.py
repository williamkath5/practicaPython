def solucion(b, n):
    intentos = 0
    condicional = True
    while condicional:
        numero = int(input("Ingrese un numero: "))
        if numero < 0 or numero > b:
            print("¡Te saliste del intervalo!")
        else:
            intentos += 1
            if numero > n:
                print("¡Ups! Te pasaste")
            if numero < n:
                print("¡Ups! Estás por debajo")
        if numero == n:
            condicional = False
    print(f"¡LO LOGRASTE! Usaste {intentos} intentos")


solucion(30, 22)
