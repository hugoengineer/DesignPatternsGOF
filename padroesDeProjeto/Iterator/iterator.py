from __future__ import annotations
from collections.abc import Iterator, Iterable
from typing import Any, List, Optional

class OrdemAlfabeticaIterator(Iterator):

    def __init__(self, colecao: ColecaoLivros, reverso: bool = False) -> None:
        self._colecao = colecao
        self._posicao: int = -1
        self._reverso = reverso

        self._dados = sorted(self._colecao.get_itens())
        if reverso:
            self._dados.reverse()

    def __next__(self) -> Any:
  
        try:
            self._posicao += 1
            valor = self._dados[self._posicao]
        except IndexError:
            raise StopIteration()

        return valor

class ColecaoLivros(Iterable):

    def __init__(self, itens: List[str] = None) -> None:
        self._itens = itens if itens is not None else []

    def get_itens(self) -> List[str]:
        return self._itens

    def adicionar_item(self, item: str):
        self._itens.append(item)

    def __iter__(self) -> OrdemAlfabeticaIterator:
        return OrdemAlfabeticaIterator(self)

    def iterar_reverso(self) -> OrdemAlfabeticaIterator:
        return OrdemAlfabeticaIterator(self, True)

if __name__ == "__main__":
    
    colecao = ColecaoLivros()
    colecao.adicionar_item("O Senhor dos Anéis")
    colecao.adicionar_item("1984")
    colecao.adicionar_item("Orgulho e Preconceito")
    colecao.adicionar_item("Cem Anos de Solidão")
    
    print("-----------------------------------------------------------------")
    print("A) Iteração Padrão (Usando o loop 'for' que chama __iter__ e __next__)")
    print("-----------------------------------------------------------------")
    
    for livro in colecao:
        print(f"- Livro: {livro}")

    print("\n-----------------------------------------------------------------")
    print("B) Iteração Explícita (Fazendo manualmente o que o loop 'for' faz)")
    print("-----------------------------------------------------------------")
    
    iterador = colecao.__iter__()
    
    try:
        print(f"Primeiro: {next(iterador)}")
        print(f"Segundo: {next(iterador)}")
    except StopIteration:
        print("Fim da iteração explícita.")


    print("\n-----------------------------------------------------------------")
    print("C) Iteração Reversa (Usando um Iterador Diferente)")
    print("-----------------------------------------------------------------")
    
    for livro in colecao.iterar_reverso():
        print(f"- Livro: {livro}")