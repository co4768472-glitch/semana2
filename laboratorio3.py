import random

print("BIENVENIDO AL JUEGO DE ADIVINANZA")
print("1. Fácil (Adivinar del 1 al 10)")
print("2. Medio (Adivinar del 1 al 50)")
print("3. Difícil (Adivinar del 1 al 100)")
print("4. Modo ultra hardcore")

opcion = input("Elige tu nivel (1, 2, 3 o 4): ")
match opcion:
    case "1":
        limite_maximo = 10
        print("Se a activado el modo facil")
    case "2":
        limite_maximo = 50
        print("se a activado el modo medio")
    case "3":
        limite_maximo = 100
        print("se a activado el modo dificil, suerte")
    case "4":
        print("Se a activado el modo ultra hardcore (conste)")
        seguro = input("Estas seguro si/ no?").lower()
        print("OK")
        if seguro == "si":
         print("imagina un futuro con ell@")
         print("El programa se ha cerrado por daño emocional.")
         exit()
        elif seguro == "no":
            print("bien echo bro")
            limite_maximo = 10
        else:
            print("opcion no valida")
            limite_maximo = 10
    case _:
        print("Opcion no valida, jugaras en modo por defecto")
        limite_maximo = 10
        
numero_secreto = random.randint(1, limite_maximo)
print(f"La computadora ya eligió un número entre 1 y {limite_maximo} !empieza a jugar¡")

historial_intentos = []

while True:
    intento = int(input("Ingresa tu numero: "))
    
    historial_intentos.append(intento)
    
    if intento == numero_secreto:
        print("¡¡Felicidades lograste adivinar el numero!!")
        break
    elif intento < numero_secreto:
        print(" ¡PISTA! , el numero secreto es mayor")
    else:
        print("¡PISTA!, el numero secreto es menor")
        
print(f" Juego terminado, te tomo {len(historial_intentos)} intentos ganar")
print("Este es tu historial de intentos")

for numero in historial_intentos:
    print(f" intentaste con el {numero}")