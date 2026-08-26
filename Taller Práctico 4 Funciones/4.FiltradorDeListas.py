"""
○​ Crea una función filtrar_aprobados que reciba una lista de notas y una
    nota de corte.
○​ Dentro de la función, crea una nueva lista vacía llamada aprobados.
 ○​ Itera sobre la lista de notas recibida. Si una nota cumple con la condición de
     aprobación, agrégala a la lista aprobados.
 ○​ Al final, la función debe retornar la lista aprobados.
 ○​ Ejemplo de uso: notas_curso = [4, 8, 10, 5, 7],
     aprobados_finales = filtrar_aprobados(notas_curso, 7).
     Imprime aprobados_finales (debería mostrar [8, 10, 7]).
"""

# nota = int(input("Introduzca su nota : "))

def filtrar_aprobados(notas_curso, nota_corte):

    lista_aprobados = []
    lista_desaprobados = []

    for nota in notas_curso:
        if nota >= nota_corte:
            lista_aprobados.append(nota)
        else:
            lista_desaprobados.append(nota)

    return lista_aprobados, lista_desaprobados

notas_curso = [4, 8, 10, 5, 7]
nota_corte = 7

aprobados_finales, desaprobados_finales  = filtrar_aprobados(notas_curso, nota_corte)

# Añadir estos resultados en la terminal más tarde
print(f"Aprobados {aprobados_finales}") 
print(f"Desaprobados {desaprobados_finales}")
