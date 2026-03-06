Algoritmo Ejercicio10_MayorMenor
    Definir num1, num2 Como Real
    Escribir "Ingrese el primer número "
    Leer num1
    Escribir "Ingrese el segundo número "
    Leer num2
    
    Si num1 > num2 Entonces
        Escribir num1, " es mayor que ", num2
        Escribir num2, " es menor que ", num1
    Sino
        Si num1 < num2 Entonces
            Escribir num2, " es mayor que ", num1
            Escribir num1, " es menor que ", num2
        Sino
            Escribir "Ambos números son iguales (", num1, " = ", num2, ")"
        FinSi
    FinSi
FinAlgoritmo
