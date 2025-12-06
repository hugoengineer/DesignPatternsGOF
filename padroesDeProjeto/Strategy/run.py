import alg1
import alg2
from typing import Any, List, Tuple

class ProdutoHandler:
    """
    O Contexto que usa a estratégia (Strategy) para processar o pagamento.
    """
    def __init__(self):
        self._itens: List[Tuple[str, float]] = []
        self.pagamento_strategy: Any = None

    def add_item(self, name: str, valor: float) -> None:
        formated_item = (name, valor)
        self._itens.append(formated_item)

    def set_strategy(self, strategy: Any) -> None:
        self.pagamento_strategy = strategy

    def finish_purchase(self) -> None:
        if not self.pagamento_strategy:
            print("Erro: Nenhuma estratégia de pagamento definida.")
            return

        total = 0.0
        for item in self._itens:
            total += item[1]
            
        print(f"\n[Contexto] Valor total da compra: R${total:.2f}")
        self.pagamento_strategy.pagar(total)

if __name__ == "__main__":
    produto = ProdutoHandler()
    produto.add_item("Caneta", 2.5)
    produto.add_item("Caderno", 15.0)

    print("= = = PAGAMENTO COM CARTÃO DE CRÉDITO (alg1) = = =")
    strategy_credito = alg1.PagamentoCredito()
    produto.set_strategy(strategy_credito)
    produto.finish_purchase()

    print("\n= = = PAGAMENTO COM PIX (alg2) = = =")
    strategy_pix = alg2.PagamentoPix()
    produto.set_strategy(strategy_pix)
    produto.finish_purchase()