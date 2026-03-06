Algoritmo Ejercicio1_Calificacion
    Definir nota Como Real
    Escribir "Ingrese la nota del estudiante (0 a 10)"
    Leer nota
    
    
    Si nota >= 0 Y nota <= 10 Entonces
        Si nota >= 6 Entonces
            Escribir "Aprobado"
        Sino
            Si nota <= 4 Entonces
                Escribir "Reprobado"
            Sino
                Escribir "Recuperación"
            FinSi
        FinSi
    Sino
        Escribir "Error: La nota debe estar entre 0 y 10"
    FinSi
FinAlgoritmo
