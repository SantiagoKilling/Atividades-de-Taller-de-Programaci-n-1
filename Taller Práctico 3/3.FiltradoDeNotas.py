"""
Filtrado de notas: Dada la lista notas = [4, 7, 2, 9, 5, 10, 8], crea una
nueva lista llamada aprobados que contenga solo las notas mayores o iguales a 7.
Deberás usar un bucle for y un condicional if.
"""
#Lista de notas
listaDeNotas = [4, 7, 2, 9, 5, 10, 8]
notaDeCorte = 7

notaDeAprobados = []
notaDeDesaprobados = []

for nota in listaDeNotas:
    if nota >= notaDeCorte:
        print(f"Nota es {nota}: Aprobado")
        notaDeAprobados.append(nota)
    else:
        print(f"Nota es {nota}: Desaprobado")
        notaDeDesaprobados.append(nota)

#Mostrar los resultados finales
print("\n---Resultados De las notas---")
print(f"Resultados de los aprobados : {notaDeAprobados} ")
print(f"Resultados de los desaprobados : {notaDeDesaprobados} ")