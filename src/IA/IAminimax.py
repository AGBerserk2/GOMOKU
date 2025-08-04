from .IIA import IIA
import copy
import time

class IAMinimax(IIA):
    def __init__(self, profundidad=6, tiempo_max=3):
        self.profundidad_max = profundidad
        self.tiempo_max = tiempo_max
        self.inicio_tiempo = None

    def heuristica(self, tablero, jugador):
        # Mejora esto con más heurísticas reales
        return sum(row.count(jugador) for row in tablero)

    def elegir_movimiento(self, tablero, jugador):
        self.inicio_tiempo = time.time()
        _, mejor = self.minimax(tablero, jugador, self.profundidad_max, -float('inf'), float('inf'), True)
        return mejor

    def minimax(self, tablero, jugador, profundidad, alpha, beta, maximizando):
        if profundidad == 0 or self.tiempo_agotado():
            return self.heuristica(tablero, jugador), None

        movimientos = [(i, j) for i in range(len(tablero)) for j in range(len(tablero[0])) if tablero[i][j] == "⬛"]
        if not movimientos:
            return self.heuristica(tablero, jugador), None

        mejor_movimiento = None
        oponente = "🔵" if jugador == "🔴" else "🔴"

        if maximizando:
            max_eval = -float('inf')
            for i, j in movimientos:
                copia = copy.deepcopy(tablero)
                copia[i][j] = jugador
                eval, _ = self.minimax(copia, jugador, profundidad - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    mejor_movimiento = (i, j)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, mejor_movimiento
        else:
            min_eval = float('inf')
            for i, j in movimientos:
                copia = copy.deepcopy(tablero)
                copia[i][j] = oponente
                eval, _ = self.minimax(copia, jugador, profundidad - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    mejor_movimiento = (i, j)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, mejor_movimiento

    def tiempo_agotado(self):
        return (time.time() - self.inicio_tiempo) > self.tiempo_max
