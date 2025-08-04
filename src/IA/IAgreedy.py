from .IIA import IIA
import copy

class IAGreedy(IIA):
    def evaluar_movimiento(self, tablero, x, y, jugador):
        direcciones = [(1, 0), (0, 1), (1, 1), (1, -1)]
        score = 0
        for dx, dy in direcciones:
            conteo = 0
            for dir in [1, -1]:
                nx, ny = x + dir * dx, y + dir * dy
                while 0 <= nx < len(tablero) and 0 <= ny < len(tablero) and tablero[nx][ny] == jugador:
                    conteo += 1
                    nx += dir * dx
                    ny += dir * dy
            score = max(score, conteo)
        return score

    def elegir_movimiento(self, tablero, jugador):
        mejor = (-1, -1)
        mejor_valor = -1
        for i in range(len(tablero)):
            for j in range(len(tablero[0])):
                if tablero[i][j] == "⬛":
                    tablero_sim = copy.deepcopy(tablero)
                    tablero_sim[i][j] = jugador
                    valor = self.evaluar_movimiento(tablero_sim, i, j, jugador)
                    if valor > mejor_valor:
                        mejor_valor = valor
                        mejor = (i, j)
        return mejor
