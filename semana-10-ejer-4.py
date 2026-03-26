def transformar_lista(lista_palabras, opcion):
    for palabra in lista_palabras:

        if opcion == 1:
            resultado = palabra.upper()

        elif opcion == 2:
            resultado = palabra.lower()

        elif opcion == 3:
            resultado = palabra.capitalize()
        else:
            resultado = "Opcion no valida"

        print("El resultado de la transformaccion es:", resultado)


mis_palabras = ["HOla", "iNgEniEro", "CoMo eStA?"]

print("Transformando palabras....")

transformar_lista(mis_palabras, 3)
