def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares 

resultado_pares, resultado_impares = contar_pares_impares([1, 2, 3, 4, 5, 6, 7])
print(f"pares {resultado_pares} , impares {resultado_impares}")
