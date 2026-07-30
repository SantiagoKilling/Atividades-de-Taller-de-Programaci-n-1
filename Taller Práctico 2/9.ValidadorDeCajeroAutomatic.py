"""
Simula una transacción de un cajero automático.
    1.​ Define una variable con un saldo inicial (ej: saldo = 1000).
    2.​ Define una variable con un PIN secreto (ej: pin_correcto = "1234").
    3.​ Pide al usuario que ingrese su PIN.
    4.​ Si el PIN es correcto, pide al usuario que ingrese la cantidad de dinero a
    retirar.
    5.​ Luego, verifica si la cantidad a retirar es menor o igual al saldo disponible y
    si es un monto positivo.

    ■​ Si ambas condiciones se cumplen, resta el monto del saldo, y
muestra "Retiro exitoso. Tu nuevo saldo es: [nuevo_saldo]".
    ■​ Si la cantidad es mayor que el saldo, muestra "Fondos insuficientes".
    ■​ Si la cantidad es un número negativo o cero, muestra "Monto no
válido".

    6.​ Si el PIN está incorrecto, muestra "PIN incorrecto. Operación cancelada".
"""

# Ejercicio de simulación de transacción de cajero automático

# Definir el saldo inicial y el PIN secreto
saldo = 1000
pin_correcto = 1234

# Solicitar al usuario que ingrese su PIN
pin_ingresado = int(input("Ingrese su PIN: "))

# Verificar si el PIN ingresado es el correcto
if pin_ingresado == pin_correcto:
    # Solicitar al usuario que ingrese la cantidad de dinero a retirar
    monto_a_retirar = float(input("Ingrese la cantidad de dinero a retirar: "))

    if monto_a_retirar <= saldo and monto_a_retirar > 0:
        print(f"\nRetiro exitoso. Tu nuevo saldo es: {saldo - monto_a_retirar:.2f}")
    elif monto_a_retirar > saldo :
        print("Fondos insuficientes.")
    else:
        print("\nMonto no válido.")
else:
    print("\nPIN incorrecto. Operación cancelada.")