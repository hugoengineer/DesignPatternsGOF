from Pagamento import PagamentoCartao, PagamentoBoleto

def PagamentoFactory(tipo:str):
    if tipo == "cartao":
        return PagamentoCartao()
    if tipo == "boleto":
        return PagamentoBoleto()
    
if __name__ == "__main__":
    pagamento1 = PagamentoFactory("cartao")
    pagamento1.processar_pagamento(150.0)
    pagamento2 = PagamentoFactory("boleto")
    pagamento2.processar_pagamento(200.0)