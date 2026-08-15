"""
 Validador de Datos Numéricos: Pide al usuario que ingrese una nota (de 0 a 10).
Usa un bucle while para asegurar que el número esté en ese rango. Si el usuario
ingresa un valor incorrecto, el programa debe volver a pedírselo con un mensaje de
error.

"""
# Solicitar al usuario que ponga una nota dentro de un rango comprendido

# Inicializar el programa con un dato inválido para que comience el bucle
dato_valido = False

while not dato_valido:
    dato_entrada = input("Ingrese una nota del 0 a 10 : ")

	# Verificamos si la entrada es un dato numérico usando is.digit()
    if dato_entrada.isdigit():
        nota = int(dato_entrada)

        # Validar el rango en el que vamos a estar operando
        if 0 <= nota <= 10:
           dato_valido = True
        else:
            print("Error : un número dentro del rango comprendido (entre 0 y 10) : ")
    else:
        print("Error : Debe ingresar un número válido sin letras...")
print(f"numero validado correctamente: {nota}")
