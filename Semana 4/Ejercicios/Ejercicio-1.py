# Programa para jugar piedra papel o tijeras con posibilidad de escoger la cantidad de rondas a jugar.

# Pedimos la cantidad de rondas que se desea jugar
rondas = int(input("Indique cantidad de rondas a jugar: "))

# Creamos una variable para almacenar el resultado total del juego
resultado_final = 0

# Creamos un ciclo while para cada ronda (esto también se podría hacer con un ciclo for pero no se si lo han pasado aún)
while (rondas > 0):

    # Fijamos el resultado de la ronda en el valor 0 (el cero lo tomamos como neutral)
    resultado_ronda = 0

    # Creamos un ciclo while para asegurarnos de que hay un ganador en cada ronda
    while (resultado_ronda == 0):

        # Pedimos a los jugadores que ingresen sus elecciones de jugada
        j1 = input("Ingrese la elección del jugador 1: ")
        j2 = input("Ingrese la elección del jugador 2: ")

        # Preguntamos si el jugador 1 ganó con la sentencia lógica correspondiente
        if ((j1 == "piedra" and j2 =="tijera") or (j1 =="papel" and j2 == "piedra") or (j1 == "tijera" and j2 == "papel")):
            print("El jugador 1 ha ganado esta ronda")
            resultado_ronda = -1

        # Preguntamos si el jugador 2 ganó con la sentencia lógica correspondiente
        elif ((j2 == "piedra" and j1 =="tijera") or (j2 =="papel" and j1 == "piedra") or (j2 == "tijera" and j1 == "papel")):
            print("El jugador 2 ha ganado esta ronda")
            resultado_ronda = 1

        # Si ninguno de los jugadores ganó la ronda se declara empate de la ronda (Notar que en este caso no se cambia el valor de la variable resultado_ronda)
        else:
            print("Empate, se repite la ronda.")
        
        # Se integra el resultado de la ronda al resultado final del juego completo (en caso de que haya sido empate, se le suma 0 al resultado_final por lo que no hay cambios)
        resultado_final += resultado_ronda
    
    # Una vez declarado el ganador de la ronda, se resta 1 al número de rondas que falta por jugar
    rondas-=1

# Luego de terminar todas las rondas se evalua el valor de la variable resultado_final para determinar el resultado del juego
if (resultado_final < 0):
    print("El jugador 1 es el ganador del juego.")
elif (resultado_final > 0):
    print("El jugador 2 es el ganador del juego.")
else:
    print("Ambos jugadores ganaron la misma cantidad de rondas por lo que se declara un empate.")