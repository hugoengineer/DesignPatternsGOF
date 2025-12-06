import copy
from typing import Dict, Any

# ----------------------------------------------------------------------
# 1. Classes de Componentes Complexos
# ----------------------------------------------------------------------

class Motor:
    """Um componente complexo que é lento de inicializar."""
    def __init__(self, tipo: str, potencia: int):
        self.tipo = tipo
        self.potencia = potencia
        print(f"  [Motor] Motor {tipo} de {potencia} HP criado.")

    def __str__(self):
        return f"{self.tipo} ({self.potencia} HP)"

class Pneus:
    """Um componente complexo que precisa ser clonado corretamente."""
    def __init__(self, marca: str, tamanho: int):
        self.marca = marca
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.marca} R{self.tamanho}"

# ----------------------------------------------------------------------
# 2. A Classe Base do Prototype
# ----------------------------------------------------------------------

class CarroPrototype:
    """
    O Protótipo. A chave é o método 'clone()', que usa deepcopy.
    """
    def __init__(self, modelo: str, cor: str, motor: Motor, pneus: Pneus):
        self.modelo = modelo
        self.cor = cor
        self.motor = motor
        self.pneus = pneus
        self.acessorios: Dict[str, Any] = {}
        print(f"  [Carro] Objeto base '{modelo}' criado.")

    def clone(self) -> 'CarroPrototype':
        """
        Método de clonagem. Cria uma cópia profunda (Deep Copy) do objeto.
        Isso garante que todos os objetos aninhados (Motor, Pneus) também
        sejam copiados, em vez de apenas referenciados.
        """
        # copy.deepcopy é o coração do padrão Prototype em Python
        return copy.deepcopy(self)

    def adicionar_acessorio(self, nome: str, valor: Any):
        self.acessorios[nome] = valor

    def mostrar_config(self):
        acessorios_str = ', '.join([f'{k}: {v}' for k, v in self.acessorios.items()])
        print("\n==============================================")
        print(f"Modelo: {self.modelo} | Cor: {self.cor}")
        print(f"Motor: {self.motor}")
        print(f"Pneus: {self.pneus}")
        print(f"Acessórios: {acessorios_str if acessorios_str else 'Nenhum'}")
        print(f"ID do Objeto (Clone): {id(self)}")
        print(f"ID do Motor (Componente): {id(self.motor)}")
        print("==============================================")

# ----------------------------------------------------------------------
# 3. Código Cliente (Uso)
# ----------------------------------------------------------------------

if __name__ == "__main__":
    
    print("--- 1. Criando o Protótipo Original (Lento) ---")
    
    # Criação dos componentes complexos
    motor_base = Motor("V8 Turbo", 500)
    pneus_base = Pneus("Michelin", 18)

    # Criação do Protótipo (Carro Modelo A)
    prototipo_a = CarroPrototype(
        modelo="GT-X",
        cor="Azul Metálico",
        motor=motor_base,
        pneus=pneus_base
    )
    prototipo_a.adicionar_acessorio("Teto Solar", True)
    prototipo_a.mostrar_config()

    print("\n--- 2. Clonando para Criar o Modelo B (Rápido) ---")

    # CLONE 1: Cria um novo objeto B a partir do Protótipo A
    carro_b = prototipo_a.clone()
    carro_b.modelo = "GT-Y"
    carro_b.cor = "Vermelho Fogo"
    # Modifica apenas o acessório: o motor (caro) é reutilizado/clonado
    carro_b.adicionar_acessorio("Aerofólio", True) 
    carro_b.acessorios["Teto Solar"] = False # Remove o teto solar
    carro_b.mostrar_config()

    print("\n--- 3. Clonando e Alterando um Subcomponente (Modelo C) ---")

    # CLONE 2: Cria um novo objeto C a partir do Protótipo A
    carro_c = prototipo_a.clone()
    carro_c.modelo = "GT-Z"
    carro_c.cor = "Preto Fosco"
    
    # Altera o subcomponente Pneus APENAS para este clone
    carro_c.pneus.tamanho = 20
    carro_c.pneus.marca = "Pirelli"

    carro_c.mostrar_config()

    print("\n--- Verificação Final do Protótipo Original ---")
    # O protótipo original deve permanecer inalterado
    prototipo_a.mostrar_config()
    
    # Verifica que Motor B e Motor C são objetos diferentes do Motor A
    print(f"\nMotor do Protótipo A é o mesmo objeto do Motor do Carro B? {id(prototipo_a.motor) == id(carro_b.motor)}")
    print(f"Pneus do Protótipo A é o mesmo objeto dos Pneus do Carro C? {id(prototipo_a.pneus) == id(carro_c.pneus)}")