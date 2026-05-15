nombre = input("ingrese su nombre completo:")

invertido = nombre.split()[::-1]
for palabra in invertido:
    formato = ""
    for letra in palabra:
        formato += letra + "."
    print(formato[:-1])
        
        
        