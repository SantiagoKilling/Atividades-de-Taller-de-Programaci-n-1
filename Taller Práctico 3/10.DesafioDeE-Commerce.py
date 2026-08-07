"""
Desafío  de  E-commerce

🛒: Tienes  dos  listas:  productos = ["Camiseta",
"Pantalón", "Zapatillas", "Gorra"] precios = [25.00, 40.00, 80.00, 15.00]​

Escribe un programa que haga lo siguiente: 
a. Muestre al usuario una lista de los
productos con su precio al lado (ej: "1. Camiseta - $25.00"). 
b. Calcule y muestre el
costo total del inventario (la suma de todos los precios). 
c. Encuentre y muestre el
nombre del producto más caro y el más barato.

"""
productos = ["Camiseta", "Pantalón", "Zapatillas", "Gorra"]
precios = [25.00, 40.00, 80.00, 15.00]

# Mostrar el output del inventario de los productos y los precios

print("""
---Inventario---
""")
for x in range(len(productos)): 
    print(f"{x + 1}. {productos[x]} - ${precios[x]:.2f}")


total = sum(precios)
print(f"El total de la suma de los productos es {total}")

# Buscar el precio más caro de la lista y relacionarlo con la persona de la lista paralela
precio_mas_caro = max(precios)
indice_caro = precios.index(precio_mas_caro)
nombre_caro = productos[indice_caro]
print(f"El producto más caro es de {nombre_caro}")

precio_barato = min(precios)
indice_barato = precios.index(precio_barato)
nombre_barato = productos[indice_barato]
print(f"El producto más barato es de {nombre_barato}")