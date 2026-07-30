"""
Pide una contraseña y verifica si tiene al menos 6 caracteres.
"""

# Generador de Contraseña de menos de 6 caracteres
contrasenia = input("Generar una contraseña de menos de 6 caracteres: ")

# Verificar si la contraseña tiene al menos 6 caracteres
if len(contrasenia) <= 6:
    print("Su contraseña es válida.")
else:
    print("La contraseña es inválida. Su contraseña tiene más de 6 caracteres.")

