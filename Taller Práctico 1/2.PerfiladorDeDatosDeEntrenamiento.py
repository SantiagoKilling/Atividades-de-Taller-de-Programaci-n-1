# Crea un programa que solicite el nombre de un dataset (ej: "Imágenes de Gatos"), la
# cantidad de imágenes que contiene y el tamaño total del dataset en Gigabytes (GB).
# Muestra un resumen bien formateado con toda la información

imagenes_De_Datos = input("Ingrese el nombre del dataset (ej: 'Imágenes de Gatos'): ")
cantidad_De_Imagenes = int(input("Ingrese la cantidad de imagenes que contiene el dataset: "))
totalSize_Del_Dataset = float(input("Ingrese el tamaño total del dataset en Gigabytes (GB): "))

print("\n=== Resumen del Dataset ===")
print(f"Nombre del dataset: {imagenes_De_Datos}")
print(f"Cantidad de imágenes: {cantidad_De_Imagenes}")
print(f"Tamaño total del dataset: {totalSize_Del_Dataset} GB")

