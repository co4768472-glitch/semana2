def probar_validacion(texto, numero):
    if numero == 1:
        resultado = texto.upper()
    elif numero == 2:
        resultado = texto.lower()
    elif numero == 3:
        resultado = texto.capitalize()
    else:

        resultado = "opción inválida"

    print("Resultado de la operación:", resultado)


print("Sistema de validacion")
texto_usuario = input("Ingresa una palabra:")

opcion_usuario = int(
    input("Elige una opcion (1:MAYUSCULAS, 2:minusculas, 3:primera letra mayuscula):")
)

probar_validacion(texto_usuario, opcion_usuario)
