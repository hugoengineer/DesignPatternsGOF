from __future__ import annotations
from abc import ABC, abstractmethod

class Comando(ABC):

    @abstractmethod
    def executar(self) -> None:
        pass


class Luz:
    def ligar(self) -> None:
        print("Luz: Está acesa.")

    def desligar(self) -> None:
        print("Luz: Está apagada.")

class SistemaDeSom:
    def __init__(self, volume: int = 0):
        self.volume = volume
        
    def aumentar_volume(self) -> None:
        self.volume = min(10, self.volume + 1)
        print(f"Sistema de Som: Volume aumentado para {self.volume}.")
        
    def diminuir_volume(self) -> None:
        self.volume = max(0, self.volume - 1)
        print(f"Sistema de Som: Volume diminuído para {self.volume}.")


class LigarLuzComando(Comando):
    def __init__(self, luz: Luz) -> None:
        self._luz = luz

    def executar(self) -> None:
        print("-> [Comando: Ligar Luz] Delegando a execução...")
        self._luz.ligar()

class AumentarVolumeComando(Comando):
    def __init__(self, som: SistemaDeSom) -> None:
        self._som = som

    def executar(self) -> None:
        print("-> [Comando: Aumentar Volume] Delegando a execução...")
        self._som.aumentar_volume()


class ControleRemoto:
    def __init__(self):
        # O controle armazena comandos para cada botão
        self._botao_a: Comando = None
        self._botao_b: Comando = None
        
    def configurar_botao(self, botao: str, comando: Comando):
        if botao.lower() == 'a':
            self._botao_a = comando
            print(f"Controle: Botão 'A' configurado para o comando {comando.__class__.__name__}.")
        elif botao.lower() == 'b':
            self._botao_b = comando
            print(f"Controle: Botão 'B' configurado para o comando {comando.__class__.__name__}.")

    def apertar_botao_a(self) -> None:
        print("\n[Ação do Usuário] Botão 'A' pressionado.")
        if self._botao_a:
            self._botao_a.executar()
        else:
            print("Nenhum comando configurado para o botão 'A'.")

    def apertar_botao_b(self) -> None:
        """Ação de apertar o botão 'B'."""
        print("\n[Ação do Usuário] Botão 'B' pressionado.")
        if self._botao_b:
            self._botao_b.executar()
        else:
            print("Nenhum comando configurado para o botão 'B'.")


if __name__ == "__main__":
    
    # 1. Criar os Receivers (Dispositivos)
    minha_luz = Luz()
    meu_som = SistemaDeSom(volume=5)
    
    # 2. Criar os Comandos Concretos, associando-os aos Receivers
    comando_ligar_luz = LigarLuzComando(minha_luz)
    comando_aumentar_volume = AumentarVolumeComando(meu_som)
    
    # 3. Criar o Invoker (Controle Remoto)
    controle = ControleRemoto()
    
    # 4. Configurar o Controle Remoto (Invoker) com os Comandos
    # O controle não sabe que está lidando com uma Luz ou um Som, apenas com 'Comandos'.
    controle.configurar_botao('A', comando_ligar_luz)
    controle.configurar_botao('B', comando_aumentar_volume)
    
    print("\n---------------- INÍCIO DAS OPERAÇÕES ----------------")
    
    # Ação 1: Apertar o botão 'A' (Ligar Luz)
    controle.apertar_botao_a() 
    
    # Ação 2: Apertar o botão 'B' (Aumentar Volume)
    controle.apertar_botao_b()
    controle.apertar_botao_b()
    
    # Demonstração de Reconfiguração: Trocar o comando do botão 'A'
    print("\n[Configuração] Reconfigurando Botão 'A' para Diminuir Volume...")
    
    # Criação de um novo comando (necessitaria de uma classe DiminuirVolumeComando, 
    # mas para simplificar, usaremos AumentarVolumeComando como exemplo de troca de foco)
    # OBS: Se fosse DiminuirVolumeComando, a lógica continuaria a mesma para o Invoker.
    
    class DesligarLuzComando(Comando):
        def __init__(self, luz: Luz) -> None:
            self._luz = luz
        def executar(self) -> None:
            print("-> [Comando: Desligar Luz] Delegando a execução...")
            self._luz.desligar()

    comando_desligar_luz = DesligarLuzComando(minha_luz)
    
    controle.configurar_botao('A', comando_desligar_luz)

    # Ação 3: Apertar o botão 'A' novamente (Agora Desliga a Luz)
    controle.apertar_botao_a()