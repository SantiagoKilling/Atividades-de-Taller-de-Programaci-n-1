# Crea un programa que le pida al usuario la cantidad de predicciones correctas de un modelo
# y el total de predicciones realizadas. Luego, calcula y muestra la tasa de aciertos (accuracy)
# con la fórmula: accuracy = correctas / totales


# Programa para calcular la tasa de aciertos (Accuracy)

print("=== Calculadora de Tasa de Aciertos ===")

# Pedir al usuario la cantidad de predicciones correctas
correctas = int(input("Ingrese la cantidad de predicciones correctas: "))

# Pedir al usuario el total de predicciones realizadas
totales = int(input("Ingrese el total de predicciones realizadas: "))

# Calcular y mostrar la tasa de aciertos (accuracy)
if totales > 0:
    accuracy = correctas / totales
    print(f"\nTasa de Aciertos (Accuracy): {accuracy:.2%}")
else:
    print("Error: El total de predicciones realizadas no puede ser cero.")

# Opcional: Mostrar el resultado en formato más claro
print("\nResultado:")
print(f"Correctas: {correctas} / Totales: {totales}")
