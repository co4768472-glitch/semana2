nombres_ingresados = []

for i in range(10):
    nombre = input(f"ingrese el nombre {i + 1}: ")
    nombres_ingresados.append(nombre)

def mostrar_nombres(lista):
    print("Los nombres con mas de 5 caracteres son:")
    for nombre in lista:
        if len(nombre) > 5:
            print(nombre)

mostrar_nombres(nombres_ingresados)
        