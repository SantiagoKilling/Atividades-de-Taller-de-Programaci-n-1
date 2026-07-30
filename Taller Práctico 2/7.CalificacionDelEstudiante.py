"""
Pide al usuario que ingrese una calificación numérica (0-100). El programa debe
mostrar la letra correspondiente a esa calificación según la siguiente escala:
    ​○​ 90-100: "A (Excelente)"
    ○​ 80-89: "B (Muy Bueno)"
    ○​ 70-79: "C (Bueno)"
    ○​ 60-69: "D (Suficiente)"
    ○​ 0-59: "F (Insuficiente)"

    Pista: Este es un ejercicio ideal para usar operadores lógicos (and) para definir los
rangos en cada condición: if calificacion >= 90 and calificacion <=
100:.
"""
# Ejercicio de calificación del estudiante

calificacion = int(input("Ingrese la calificación numérica (0-100): "))

# Procesar la calificación y mostrar la letra correspondiente según la escala
if calificacion >= 90 and calificacion <= 100:
        print("\nLa calificación es: A (Excelente)")
elif calificacion >= 80 and calificacion <= 89:
        print("\nLa calificación es: B (Muy Bueno)")
elif calificacion >= 70 and calificacion <= 79:
        print("\nLa calificación es: C (Bueno)")
elif calificacion >= 60 and calificacion <= 69:
        print("\nLa calificación es: D (Suficiente)")
elif calificacion >= 0 and calificacion <= 59:
        print("\nLa calificación es: F (Insuficiente)")
else:
    print("\nError: La calificación ingresada no es válida. Debe estar entre 0 y 100.")
    