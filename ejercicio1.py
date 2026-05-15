opcion = input("Ingrese la etiqueta de rastreo : ")
if not opcion:
     print("Error, la etiqueta no puede estar vacía")
else:
    categoria = opcion[5:-3]
    print((f"Categoría: {categoria}"))
    ruta = "Ruta local"if opcion[-2:] == "SV" else "Ruta internacional"
    print(ruta)