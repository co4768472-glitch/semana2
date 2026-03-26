def mostrar_transformacion(palabra, numero):

    if numero == 1:
        resultado = palabra.upper()

    elif numero == 2:
        resultado = palabra.lower()

    elif numero == 3:
        resultado = palabra.capitalize()

    else:
        resultado = "Opcion no valida"

    print("El resultado es:", resultado)


texto_usuario = input("Ingresa una palabra o frase: ")

opcion_usuario = int(
    input("Elige una opcion (1:MAYUSCULAS, 2:minusculas, 3:primera letra mayuscula):")
)

mostrar_transformacion(texto_usuario, opcion_usuario)
