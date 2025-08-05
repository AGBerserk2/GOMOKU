from .IIA import IIA
import copy
import time

class IAMinimax(IIA):
    def __init__(self, profundidad=6, tiempo_max=3):
        self.profundidad_max = profundidad
        self.tiempo_max = tiempo_max
        self.inicio_tiempo = None

    def heuristica(self, tablero, jugador):
        oponente = "🔵" if jugador == "🟡" else "🟡"
        score = 0

        # Heurística: control del centro
        centro = len(tablero) // 2
        for i in range(len(tablero)):
            for j in range(len(tablero[0])):
                if tablero[i][j] == jugador:
                    dist_centro = abs(i - centro) + abs(j - centro)
                    score += max(0, 7 - dist_centro)  # Más cerca del centro, más puntos

        # Heurísticas de patrones
        patrones = [
            (jugador, 5, 100000),   # Cinco en línea (victoria)
            (jugador, 4, 10000),    # Cuatro abierto
            (jugador, 3, 1000),     # Tres abierto
            (jugador, 2, 100),      # Dos abierto
            (oponente, 5, -100000), # El oponente gana (bloquear)
            (oponente, 4, -10000),  # El oponente tiene cuatro abierto (bloquear)
            (oponente, 3, -1000),   # El oponente tiene tres abierto (bloquear)
            (oponente, 2, -100),    # El oponente tiene dos abierto (bloquear)
        ]

        for ficha, longitud, valor in patrones:
            for i in range(len(tablero)):
                for j in range(len(tablero[0])):
                    if tablero[i][j] == ficha:
                        score += self.contar_patrones(tablero, i, j, ficha, longitud) * valor

        return score

    def contar_patrones(self, tablero, x, y, jugador, longitud):
        total = 0
        direcciones = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in direcciones:
            count = 1
            bloqueados = 0
            # Hacia adelante
            i, j = x + dx, y + dy
            while 0 <= i < len(tablero) and 0 <= j < len(tablero) and tablero[i][j] == jugador:
                count += 1
                i += dx
                j += dy
            if not (0 <= i < len(tablero) and 0 <= j < len(tablero)) or tablero[i][j] != "⬛":
                bloqueados += 1
            # Hacia atrás
            i, j = x - dx, y - dy
            while 0 <= i < len(tablero) and 0 <= j < len(tablero) and tablero[i][j] == jugador:
                count += 1
                i -= dx
                j -= dy
            if not (0 <= i < len(tablero) and 0 <= j < len(tablero)) or tablero[i][j] != "⬛":
                bloqueados += 1

            if count == longitud:
                # Solo cuenta si es abierto o semi-abierto
                if bloqueados == 0:  # Abierto
                    total += 2
                elif bloqueados == 1:  # Semi-abierto
                    total += 1
        return total

    def elegir_movimiento(self, tablero, jugador):
        self.inicio_tiempo = time.time()
        _, mejor = self.minimax(tablero, jugador, self.profundidad_max, -float('inf'), float('inf'), True, jugador)
        return mejor

    def minimax(self, tablero, jugador_actual, profundidad, alpha, beta, maximizando, jugador_ia):
        if profundidad == 0 or self.tiempo_agotado():
            return self.heuristica(tablero, jugador_ia), None

        movimientos = [(i, j) for i in range(len(tablero)) for j in range(len(tablero[0])) if tablero[i][j] == "⬛"]
        if not movimientos:
            return self.heuristica(tablero, jugador_ia), None

        mejor_movimiento = None
        oponente = "🔵" if jugador_actual == "🟡" else "🟡"

        if maximizando:
            max_eval = -float('inf')
            for i, j in movimientos:
                copia = copy.deepcopy(tablero)
                copia[i][j] = jugador_actual
                eval, _ = self.minimax(copia, oponente, profundidad - 1, alpha, beta, False, jugador_ia)
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
                copia[i][j] = jugador_actual
                eval, _ = self.minimax(copia, oponente, profundidad - 1, alpha, beta, True, jugador_ia)
                if eval < min_eval:
                    min_eval = eval
                    mejor_movimiento = (i, j)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, mejor_movimiento

    def tiempo_agotado(self):
        return (time.time() - self.inicio_tiempo) > self.tiempo_max
