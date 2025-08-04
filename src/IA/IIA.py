from abc import ABC, abstractmethod

class IIA(ABC):
    @abstractmethod
    def elegir_movimiento(self, tablero, jugador):
        pass
