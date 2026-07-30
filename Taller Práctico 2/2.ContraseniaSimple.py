"""
○​ Guardar una contraseña en una variable (ej: contraseña_guardada =
"Python123").
○​ Pedir al usuario que ingrese la contraseña.
○​ Si la contraseña ingresada es correcta, mostrar "Acceso concedido". Si no,
mostrar "Contraseña incorrecta".

"""

# Generador de contraseñas simples

contrasenia_guardada = "Python123"

# Solicitar al usuario que ingrese su contraseña
contrasenia_Usuario = str(input("Ingrese su contraseña: "))

# Verificar si la contraseña ingresada matchea con la contraseña guardada
if contrasenia_Usuario == contrasenia_guardada:
    print("\nAcceso concedido.")
else:
    print("\nLas contraseñas no coinciden, por favor intentelo de nuevo.")

