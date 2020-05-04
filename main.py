from inpi_request_patente import busca_ as busca_patente
from inpi_request_patente import busca_pedido as busca_pedido_patente
from inpi_request_patente import cod_pedido as cod_pedido_patente
from inpi_request_patente import nome_procurador as nome_procurador_patente
from inpi_request_desenho import busca_ as busca_desenho
from inpi_request_desenho import busca_pedido as busca_pedido_desenho
from inpi_request_desenho import cod_pedido as cod_pedido_desenho
from inpi_request_desenho import nome_procurador as nome_procurador_desenho

def main_patente(cod):
    print(cod)
    cod_ = busca_pedido_patente(cod)
    cod_ = cod_pedido_patente(cod_)
    cod_ = busca_patente(cod_)
    nome = nome_procurador_patente(cod_)
    print(nome)
    return 


def main_desenho(cod):
    print(cod)
    cod_ = busca_pedido_desenho(cod)
    cod_ = cod_pedido_desenho(cod_)
    cod_ = busca_desenho(cod_)
    nome = nome_procurador_patente(cod_)
    print(nome)
    return nome
