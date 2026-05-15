from decimal import Decimal

total = Decimal("0.00")
while True:
    opcion = input("Ingrese el precio del producto o 0 para salir: ")
    try:
        validar = float(opcion)
        if validar == 0.0:
            break
        precio = Decimal(opcion)
        total += precio
    except ValueError:
        print("Advertencia. Ha ingresado texto, Por favor ingrese un número válido.")
        
print(f"el total es {total}")