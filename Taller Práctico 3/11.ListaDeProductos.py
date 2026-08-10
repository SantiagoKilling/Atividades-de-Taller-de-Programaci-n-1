"""
Tienes una lista de productos: inventario = ["manzana", "pan", "leche", "huevos", "pan", "pan", "agua"]. 
Se descubrió que todo el "pan" está en mal estado. 
No uses .count() o .remove() directamente. En su lugar, usa un bucle for para recorrer la lista
y un condicional if para encontrar cada elemento "pan". 
Cada vez que encuentres uno, imprimir "Producto dañado encontrado: pan" y eliminarlo de la lista usando
.remove().

(Pista: Esto puede tener un comportamiento inesperado al modificar la lista mientras
se itera. Es un buen desafío).

"""

# Recorrer la lista y eliminar el pan

inventario = ["manzana", "pan", "leche", "huevos", "pan", "pan", "agua"]

inventario_nuevo = []

for producto in reversed(inventario):
    if producto == "pan":
        print(f"Producto Dañado Encontrado : {producto}")
        inventario.remove(producto)

print(f"\nCatálogo actualizado : {inventario}")
"""
for medicion_valida in mediciones:
    if medicion_valida >= 0:
        mediciones_validas.append(medicion_valida)
"""

# print(f"La lista de mediciones válidas son : {mediciones_validas}")