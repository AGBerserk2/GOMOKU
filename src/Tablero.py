import os
BOARD_SIZE = 15 

def crear_tablero():
    return [["⬛" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def imprimir_tablero(tablero, cursor_x, cursor_y,jugador_actual):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Usa flechas para moverte y ENTER/ESPACIO para colocar ficha.")
    print("   " + " ".join([f"{i:2}" for i in range(BOARD_SIZE)]))
    for i in range(BOARD_SIZE):
        fila = ""
        for j in range(BOARD_SIZE):
            if i == cursor_x and j == cursor_y:
                fila += jugador_actual 
            else:
                fila += f"{tablero[i][j]}"
        print(f"{i:2} {fila}")
