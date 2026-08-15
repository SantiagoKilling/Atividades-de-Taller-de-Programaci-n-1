"""
 Limpieza de Datos Erróneos: Tienes una lista de mediciones con errores al final:
datos_sensor = [25.1, 24.8, 25.0, 24.9, 999, 999], donde 999 es un
error. Usa un bucle while para eliminar todos los errores del final de la lista. La
condición podría ser while datos_sensor[-1] == 999:. (Pista: usa .pop()).

"""

datos_sensor = [25.1, 24.8, 25.0, 24.9, 999, 999]

while datos_sensor[-1] == 999:
    datos_sensor.pop()
    print(f"Procesando datos de la lista... : {datos_sensor}")
    break



"""
mediciones = [8.5, 9.1, 7.8, -1.0, 6.5, 8.8]

while len(mediciones) > 0:
    medicion = mediciones.pop(0)

    if medicion == -1.0:
        print("Fin de la transmisión")
        break
    else:
        print(f"Procesando medición : {medicion}")
"""