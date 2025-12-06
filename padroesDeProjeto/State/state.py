from abc import ABC, abstractmethod

# ----------------------------------------------------------------------
# 1. Interface de Estado (State)
# ----------------------------------------------------------------------

class EstadoPlayer(ABC):
    """
    Define a interface comum para todos os estados concretos.
    O Player irá delegar suas chamadas a um objeto desta interface.
    """
    
    @abstractmethod
    def lidar_com_play(self, player):
        """Ação a ser executada ao pressionar o botão Play/Pause."""
        pass

    @abstractmethod
    def lidar_com_stop(self, player):
        """Ação a ser executada ao pressionar o botão Stop."""
        pass


# ----------------------------------------------------------------------
# 2. Estados Concretos (Concrete States)
# ----------------------------------------------------------------------

class EstadoParado(EstadoPlayer):
    """Estado 'Parado': O player não está tocando música."""
    
    def lidar_com_play(self, player):
        print("Música iniciada. Transição de PARADO para REPRODUZINDO.")
        # Transição de estado: muda o estado do Contexto
        player.mudar_estado(EstadoReproduzindo())

    def lidar_com_stop(self, player):
        print("O player já está parado. Nenhuma ação.")

class EstadoReproduzindo(EstadoPlayer):
    """Estado 'Reproduzindo': O player está tocando música ativamente."""
    
    def lidar_com_play(self, player):
        print("Música pausada. Transição de REPRODUZINDO para PAUSADO.")
        # Transição de estado
        player.mudar_estado(EstadoPausado())

    def lidar_com_stop(self, player):
        print("Música interrompida. Transição de REPRODUZINDO para PARADO.")
        # Transição de estado
        player.mudar_estado(EstadoParado())

class EstadoPausado(EstadoPlayer):
    """Estado 'Pausado': O player está com a reprodução suspensa."""
    
    def lidar_com_play(self, player):
        print("Música retomada. Transição de PAUSADO para REPRODUZINDO.")
        # Transição de estado
        player.mudar_estado(EstadoReproduzindo())

    def lidar_com_stop(self, player):
        print("Música interrompida. Transição de PAUSADO para PARADO.")
        # Transição de estado
        player.mudar_estado(EstadoParado())


# ----------------------------------------------------------------------
# 3. Contexto (Context)
# ----------------------------------------------------------------------

class PlayerDeMusica:
    """
    O Contexto: Armazena o estado atual e delega as ações a ele.
    """
    def __init__(self):
        # O estado inicial é sempre Parado
        self._estado_atual: EstadoPlayer = EstadoParado()
        print(f"Player inicializado no estado: {self._estado_atual.__class__.__name__}")

    def mudar_estado(self, novo_estado: EstadoPlayer):
        """Permite a transição de estado, chamada pelas classes de Estado."""
        self._estado_atual = novo_estado
        print(f"Estado atual do Player: {self._estado_atual.__class__.__name__}")

    # Métodos do Player que delegam a execução para o estado atual
    
    def apertar_play(self):
        print("\n[Ação] Pressionado PLAY/PAUSE...")
        self._estado_atual.lidar_com_play(self)
    
    def apertar_stop(self):
        print("\n[Ação] Pressionado STOP...")
        self._estado_atual.lidar_com_stop(self)


# ----------------------------------------------------------------------
# 4. Código Cliente (Uso e Teste de Transição)
# ----------------------------------------------------------------------

if __name__ == "__main__":
    
    player = PlayerDeMusica()
    
    # 1. Pressionar Play (Parado -> Reproduzindo)
    player.apertar_play() 
    
    # 2. Pressionar Play novamente (Reproduzindo -> Pausado)
    player.apertar_play()
    
    # 3. Pressionar Play novamente (Pausado -> Reproduzindo)
    player.apertar_play()
    
    # 4. Pressionar Stop (Reproduzindo -> Parado)
    player.apertar_stop()

    # 5. Pressionar Stop (Parado -> Parado)
    player.apertar_stop()