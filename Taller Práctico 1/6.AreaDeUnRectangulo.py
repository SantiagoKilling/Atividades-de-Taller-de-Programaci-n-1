"""
Calculadora de Área de un Rectángulo: Pide al usuario el largo y ancho de un rectángulo
(en metros). Calcula y muestra el área.
"""
# Programa para calcular el área de un rectángulo
# Soliciar el largo (base) del rectángulo al usuario
largo = float(input("Ingrese el largo del rectángulo en metros: "))

# Solicitar el ancho (altura) del rectángulo al usuario
ancho = float(input("Ingrese el ancho del rectángulo en metros: "))

# Calcular el área del rectángulo usando la fórmula : Base * Altura
areaDelRectangulo = largo * ancho
print(f"El área del rectángulo es de {areaDelRectangulo:.2f} metros cuadrados.")

