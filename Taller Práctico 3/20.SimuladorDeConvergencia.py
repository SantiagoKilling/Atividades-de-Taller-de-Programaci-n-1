"""
Simulación de Convergencia: Un modelo de Machine Learning simple ajusta un
parámetro llamado peso para minimizar el error.
○​ Inicializa peso = 0.5 y error = 100.
○​ Establece una tasa_aprendizaje = 0.1.
○​ Usa un bucle while que se ejecute mientras error > 1.
○​ Dentro del bucle:
    1.​ "Ajusta" el peso: peso = peso * (1 + tasa_aprendizaje).
    2.​ "Recalcula" el error: error = error / 1.1 (una forma simple de
    simular que baja).
    3.​ Imprime el número de iteración, el nuevo peso y el error.
○​ Este ejercicio simula cómo un algoritmo iterativamente se acerca a una
solución.
"""

peso = 0.5
error = 100
tasa_aprendizaje = 0.1
iteracion = 0

while error > 1:
    # Actualizar los parámetros de la red
    peso = peso * (1 + tasa_aprendizaje)
    error = error / 1.1
    iteracion += 1
    print(f"Iteración {iteracion}: Peso = {peso:.4f}, Error = {error:.2f}")

print("\n¡El modelo ha convergido!")
