def evaluar_promedio(notas):
    promedio = sum(notas) / len(notas)
    if promedio >= 6:
        print("Excelente, aprobado")
    else:
        print("reprobado, deja el vicio del freefire")
    return promedio

notas_estudiante = [7.5, 8.0, 5.5, 6.0]
resultado = evaluar_promedio(notas_estudiante)
print(f"El promedio del estudiante es: {resultado}")
      

