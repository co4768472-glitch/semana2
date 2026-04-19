monto = float(input("Ingrese el monto de su compra "))

if monto > 100:
    descuento = monto * 0.20
    total_pagar = monto - descuento
    print(f"Usted tiene un descuento del 20%: {descuento:.2f}. El total a pagar es: {total_pagar:.2f}")
elif monto >= 50:
    descuento = monto * 0.10
    total_pagar = monto - descuento
    print(f"Usted tiene un descuento del 10%: {descuento:.2f}. El total a pagar es: {total_pagar:.2f}")
else:
    print(f"no cuenta con descuento, su total a pagar es: {monto:.2f}")
    