def contar_mayores(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    return contador

edades_personas = [15, 18, 22, 14, 30, 17, 19]
cantidad_mayores = contar_mayores(edades_personas)

print(f"Las edades analizadas son: {edades_personas}")
print(f"Hay {cantidad_mayores} personas mayores de edad.")