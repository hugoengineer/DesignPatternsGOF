from PagamentoInterface import Pagamento

class PagamentoCartao(Pagamento):
    def processar_pagamento(self, valor:float):
       print(f"Processando pagamento de R${valor:.2f} via Cartão de Crédito.")
    
    
class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor:float):
        print(f"Processando pagamento de R${valor:.2f} via Boleto Bancário.")
        pass
    
