from time import sleep
from model import *
from dal import *
from datetime import datetime, date


class CategoriaController:
    

    def cadastrar_categoria(self, nome):
        existe = False
        cats = CategoriaDal.ler()
        for c in cats:
            if c.nome == nome:
                existe = True
                break
        
        if not existe:
            try:
                id = proximo_id("categoria.csv")
                CategoriaDal.salvar(Categoria(id, nome))
                return 1
            except:
                return 2
        else:
            return 0
            

    def remover_categoria(self, nome):
        cats = CategoriaDal.ler()
        cat = list(filter(lambda cats: cats.nome == nome, cats))
        if len(cat) > 0:
            try:
                CategoriaDal.remover(Categoria(cat[0].id, nome))
                return 1
            except:
                return 2
        else:
            return 0


    def alterar_categoria(self, nome, novo_nome):
        cats = CategoriaDal.ler()
        cat = list(filter(lambda cats: cats.nome == nome, cats))
        if len(cat) > 0:
            try:
                CategoriaDal.alterar(Categoria(cat[0].id, novo_nome))
                return 1
            except:
                return 2
        else:
            return 0

    def listar_categorias(self):
        cat = CategoriaDal.ler()
        # print(f"tipo catDal: {type(cat)}")
        if len(cat) > 0:
            print("-" * 40)
            print("Categorias Cadastradas".center(40, " "))
            print("-" * 40)
            for c in cat:
                print(f"{c.id}\t{c.nome}")
            print("-" * 40)
        else:
            print("Não há categorias cadastradas.")        


class ClienteController:
    

    def cadastrar_cliente(self, nome, cpf_cnpj, telefone, email, endereco):
        existe = False
        clientes = ClienteDal.ler()
        for c in clientes:
            if c.nome == nome:
                existe = True
                break
        
        if not existe:
            try:
                id = proximo_id("cliente.csv")
                ClienteDal.salvar(Cliente(id, nome, cpf_cnpj, telefone, email, endereco))
                return 1
            except:
                return 2
        else:
            return 0
            

    def alterar_cliente(self, nome, alterar_campos: list):
        clientes = ClienteDal.ler()
        cli = list(filter(lambda clientes: clientes.nome == nome, clientes))
        if len(cli) > 0:
            cli[0].nome = alterar_campos[0]
            cli[0].cpf_cnpj = alterar_campos[1]
            cli[0].telefone = alterar_campos[2]
            cli[0].email = alterar_campos[3]
            cli[0].endereco = alterar_campos[4]
            try:
                ClienteDal.alterar(cli[0])
                return 1
            except:
                return 2
        else:
            return 0


    def remover_cliente(self, nome):
        clientes = ClienteDal.ler()
        cli = list(filter(lambda clientes: clientes.nome == nome, clientes))
        if len(cli) > 0:
            try:
                # ClienteDal.remover(Cliente(cli[0].id, nome))
                ClienteDal.remover(cli[0])
                return 1
            except:
                return 2
        else:
            return 0


    def listar_clientes(self):
        cli = ClienteDal.ler()
        if len(cli) > 0:
            print("-" * 120)
            print("Clientes Cadastrados".center(120, " "))
            print("-" * 120)
            print(f"{'ID':5}{'NOME':25}{'CPF/CNPJ':16}{'TELEFONE':14}{'E-MAIL':25}{'ENDEREÇO'}")
            print("-" * 120)
            for c in cli:
                print(f"{c.id:5}{c.nome:25}{c.cpf_cnpj:16}{c.telefone:14}{c.email:25}{c.endereco}")
            print("-" * 120)
        else:
            print("Não há clientes cadastrados.")        


class EstoqueController:


    def adicionar_produto(self, produto: Produto, quantidade: float):
        pass


    def remover_produto(self, produto: Produto, quantidade: float):
        pass


    def listar_estoque(self):
        pass


