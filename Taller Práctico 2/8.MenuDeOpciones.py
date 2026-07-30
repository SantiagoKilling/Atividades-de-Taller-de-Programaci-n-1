import datetime
"""
# Muestra al usuario un menú simple con 4 opciones:
    ○​ Saludar
    ○​ Despedirse
    ○​ Mostrar la hora
    ○​ Salir
Pide al usuario que elija una opción ingresando un número del 1 al 4.

Sugerencia: Resuelve este ejercicio utilizando la estructura match-case para
manejar la opción elegida por el usuario. Incluye un case _: para gestionar
cualquier entrada no válida.

    ○​ case 1: mostrará "¡Hola! Bienvenido al programa."
    ○​ case 2: mostrará "¡Adiós! Gracias por usar el programa."
    ○​ case 3: (opcionalmente) puedes usar el módulo datetime de Python para mostrar la hora actual.
    ○​ case 4: mostrará "Saliendo del programa..."
"""
# Ejercicio de menú de opciones

# Solicitar al usuario que elija una opción del menú

print("""
---Menú de Opciones---
1. Saludar
2. Despedirse
3. Mostrar la hora
4. Salir
""")

MenuDeOpciones = int(input("Ingrese una opción del menú (1-4): "))


# Usar match-case para manejar la opción elegida por el usuario
match MenuDeOpciones:
    case 1:
        print("\n¡Hola! Bienvenido al programa.")
    case 2:
        print("\n¡Adiós! Gracias por usar el programa.")
    case 3:
        fecha = datetime.datetime.now()
        print(f"\nLa hora actual es: {fecha.strftime('%H:%M:%S')}")
    case 4:
        print("\nSaliendo del programa...")
    case _:
        print("\nError: Opción no válida. Por favor, ingrese un número del 1 al 4.")

