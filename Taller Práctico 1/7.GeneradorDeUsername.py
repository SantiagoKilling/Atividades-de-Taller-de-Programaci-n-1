"""
Pide el nombre y apellido del usuario y genera un username combinando partes de ambos.
"""

# Generador de Username

# Solicitar al usuario nombre y apellido
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Generar el username combinando las letras del nombre y apellido
username = nombre[:4].lower() + apellido[:4].lower()
print(f"\nSu username generado es: {username}")
