lado = float(input("Ingresa la medida del primer lado "))
lado_2 = float(input("Ingresa la medida del segundo lado "))
lado_3 = float(input("Ingresa la medida del tercer lado "))

if lado == lado_2 and lado_2 == lado_3:
    print("El triangulo es equilatero.")
elif lado == lado_2 or lado == lado_3 or lado_2 == lado_3:
    print("El triangulo es isosceles.")
else:
    print("El triangulo es escaleno.")
    
