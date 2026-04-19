usuarrio_correcto = "ing"
pass_correcta = "1234"

usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

if usuario == usuarrio_correcto and contraseña == pass_correcta:
    print("Bienvenido al sistema crack")
else:
    print("usuario o contraseña incorrecta, intente nuevamente")
    