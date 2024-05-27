from abc import ABC, abstractmethod

class Builder:

    @abstractmethod
    def pintar_tablero(self, Panel):
        pass