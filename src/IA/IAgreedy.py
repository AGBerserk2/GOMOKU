from .IIA import IIA
import copy

class IAGreedy(IIA):
    def evaluar_movimiento(self, tablero, x, y, jugador):
        oponente = "🔵" if jugador == "🟡" else "🟡"
        score = 0

        # Heurística: control del centro
        centro = len(tablero) // 2
        dist_centro = abs(x - centro) + abs(y - centro)
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
            score += self.contar_patrones(tablero, x, y, ficha, longitud) * valor

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
        mejor = (-1, -1)
        mejor_valor = float('-inf')
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
