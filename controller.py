from ast import Pass
from curses.ascii import isdigit
from ntpath import join
from time import sleep
from model import *
from dal import *
from datetime import datetime, date


class CategoriaController:
    

    def cadastrar_categoria(self, nome):
        try:
            id = proximo_id("categoria.txt")
            CategoriaDal.salvar(Categoria(id, nome))
            return 1
        except:
            return 2
            
    def alterar_categoria(self, cat_alt, novo_nome):
        cats = CategoriaDal.ler()
        cat = list(filter(lambda cats: (cats.id == cat_alt or cats.nome == cat_alt), cats))
        if len(cat) > 0:
            try:
                CategoriaDal.alterar(Categoria(cat[0].id, novo_nome))
                return 1
            except:
                return 2

    def remover_categoria(self, cat_remove):
        cats = CategoriaDal.ler()
        cat = list(filter(lambda cats: (cats.id == cat_remove or cats.nome == cat_remove), cats))
        if len(cat) > 0:
            try:
                CategoriaDal.remover(cat[0])
                return 1
            except:
                return 2

    def existe_categoria(self, cat):
        cats = CategoriaDal.ler()     
        return len(list(filter(lambda cats: (cats.id == cat or cats.nome == cat.upper()), cats))) > 0

    def listar_categorias(self):
        return CategoriaDal.ler()      


class ClienteController:
    

    def cadastrar_cliente(self, nome, cpf_cnpj, telefone, email, endereco):
        try:
            id = proximo_id("cliente.txt")
            ClienteDal.salvar(Cliente(id, nome, cpf_cnpj, telefone, email.lower(), endereco))
            return 1
        except:
            return 2
            
    def alterar_cliente(self, cli_alt, alterar_campos: list):
        clientes = ClienteDal.ler()
        cli = list(filter(lambda clientes: (clientes.id == cli_alt or clientes.cpf_cnpj == cli_alt), clientes))
        if len(cli) > 0:
            cli[0].nome = alterar_campos[0]
            cli[0].cpf_cnpj = alterar_campos[1]
            cli[0].telefone = alterar_campos[2]
            cli[0].email = alterar_campos[3].lower()
            cli[0].endereco = alterar_campos[4]
            try:
                ClienteDal.alterar(cli[0])
                return 1
            except:
                return 2

    def remover_cliente(self, cli_remove):
        clientes = ClienteDal.ler()
        cli = list(filter(lambda clientes: (clientes.id == cli_remove or clientes.cpf_cnpj == cli_remove), clientes))
        if len(cli) > 0:
            try:
                ClienteDal.remover(cli[0])
                return 1
            except:
                return 2
        else:
            return 0

    def existe_cliente(self, cliente):
        cli = ClienteDal.ler()
        return len(list(filter(lambda cli: (cli.id == cliente or cli.cpf_cnpj == cliente), cli))) > 0

    def listar_clientes(self):
        return ClienteDal.ler()


class EstoqueController:


    def adicionar_produto(self, produto: Produto, quantidade: float):
        pass


    def remover_produto(self, produto: Produto, quantidade: float):
        pass


    def listar_estoque(self):
        pass


class FornecedorController:

    
    def cadastrar_fornecedor(self, ie, nome, cpf_cnpj, telefone, email, endereco, categoria_id):
        cats = CategoriaDal.ler()
        cat = list(filter(lambda cats: cats.id == categoria_id, cats))
        try:
            id = proximo_id("fornecedor.txt")
            FornecedorDal.salvar(Fornecedor(id, ie, nome, cpf_cnpj, telefone, email.lower(), endereco, cat[0]))
            return 1
        except:
            return 2

    def alterar_fornecedor(self, fo_alt, alterar_campos: dict):
        forns = FornecedorDal.ler()
        fo = list(filter(lambda forns: (forns.id == fo_alt or forns.cpf_cnpj == fo_alt), forns))
        if len(fo) > 0:
            cats = CategoriaDal.ler()
            if len(alterar_campos["categoria"]) > 0:  # categoria foi alterada
                cat = list(filter(lambda cats: cats.id == alterar_campos["categoria"], cats))
            else:
                cat = list(filter(lambda cats: cats.id == fo[0].categoria, cats))

            fo[0].ie = alterar_campos["ie"]
            fo[0].nome = alterar_campos["nome"]
            fo[0].cpf_cnpj = alterar_campos["cpf_cnpj"]
            fo[0].telefone = alterar_campos["telefone"]
            fo[0].email = alterar_campos["email"].lower()
            fo[0].endereco = alterar_campos["endereco"]
            fo[0].categoria = cat[0]
            try:
                FornecedorDal.alterar(fo[0])
                return 1
            except:
                return 2

    def remover_fornecedor(self, fo_rem):
        forns = FornecedorDal.ler()
        fo = list(filter(lambda forns: (forns.id == fo_rem or forns.cpf_cnpj == fo_rem), forns))
        if len(fo) > 0:
            try:
                FornecedorDal.remover(fo[0])
                return 1
            except:
                return 2

    def listar_fornecedores(self):
        return FornecedorDal.ler()

    def existe_fornecedor(self, forn):
        fo = FornecedorDal.ler()
        return len(list(filter(lambda fo: (fo.id == forn or fo.cpf_cnpj == forn), fo))) > 0


class FuncionarioController:


    def cadastrar_funcionario(self, matricula, nome, cpf, telefone, email, endereco):
        try:
            id = proximo_id("funcionario.txt")
            FuncionarioDal.salvar(Funcionario(id, matricula, nome, cpf, telefone, email.lower(), endereco))
            return 1
        except:
            return 2
            
    def alterar_funcionario(self, fun_alt, alterar_campos: list):
        funcionarios = FuncionarioDal.ler()
        fun = list(filter(lambda funcionarios: (funcionarios.id == fun_alt or funcionarios.cpf_cnpj == fun_alt), funcionarios))
        if len(fun) > 0:
            fun[0].matricula = alterar_campos[0]
            fun[0].nome = alterar_campos[1]
            fun[0].cpf_cnpj = alterar_campos[2]
            fun[0].telefone = alterar_campos[3]
            fun[0].email = alterar_campos[4].lower()
            fun[0].endereco = alterar_campos[5]
            try:
                FuncionarioDal.alterar(fun[0])
                return 1
            except:
                return 2

    def remover_funcionario(self, fun_rem):
        funcionarios = FuncionarioDal.ler()
        fun = list(filter(lambda funcionarios: (funcionarios.id == fun_rem or funcionarios.cpf_cnpj == fun_rem), funcionarios))
        if len(fun) > 0:
            try:
                FuncionarioDal.remover(fun[0])
                return 1
            except:
                return 2

    def listar_funcionarios(self):
        return FuncionarioDal.ler()

    def existe_funcionario(self, func):
        fun = FuncionarioDal.ler()
        return len(list(filter(lambda fun: (fun.id == func or fun.cpf_cnpj == func), fun))) > 0


class ProdutoController:

    
    def cadastrar_produto(self, nome, preco, cat_id):
        cats = CategoriaDal.ler()
        cat = list(filter(lambda cats: cats.id == cat_id, cats))
        try:
            id = proximo_id("produto.txt")
            ProdutoDal.salvar(Produto(id, nome, preco, cat[0]))
            return 1
        except:
            return 2

    def alterar_produto(self, prod_alt, alterar_campos: list):
        prods = ProdutoDal.ler()
        prod = list(filter(lambda prods: (prods.id == prod_alt or prods.nome == prod_alt), prods))
        if len(prod) > 0:
            cats = CategoriaDal.ler()
            if len(alterar_campos[2]) > 0:  # categoria foi alterada
                cat = list(filter(lambda cats: cats.id == alterar_campos[2], cats))
            else:
                cat = list(filter(lambda cats: cats.id == prod[0].categoria, cats))

            prod[0].nome = alterar_campos[0]
            prod[0].preco = alterar_campos[1]
            prod[0].categoria = cat[0]
            try:
                ProdutoDal.alterar(prod[0])
                return 1
            except:
                return 2

    def remover_produto(self, prod_rem):
        prods = ProdutoDal.ler()
        prod = list(filter(lambda prods: (prods.id == prod_rem or prods.nome == prod_rem), prods))
        if len(prod) > 0:
            try:
                ProdutoDal.remover(prod[0])
                return 1
            except:
                return 2

    def listar_produtos(self):
        return ProdutoDal.ler()

    def existe_produto(self, produto):
        prods = ProdutoDal.ler()
        return len(list(filter(lambda prods: (prods.id == produto or prods.nome == produto), prods))) > 0

