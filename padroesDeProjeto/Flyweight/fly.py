from typing import Dict

class Caractere:

    def __init__(self, fonte: str, cor: str):

        self._fonte = fonte
        self._cor = cor
        print(f"Criando Caractere Flyweight: Fonte={fonte}, Cor={cor}")

    def desenhar(self, posicao_x: int, posicao_y: int, tamanho: int) -> None:
        print(f"  > Desenhando [{self._fonte} {self._cor}]: na Posição=({posicao_x},{posicao_y}), Tamanho={tamanho}")


class FabricaCaractere:

    _caracteres: Dict[str, Caractere] = {}

    def get_chave_flyweight(self, fonte: str, cor: str) -> str:
        return f"{fonte}_{cor}"

    def get_caractere(self, fonte: str, cor: str) -> Caractere:
        chave = self.get_chave_flyweight(fonte, cor)

        if chave not in self._caracteres:
            print(f"Fábrica: Cache miss. Criando novo Flyweight para {fonte}/{cor}.")
            self._caracteres[chave] = Caractere(fonte, cor)
        else:
            print(f"Fábrica: Cache hit. Reutilizando Flyweight para {fonte}/{cor}.")
            
        return self._caracteres[chave]

    def listar_caracteres_em_cache(self) -> None:
        print(f"\nTotal de objetos Flyweight únicos criados: {len(self._caracteres)}")
        for chave in self._caracteres:
            print(f"  - {chave}")

if __name__ == "__main__":
    fabrica = FabricaCaractere()
    

    documento = [

        ("A", "Arial", "Preto", 10, 5, 12),
        ("l", "Arial", "Preto", 20, 5, 12),
        ("i", "Arial", "Preto", 30, 5, 12),
        ("c", "Times New Roman", "Azul", 40, 5, 14),
        ("e", "Times New Roman", "Vermelho", 50, 5, 14),
        ("C", "Times New Roman", "Azul", 60, 5, 14),
        ("o", "Verdana", "Preto", 70, 5, 10),
    ]

    print("--- Processamento do Documento ---")
    
    x = 10
    y = 10
    
    for char, fonte, cor, _, _, tamanho in documento:
        flyweight_caractere = fabrica.get_caractere(fonte, cor)
        
        flyweight_caractere.desenhar(x, y, tamanho)
        
        x += 15

    fabrica.listar_caracteres_em_cache()
    
    print("\nEficiência de Memória:")
    print(f"O documento tinha {len(documento)} caracteres totais, mas apenas {len(fabrica._caracteres)} objetos Flyweight foram criados.")