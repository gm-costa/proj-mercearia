from datetime import datetime, date


class Categoria:

    # id = 0

    def __init__(self, id, nome):
        self.id = id    # Categoria.id += 1
        self.nome = nome


class Produto:

    def __init__(self, id, nome, preco, categoria: Categoria):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


class Estoque:

    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Venda:

    def __init__(self, id, vendedor, comprador, itens: Produto, quantidade, data = datetime.now()):
        sefl.id = id
        self.data = data 
        self.vendedor = vendedor
        self.comprador = comprador
        self.itens = itens
        self.quantidade = quantidade


class Pessoa:

    def __init__(self, nome, cpf_cnpj, telefone, email, endereco):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.telefone = telefone
        self.email = email
        self.endereco = endereco


class Fornecedor(Pessoa):

    def __init__(self, id, ie, nome, cpf_cnpj, telefone, email, endereco, categoria: Categoria):
        self.id = id
        self.ie = ie
        self.categoria = categoria
        super(Fornecedor, self).__init__(nome, cpf_cnpj, telefone, email, endereco)


class Cliente(Pessoa):

    def __init__(self, id, nome, cpf_cnpj, telefone, email, endereco):
        self.id = id
        super(Cliente, self).__init__(nome, cpf_cnpj, telefone, email, endereco)


class Funcionario(Pessoa):

    def __init__(self, id, matricula, nome, cpf_cnpj, telefone, email, endereco):
        self.id = id
        self.matricula = matricula
        super(Funcionario, self).__init__(nome, cpf_cnpj, telefone, email, endereco)
