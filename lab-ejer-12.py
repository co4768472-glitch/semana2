nombre = "ING. Geovany.txt"

sin_prefijo = nombre.removesuffix(".txt")
prefijo = sin_prefijo.removeprefix("ING. ")

minusculas = prefijo.lower()

lista_palabras = minusculas.split()

print(f"nombre original: {nombre}")
print(f"nombre sin prefijo: {prefijo}")
print(f"lista de palabras: {lista_palabras}")


