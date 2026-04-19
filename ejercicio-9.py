fecha = int(input("Ingrese el año: "))

if (fecha % 4 == 0 and fecha % 100 != 0) or (fecha % 400 == 0):
    print(f"El año {fecha} si es bisiesto")
else:
    print(f"El año {fecha} no es bisiesto")
    
    