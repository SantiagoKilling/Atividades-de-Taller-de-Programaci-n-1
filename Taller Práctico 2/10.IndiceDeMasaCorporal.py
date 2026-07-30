"""
Pide al usuario su peso en kilogramos (kg) y su altura en metros (m).
1.​ Calcula el Índice de Masa Corporal (IMC) usando la fórmula:
IMC = peso(kg) / altura(m)^2
2.​ Clasifica el resultado y muestra un mensaje según la siguiente tabla de la
OMS:
■​ Menos de 18.5: "Bajo peso"
■​ 18.5 a 24.9: "Peso normal"
■​ 25.0 a 29.9: "Sobrepeso"
■​ 30.0 o más: "Obesidad"

"""
peso = float(input("Ingrese su peso en Kilogramos (kg): "))
altura = float(input("Ingrese su altura en metros (m): "))

# 1. Aduana: Validar que no haya división por cero y datos absurdos
if altura <= 0 or peso <= 0:
    print("\nError: Peso y altura deben ser mayores a cero.")
else:
    imc = peso / (altura ** 2)

    if imc < 18.5:
        print(f"\nSu IMC es: {imc:.2f}. Bajo peso.")
    elif 18.5 <= imc <= 24.9:
        print(f"\nSu IMC es: {imc:.2f}. Peso normal.")
    elif 25.0 <= imc <= 29.9:
        print(f"\nSu IMC es: {imc:.2f}. Sobrepeso.")
    elif imc >= 30.0:
        print(f"\nSu IMC es: {imc:.2f}. Obesidad.")
