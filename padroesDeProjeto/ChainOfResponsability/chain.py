from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Manipulador(ABC):
    @abstractmethod
    def definir_sucessor(self, manipulador: Manipulador) -> Manipulador:
        """Define o próximo manipulador na cadeia."""
        pass

    @abstractmethod
    def manipular(self, quantia: int) -> Optional[str]:
        """Processa a solicitação ou passa para o próximo."""
        pass


class ManipuladorBase(Manipulador):
    _sucessor: Manipulador = None

    def definir_sucessor(self, manipulador: Manipulador) -> Manipulador:
        self._sucessor = manipulador
        return manipulador

    def manipular(self, quantia: int) -> Optional[str]:
        if self._sucessor:
            return self._sucessor.manipular(quantia)

        return None

class Gerente(ManipuladorBase):
    LIMITE = 500
    NOME = "Gerente"

    def manipular(self, quantia: int) -> Optional[str]:
        if quantia <= self.LIMITE:
            return f"A despesa de R$ {quantia} foi aprovada pelo {self.NOME}."
        else:
            print(f"[{self.NOME}]: Despesa de R$ {quantia} é alta demais. Encaminhando para o sucessor...")
            return super().manipular(quantia)

class Diretor(ManipuladorBase):
    LIMITE = 2000
    NOME = "Diretor"

    def manipular(self, quantia: int) -> Optional[str]:
        if quantia <= self.LIMITE:
            return f"A despesa de R$ {quantia} foi aprovada pelo {self.NOME}."
        else:
            print(f"[{self.NOME}]: Despesa de R$ {quantia} é alta demais. Encaminhando para o sucessor...")
            return super().manipular(quantia)

class CEO(ManipuladorBase):
    LIMITE = 10000
    NOME = "CEO"

    def manipular(self, quantia: int) -> Optional[str]:
        if quantia <= self.LIMITE:
            return f"A despesa de R$ {quantia} foi aprovada pelo {self.NOME} (Autoridade Máxima)."
        else:
            # Se nem o CEO puder aprovar, a solicitação é negada.
            return f"A despesa de R$ {quantia} foi NEGADA. Excede o limite de R$ {self.LIMITE}."

def processar_solicitacao(manipulador: Manipulador, quantia: int) -> None:
    print(f"\n--- Solicitando aprovação para R$ {quantia} ---")
    resultado = manipulador.manipular(quantia)

    if resultado:
        print(f"Resultado: {resultado}")
    else:
        print("Resultado: A solicitação não pôde ser processada por nenhum manipulador na cadeia.")

if __name__ == "__main__":
    gerente = Gerente()
    diretor = Diretor()
    ceo = CEO()

    gerente.definir_sucessor(diretor).definir_sucessor(ceo)
    cadeia_inicial = gerente

    processar_solicitacao(cadeia_inicial, 350) 

    processar_solicitacao(cadeia_inicial, 1500) 

    processar_solicitacao(cadeia_inicial, 8000) 

    processar_solicitacao(cadeia_inicial, 15000) 

    print("\n\n--- Testando Cadeia Incompleta (Apenas Gerente) ---")
    processar_solicitacao(Gerente(), 600)