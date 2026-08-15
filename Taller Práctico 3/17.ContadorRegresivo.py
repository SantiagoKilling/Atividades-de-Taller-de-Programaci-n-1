"""
 Contador Regresivo: Pide al usuario un número. Usa un bucle while para imprimir
una cuenta regresiva desde ese número hasta 1, y al final, imprimir "¡Despegue!".
"""

# Contador del cohete

contador_usuario = int(input("Por favor, introduzca un número : "))

while contador_usuario > 0:
    print(contador_usuario)
    contador_usuario -= 1
print("Despegue!")