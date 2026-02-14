Proceso Division
    Definir num1, num2, resultado Como Real
    
    Escribir "Ingrese el numero a dividir"
    Leer num1
    
    Escribir "Ingrese el segundo numero"
    Leer num2
    
    Si num2 <> 0 Entonces
        resultado = num1 / num2
        Escribir "La division es ", resultado
    SiNo
        Escribir "Error: No se puede dividir entre cero"
    FinSi
FinProceso

