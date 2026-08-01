"""
Eliminar los "malos": Dada una lista de mediciones mediciones = [8.5, 9.1, -1.0, 7.8, 6.5, -1.0, 8.8], 
donde -1.0 representa un error, crea una
nueva lista llamada mediciones_validas que contenga todas las mediciones
excepto los errores. Luego, calcula el promedio de las mediciones válidas.
"""

# Excluir los números inválidos y promediar los que corresponden

mediciones = [8.5, 9.1, -1.0, 7.8, 6.5, -1.0, 8.8]

# Crear la lista vacía 
mediciones_validas = []

for medicion_valida in mediciones:
    if medicion_valida >= 0:
        mediciones_validas.append(medicion_valida)

print(f"La lista de mediciones válidas son : {mediciones_validas}")

# Armar la lista promedio
promedio = sum(mediciones_validas)/len(mediciones_validas)
print(f"El promedio de la lista es {promedio:.2f}")