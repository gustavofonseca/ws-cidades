# coding: utf8

from cidades import BD
from cidades import cidades_do_estado
from cidades import qtd_cidades
from cidades import listar_estados

def teste_carregar():
    fixture = open('fixture.txt')
    BD.carregar(fixture)
    fixture.close()

def teste_qtd_cidades():
    assert qtd_cidades() == 8, qtd_cidades()


def teste_cidades_por_estado():
    cidades = cidades_do_estado('Rondônia')
    assert len(cidades) == 3
    assert "Alta Floresta D'Oeste" in cidades

def teste_estados():
    estados = listar_estados()
    assert len(estados) == 3
    assert estados == ['Distrito Federal', 'Pará', 'Rondônia']


