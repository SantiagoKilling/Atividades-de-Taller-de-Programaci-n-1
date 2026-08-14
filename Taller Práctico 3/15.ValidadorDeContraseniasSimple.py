"""
 Validador de contraseñas simple (Combinando for, if/else): Pídele al usuario que
ingrese una contraseña. 
Luego, usando un bucle for, recorre cada carácter de la contraseña ingresada y verifica si es un número (usando caracter in "0123456789").
Si encuentras al menos un número, imprime "La contraseña contiene al menos un
número.". Si después de recorrer toda la contraseña no encontraste ningún número,
imprime "La contraseña no contiene números. Es débil.".

"""

# Validar la contraseña

contrasenia_usaurio = input("Ingrese su contraseña : ")

if len(contrasenia_usaurio) == 0:
    print("Por favor, ponga una contraseña")
else:
    tiene_numero = False

    for validador in contrasenia_usaurio:
        if validador.isdigit():
            tiene_numero = True

    if tiene_numero:
        print("La contraseña tiene al menos un número")
    else:
        print("La contraseña no contiene al menos un número. Es débil")

# Para darle más robustez al código podría pedirle al usaurio que si o si ponga algo en el campo 
