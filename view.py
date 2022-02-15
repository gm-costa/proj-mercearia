from curses.ascii import isdigit
from os import path, system
from time import sleep
from datetime import datetime
from controller import *


lst_classes = ["categoria", "cliente", "estoque", "fornecedor", 
               "funcionario", "produto", "venda"]


def limpa_tela():
    system("clear") or None


def criaArquivo():

    for x in lst_classes:
        if not path.exists(x + ".txt"):
            with open(x + ".txt", "w") as arq:
                arq.write("")


def menu(opcao, *args):

    limpa_tela()
    mnu = "MENU PRINCIPAL" if opcao == 0 else lst_classes[opcao - 1]

    print("-" * 60)
    print(f"{mnu.upper().center(60, ' ')}")
    print("-" * 60)
    i = 1
    if opcao == 0:
        for x in lst_classes:
            print(f"[ {i} ] Para {x.capitalize()}")
            i += 1
        print("[ 9 ] Para Sair")
    else:
        opc = ["cadastrar", "alterar", "remover"]
        if len(args) > 0:
            for a in args:
                opc.append(a)

        for o in opc:
            print(f"[ {i} ] Para {o.capitalize()}")
            i += 1
        print("[ 8 ] Para Retornar ao Menu Principal")
        print("[ 9 ] Para Sair do Sistema")

    print()


def pausar(texto):
    print("\n" + texto)
    sleep(1.5)


def cabecalho(texto, campos, largura = 60):
    print("-" * largura)
    print(f"{texto.center(largura, ' ')}")
    print("-" * largura)
    print(campos)
    # print(f"{campos}")
    print("-" * largura)


def encerrar_sistema():
    sai = input("\nConfirma o encerramento do sistema? [S/n] ").strip().upper()
    if len(sai) == 0 or sai[0] == 'S':
        quit()


if __name__ == "__main__":

    while True:
        menu(0)
        try:
            opcao = int(input("Informe a sua opção: "))

            if opcao == 9:
                break

            if opcao < 1 or opcao > 7:
                pausar("Opção inválida, tente novamente!")
                continue

            criaArquivo()

            if opcao == 1:
                cat = CategoriaController()
                while True:
                    menu(opcao, "Mostrar categorias cadastradas")
                    try:
                        op_1 = int(input("Informe a sua opção: "))

                        if op_1 == 9:
                            encerrar_sistema()
                            continue

                        if op_1 == 8:
                            break

                        if op_1 == 1:
                            cat_nome = input("\nInforme o nome da categoria que deseja cadastrar: ").strip().upper()
                            if len(cat_nome) == 0:
                                pausar("O nome da categoria não foi informado!")
                            elif cat.existe_categoria(cat_nome):
                                pausar("Categoria já cadastrada, tente novamente.")
                            else:
                                retorno = cat.cadastrar_categoria(cat_nome)
                                if retorno == 1:
                                    pausar("Categoria cadastrada com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível cadastrar a categoria.")
                        
                        elif op_1 == 2:
                            cat_busca = input("\nInforme o código ou nome da categoria que deseja alterar: ").strip().upper()
                            if len(cat_busca) == 0:
                                pausar("Categoria não informada!")
                            elif not cat.existe_categoria(cat_busca):
                                pausar("Categoria inexistente no cadastro, tente novamente.")
                            else:
                                cat_novonome = input("\nInforme o novo nome para a categoria: ").strip().upper()
                                if len(cat_novonome) > 0:
                                    retorno = cat.alterar_categoria(cat_busca, cat_novonome)
                                    if retorno == 1:
                                        pausar("Categoria alterada com sucesso.")
                                    elif retorno == 2:
                                        pausar("Ocorreu um erro, não foi possível alterar a categoria.")
                                else:
                                    pausar("O 'novo nome' para a categoria não foi informado!")

                        elif op_1 == 3:
                            cat_busca = input("\nInforme o código ou nome da categoria que deseja remover: ").strip().upper()
                            if len(cat_busca) == 0:
                                pausar("Categoria não informada!")
                            elif not cat.existe_categoria(cat_busca):
                                pausar("Categoria inexistente no cadastro, tente novamente.")
                            elif ProdutoController.existe_produto_com_categoria(cat_busca):
                                pausar("Categoria não pode ser removida, pois existe produto com essa categoria.")
                            else:
                                retorno = cat.remover_categoria(cat_busca)
                                if retorno == 1:
                                    pausar("Categoria removida com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível remover a categoria.")

                        elif op_1 == 4:
                            limpa_tela()
                            cats = cat.listar_categorias()
                            if len(cats) > 0:
                                campos = f" {'ID':3} {'NOME'}"
                                cabecalho("Categorias Cadastradas", campos)
                                for c in cats:
                                    print(f" {c.id:3} {c.nome}")
                                print("-" * 60)
                            else:
                                print("Não há categorias cadastradas.")        
                            input("\nTecle <Enter> para continuar ... ")
                        else:
                            pausar("Opção inválida, tente novamente.")

                    except ValueError:
                        pausar("Opção inválida!")

            if opcao == 2:
                cli = ClienteController()
                while True:
                    menu(opcao, "Mostrar clientes cadastrados")
                    try:
                        op_2 = int(input("Informe a sua opção: "))

                        if op_2 == 9:
                            encerrar_sistema()
                            continue

                        if op_2 == 8:
                            break

                        if op_2 == 1:
                            print("\nInforme os dados do cliente que deseja cadastrar")
                            cli_doc = input("\nCPF/CNPJ: ").strip()
                            if (len(cli_doc) < 11) or (len(cli_doc) > 14) or (len(cli_doc) == 12) \
                                    or (len(cli_doc) == 13) or (not cli_doc.isdigit()):
                                pausar("CPF/CNPJ inválido!")
                            elif cli.existe_cliente(cli_doc):
                                pausar("Cliente já cadastrado, tente novamente.")
                            else:
                                cli_nome = input("Nome: ").strip().upper()
                                cli_tel = input("Telefone: ").strip().upper()
                                cli_email = input("E-mail: ").strip().lower()
                                cli_end = input("Endereço: ").strip().upper()
                                if len(cli_nome) == 0:
                                    pausar("O nome não foi informado!")
                                elif len(cli_tel) < 10:
                                    pausar("Telefone inválido!")
                                elif len(cli_email) == 0 or ('@' not in cli_email):
                                    pausar("E-mail inválido ou não informado!")
                                elif len(cli_end) == 0:
                                    pausar("O endereço não foi informado!")
                                else:
                                    retorno = cli.cadastrar_cliente(cli_nome, cli_doc, cli_tel, cli_email, cli_end)
                                    if retorno == 1:
                                        pausar("Cliente cadastrado com sucesso.")
                                    elif retorno == 2:
                                        pausar("Ocorreu um erro, não foi possível cadastrar o cliente.")

                        elif op_2 == 2:
                            cli_busca = input("\nInforme o código ou cpf/cnpj do cliente que deseja alterar: ").strip()
                            if len(cli_busca) == 0 or not cli_busca.isdigit():
                                pausar("Código ou CPF/CNPJ inválido!")
                            elif not cli.existe_cliente(cli_busca):
                                pausar("Cliente inexistente no cadastro, tente novamente.")
                            else:
                                atributos = ["nome", "cpf/cnpj", "telefone", "e-mail", "endereço"]
                                print("\nDeixar em branco o que NÃO deseja alterar\n")
                                alterar_campos = [input(f"{i.capitalize()}: ").strip().upper() for i in atributos]
                                retorno = cli.alterar_cliente(cli_busca, alterar_campos)
                                if retorno == 1:
                                    pausar("Cliente alterado com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível alterar os dados do cliente.")

                        elif op_2 == 3:
                            cli_busca = input("\nInforme o código ou cpf/cnpj do cliente que deseja remover: ").strip()
                            if len(cli_busca) == 0 or not cli_busca.isdigit():
                                pausar("Código ou CPF/CNPJ inválido!")
                            elif not cli.existe_cliente(cli_busca):
                                pausar("Cliente inexistente no cadastro, tente novamente.")
                            else:
                                retorno = cli.remover_cliente(cli_busca)
                                if retorno == 1:
                                    pausar("Cliente removido com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível remover o cliente.")

                        elif op_2 == 4:
                            limpa_tela() 
                            clientes = cli.listar_clientes()
                            if len(clientes) > 0:
                                campos = f" {'ID':5}{'NOME':25}{'CPF/CNPJ':16}{'TELEFONE':14}{'E-MAIL':25}{'ENDEREÇO'}"
                                cabecalho("Clientes Cadastrados", campos, 120)
                                for c in clientes:
                                    print(f" {c.id:5}{c.nome:25}{c.cpf_cnpj:16}{c.telefone:14}{c.email:25}{c.endereco}")
                                print("-" * 120)
                            else:
                                print("Não há clientes cadastrados.")        
                            input("\nTecle <Enter> para continuar ... ")
                        else:
                            pausar("Opção inválida, tente novamente.")

                    except ValueError:
                        pausar("Opção inválida!")

            if opcao == 3:
                est = EstoqueController()
                while True:
                    menu(opcao, "Adicionar novo produto ao estoque", "Mostrar estoques cadastradas")
                    try:
                        decisao = int(input("Informe a sua opção: "))

                        if decisao == 9:
                            encerrar_sistema()
                            continue

                        if decisao == 8:
                            break

                        if decisao == 1:
                            prod_busca = input("\nInforme o código do produto que deseja adicionar ao estoque: ").strip()
                            if len(prod_busca) == 0:
                                pausar("O código não foi informado!")
                            elif not prod_busca.isdigit():
                                pausar("Código inválido, tente novamente!")
                            elif not ProdutoController.existe_produto(prod_busca):
                                pausar("Produto não cadastrado, utilize a opção 4.")
                            elif est.existe_estoque(prod_busca):
                                pausar("Produto já cadastrado no estoque, utilize a opção de alteração.")
                            else:
                                est_qtd = input("Informe a quantidade: ").strip()
                                if len(est_qtd) == 0:
                                    pausar("Quantidade não informada, tente novamente!")
                                elif not est_qtd.isdecimal():
                                    pausar("Quantidade inválida, tente novamente!")
                                else:
                                    retorno = est.adicionar_estoque(prod_busca, est_qtd)
                                    if retorno == 1:
                                        pausar("Produto adicionado com sucesso ao estoque.")
                                    elif retorno == 2:
                                        pausar("Ocorreu um erro, não foi possível adicionar o produto ao estoque.")
                        
                        elif decisao == 2:
                            prod_busca = input("\nInforme o código ou nome do produto que deseja alterar no estoque: ").strip()
                            if len(prod_busca) == 0:
                                pausar("O código não foi informado!")
                            elif not prod_busca.isdigit():
                                pausar("Código inválido, tente novamente!")
                            elif not est.existe_estoque(prod_busca):
                                pausar("Produto não cadastrado no estoque!")
                            else:
                                est_qtd = input("\nInforme a nova quantide do produto para o estoque: ").strip()
                                if len(est_qtd) > 0:
                                    retorno = est.alterar_estoque(prod_busca, est_qtd)
                                    if retorno == 1:
                                        pausar("Estoque da quantidade do produto alterada com sucesso.")
                                    elif retorno == 2:
                                        pausar("Ocorreu um erro, não foi possível alterar a quantidade do produto no estoque.")
                                else:
                                    pausar("Quantidade não informada, nenhuma alteração realizada!")

                        elif decisao == 3:
                            prod_busca = input("\nInforme o código ou nome do produto que deseja remover do estoque: ").strip()
                            if len(prod_busca) == 0:
                                pausar("O código não foi informado!")
                            elif not prod_busca.isdigit():
                                pausar("Código inválido, tente novamente!")
                            elif not est.existe_estoque(prod_busca):
                                pausar("Produto não cadastrado no estoque!.")
                            else:
                                retorno = est.remover_estoque(prod_busca)
                                if retorno == 1:
                                    pausar("Produto removido com sucesso do estoque.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível remover o produto do estoque.")

                        elif decisao == 4:
                            print("\nInforme os dados do produto que deseja cadastrar")
                            p_nome = input("\nNome: ").strip().upper()
                            if len(p_nome) == 0:
                                pausar("Nome não informado, tente novamente!")
                            elif ProdutoController.existe_produto(p_nome):
                                pausar("Produto já cadastrado, tente novamente!")
                            else:
                                p_preco = input("Preço: ").strip()
                                if not p_preco.isdecimal:
                                    pausar("O preço não foi informado corretamente!")
                                else:
                                    cat_existe = False
                                    tentativas = 0
                                    while not cat_existe:
                                        if tentativas == 0:
                                            p_cat = input("Código da Categoria: ").strip()
                                        else:
                                            p_cat = input("Categoria não cadastrada, informe outra: ").strip()
                                        if len(p_cat) == 0:
                                            pausar("Categoria não informada!")
                                        elif not p_cat.isdigit():
                                            pausar("Categoria deve ser numérica!")
                                        else:
                                            cat_existe = CategoriaController().existe_categoria(p_cat)
                                        tentativas += 1

                                    est_qtd = input("Informe a quantidade: ").strip()
                                    if len(est_qtd) == 0:
                                        pausar("Quantidade não informada, tente novamente!")
                                    elif not est_qtd.isdecimal():
                                        pausar("Quantidade inválida, tente novamente!")
                                    else:
                                        retorno = est.cadastrar_produto_estoque(p_nome, p_preco, p_cat, est_qtd)
                                        if retorno == 1:
                                            pausar("Produto cadastrado e adicionado ao estoque com sucesso.")
                                        elif retorno == 2:
                                            pausar("Ocorreu um erro, não foi possível cadastrar o produto.")

                        elif decisao == 5:
                            limpa_tela()
                            estoques = est.listar_estoque()
                            if len(estoques) > 0:
                                campos = f" {'PRODUTO':30}  {'PROD. ID':8}  {'QUANTIDADE'}"
                                cabecalho("Estoque dos Produtos", campos, 53)
                                for e in estoques:
                                    print(f" {e.produto.nome[:30]:30}  {e.produto.id:8}  {float(e.quantidade):>10.2f}")
                                print("-" * 53)
                            else:
                                print("Não há produtos cadastrados no estoque.")        
                            input("\nTecle <Enter> para continuar ... ")
                        else:
                            pausar("Opção inválida, tente novamente.")

                    except ValueError:
                        pausar("Opção inválida!")

            if opcao == 4:
                fo = FornecedorController()
                while True:
                    menu(opcao, "Mostrar fornecedores cadastrados")
                    try:
                        op_4 = int(input("Informe a sua opção: "))

                        if op_4 == 9:
                            encerrar_sistema()
                            continue

                        if op_4 == 8:
                            break

                        if op_4 == 1:
                            print("\nInforme os dados do fornecedor que deseja cadastrar")
                            fo_doc = input("\nCPF/CNPJ: ").strip()
                            if (len(fo_doc) < 11) or (len(fo_doc) > 14) or (len(fo_doc) == 12) \
                                    or (len(fo_doc) == 13) or (not fo_doc.isdigit()):
                                pausar("CPF/CNPJ inválido!")
                            elif fo.existe_fornecedor(fo_doc):
                                pausar("Fornecedor já cadastrado, tente novamente.")
                            else:
                                fo_ie = input("Inscrição Estadual: ").strip().upper()
                                fo_nome = input("Nome: ").strip().upper()
                                fo_tel = input("Telefone: ").strip().upper()
                                fo_email = input("E-mail: ").strip().lower()
                                fo_end = input("Endereço: ").strip().upper()
                                cat_existe = False
                                while not cat_existe:
                                    fo_cat = input("Código da Categoria: ").strip()
                                    if len(fo_cat) == 0:
                                        pausar("Categoria não informada!")
                                    elif not fo_cat.isdigit():
                                        pausar("Categoria deve ser numérica!")
                                    else:
                                        cat_existe = CategoriaController().existe_categoria(fo_cat)

                                if len(fo_ie) < 9:
                                    pausar("A inscrição deve ter 9 dígitos ou mais!")
                                elif len(fo_nome) == 0:
                                    pausar("O nome não foi informado!")
                                elif len(fo_tel) < 10:
                                    pausar("Telefone inválido!")
                                elif len(fo_email) == 0 or ('@' not in fo_email):
                                    pausar("E-mail inválido ou não informado!")
                                elif len(fo_end) == 0:
                                    pausar("O endereço não foi informado!")
                                else:
                                    retorno = fo.cadastrar_fornecedor(fo_ie, fo_nome, fo_doc, fo_tel, fo_email, fo_end, fo_cat)
                                    if retorno == 1:
                                        pausar("Fornecedor cadastrado com sucesso.")
                                    elif retorno == 2:
                                        pausar("Ocorreu um erro, não foi possível salvar o fornecedor.")

                        elif op_4 == 2:
                            fo_busca = input("\nInforme o código ou cpf/cnpj do fornecedor que deseja alterar: ").strip()
                            if len(fo_busca) == 0 or not fo_busca.isdigit():
                                pausar("Código ou CPF/CNPJ inválido!")
                            elif not fo.existe_fornecedor(fo_busca):
                                pausar("Fornecedor inexistente no cadastro, tente novamente.")
                            else:
                                atributos = {"ie": "", "nome": "", "cpf_cnpj": "", "telefone": "", 
                                            "email": "", "endereco": "", "categoria": ""}
                                print("\nDeixe em branco o que NÃO deseja alterar\n")
                                alterar_campos = {k: input(f"{k.capitalize()}: ").strip().upper() for k in atributos}
                                alterar_campos["email"] = alterar_campos["email"].lower()
                                fo_cat = alterar_campos["categoria"]
                                if len(fo_cat) > 0:  # categoria foi informada
                                    cat_existe = CategoriaController().existe_categoria(fo_cat)
                                    while not cat_existe:
                                        pausar("Categoria inexistente no cadastro, tente novamente!")
                                        fo_cat = input("\nCódigo da Categoria: ").strip()
                                        if len(fo_cat) == 0:
                                            break   # não altera a categoria
                                        elif not fo_cat.isdigit():
                                            pausar("Categoria deve ser numérica!")
                                        else:
                                            cat_existe = CategoriaController().existe_categoria(fo_cat)
                                    alterar_campos["categoria"] = fo_cat

                                retorno = fo.alterar_fornecedor(fo_busca, alterar_campos)
                                if retorno == 1:
                                    pausar("Fornecedor alterado com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível alterar os dados do fornecedor.")

                        elif op_4 == 3:
                            fo_busca = input("\nInforme o código ou cpf/cnpj do fornecedor que deseja remover: ").strip()
                            if len(fo_busca) == 0 or not fo_busca.isdigit():
                                pausar("Código ou CPF/CNPJ inválido!")
                            elif not fo.existe_fornecedor(fo_busca):
                                pausar("Fornecedor inexistente no cadastro, tente novamente.")
                            else:
                                retorno = fo.remover_fornecedor(fo_busca)
                                if retorno == 1:
                                    pausar("Fornecedor removido com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível remover o fornecedor.")

                        elif op_4 == 4:
                            limpa_tela()
                            forns = fo.listar_fornecedores()
                            if len(forns) > 0:
                                campos = f" {'ID':3}  {'INSCRIÇÃO':12}  {'NOME':30}  {'CPF/CNPJ':14}  {'TELEFONE':11}  "
                                campos += f"{'E-MAIL':30}  {'ENDEREÇO':30}  {'CATEGORIA'}"
                                cabecalho("Fornecedores Cadastrados", campos, 160)
                                for x in forns:
                                    print(f" {x.id:3}  {x.ie:12}  {x.nome:30}  {x.cpf_cnpj:14}  {x.telefone:11}  "
                                        + f"{x.email[:30]:30}  {x.endereco[:30]:30}  {x.categoria}")
                                print("-" * 160)
                            else:
                                print("Não há fornecedores cadastrados.")
                            input("\nTecle <Enter> para continuar ... ")
                        else:
                            pausar("Opção inválida, tente novamente.")

                    except ValueError:
                        pausar("Opção inválida!")

            if opcao == 5:
                fun = FuncionarioController()
                while True:
                    menu(opcao, "Mostrar funcionários cadastrados")
                    try:
                        op_5 = int(input("Informe a sua opção: "))

                        if op_5 == 9:
                            encerrar_sistema()
                            continue

                        if op_5 == 8:
                            break

                        if op_5 == 1:
                            print("\nInforme os dados do funcionário que deseja cadastrar")
                            fun_doc = input("\nCPF: ").strip()
                            if (len(fun_doc) != 11) or (not fun_doc.isdigit()):
                                pausar("CPF inválido!")
                            elif fun.existe_funcionario(fun_doc):
                                pausar("Funcionário já existe, tente novamente.")
                            else:
                                fun_mat = input("Matrícula: ").strip()
                                fun_nome = input("Nome: ").strip().upper()
                                fun_tel = input("Telefone: ").strip().upper()
                                fun_email = input("E-mail: ").strip().upper()
                                fun_end = input("Endereço: ").strip().upper()
                                if len(fun_mat) < 3:
                                    pausar("A matrícula deve ter 3 dígitos ou mais!")
                                elif not fun_mat.isdigit():
                                    pausar("Informe somente números para a matrícula!")
                                elif len(fun_nome) == 0:
                                    pausar("O nome não foi informado!")
                                elif len(fun_tel) < 10:
                                    pausar("Telefone inválido!")
                                elif len(fun_email) == 0 or ('@' not in fun_email):
                                    pausar("E-mail inválido ou não informado!")
                                elif len(fun_end) == 0:
                                    pausar("O endereço não foi informado!")
                                else:
                                    retorno = fun.cadastrar_funcionario(fun_mat, fun_nome, fun_doc, fun_tel, fun_email, fun_end)
                                    if retorno == 1:
                                        pausar("Funcionário cadastrado com sucesso.")
                                    elif retorno == 2:
                                        pausar("Ocorreu um erro, não foi possível salvar o funcionário.")

                        elif op_5 == 2:
                            fun_busca = input("\nInforme o Código ou CPF do funcionário que deseja alterar: ").strip()
                            if len(fun_busca) == 0 or not fun_busca.isdigit():
                                pausar("Código ou CPF inválido!")
                            elif not fun.existe_funcionario(fun_busca):
                                pausar("Funcionário inexistente no cadastro, tente novamente.")
                            else:
                                atributos = ["matricula", "nome", "cpf/cnpj", "telefone", "e-mail", "endereço"]
                                print("\nDeixe em branco o que não deseja alterar\n")
                                alterar_campos = [input(f"{i.capitalize()}: ").strip().upper() for i in atributos]
                                retorno = fun.alterar_funcionario(fun_busca, alterar_campos)
                                if retorno == 1:
                                    pausar("Funcionário alterado com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível alterar os dados do funcionário.")

                        elif op_5 == 3:
                            fun_busca = input("\nInforme o Código ou CPF do funcionário que deseja remover: ").strip()
                            if len(fun_busca) == 0 or not fun_busca.isdigit():
                                pausar("Código ou CPF inválido!")
                            elif not fun.existe_funcionario(fun_busca):
                                pausar("Funcionário inexistente no cadastro, tente novamente.")
                            else:
                                retorno = fun.remover_funcionario(fun_busca)
                                if retorno == 1:
                                    pausar("Funcionário removido com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível remover o funcionário.")

                        elif op_5 == 4:
                            limpa_tela()
                            funs = fun.listar_funcionarios()
                            if len(funs) > 0:
                                campos = f" {'ID':5} {'MATRICULA':10} {'NOME':30} {'CPF/CNPJ':15} {'TELEFONE':12} "
                                campos += f"{'E-MAIL':30} {'ENDEREÇO'}"
                                cabecalho("Funcionários Cadastrados", campos, 160)
                                for x in funs:
                                    print(f" {x.id:5} {x.matricula:10} {x.nome[:30]:30} {x.cpf_cnpj:15} "
                                          + f"{x.telefone:12} {x.email[:30]:30} {x.endereco}")
                                print("-" * 160)
                            else:
                                print("Não há funcionários cadastrados.")
                            input("\nTecle <Enter> para continuar ... ")
                        else:
                            pausar("Opção inválida, tente novamente.")

                    except ValueError:
                        pausar("Opção inválida!")

            if opcao == 6:
                pc = ProdutoController()
                while True:
                    menu(opcao, "Mostrar produtos cadastrados")
                    try:
                        decisao = int(input("Informe a sua opção: "))

                        if decisao == 9:
                            encerrar_sistema()
                            continue

                        if decisao == 8:
                            break

                        if decisao == 1:
                            print("\nInforme os dados do produto que deseja cadastrar")
                            p_nome = input("\nNome: ").strip().upper()
                            if len(p_nome) == 0:
                                pausar("Nome não informado, tente novamente!")
                            elif pc.existe_produto(p_nome):
                                pausar("Produto já cadastrado, tente novamente!")
                            else:
                                p_preco = input("Preço: ").strip()
                                if not p_preco.isdecimal:
                                    pausar("O preço não foi informado corretamente!")
                                else:
                                    cat_existe = False
                                    tentativas = 0
                                    while not cat_existe:
                                        if tentativas == 0:
                                            p_cat = input("Código da Categoria: ").strip()
                                        else:
                                            p_cat = input("Categoria não cadastrada, informe outra: ").strip()
                                        if len(p_cat) == 0:
                                            pausar("Categoria não informada!")
                                        elif not p_cat.isdigit():
                                            pausar("Categoria deve ser numérica!")
                                        else:
                                            cat_existe = CategoriaController().existe_categoria(p_cat)
                                        tentativas += 1

                                    retorno = pc.cadastrar_produto(p_nome, p_preco, p_cat)
                                    if retorno == 1:
                                        pausar("Produto cadastrado com sucesso.")
                                    elif retorno == 2:
                                        pausar("Ocorreu um erro, não foi possível cadastrar o produto.")

                        elif decisao == 2:
                            p_busca = input("\nInforme o código ou nome do produto que deseja alterar: ").strip().upper()
                            if len(p_busca) == 0:
                                pausar("O Código ou Nome não foi informado!")
                            elif not pc.existe_produto(p_busca):
                                pausar("Produto inexistente no cadastro, tente novamente.")
                            else:
                                atributos = ["nome", "preço", "categoria"]
                                print("\nDeixe em branco o que NÃO deseja alterar\n")
                                alterar_campos = [input(f"{k.capitalize()}: ").strip().upper() for k in atributos]
                                p_cat = alterar_campos[2]
                                if len(p_cat) > 0:  # categoria foi informada
                                    cat_existe = CategoriaController().existe_categoria(p_cat)
                                    while not cat_existe:
                                        pausar("Categoria inexistente no cadastro, tente novamente!")
                                        p_cat = input("\nCódigo da Categoria: ").strip()
                                        if len(p_cat) == 0:
                                            break   # não altera a categoria
                                        elif not p_cat.isdigit():
                                            pausar("Categoria deve ser numérica!")
                                        else:
                                            cat_existe = CategoriaController().existe_categoria(p_cat)
                                    alterar_campos[2] = p_cat
                                if (len(alterar_campos[1]) > 0) and (not alterar_campos[1].isdecimal):  # preço informado
                                    pausar("O preço foi informado incorretamente!")
                                else:
                                    retorno = pc.alterar_produto(p_busca, alterar_campos)
                                    if retorno == 1:
                                        pausar("Produto alterado com sucesso.")
                                    elif retorno == 2:
                                        pausar("Ocorreu um erro, não foi possível alterar os dados do produto.")

                        elif decisao == 3:
                            p_busca = input("\nInforme o código ou nome do produto que deseja remover: ").strip().upper()
                            if len(p_busca) == 0:
                                pausar("O Código ou Nome não foi informado!")
                            elif not pc.existe_produto(p_busca):
                                pausar("Produto inexistente no cadastro, tente novamente.")
                            elif EstoqueController.existe_estoque(p_busca):
                                pausar("Produto não pode ser removido, pois existe no estoque.")
                            else:
                                retorno = pc.remover_produto(p_busca)
                                if retorno == 1:
                                    pausar("Produto removido com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível remover o produto.")

                        elif decisao == 4:
                            limpa_tela()
                            prods = pc.listar_produtos()
                            if len(prods) > 0:
                                campos = f" {'ID':3}  {'NOME':30}  {'PREÇO':8}  {'CATEGORIA'}"
                                cabecalho("Produtos Cadastrados", campos, 61)
                                for x in prods:
                                    print(f" {x.id:3}  {x.nome[:30]:30}  {float(x.preco):>8.2f}  {x.categoria.nome}")
                                print("-" * 61)
                            else:
                                print("Não há produtos cadastrados.")
                            input("\nTecle <Enter> para continuar ... ")
                        else:
                            pausar("Opção inválida, tente novamente.")

                    except ValueError:
                        pausar("Opção inválida!")

            if opcao == 7:
                vc = VendaController()
                while True:
                    menu(opcao, "Mostrar vendas cadastradas")
                    try:
                        decisao = int(input("Informe a sua opção: "))

                        if decisao == 9:
                            encerrar_sistema()
                            continue

                        if decisao == 8:
                            break

                        if decisao == 1:
                            print("\nInforme os dados da venda que deseja cadastrar")
                            vendedor = input("\nInforme o código ou cpf do vendedor: ").strip().upper()
                            comprador = input("\nInforme o código ou cpf/cnpj do comprador: ").strip().upper()
                            produto = input("\nInforme o código ou nome do produto: ").strip().upper()
                            if len(vendedor) == 0:
                                pausar("Vendedor não informado, tente novamente!")
                            elif len(comprador) == 0:
                                pausar("Comprador não informado, tente novamente!")
                            elif len(produto) == 0:
                                pausar("Produto não informado, tente novamente!")
                            elif not FuncionarioController.existe_funcionario(vendedor):
                                pausar("Vendedor não cadastrado, tente novamente!")
                            elif not ClienteController.existe_cliente(comprador):
                                pausar("Comprador não cadastrado, tente novamente!")
                            elif not ProdutoController.existe_produto(produto):
                                pausar("Produto não cadastrado, tente novamente!")
                            else:
                                qtd = input("\nQuantidade: ").strip()
                                if not qtd.isdecimal or len(qtd) == 0:
                                    pausar("A quantidade não foi informada corretamente!")
                                elif float(qtd) > EstoqueController.get_quantidade(produto):
                                    pausar("A quantidade é superior ao estoque.")
                                else:
                                    retorno = vc.cadastrar_venda(vendedor, comprador, produto, qtd)
                                    if retorno == 1:
                                        pausar("Venda cadastrada com sucesso.")
                                    elif retorno == 2:
                                        pausar("Ocorreu um erro, não foi possível cadastrar o venda.")

                        elif decisao == 2:
                            pausar("A venda não pode ser alterada, somente extornada (excluída)!")

                        elif decisao == 3:
                            p_busca = input("\nInforme o código da venda que deseja remover: ").strip()
                            if len(p_busca) == 0:
                                pausar("O Código não foi informado!")
                            elif not vc.existe_venda(p_busca):
                                pausar("Venda inexistente no cadastro, tente novamente.")
                            else:
                                retorno = vc.remover_venda(p_busca)
                                if retorno == 1:
                                    pausar("Venda removida com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível remover a venda.")

                        elif decisao == 4:
                            limpa_tela()
                            vendas = vc.listar_vendas()
                            if len(vendas) > 0:
                                campos = f" {'ID':3}  {'VENDEDOR':30}  {'COMPRADOR':30}  {'PRODUTO':30}  {'QUANTIDADE':10}  {'DATA'}"
                                cabecalho("Vendas Cadastrados", campos, 124)
                                for x in vendas:
                                    dt = datetime.strptime(x.data[:10], '%Y-%m-%d').strftime('%d/%m/%Y')
                                    print(f" {x.id:3}  {x.vendedor.nome[:30]:30}  {x.comprador.nome[:30]:30}  {x.produto.nome[:30]:30}  "
                                          + f"{float(x.quantidade):>10.2f}  {dt}")
                                print("-" * 124)
                            else:
                                print("Não há vendas cadastrados.")
                            input("\nTecle <Enter> para continuar ... ")
                        else:
                            pausar("Opção inválida, tente novamente.")

                    except ValueError:
                        pausar("Opção inválida!")

        except ValueError:
            pausar("Opção inválida!")
