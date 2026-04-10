texto = "Python2026"

es_alfanumerico = texto.isalnum()

if es_alfanumerico == True:
    minusculas = texto.lower()
    reemplazar = minusculas.replace("2026", "")
    print(f"texto final: {reemplazar}")
else:
    print("el texto no es alfanumerico")
    