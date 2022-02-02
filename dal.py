from time import sleep
from model import *


# Obter o id a ser cadastrado
def proximo_id(tabela):
    with open(tabela, "r") as arq:
        lista = arq.readlines()
    return 1 if len(lista) == 0 else int(lista[-1].split('|')[0]) + 1


class CategoriaDal:


    @classmethod
    def salvar(cls, categoria: Categoria):
        with open("categoria.csv", "a") as arq:
            arq.writelines(f"{categoria.id}|{categoria.nome}\n") 

    @classmethod
    def remover(cls, categoria: Categoria):
        cats = cls.ler()
        for i in range(len(cats)):
            if cats[i].id == categoria.id:
                del cats[i]
                break
        
        with open("categoria.csv", "w") as arq:
            for c in cats:
                arq.writelines(f"{c.id}|{c.nome}\n") 

        #TODO: remover a categoria nos produtos relacionados


    @classmethod
    def alterar(cls, categoria: Categoria):
        cats = cls.ler()
        for i in range(len(cats)):
            if cats[i].id == categoria.id:
                cats[i].nome = categoria.nome
                break
        
        with open("categoria.csv", "w") as arq:
            for c in cats:
                arq.writelines(f"{c.id}|{c.nome}\n") 

        #TODO: remover a categoria nos produtos relacionados


    @classmethod
    def ler(cls):
        with open("categoria.csv", "r") as arq:
            cls.categorias = arq.readlines()

        cls.categorias = list(map(lambda x: x.replace("\n", ""), cls.categorias))
        cls.categorias = list(map(lambda x: x.split("|"), cls.categorias))

        cat = []
        for i in cls.categorias:
            cat.append(Categoria(i[0], i[1]))

        return cat
        

class ProdutoDal:


    @classmethod
    def salvar(cls, produto: Produto, categoria: Categoria):
        with open("produto.csv", "a") as arq:
            arq.writelines(f"{produto.id}|{produto.nome}|{produto.preco}|{produto.categoria}\n")


    @classmethod
    def alterar(cls, produto: Produto, categoria: Categoria):
        produtos = cls.ler()
        for p in range(len(produtos)):
            if produtos[p].id == produto.id:
                produtos[p].nome = produto.nome
                produtos[p].preco = produto.preco
                produtos[p].categoria = produto.categoria
                break
        
        with open("produto.csv", "w") as arq:
            for p in produtos:
                arq.writelines(f"{p.id}|{p.nome}|{p.preco}|{p.categoria}\n")


    @classmethod
    def remover(cls, produto: Produto):
        produtos = cls.ler()
        for p in range(len(produtos)):
            if produtos[p].id == produto.id:
                del produtos[p]
                break
        
        with open("produto.csv", "w") as arq:
            for p in produtos:
                arq.writelines(f"{p.id}|{p.nome}|{p.preco}|{p.categoria}\n")

        #TODO: remover produto do estoque


    @classmethod
    def ler(cls):
        with open("produto.csv", "r") as arq:
            cls.produtos = arq.readlines()

        cls.produtos = list(map(lambda x: x.replace("\n", ""), cls.produtos))
        cls.produtos = list(map(lambda x: x.split("|"), cls.produtos))

        prods = []
        for i in cls.produtos:
            prods.append(Produto(i[0], i[1], i[2], i[3]))

        return prods
        

class EstoqueDal:


    @classmethod
    def adicionar(cls, produto: Produto, quantidade):
        with open("estoque.csv", "a") as arq:
            # arq.writelines(f"{produto.id}|{produto.nome}|{produto.preco}|{produto.categoria}\n")
            arq.writelines(f"{produto}|{quantidade}\n")


    @classmethod
    def remover(cls, produto: Produto, quantidade):
        pass


    @classmethod
    def alterar(cls, produto: Produto, quantidade):
        pass


    @classmethod
    def ler(cls):
        pass


class ClienteDal:


    @classmethod
    def salvar(cls, c: Cliente):
        with open("cliente.csv", "a") as arq:
            arq.writelines(f"{c.id}|{c.nome}|{c.cpf_cnpj}|{c.telefone}|{c.email}|{c.endereco}\n")


    @classmethod
    def alterar(cls, c: Cliente):
        clientes = cls.ler()
        for x in range(len(clientes)):
            if clientes[x].id == c.id:
                clientes[x].nome = c.nome if len(c.nome) > 0 else clientes[x].nome
                clientes[x].cpf_cnpj = c.cpf_cnpj if len(c.cpf_cnpj) > 0 else clientes[x].cpf_cnpj
                clientes[x].telefone = c.telefone if len(c.telefone) > 0 else clientes[x].telefone
                clientes[x].email = c.email if len(c.email) > 0 else clientes[x].email
                clientes[x].endereco = c.endereco if len(c.endereco) > 0 else clientes[x].endereco
                break
        
        with open("cliente.csv", "w") as arq:
            for c in clientes:
                arq.writelines(f"{c.id}|{c.nome}|{c.cpf_cnpj}|{c.telefone}|{c.email}|{c.endereco}\n")


    @classmethod
    def remover(cls, c: Cliente):
        clientes = cls.ler()
        for x in range(len(clientes)):
            if clientes[x].id == c.id:
                del clientes[x]
                break

        with open("cliente.csv", "w") as arq:
            for c in clientes:
                arq.writelines(f"{c.id}|{c.nome}|{c.cpf_cnpj}|{c.telefone}|{c.email}|{c.endereco}\n")


    @classmethod
    def ler(cls):
        with open("cliente.csv", "r") as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace("\n", ""), cls.clientes))
        cls.clientes = list(map(lambda x: x.split("|"), cls.clientes))

        cli = []
        for i in cls.clientes:
            cli.append(Cliente(i[0], i[1], i[2], i[3], i[4], i[5]))

        return cli


class FuncionarioDal:


    @classmethod
    def salvar(cls, func: Funcionario):
        with open("funcionario.csv", "a") as arq:
            arq.writelines(f"{func.id}|{func.matricula}|{func.nome}|{func.cpf_cnpj}|{func.telefone}|{func.email}|{func.endereco}\n")


    @classmethod
    def alterar(cls, func: Funcionario):
        funcionarios = cls.ler()
        for x in range(len(funcionarios)):
            if funcionarios[x].id == func.id:
                funcionarios[x].matricula = func.matricula
                funcionarios[x].nome = func.nome
                funcionarios[x].cpf_cnpj = func.cpf_cnpj
                funcionarios[x].telefone = func.telefone
                funcionarios[x].email = func.email
                funcionarios[x].endereco = func.endereco
                break
        
        with open("funcionario.csv", "w") as arq:
            for x in funcionarios:
                arq.writelines(f"{x.id}|{x.matricula}|{x.nome}|{x.cpf_cnpj}|{x.telefone}|{x.email}|{x.endereco}\n")


    @classmethod
    def remover(cls, func: Funcionario):
        funcionarios = cls.ler()
        for x in range(len(funcionarios)):
            if funcionarios[x].id == func.id:
                del funcionarios[x]
                break

        with open("funcionario.csv", "w") as arq:
            for x in funcionarios:
                arq.writelines(f"{x.id}|{x.matricula}|{x.nome}|{x.cpf_cnpj}|{x.telefone}|{x.email}|{x.endereco}\n")


    @classmethod
    def ler(cls):
        with open("funcionario.csv", "r") as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace("\n", ""), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split("|"), cls.funcionarios))

        funcs = []
        for i in cls.funcionarios:
            funcs.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        return funcs


class FornecedorDal:


    @classmethod
    def salvar(cls, forn: Fornecedor):
        with open("fornecedor.csv", "a") as arq:
            arq.writelines(
                f"{forn.id}|{forn.ie}|{forn.nome}|{forn.cpf_cnpj}|{forn.telefone}|{forn.email}|{forn.endereco}|{forn.categoria}\n"
            )


    @classmethod
    def alterar(cls, forn: Fornecedor):
        fornecedores = cls.ler()
        for x in range(len(fornecedores)):
            if fornecedores[x].id == forn.id:
                fornecedores[x].ie = forn.ie
                fornecedores[x].nome = forn.nome
                fornecedores[x].cpf_cnpj = forn.cpf_cnpj
                fornecedores[x].telefone = forn.telefone
                fornecedores[x].email = forn.email
                fornecedores[x].endereco = forn.endereco
                fornecedores[x].categoria = forn.categoria
                break
        
        with open("fornecedor.csv", "w") as arq:
            for x in fornecedores:
                arq.writelines(
                    f"{forn.id}|{forn.ie}|{forn.nome}|{forn.cpf_cnpj}|{forn.telefone}|{forn.email}|{forn.endereco}|{forn.categoria}\n"
                )


    @classmethod
    def remover(cls, forn: Fornecedor):
        fornecedores = cls.ler()
        for x in range(len(fornecedores)):
            if fornecedores[x].id == forn.id:
                del fornecedores[x]
                break

        with open("fornecedor.csv", "w") as arq:
            for x in fornecedores:
                arq.writelines(
                    f"{forn.id}|{forn.ie}|{forn.nome}|{forn.cpf_cnpj}|{forn.telefone}|{forn.email}|{forn.endereco}|{forn.categoria}\n"
                )


    @classmethod
    def ler(cls):
        with open("fornecedor.csv", "r") as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace("\n", ""), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split("|"), cls.fornecedores))

        forns = []
        for i in cls.fornecedores:
            forns.append(Fornecedor(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

        return forns


class VendaDal:


    @classmethod
    def salvar(cls, v: Venda):
        with open("venda.csv", "a") as arq:
            arq.writelines(f"{v.id}|{v.vendedor}|{v.comprador}|{v.itens}|{v.quantidade}|{v.data}\n")


    @classmethod
    def alterar(cls, v: Venda):
        vendas = cls.ler()
        for x in range(len(vendas)):
            if vendas[x].id == v.id:
                vendas[x].vendedor = v.vendedor
                vendas[x].comprador = v.comprador
                vendas[x].itens = v.itens
                vendas[x].quantidade = v.quantidade
                vendas[x].data = v.data
                break
        
        with open("venda.csv", "w") as arq:
            for v in vendas:
                arq.writelines(f"{v.id}|{v.vendedor}|{v.comprador}|{v.itens}|{v.quantidade}|{v.data}\n")


    @classmethod
    def remover(cls, v: Venda):
        vendas = cls.ler()
        for x in range(len(vendas)):
            if vendas[x].id == v.id:
                del vendas[x]
                break

        with open("venda.csv", "w") as arq:
            for v in vendas:
                arq.writelines(f"{v.id}|{v.vendedor}|{v.comprador}|{v.itens}|{v.quantidade}|{v.data}\n")


    @classmethod
    def ler(cls):
        with open("venda.csv", "r") as arq:
            cls.vendas = arq.readlines()

        cls.vendas = list(map(lambda x: x.replace("\n", ""), cls.vendas))
        cls.vendas = list(map(lambda x: x.split("|"), cls.vendas))

        vends = []
        for i in cls.vendas:
            vends.append(Venda(i[0], i[1], i[2], i[3], i[4], i[5]))

        return vends
