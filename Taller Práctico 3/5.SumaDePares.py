"""
Suma de pares: Dada una lista de números numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
calcula e imprime la suma de solo los números pares de la lista.
"""

# Armar la lista de números 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Algoritmo para imprimir los números solamente pares 

numeros_pares = []

for numero in numeros: 
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(f"\nLos numeros pares son : {numeros_pares} ")
