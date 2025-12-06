from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor:float):
        pass
