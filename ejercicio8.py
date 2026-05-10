productos = []

for i in range(5):
    nombre = input(f"ingresa el nombre del producto {i + 1}: ")
    productos.append(nombre)
    
def mostrar_productos(lista, producto_buscado):
    if producto_buscado in lista:
        print(f"el producto {producto_buscado} se encuentra en la lista.")
    else:
        print(f"el producto {producto_buscado} no se encuentra en la lista")

producto_a_buscar = input("Ingresa el nombre del producto a buscar: ")
mostrar_productos(productos, producto_a_buscar)  