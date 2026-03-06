Algoritmo Ejercicio2_SumaPositivos
    Definir num, suma Como Entero
    suma <- 0
    
    Repetir
        Escribir "Ingrese un número (ingrese un negativo para salir)"
        Leer num
        Si num >= 0 Entonces
            suma <- suma + num
        FinSi
    Hasta Que num < 0
    
    Escribir "La suma de todos los números positivos ingresados es ", suma
FinAlgoritmo
