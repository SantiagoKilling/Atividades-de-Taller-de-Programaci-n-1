"""
Aplicar descuento (Combinando for e if): Tenemos una lista de precios:
precios_originales = [100, 50, 200, 80, 150]. Queremos crear una nueva lista llamada
precios_con_descuento. Usa un bucle for para recorrer precios_originales. Si un
precio es de $100 o más, aplícale un 10% de descuento (precio * 0.9) y agrégalo a la
nueva lista. Si no, agrega el precio original sin cambios. Finalmente, imprime ambas
listas.

"""

# Categorizar y aplicar descuentos según corresponda 

precios_originales = [100, 50, 200, 80, 150]
precios_con_descuento = []
descuento = 0.9

for precio in precios_originales:
    if precio > 100:
        precio_final = precio * descuento
    else:
        precio_final = precio

    precios_con_descuento.append(precio_final)

print(f"Imprimeindo la lista de precios originales : {precios_originales}")
print(f"Imprimeindo la lista de precios con descuento : {precios_con_descuento}")