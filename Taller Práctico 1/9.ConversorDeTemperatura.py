"""
Pide una temperatura en °C y conviértela a °F.
"""

#Conversor de Temperatura de Celsius a Fahrenheit

# Solicitar al usuario la temperatura en grados Celsius
temperatura_En_Celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir la temperatura a grados Fahrenheit usando la fórmula: (°C * 9/5) + 32
temperatura_En_Fahrenheit = (temperatura_En_Celsius * 9/5) + 32

print(f"\nLa temperatura de {temperatura_En_Celsius}°C es equivalente a {temperatura_En_Fahrenheit:.2f}°F.")
