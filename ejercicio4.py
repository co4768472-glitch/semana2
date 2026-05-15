for registro in range(1,51):
    if registro == 42:
        break
    if registro % 3 == 0:
        continue
    print(f"Procesando registro ID: {registro}")