def cadena_de_montaje(texto_inicial, lista_de_opciones):
    texto_actual = texto_inicial

    for opcion in lista_de_opciones:

        if opcion == 1:
            texto_actual = texto_actual.upper()
        elif opcion == 2:
            texto_actual = texto_actual.lower()
        elif opcion == 3:
            texto_actual = texto_actual.capitalize()
        else:
            print("Ignorando opción no válida:", opcion)

    return texto_actual


mi_texto = "hOlA mUnDo"
mis_instrucciones = [1, 2]

print("Texto original:", mi_texto)
print("Instrucciones a ejecutar:", mis_instrucciones)

resultado_final = cadena_de_montaje(mi_texto, mis_instrucciones)
print("El resultado final de la cadena de montaje es:", resultado_final)
