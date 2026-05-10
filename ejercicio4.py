numeros_usuario = []

for i in range(8):
    numero = int(input(f"Ingresa el numero {i + 1} "))
    numeros_usuario.append(numero)
    
   
    
def determinar_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

numero_mayor = determinar_mayor(numeros_usuario)
print(f"El numero mayor hasta ahora es: {numero_mayor}")

        
    