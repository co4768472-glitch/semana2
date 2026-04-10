texto_numero = "42"
numero_rellenado = texto_numero.zfill(5)
termina_con2 = numero_rellenado.endswith("2")

print(f"texto original: {texto_numero}")
print(f"numero rellenado con ceros: {numero_rellenado}")
print(f"¡termina con 2? {termina_con2}")
