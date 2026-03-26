def transformar_y_contar(texto, numero):
    if numero == 1:
        resultado_texto = texto.upper()
    elif numero == 2:
        resultado_texto = texto.lower()
    elif numero == 3:
        resultado_texto = texto.capitalize()
    else:
        resultado_texto = "opcion invalida"

    cantidad_letras = len(resultado_texto)

    return cantidad_letras


print("Bienvenido al transformador de texto y contador de caracteres")
mi_texto = input("Escribe una palabra: ")
opcion = int(
    input("Elige una opcion (1:MAYUSCULAS, 2:minusculas, 3:primera letra mayuscula): ")
)

cantidad = transformar_y_contar(mi_texto, opcion)

print(" PROCESANDO....")

print("El texto transformnado tiene", cantidad, "caracteres")
