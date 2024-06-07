Tablero = [" " for p in range(9)]

def primir_tablero():
    for p in range(3):
        fila = f" | {Tablero[p*3]} | {Tablero[p*3 + 1]} | {Tablero[p*3 + 2]} | "
        print(fila)

def ganador():
    for p in range(0, 9, 3):
        if Tablero[p] == Tablero[p + 1] == Tablero[p + 2] != " ":
            return True
   
    for p in range(3):
        if Tablero[p] == Tablero[p + 3] == Tablero[p + 6] != " ":
            return True

    if Tablero[0] == Tablero[4] == Tablero[8] != " " or Tablero[2] == Tablero[4] == Tablero[6] != " ":
        return True
    return False

def verificar_empate():
    return " " not in Tablero

def jugadores(turno, nombre_jugador):
    print(f"\nTurno de {nombre_jugador}")
    while True:
        try:
            eleccion = int(input("Ingrese su movimiento (1-9):\n ").strip())
            if eleccion >= 1 and eleccion <= 9:
                if Tablero[eleccion - 1] == " ":
                    Tablero[eleccion - 1] = turno
                    break
                else:
                    print("Casilla ocupada, inténtelo de nuevo.")
            else:
                print("Ingrese un número del 1 al 9.")
        except ValueError:
            print("Movimiento inválido.")

nombre_jugador1 = input("Ingrese el nombre del Jugador 1:\n ")
nombre_jugador2 = input("Ingrese el nombre del Jugador 2:\n ")

while True:
    primir_tablero()
    jugadores("x", nombre_jugador1)
    if ganador():
        primir_tablero()
        print(f"¡{nombre_jugador1} ha ganado!")
        break
    
    elif verificar_empate():
        primir_tablero()
        print(f"¡Empate entre {nombre_jugador1} y {nombre_jugador2}!")
        break

    primir_tablero()
    jugadores("o", nombre_jugador2)
    if ganador():
        primir_tablero()
        print(f"¡{nombre_jugador2} ha ganado!")
        break
    
    elif verificar_empate():
        primir_tablero()
        print(f"¡Empate entre {nombre_jugador1} y {nombre_jugador2}!")
        break