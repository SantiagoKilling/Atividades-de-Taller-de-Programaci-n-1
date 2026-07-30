"""
○​ Pedir al usuario dos números.
○​ Pedir al usuario que ingrese una operación ("+", "-", "*" o "/").
○​ Usando if/elif/else, realizar el cálculo correspondiente y mostrar el
resultado.
○​ Incluir un else final para el caso en que la operación no sea válida.

"""
# Ejercicio de calculadora básica

# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Solicitar al usuario que ingrese la operación a realizar
operacionAritmetica = str(input("Ingrese la operación a realizar (+, -, *, /): "))

# Realizar la operación correspondiente según la entrada del usuario
if operacionAritmetica == "+":
    resultado = numero1 + numero2
    print(f"\nEl resultado de {numero1} + {numero2} es: {resultado:.2f}")
elif operacionAritmetica == "-":
    resultado = numero1 - numero2
    print(f"\nEl resultado de {numero1} - {numero2} es: {resultado:.2f}")
elif operacionAritmetica == "*":
    resultado = numero1 * numero2
    print(f"\nEl resultado de {numero1} * {numero2} es: {resultado:.2f}")
elif operacionAritmetica == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"\nEl resultado de {numero1} / {numero2} es: {resultado:.2f}")
    else:
        print("\nError: No se puede dividir entre cero.")

