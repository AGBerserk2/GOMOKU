import os
import keyboard
from Logica import verificar_victoria
from Movimiento import movimiento_valido, colocar_pieza
from Tablero import imprimir_tablero, crear_tablero

BOARD_SIZE = 15

def jugar():
    tablero = crear_tablero()
    jugador_actual = "🟡"
    cursor_x, cursor_y = BOARD_SIZE // 2, BOARD_SIZE // 2

    while True:
        imprimir_tablero(tablero, cursor_x, cursor_y,jugador_actual)
        keyboard.read_event() # Esperar una tecla para evitar saltos rápidos
        if keyboard.is_pressed('up') and cursor_x > 0:
            cursor_x -= 1
        elif keyboard.is_pressed('down') and cursor_x < BOARD_SIZE - 1:
            cursor_x += 1
        elif keyboard.is_pressed('left') and cursor_y > 0:
            cursor_y -= 1
        elif keyboard.is_pressed('right') and cursor_y < BOARD_SIZE - 1:
            cursor_y += 1
        elif keyboard.is_pressed('enter') or keyboard.is_pressed('space'):
            if movimiento_valido(tablero, cursor_x, cursor_y):
                colocar_pieza(tablero, cursor_x, cursor_y, jugador_actual)
                if verificar_victoria(tablero, cursor_x, cursor_y, jugador_actual):
                    print(f"¡Jugador {jugador_actual} gana!")
                    keyboard.read_event() 
                    break
                
                jugador_actual = "🔵" if jugador_actual == "🟡" else "🟡"
            else:
                print("Celda ocupada, intenta otro lugar.")


