def ordenar_menorMayor(arreglo):
    n = len(arreglo)
    for i in range(n):
        
     for j in range(0, n - 1):
         if arreglo[j] > arreglo[j + 1]:
            arreglo[j], arreglo[j + 1]= arreglo[j + 1], arreglo[j]
    return arreglo        

ingresados = []
for i in range(6):
    numero = int(input(f"ingresa el numero {i + 1}: "))
    ingresados.append(numero)
print(f"numero original {ingresados}")
ordenados = ordenar_menorMayor(ingresados)
print(f"Lista ordenada: {ordenados}")