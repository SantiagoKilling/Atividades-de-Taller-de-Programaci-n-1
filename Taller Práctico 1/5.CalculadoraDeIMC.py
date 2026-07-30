"""
El Índice de Masa Corporal (IMC) se usa en medicina para evaluar el estado nutricional.
Crea una calculadora que:

    1. Pida al usuario su peso en kilogramos (puede tener decimales).
    2. Pida al usuario su altura en metros (puede tener decimales, ej: 1.75).
    3. Calcule el IMC usando la fórmula: IMC = peso / (altura * altura).
    4. Muestre el resultado en un mensaje bien formateado usando un f-string, como: "Para
    un peso de 70.5 kg y una altura de 1.75 m, su IMC es de 23.02."
"""

#Programa para calcular el IMC
peso_Del_Usuario = float(input("Ingrese su peso en kilogramos (ej: 70.5): "))
altura_Del_Usuario = float(input("Ingrese su altura en metros (ej: 1.75): "))

# Calcular el IMC
imc = peso_Del_Usuario / (altura_Del_Usuario * altura_Del_Usuario)
print(f"\nPara un peso de {peso_Del_Usuario} kg y una altura de {altura_Del_Usuario} m, su IMC es de {imc:.2f}.")

