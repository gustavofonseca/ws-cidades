# coding: utf8

class BD(object):
    estados = {}
    qtd_cidades = 0

    @classmethod
    def carregar(cls, arq):
        linhas = [l.strip() for l in list(arq) if l.strip()]
        for linha in linhas:
            estado, cod, cidade = linha.split('\t')
            cls.estados.setdefault(estado, []).append(cidade)

            cls.qtd_cidades += 1

# Web services

def qtd_cidades():
    return BD.qtd_cidades

def cidades_do_estado(estado):
    return BD.estados[estado]

def listar_estados():
    return sorted(BD.estados.keys())