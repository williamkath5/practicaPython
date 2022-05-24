
iva = 0.19
respuesta = "S"
total = 0
while respuesta == "S":
    valorProducto = int(input('Ingrese el valor unitario: '))
    respuesta = input('¿El producto cuenta con IVA?: ')
    cantidad = int(input('Ingrese la cantidad que lleva el cliente del producto a registrar: '))
    if respuesta == "S":
        print("IVA incluído")
        IVA = valorProducto + (valorProducto * iva)
    else:
        print("Producto sin IVA")
        IVA = valorProducto

    total += IVA * cantidad
    print(f"SUBTOTAL: {total}")

    respuesta = input('¿Faltan productos por cobrar? S/N: ')

print(f"TOTAL A COBRAR: {total}")
