"""
○​ Crea una función verificar_aprobacion que reciba una nota y una
    nota_de_corte (por ejemplo, 7).
○​ La función debe retornar True si la nota es mayor o igual a la nota de corte,
    y False en caso contrario.
○​ Llama a la función con una nota de 4 y otra de 9, e imprime los resultados
    booleanos (True/False).
"""



nota_de_corte = 7

def verificar_aprobacion(nota_usuario, nota_de_corte):
    if nota_usuario >= nota_de_corte:
        return True
    else:
        return False

nota_usuario = int(input("Introduzca su nota : "))

validador = verificar_aprobacion(nota_usuario, nota_de_corte)

print(f"¿El estudiante fue aprobado? : {validador}")