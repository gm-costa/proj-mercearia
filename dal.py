from model import *


# Obter o id a ser cadastrado
def proximo_id(tabela):
    with open(tabela, "r") as arq:
        lista = arq.readlines()
    return 1 if len(lista) == 0 else int(lista[-1].split('|')[0]) + 1


class CategoriaDal:

    @classmethod
    def salvar(cls, categoria: Categoria):
        tabela = "categoria.csv"
        id = proximo_id(tabela)
        with open(tabela, "a") as arq:
            arq.writelines(f"{id}|{categoria.nome}\n") 

    @classmethod
    def ler(cls):
        with open("categoria.csv", "r") as arq:
            cls.categorias = arq.readlines()
        return cls.categorias