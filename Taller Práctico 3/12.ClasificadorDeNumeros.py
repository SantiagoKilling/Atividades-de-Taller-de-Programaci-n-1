"""
 Clasificador de números (Combinando for e if/elif/else): Dada una lista de número,
numeros = [15, 7, -2, 0, 12, -5, 0, 8], itera sobre cada número y clasifícalo usando
condicionales (if, elif, else) en tres categorías:

- Positivo mayor a 10
- Cero
- Cualquier otro número (que serían los positivos <=10 y los negativos.

Imprime un mensaje para cada número, por ejemplo: "15 es Positivo mayor a 10", "0
es Cero", "-5 es Otro".

"""
# Armar un clasficador de números

numeros = [15, 7, -2, 0, 12, -5, 0, 8]
resultados = []

for clasificador in numeros:
    if clasificador > 10:
        mensaje = f"El numero : {clasificador} es positivo mayor a 10"
    elif clasificador == 0:
        mensaje = f"El numero {clasificador} es cero"
    else:
        mensaje = f"Tanto los positivos y negativos a 10 caen acá : {clasificador}"

    resultados.append(mensaje)

for r in resultados:
    print(r)

"""
numeros = [15, 7, -2, 0, 12, -5, 0, 8]
# 1. Creamos una lista para guardar los resultados
resultados = []

# 2. Usamos un nombre descriptivo para el elemento (ej: 'numero')
for numero in numeros:
    if numero > 10:
        mensaje = f"{numero} es Positivo mayor a 10"
    elif numero == 0:
        mensaje = f"{numero} es Cero"
    else:
        mensaje = f"{numero} es Otro"

    # 3. Guardamos el mensaje en nuestra lista
    resultados.append(mensaje)

# 4. Mostramos el resultado final
for r in resultados:
    print(r)
"""