"""
○​ Pedir al usuario que ingrese un número entero.
○​ El programa debe determinar y mostrar si el número es par o impar.
○​ Pista: Usar el operador módulo (%). numero % 2 == 0.
"""

# Ejercicio de par o impar

numero = int(input("Ingrese un número entero: "))

if numero % 2 != 0:
    print(f"\nEl número {numero} es impar.")
else:
    print(f"\nEl número {numero} es par.")

# Método de comprobación aplicando el principio de Guard Classes
