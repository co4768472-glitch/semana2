def filtrar_positivos(lista):
    positivos = []
    for num in lista:
        if num > 0:
            positivos.append(num)
    return positivos 

prueba = [-5, 10, -3, 0, 8, -1, 15]
resultado = filtrar_positivos(prueba)
print(f"Los numeros positivos son: {resultado}")