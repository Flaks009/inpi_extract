from inpi_request import busca_,busca_pedido,cod_pedido,nome_procurador

def main(cod):
    cod_ = busca_pedido(cod)
    cod_ = cod_pedido(cod_)
    cod_ = busca_(cod_)
    return nome_procurador(cod_)