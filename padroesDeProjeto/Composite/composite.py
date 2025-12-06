from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class ComponenteSistemaArquivos(ABC):
    
    @property
    def pai(self) -> ComponenteSistemaArquivos:
        return self._pai

    @pai.setter
    def pai(self, pai: ComponenteSistemaArquivos):
        self._pai = pai

    def adicionar(self, componente: ComponenteSistemaArquivos) -> None:
        pass

    def remover(self, componente: ComponenteSistemaArquivos) -> None:
        pass

    @abstractmethod
    def exibir(self, indentacao: str = "") -> str:
        pass

class Arquivo(ComponenteSistemaArquivos):
    def __init__(self, nome: str, tamanho: float) -> None:
        self.nome = nome
        self.tamanho = tamanho
        self._pai: ComponenteSistemaArquivos = None

    def exibir(self, indentacao: str = "") -> str:
        return f"{indentacao} [A] {self.nome} ({self.tamanho} MB)"

class Pasta(ComponenteSistemaArquivos):
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._filhos: List[ComponenteSistemaArquivos] = []
        self._pai: ComponenteSistemaArquivos = None

    def adicionar(self, componente: ComponenteSistemaArquivos) -> None:
        self._filhos.append(componente)
        componente.pai = self # Define o pai

    def remover(self, componente: ComponenteSistemaArquivos) -> None:
        if componente in self._filhos:
            self._filhos.remove(componente)
            componente.pai = None

    def exibir(self, indentacao: str = "") -> str:
        resultado = f"{indentacao} [P] {self.nome}/\n"
        nova_indentacao = indentacao + "  " 
        
        for filho in self._filhos:
            resultado += filho.exibir(nova_indentacao) + "\n"
        
        return resultado.rstrip('\n')

def operacao_cliente(componente: ComponenteSistemaArquivos) -> None:
    print(componente.exibir())

if __name__ == "__main__":
    
    relatorio = Arquivo("Relatorio_Final.pdf", 5.2)
    imagem_perfil = Arquivo("Foto_Perfil.jpg", 1.1)
    
    pasta_documentos = Pasta("Documentos")
    pasta_documentos.adicionar(relatorio)
    pasta_documentos.adicionar(Arquivo("Ata_Reuniao.docx", 0.3))
    
    pasta_imagens = Pasta("Imagens")
    pasta_imagens.adicionar(imagem_perfil)
    pasta_imagens.adicionar(Arquivo("Fundo_Tela.png", 3.5))

    pasta_raiz = Pasta("Meu_PC_C:")
    pasta_raiz.adicionar(pasta_documentos)
    pasta_raiz.adicionar(pasta_imagens)
    pasta_raiz.adicionar(Arquivo("readme.txt", 0.01))

    print("--- Visualização da Estrutura de Arquivos Completa ---")
    operacao_cliente(pasta_raiz)
    
    print("\n" + "="*50 + "\n")
    
    print("--- Visualização de um Arquivo Isolado ---")
    operacao_cliente(relatorio)
    
    print("\n" + "="*50 + "\n")

    print("--- Visualização apenas da Pasta de Imagens ---")
    operacao_cliente(pasta_imagens)
    