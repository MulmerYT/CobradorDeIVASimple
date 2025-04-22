import os
import time

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def calcular_iva(monto):
    iva = monto * 0.16
    total = monto + iva
    return iva, total

def mostrar_ticket(monto, iva, total):
    print("\n🧾 TICKET DE COMPRA")
    print("-" * 30)
    print(f"🪙 Subtotal:     ${monto:.2f}")
    print(f"💰 IVA (16%):    ${iva:.2f}")
    print(f"💵 Total a pagar: ${total:.2f}")
    print("-" * 30)
    print("✅ ¡Gracias por tu compra!\n")

def main():
    while True:
        limpiar_pantalla()
        print("🔢 CALCULADORA DE IVA 16%")
        try:
            monto = float(input("💸 Ingresa la cantidad de dinero: $"))
            iva, total = calcular_iva(monto)
            mostrar_ticket(monto, iva, total)
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingresa un número.")
        
        seguir = input("¿Deseas calcular otro monto? (s/n): ").strip().lower()
        if seguir != 's':
            print("\n👋 ¡Hasta luego!")
            time.sleep(1.5)
            break

if __name__ == "__main__":
    main()