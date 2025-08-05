import time
from IA.factoryIA import FabricaIA
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
                    return
                jugador_actual = "🔵" if jugador_actual == "🟡" else "🟡"
            else:
                print("Celda ocupada, intenta otro lugar.")


BOARD_SIZE = 15

def jugar_con_ia(tipo_ia):
    tablero = crear_tablero()
    jugador_humano = "🟡"
    jugador_ia = "🔵"
    ia = FabricaIA.crear_agente(tipo_ia)
    cursor_x, cursor_y = BOARD_SIZE // 2, BOARD_SIZE // 2
    turno_ia = False

    while True:
        imprimir_tablero(tablero, cursor_x, cursor_y, jugador_humano if not turno_ia else jugador_ia)

        if turno_ia:
            x, y = ia.elegir_movimiento(tablero, jugador_ia)
            if x is None:
                print("¡Empate! No hay más movimientos posibles.")
                return
            colocar_pieza(tablero, x, y, jugador_ia)
            if verificar_victoria(tablero, x, y, jugador_ia):
                imprimir_tablero(tablero, x, y, jugador_ia)
                print("¡La IA gana!")
                time.sleep(5)
                return
            turno_ia = False
        else:
            keyboard.read_event()
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
                    colocar_pieza(tablero, cursor_x, cursor_y, jugador_humano)
                    if verificar_victoria(tablero, cursor_x, cursor_y, jugador_humano):
                        imprimir_tablero(tablero, cursor_x, cursor_y, jugador_humano)
                        print("¡Jugador humano gana!")
                        time.sleep(5)
                        return

                    turno_ia = True
                else:
                    print("Casilla ocupada, intenta otra.")


def jugar_ia_vs_ia(tipo_ia1, tipo_ia2):
    tablero = crear_tablero()
    jugador1 = "🟡"
    jugador2 = "🔵"
    ia1 = FabricaIA.crear_agente(tipo_ia1)
    ia2 = FabricaIA.crear_agente(tipo_ia2)
    turno_ia1 = True
    cursor_x, cursor_y = BOARD_SIZE // 2, BOARD_SIZE // 2

    while True:
        imprimir_tablero(tablero, cursor_x, cursor_y, jugador1 if turno_ia1 else jugador2)
        time.sleep(0.5)  # Pausa para ver el avance

        if turno_ia1:
            x, y = ia1.elegir_movimiento(tablero, jugador1)
            if x is None:
                print("¡Empate! No hay más movimientos posibles.")
                break
            colocar_pieza(tablero, x, y, jugador1)
            if verificar_victoria(tablero, x, y, jugador1):
                imprimir_tablero(tablero, x, y, jugador1)
                print("¡IA 1 (🟡) gana!")
                time.sleep(3)
                return
            turno_ia1 = False
        else:
            x, y = ia2.elegir_movimiento(tablero, jugador2)
            if x is None:
                print("¡Empate! No hay más movimientos posibles.")
                break
            colocar_pieza(tablero, x, y, jugador2)
            if verificar_victoria(tablero, x, y, jugador2):
                imprimir_tablero(tablero, x, y, jugador2)
                print("¡IA 2 (🔵) gana!")
                time.sleep(3)
                return
            turno_ia1 = True


if __name__ == "__main__":
    jugar_con_ia('minimax')
