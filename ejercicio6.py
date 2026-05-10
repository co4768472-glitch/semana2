import random

numero_alea = []

for i in range(10):
    numero = random.randint(1, 100)
    numero_alea.append(numero)

print(f"Los numeros aleatorios son: {numero_alea}")

def encontrar_mayor(lista):
    contador = 0
    for num in lista:
        if num > 50:
            contador += 1
    return contador

cantidad_mayores = encontrar_mayor(numero_alea)
print(f"Los números generados son: {numero_alea}")
print(f"Hay {cantidad_mayores} números mayores a 50.")