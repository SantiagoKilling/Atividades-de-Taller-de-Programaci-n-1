"""
○​ Pedir al usuario que ingrese un año.
○​ Determinar si el año es bisiesto. Un año es bisiesto si es divisible por 4,
excepto si es divisible por 100, a menos que también sea divisible por 400.
○​ Pista: Este es un excelente ejercicio para anidar condiciones o usar and y
or. (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
"""
# Ejercicio de año bisiesto

# Solicitar al usuario que ingrese un año
anioUsuario = int(input("Ingrese un número de año: "))

# Verificar si el año ingresado es bisiesto
if (anioUsuario % 4 == 0 and anioUsuario % 100 != 0) or (anioUsuario % 400 == 0):
    print(f"\nEl año {anioUsuario} es bisiesto.")
else:
    print(f"\nEl año {anioUsuario} no es bisiesto.")
    