texto_nombre = "geovany alas"
texto_normalizado = texto_nombre.casefold()
texto_sin_espacios = texto_normalizado.replace(" ", "")
solo_letras = texto_sin_espacios.isalpha()

print(f"Texto casefold: {texto_normalizado}")
print(f"texto sin espacios: {texto_sin_espacios}")
print("¿El texto solo tiene letras?",solo_letras)




