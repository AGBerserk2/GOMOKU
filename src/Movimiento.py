def movimiento_valido(tablero, x, y):
    return tablero[x][y] == "⬛"
def colocar_pieza(tablero, x, y, jugador):
    tablero[x][y] = jugador