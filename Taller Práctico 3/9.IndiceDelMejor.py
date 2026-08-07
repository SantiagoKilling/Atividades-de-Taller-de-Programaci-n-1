"""
Índice del mejor: Dada una lista de puntajes puntajes = [88, 95, 72, 100, 91, 85]
y una lista paralela de jugadores jugadores = ["Ana", "Juan", "Sofía", "Luis", "Carlos", "Marta"], 
encuentra el puntaje más alto y muestra el nombre del jugador que lo obtuvo. 
(Pista: primero encuentra el puntaje máximo  y  luego  busca su índice 🛒  con el  método  .index()).
"""

# Encontrar el puntaje más alto y su correspondiente jugador 

puntajes = [88, 95, 72, 100, 91, 85]
jugadores = ["Ana", "Juan", "Sofía", "Luis", "Carlos", "Marta"]

mejor_puntaje = max(puntajes)

# De esta manera logramos averiguar cuál es el mayor puntaje de la lista
# Como la lista de puntaje corre en paralelo a la de los nombre es fácil averiguar a quien le corresponde

# Vamos a apuntar a Luis que suponemos que es el que tiene el mejor puntaje

indice = puntajes.index(mejor_puntaje)
nombre_ganador = jugadores[indice]
print(f"El mayor puntaje es de : {mejor_puntaje} y le corresponde a {nombre_ganador}")