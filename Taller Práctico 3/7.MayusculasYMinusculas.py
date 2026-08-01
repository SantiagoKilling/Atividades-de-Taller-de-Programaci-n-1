"""
Dada una lista de nombres nombres = ["Ana", "juan", "SOFIA", "luis"], 
crea una nueva lista llamada
nombres_formateados donde cada nombre comience con mayúscula y el resto
en minúscula. 
(Pista: los strings tienen un método útil llamado .capitalize()).
"""

# Normalizar mayúsculas y minúsculas

nombres = ["Ana", "juan", "SOFIA", "luis"]

nombres_formateados = []

for capitalizacion in nombres:
    nombres_capitalizados = capitalizacion.capitalize()
    nombres_formateados.append(nombres_capitalizados)
print(nombres_formateados)
