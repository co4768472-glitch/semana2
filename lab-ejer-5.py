texto = "pYTHON"
texto_invertido = texto.swapcase()
texto_alineado = texto_invertido.ljust(15, "*")

print(f"texto original: {texto}")
print(f"texto invertido: {texto_invertido}")
print(f"texto alineado a la izquierda: {texto_alineado}")