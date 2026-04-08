def transformar_texto(texto, opcion):

    if opcion == 1:

        resultado = texto.upper()

    elif opcion == 2:

        resultado = texto.lower()

    elif opcion == 3:

        resultado = texto.capitalize()

    else:

        resultado = "Opción no válida"

    return resultado


prueba = transformar_texto("hola ingeniero", 3)

print(prueba)
