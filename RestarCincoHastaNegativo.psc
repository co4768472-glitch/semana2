Algoritmo RestarCincoHastaNegativo
	Definir numeroActual Como Real
	Definir EsPositivo Como Logico
	
	Escribir "Ingrese un número para empezar:"
	Leer numeroActual
	
	EsPositivo <- Verdadero
	
	Mientras EsPositivo Hacer
		numeroActual <- numeroActual - 5
		Escribir "Valor actual: ", numeroActual
		
		Si numeroActual < 0 Entonces
			EsPositivo <- Falso
		FinSi
	FinMientras
	
	Escribir "El número ya es negativo, el programa terminó."
FinAlgoritmo