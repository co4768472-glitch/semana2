numero1 = float(input("Ingrese el primer numero "))
numero2 = float(input("Ingrese el segundo numero "))
operacion = input("Ingrese la operacion a realizar(+, -, *, /): ")

if operacion == "+":
    print("El resultado de la suma es: ",numero1 + numero2)
elif operacion == "-":
    print("El resultado de la resta es:",numero1 - numero2)
elif operacion == "*":
    print("El resultado de la multiplicacion es:",numero1 * numero2)
elif operacion == "/":
    if numero2 != 0:
        print("El resultado es:",numero1 / numero2)
    else:
        print("Error: No se puede dividir por cero")
else:
    print("Operacion no valida")
    