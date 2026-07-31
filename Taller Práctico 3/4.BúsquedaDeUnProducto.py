"""
Dada la lista productos = ["leche", "pan", "huevo", "queso"], 
escribe un código que le pida al usuario que ingrese un producto.
Tu programa debe indicar si el producto está en la lista o no. (Pista: if
producto_usuario in productos:).
"""

#Buscar si el producto está o no en la lista

listaProductos = ["leche", "pan", "huevo", "queso"]

#Pedirle al usuario que escriba un producto a ver si está o no
producto_usuario = str(input("Por favor escriba su producto : ").lower().strip())

if producto_usuario in listaProductos:
    print("Tu producto está en la lista")
else:
    print("Tu producto NO está en la lista")