lectu = []

for i in range(5):
    opcion = int(input(f"ingresa la tempreratura {i+1}: "))
    lectu.append(opcion)

for opcion in lectu:
    match opcion:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            print("Estado: Estable" if 10 <= opcion <= 30 else "Estado: Crítico")
            
            
            