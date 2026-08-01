"""
Contador de vocales: Crea un programa que, dada una palabra (por ejemplo,
palabra = "universidad"), cuente cuántas vocales (a, e, i, o, u) tiene.
Deberás iterar sobre cada letra de la palabra y usar un contador.
"""

# Contador de vocales

palabra_del_usuario = input("Por favor, introduzca su palabra : ").lower()
vocales = "aeiouáéíóú"
contador = 0

for letra in palabra_del_usuario:
    if letra in vocales:
        contador += 1

print(f"Tu palabra cuenta con : {contador} vocales")
