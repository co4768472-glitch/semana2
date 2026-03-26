def mostrar_transformacion(palabra, numero):

    if numero == 1:

        resultado = palabra.upper()
    elif numero == 2:

        resultado = palabra.lower()
    elif numero == 3:

        resultado = palabra.capitalize()
    else:
        resultado = "Opción no válida"

    print("El resultado de la transformacion es:", resultado)


mostrar_transformacion("gEoVaNy", 1)
mostrar_transformacion("gEoVaNy", 2)
