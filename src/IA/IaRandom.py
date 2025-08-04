import random
from .IIA import IIA

class IARandom(IIA):
    def elegir_movimiento(self, tablero, jugador):
        movimientos_validos = [(i, j) for i in range(len(tablero)) for j in range(len(tablero[0])) if tablero[i][j] == "⬛"]
        return random.choice(movimientos_validos) if movimientos_validos else None
