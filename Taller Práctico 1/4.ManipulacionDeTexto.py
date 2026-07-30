"""
Crea un programa que pida al usuario su nombre completo y una frase que describa su
interés en la IA. El programa debe imprimir:

    1. Un saludo de bienvenida usando el nombre con todas sus letras en mayúsculas.
    2. La frase de interés con todas sus letras en minúsculas.
    3. El número de caracteres que tiene su nombre (Pista: usa la función len(). Ej:
len(mi_variable)).
"""

# Solicitar al usuario su nombre completo
nombre_completo = input("Ingrese su nombre completo: ")

# Solicitar al usuario una frase que describa su interés en la IA
frase_De_Interes = input("Ingrese una frase que describa su interés en el campo de la IA: ")

# Imprimir el numero de caracteres que tiene el nombre completo
numero_De_Caracteres = len(nombre_completo)
print(f"\nEl número de caracteres que tiene su nombre completo es: {numero_De_Caracteres}")
