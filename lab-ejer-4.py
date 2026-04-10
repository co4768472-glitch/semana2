texto = "CANTANDO"
texto_minuscula = texto.lower()
palabra_corta = texto_minuscula.removesuffix("ando")
posicion_t = palabra_corta.find("t")

print(f"texto original: {texto}")
print(f"texto en minuscula: {texto_minuscula}")
print(f"sin el sufijo : {palabra_corta}")
print(f"la posicion de la letra t es: {posicion_t}")




