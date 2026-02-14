Proceso OperacionesBasicas
    Definir num1, num2 Como Real
    Definir suma, resta, multiplicacion, division Como Real
    
    Escribir "Ingrese el primer numero"
    Leer num1
    
    Escribir "Ingrese el segundo numero"
    Leer num2
    
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    Si num2 <> 0 Entonces
        division = num1 / num2
        Escribir "Division: ", division
    SiNo
        Escribir "No se puede dividir entre cero."
    FinSi
    
    Escribir "Suma ", suma
    Escribir "Resta ", resta
    Escribir "Multiplicacion ", multiplicacion
	
	Escribir "Gracias tenga buen dia:)"
FinProceso

