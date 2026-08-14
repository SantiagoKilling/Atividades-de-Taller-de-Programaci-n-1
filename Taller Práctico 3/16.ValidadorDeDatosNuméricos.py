"""
 Validador de Datos Numéricos: Pide al usuario que ingrese una nota (de 0 a 10).
Usa un bucle while para asegurar que el número esté en ese rango. Si el usuario
ingresa un valor incorrecto, el programa debe volver a pedírselo con un mensaje de
error.

"""
# Solicitar al usuario que ponga una nota dentro de un rango comprendido

# Inicializar el programa con un dato inválido para que comience el bucle
dato_invalido = -1

while not (0 <= dato_invalido <= 10):
    nota_usaurio = int(input("Ingrese una nota del 0 a 10 : "))

	# Verificamos si la entrada es un dato numérico
    if nota_usaurio.isdigit():
        edad = int(nota_usaurio)
    else:
        print("Error : un número dentro del rango comprendido")
print(f"numero validado correctamente: ")
