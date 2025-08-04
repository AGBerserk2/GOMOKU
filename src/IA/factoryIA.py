from .IAgreedy import IAGreedy
from .IAminimax import IAMinimax
from .IaRandom import IARandom

class FabricaIA:
    @staticmethod
    def crear_agente(nombre):
        if nombre == "random":
            return IARandom()
        elif nombre == "greedy":
            return IAGreedy()
        elif nombre == "minimax":
            return IAMinimax()
        else:
            raise ValueError("Agente no reconocido.")
