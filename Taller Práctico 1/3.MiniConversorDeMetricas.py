#Crea un programa que pida al usuario una distancia en kilómetros (que puede tener decimales) 
# y la convierta a millas. Sabiendo que 1 kilómetro es aproximadamente 0.621371 millas, 
# muestra el resultado de forma clara.

# Programa para convertir los kilometros a millas
distancia_km = float(input("Ingrese la distancia en kilómetros: "))
distancia_millas = distancia_km * 0.621371
print(f"\nLa distancia de {distancia_km} kilometros a millas es de : {distancia_millas:.2f}")

