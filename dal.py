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
        with open("categoria.txt", "a") as arq:
            arq.writelines(f"{categoria.id}|{categoria.nome}\n") 

    @classmethod
    def alterar(cls, categoria: Categoria):
        cats = cls.ler()
        for i in range(len(cats)):
            if cats[i].id == categoria.id:
                cats[i].nome = categoria.nome
                break
        
        with open("categoria.txt", "w") as arq:
            for c in cats:
                arq.writelines(f"{c.id}|{c.nome}\n") 

        #TODO: remover a categoria nos produtos relacionados

    @classmethod
    def remover(cls, categoria: Categoria):
        cats = cls.ler()
        for i in range(len(cats)):
            if cats[i].id == categoria.id:
                del cats[i]
                break
        
        with open("categoria.txt", "w") as arq:
            for c in cats:
                arq.writelines(f"{c.id}|{c.nome}\n") 

        #TODO: remover a categoria nos produtos relacionados

    @classmethod
    def ler(cls):
        with open("categoria.txt", "r") as arq:
            cls.categorias = arq.readlines()

        cls.categorias = list(map(lambda x: x.replace("\n", ""), cls.categorias))
        cls.categorias = list(map(lambda x: x.split("|"), cls.categorias))

        cat = []
        for i in cls.categorias:
            cat.append(Categoria(i[0], i[1]))

        return cat
             

class EstoqueDal:


    @classmethod
    def adicionar(cls, produto: Produto, quantidade):
        with open("estoque.txt", "a") as arq:
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
        with open("cliente.txt", "a") as arq:
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
        
        with open("cliente.txt", "w") as arq:
            for cl in clientes:
                arq.writelines(f"{cl.id}|{cl.nome}|{cl.cpf_cnpj}|{cl.telefone}|{cl.email}|{cl.endereco}\n")

    @classmethod
    def remover(cls, c: Cliente):
        clientes = cls.ler()
        for x in range(len(clientes)):
            if clientes[x].id == c.id:
                del clientes[x]
                break

        with open("cliente.txt", "w") as arq:
            for c in clientes:
                arq.writelines(f"{c.id}|{c.nome}|{c.cpf_cnpj}|{c.telefone}|{c.email}|{c.endereco}\n")

    @classmethod
    def ler(cls):
        with open("cliente.txt", "r") as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace("\n", ""), cls.clientes))
        cls.clientes = list(map(lambda x: x.split("|"), cls.clientes))

        cli = []
        for i in cls.clientes:
            cli.append(Cliente(i[0], i[1], i[2], i[3], i[4], i[5]))

        return cli


class FornecedorDal:


    @classmethod
    def salvar(cls, forn: Fornecedor):
        with open("fornecedor.txt", "a") as arq:
            arq.writelines(
                f"{forn.id}|{forn.ie}|{forn.nome}|{forn.cpf_cnpj}|{forn.telefone}|" 
                + f"{forn.email}|{forn.endereco}|{forn.categoria.id}\n"
            )

    @classmethod
    def alterar(cls, forn: Fornecedor):
        fo = cls.ler()
        for x in range(len(fo)):
            if fo[x].id == forn.id:
                fo[x].ie = forn.ie if len(forn.ie) > 0 else fo[x].ie
                fo[x].nome = forn.nome if len(forn.nome) > 0 else fo[x].nome
                fo[x].cpf_cnpj = forn.cpf_cnpj if len(forn.cpf_cnpj) > 0 else fo[x].cpf_cnpj
                fo[x].telefone = forn.telefone if len(forn.telefone) > 0 else fo[x].telefone
                fo[x].email = forn.email if len(forn.email) > 0 else fo[x].email
                fo[x].endereco = forn.endereco if len(forn.endereco) > 0 else fo[x].endereco
                fo[x].categoria = forn.categoria.id
                break

        with open("fornecedor.txt", "w") as arq:
            for f in fo:
                arq.writelines(
                    f"{f.id}|{f.ie}|{f.nome}|{f.cpf_cnpj}|{f.telefone}|{f.email}|{f.endereco}|{f.categoria}\n"
                )

    @classmethod
    def remover(cls, forn: Fornecedor):
        fornecedores = cls.ler()
        for x in range(len(fornecedores)):
            if fornecedores[x].id == forn.id:
                del fornecedores[x]
                break

        with open("fornecedor.txt", "w") as arq:
            for f in fornecedores:
                arq.writelines(
                    f"{f.id}|{f.ie}|{f.nome}|{f.cpf_cnpj}|{f.telefone}|{f.email}|{f.endereco}|{f.categoria}\n"
                )

    @classmethod
    def ler(cls):
        with open("fornecedor.txt", "r") as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace("\n", ""), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split("|"), cls.fornecedores))

        forns = []
        for i in cls.fornecedores:
            forns.append(Fornecedor(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

        return forns


class FuncionarioDal:


    @classmethod
    def salvar(cls, f: Funcionario):
        with open("funcionario.txt", "a") as arq:
            arq.writelines(f"{f.id}|{f.matricula}|{f.nome}|{f.cpf_cnpj}|{f.telefone}|{f.email}|{f.endereco}\n")

    @classmethod
    def alterar(cls, f: Funcionario):
        funcs = cls.ler()
        for x in range(len(funcs)):
            if funcs[x].id == f.id:
                funcs[x].matricula = f.matricula if len(f.matricula) > 0 else funcs[x].matricula
                funcs[x].nome = f.nome if len(f.nome) > 0 else funcs[x].nome
                funcs[x].cpf_cnpj = f.cpf_cnpj if len(f.cpf_cnpj) > 0 else funcs[x].cpf_cnpj
                funcs[x].telefone = f.telefone if len(f.telefone) > 0 else funcs[x].telefone
                funcs[x].email = f.email.lower() if len(f.email) > 0 else funcs[x].email.lower()
                funcs[x].endereco = f.endereco if len(f.endereco) > 0 else funcs[x].endereco
                break
        
        with open("funcionario.txt", "w") as arq:
            for x in funcs:
                arq.writelines(f"{x.id}|{x.matricula}|{x.nome}|{x.cpf_cnpj}|{x.telefone}|{x.email}|{x.endereco}\n")

    @classmethod
    def remover(cls, func: Funcionario):
        funcionarios = cls.ler()
        for x in range(len(funcionarios)):
            if funcionarios[x].id == func.id:
                del funcionarios[x]
                break

        with open("funcionario.txt", "w") as arq:
            for x in funcionarios:
                arq.writelines(f"{x.id}|{x.matricula}|{x.nome}|{x.cpf_cnpj}|{x.telefone}|{x.email}|{x.endereco}\n")

    @classmethod
    def ler(cls):
        with open("funcionario.txt", "r") as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace("\n", ""), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split("|"), cls.funcionarios))

        funcs = []
        for i in cls.funcionarios:
            funcs.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        return funcs


class ProdutoDal:


    @classmethod
    def salvar(cls, produto: Produto):
        with open("produto.txt", "a") as arq:
            arq.writelines(f"{produto.id}|{produto.nome}|{produto.preco}|{produto.categoria.id}\n")

    @classmethod
    def alterar(cls, produto: Produto):
        prods = cls.ler()
        for x in range(len(prods)):
            if prods[x].id == produto.id:
                prods[x].nome = produto.nome if len(produto.nome) > 0 else prods[x].nome
                prods[x].preco = produto.preco if len(produto.preco) > 0 else prods[x].preco
                prods[x].categoria = produto.categoria.id
                break
        
        with open("produto.txt", "w") as arq:
            for p in prods:
                arq.writelines(f"{p.id}|{p.nome}|{p.preco}|{p.categoria}\n")

    @classmethod
    def remover(cls, produto: Produto):
        produtos = cls.ler()
        for x in range(len(produtos)):
            if produtos[x].id == produto.id:
                del produtos[x]
                break
        
        with open("produto.txt", "w") as arq:
            for p in produtos:
                arq.writelines(f"{p.id}|{p.nome}|{p.preco}|{p.categoria}\n")

        #TODO: remover produto do estoque

    @classmethod
    def ler(cls):
        with open("produto.txt", "r") as arq:
            cls.produtos = arq.readlines()

        cls.produtos = list(map(lambda x: x.replace("\n", ""), cls.produtos))
        cls.produtos = list(map(lambda x: x.split("|"), cls.produtos))

        prods = []
        for i in cls.produtos:
            prods.append(Produto(i[0], i[1], i[2], i[3]))

        return prods


class VendaDal:


    @classmethod
    def salvar(cls, v: Venda):
        with open("venda.txt", "a") as arq:
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
        
        with open("venda.txt", "w") as arq:
            for v in vendas:
                arq.writelines(f"{v.id}|{v.vendedor}|{v.comprador}|{v.itens}|{v.quantidade}|{v.data}\n")


    @classmethod
    def remover(cls, v: Venda):
        vendas = cls.ler()
        for x in range(len(vendas)):
            if vendas[x].id == v.id:
                del vendas[x]
                break

        with open("venda.txt", "w") as arq:
            for v in vendas:
                arq.writelines(f"{v.id}|{v.vendedor}|{v.comprador}|{v.itens}|{v.quantidade}|{v.data}\n")


    @classmethod
    def ler(cls):
        with open("venda.txt", "r") as arq:
            cls.vendas = arq.readlines()

        cls.vendas = list(map(lambda x: x.replace("\n", ""), cls.vendas))
        cls.vendas = list(map(lambda x: x.split("|"), cls.vendas))

        vends = []
        for i in cls.vendas:
            vends.append(Venda(i[0], i[1], i[2], i[3], i[4], i[5]))

        return vends
