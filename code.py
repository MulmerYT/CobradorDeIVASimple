while True:
    def calcular_iva(monto):
        iva = monto * 0.16
        total = monto + iva
        return iva, total

    # Solicitar monto al usuario
    try:
        monto = float(input("Ingresa la cantidad de dinero: $"))
        iva, total = calcular_iva(monto)
        print(f"\nMonto ingresado: ${monto:.2f}")
        print(f"IVA (16%): ${iva:.2f}")
        print(f"Total a pagar: ${total:.2f}")
    except ValueError:
        print("Por favor, ingresa un número válido.")
        break
