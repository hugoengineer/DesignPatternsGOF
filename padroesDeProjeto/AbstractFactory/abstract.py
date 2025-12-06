from abc import ABC, abstractmethod


class Botao(ABC):
    @abstractmethod
    def desenhar(self) -> str:
        pass

class Janela(ABC):
    @abstractmethod
    def mostrar(self) -> str:
        pass

class BotaoWindows(Botao):
    def desenhar(self) -> str:
        pass

class JanelaWindows(Janela):
    def mostrar(self) -> str:
        return 


class BotaoMacOS(Botao):
    def desenhar(self) -> str:
        return 

class JanelaMacOS(Janela):
    def mostrar(self) -> str:
        return 


class FabricaAbstrata(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

class FabricaWindows(FabricaAbstrata):
    def criar_botao(self) -> Botao:
        return BotaoWindows()

    def criar_janela(self) -> Janela:
        return JanelaWindows()

class FabricaMacOS(FabricaAbstrata):
    def criar_botao(self) -> Botao:
        return BotaoMacOS()

    def criar_janela(self) -> Janela:
        return JanelaMacOS()

def logica_cliente(fabrica: FabricaAbstrata) -> None:
    botao = fabrica.criar_botao()
    janela = fabrica.criar_janela()

    print(f"Produto 1 (Botão): {botao.desenhar()}")
    print(f"Produto 2 (Janela): {janela.mostrar()}")

    print(f"Interação garantida: Botão '{botao.__class__.__name__}' é compatível com Janela '{janela.__class__.__name__}'.")


if __name__ == "__main__":
    print("--- Cliente usando a Fábrica Windows ---")
    fabrica_windows = FabricaWindows()
    logica_cliente(fabrica_windows)

    print("\n--- Cliente usando a Fábrica macOS ---")
    fabrica_macos = FabricaMacOS()
    logica_cliente(fabrica_macos)
    
    print("\n--- Exemplo de Uso Semântico do Abstract Factory ---")
    print("O cliente pode trocar a fábrica inteira (ex: 'Windows' por 'MacOS') com uma única mudança, mantendo o código de uso inalterado.")