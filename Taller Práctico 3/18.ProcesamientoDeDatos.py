"""
 Procesamiento de Datos en "Stream": Simula que recibes datos de un sensor en
una lista: mediciones = [8.5, 9.1, 7.8, -1.0, 6.5, 8.8]. 
El valor -1.0 es una señal de "fin de transmisión". 
Usa un bucle while y el método .pop(0) para
procesar (imprimir) cada medición hasta que te encuentres con el valor -1.0 o la
lista se vacíe.
"""

mediciones = [8.5, 9.1, 7.8, -1.0, 6.5, 8.8]

while len(mediciones) > 0:
    medicion = mediciones.pop(0)

    if medicion == -1.0:
        print("Fin de la transmisión")
        break
    else:
        print(f"Procesando medición : {medicion}")