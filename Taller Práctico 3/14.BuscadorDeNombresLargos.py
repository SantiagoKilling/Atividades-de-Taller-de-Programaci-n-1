"""
Buscador de nombres largos (Combinando for, if y .append()): Dada una lista de
nombres nombres = ["Ana", "Alejandro", "Eva", "Guillermo", "Lu"], crea una nueva
lista vacía llamada nombres_largos. Luego, recorre la lista original con un bucle for y,
si la longitud del nombre (usa len(nombre)) es mayor a 4 caracteres, agrega ese
nombre a la lista nombres_largos. Imprime el resultado.

"""

nombres = ["Ana", "Alejandro", "Eva", "Guillermo", "Lu"]
nombres_largos = []

for r in nombres:
    if len(nombres) > 4: 
        nombres_largos.append(r)

print(nombres_largos)