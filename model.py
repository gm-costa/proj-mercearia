from datetime import datetime, date


class Categoria:

    def __init__(self, nome):
        self.nome = nome


class Produto:

    def __init__(self, categoria, nome, preco):
        self.categoria = categoria
        self.nome = nome
        self.preco = preco


class Estoque:

    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Venda:

    def __init__(self, vendedor, comprador, itens: Produto, quantidade, data = datetime.now())
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

    def __init__(self, categoria, ie, nome, cpf_cnpj, telefone, email, endereco):
        self.categoria = categoria
        self.ie = ie
        super(Fornecedor, self).__init__(nome, cpf_cnpj, telefone, email, endereco)


class Cliente(Pessoa):

    def __init__(self, nome, cpf_cnpj, telefone, email, endereco):
        super(Cliente, self).__init__(nome, cpf_cnpj, telefone, email, endereco)


class Funcionario(Pessoa):

    def __init__(self, matricula, nome, cpf_cnpj, telefone, email, endereco):
        self.matricula = matricula
        super(Funcionario, self).__init__(nome, cpf_cnpj, telefone, email, endereco)

