from model import *
from dal import *
from datetime import datetime


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

    @staticmethod
    def existe_categoria(cat):
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

    @staticmethod
    def existe_cliente(cliente):
        cli = ClienteDal.ler()
        return len(list(filter(lambda cli: (cli.id == cliente or cli.cpf_cnpj == cliente), cli))) > 0

    def listar_clientes(self):
        return ClienteDal.ler()


class EstoqueController:


    def adicionar_estoque(self, produto, quantidade: float):
        produtos = ProdutoDal.ler()
        prod = list(filter(lambda produtos: produtos.id == produto, produtos))
        if len(prod) > 0:
            try:
                EstoqueDal.adicionar(prod[0], quantidade)
                return 1
            except:
                return 2

    def alterar_estoque(self, produto, quantidade: float):
        produtos = ProdutoDal.ler()
        prod = list(filter(lambda produtos: produtos.id == produto, produtos))
        if len(prod) > 0:
            try:
                EstoqueDal.alterar(prod[0], quantidade)
                return 1
            except:
                return 2

    def remover_estoque(self, produto):
        produtos = ProdutoDal.ler()
        prod = list(filter(lambda produtos: produtos.id == produto, produtos))
        if len(prod) > 0:
            try:
                EstoqueDal.remover(prod[0])
                return 1
            except:
                return 2

    def cadastrar_produto_estoque(self, prod_nome, prod_preco, prod_cat, quantidade: float):
        if ProdutoController.cadastrar_produto(self, prod_nome, prod_preco, prod_cat) == 1:
            produtos = ProdutoDal.ler()
            prod = list(filter(lambda produtos: produtos.nome == prod_nome, produtos))
            return self.adicionar_estoque(prod[0].id, quantidade)
        else:
            return 2    

    @staticmethod
    def existe_estoque(produto):
        ests = EstoqueDal.ler()
        est = list(filter(lambda ests: (ests.produto.id == produto or ests.produto.nome == produto), ests))
        return len(est) > 0

    @staticmethod
    def get_quantidade(produto):
        ests = EstoqueDal.ler()
        est = list(filter(lambda ests: (ests.produto.id == produto or ests.produto.nome == produto), ests))
        if len(est) > 0:
            return float(est[0].quantidade)
        else:
            return 0

    def listar_estoque(self):
        return EstoqueDal.ler()


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

    @staticmethod
    def existe_fornecedor(forn):
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

    @staticmethod
    def existe_funcionario(func):
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
                cat = list(filter(lambda cats: cats.id == prod[0].categoria.id, cats))

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

    @staticmethod
    def existe_produto(produto):
        prods = ProdutoDal.ler()
        return len(list(filter(lambda prods: (prods.id == produto or prods.nome == produto), prods))) > 0

    @staticmethod
    def existe_produto_com_categoria(categoria):
        cats = CategoriaDal.ler()
        cat = list(filter(lambda cats: (cats.id == categoria or cats.nome == categoria), cats))
        if len(cat) > 0:
            prods = ProdutoDal.ler()
            for x in range(len(prods)):
                if prods[x].categoria.id == cat[0].id:
                    return True
            return False


class VendaController:


    def cadastrar_venda(self, vendedor, comprador, produto, quantidade):
        funcs = FuncionarioDal.ler()
        fun = list(filter(lambda funcs: (funcs.id == vendedor or funcs.nome == vendedor), funcs))
        clientes = ClienteDal.ler()
        cli = list(filter(lambda clientes: (clientes.id == comprador or clientes.nome == comprador), clientes))
        prods = ProdutoDal.ler()
        prod = list(filter(lambda prods: (prods.id == produto or prods.nome == produto), prods))
        try:
            id = proximo_id("venda.txt")
            VendaDal.salvar(Venda(id, fun[0], cli[0], prod[0], quantidade))
            EstoqueDal.alterar(prod[0], quantidade, "V")     # diminuir a quantidade do estoque
            return 1
        except:
            return 2

    # def alterar_venda(self, venda_id, vendedor, comprador, produto, quantidade):
    #     vendas = VendaDal.ler()
    #     venda = list(filter(lambda vendas: vendas.id == venda_id, vendas))
    #     if len(venda) > 0:
    #         funcs = FuncionarioDal.ler()
    #         fun = list(filter(lambda funcs: funcs.id == vendedor, funcs))
    #         clientes = ClienteDal.ler()
    #         cli = list(filter(lambda clientes: clientes.id == comprador, clientes))
    #         prods = ProdutoDal.ler()
    #         prod = list(filter(lambda prods: prods.id == produto, prods))
    #         venda[0].vendedor = fun[0]
    #         venda[0].comprador = cli[0]
    #         venda[0].produto = prod[0]
    #         venda[0].quantidade = quantidade
    #         try:
    #             VendaDal.alterar(venda[0])
    #             return 1
    #         except:
    #             return 2

    def remover_venda(self, venda_id):
        vendas = VendaDal.ler()
        venda = list(filter(lambda vendas: vendas.id == venda_id, vendas))
        if len(venda) > 0:
            try:
                VendaDal.remover(venda[0])
                EstoqueDal.alterar(venda[0].produto, venda[0].quantidade, "C")     # aumentar a quantidade do estoque
                return 1
            except:
                return 2

    def listar_vendas(self):
        return VendaDal.ler()

    @staticmethod
    def existe_venda(venda_id):
        vendas = VendaDal.ler()
        return len(list(filter(lambda vendas: vendas.id == venda_id, vendas))) > 0
