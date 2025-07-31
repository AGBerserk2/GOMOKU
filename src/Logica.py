BOARD_SIZE = 15

def verificar_victoria(tablero, x, y, jugador):
    direcciones = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in direcciones:
        conteo = 1
        for dir in [1, -1]:
            nx, ny = x + dir*dx, y + dir*dy
            while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and tablero[nx][ny] == jugador:
                conteo += 1
                nx += dir*dx
                ny += dir*dy
        if conteo >= 5:
            return True
    return False

