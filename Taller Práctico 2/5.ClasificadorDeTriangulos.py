"""
○​ Pedir al usuario las longitudes de los tres lados de un triángulo.
○​ Primero, verificar si con esas longitudes se puede formar un triángulo (la
suma de dos lados cualquiera debe ser mayor que el tercero).
○​ Si se puede formar, determinar si es equilátero (tres lados iguales),
isósceles (dos lados iguales) o escaleno (ningún lado igual).
"""

# Ejercicio de clasificación de triángulos

# Solicitar al usuario que ingrese los longitudes de los 3 lados del triángulo

lado1 = float(input("Ingrese la longitud del primer lado del triangulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triangulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triangulo: "))

# Verificar si se puede formar un triángulo con las longitudes ingresadas
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Determinar que tipo de triángulo es
    if lado1 == lado2 == lado3:
        print("\nEl triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("\nEl triángulo es isósceles porque solo 2 lados son iguales.")
    else:
        print("\nEl triángulo es escaleno porque ningún lado es igual.")

else:
    print("\nNo se puede formar un triángulo con las longitudes ingresadas.")
