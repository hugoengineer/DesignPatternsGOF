from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime

class Mediator(ABC):
    @abstractmethod
    def notificar(self, remetente: Componente, evento: str) -> None:
        pass

class Componente:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class MembroChat(Componente):
    def __init__(self, nome: str, mediator: Mediator = None) -> None:
        super().__init__(mediator)
        self.nome = nome

    def enviar_mensagem(self, mensagem: str, destinatario: Optional[MembroChat] = None) -> None:
        print(f"[{self.nome}] enviou: '{mensagem}'")
        if self.mediator:
            self.mediator.notificar(self, f"mensagem:{mensagem}", destinatario)
        else:
            print(f"[{self.nome}]: Sem mediador configurado, mensagem não enviada.")

    def receber_mensagem(self, remetente: str, mensagem: str) -> None:
        print(f"[{self.nome}] recebeu de [{remetente}]: '{mensagem}'")


class ChatMediator(Mediator):
    def __init__(self) -> None:
        self._membros: list[MembroChat] = []

    def adicionar_membro(self, membro: MembroChat) -> None:
        self._membros.append(membro)
        membro.mediator = self
        print(f"Mediator: {membro.nome} entrou no chat.")

    def notificar(self, remetente: Componente, evento: str, destinatario: Optional[MembroChat] = None) -> None:
        if evento.startswith("mensagem:"):
            mensagem = evento.split(":", 1)[1]
            if destinatario:
                print(f"Mediator: Roteando mensagem privada de {remetente.nome} para {destinatario.nome}")
                destinatario.receber_mensagem(remetente.nome, mensagem)
            else:
                print(f"Mediator: Roteando mensagem global de {remetente.nome} para todos.")
                for membro in self._membros:
                    if membro != remetente:
                        membro.receber_mensagem(remetente.nome, mensagem)

if __name__ == "__main__":
    
    chat_room = ChatMediator()
    
    joao = MembroChat("João")
    maria = MembroChat("Maria")
    pedro = MembroChat("Pedro")
    
    chat_room.adicionar_membro(joao)
    chat_room.adicionar_membro(maria)
    chat_room.adicionar_membro(pedro)
    
    print("\n--- Início da Conversa ---")
    
    joao.enviar_mensagem("Olá a todos! Alguém tem notícias da reunião?")
    
    maria.enviar_mensagem("Sim, foi adiada para amanhã de manhã.")
    
    pedro.enviar_mensagem("João, você recebeu a ata?", joao)
    
    print("\n--- Fim da Conversa ---")