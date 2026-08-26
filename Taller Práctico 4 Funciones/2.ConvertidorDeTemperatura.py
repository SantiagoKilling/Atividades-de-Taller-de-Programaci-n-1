"""
○​ Crea una función celsius_a_fahrenheit que reciba una temperatura en
    grados Celsius.
○​ Dentro de la función, aplica la fórmula: F = (C * 9/5) + 32.
○​ La función debe retornar la temperatura calculada en Fahrenheit.
○​ Pruébala con varios valores (ej. 0°C, 25°C, 100°C) e imprime los resultados.
"""

C = int(input("Ponga su temperatura en grados Celsius : "))

def celsius_a_farenheit():
    F = (C * 9/5) + 32
    return print(f"tu temperatura de celsius a farenheit es de : {F}")

celsius_a_farenheit()