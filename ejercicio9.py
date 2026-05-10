def sumar_pares(numeros):
    suma = 0
    for num in numeros:
        if num % 2 == 0:
            suma += num
    return suma
    
arreglo = [1, 4, 5, 8, 10, 3]
resultado = sumar_pares(arreglo)
print(f"El resultado es {resultado}")
        