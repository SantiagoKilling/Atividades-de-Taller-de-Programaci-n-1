"""
Pide al usuario que ingrese su edad. El programa debe determinar si la persona es
mayor o igual a 18 años. Si lo es, mostrar el mensaje "Tienes edad suficiente para
obtener la licencia de conducir". De lo contrario, mostrar "Aún no tienes edad para
obtener la licencia de conducir".
"""

# Ejercicio de edad para licencia de conducir

# Solicitar al usuario que ingrese su edad
edadUsuario = int(input("Por favor, ingrese su edad: "))

# Verificar si la edad ingresada es mayor o igual a 18 años
if edadUsuario >= 18:
    print("\nTienes edad suficiente para obtener la licencia de conducir.")
else:
    print("\nAún no tienes edad para obtener la licencia de conducir.")

