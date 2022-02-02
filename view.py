from curses.ascii import isdigit
from os import path, system
from time import sleep
from controller import *


lst_classes = ["categoria", "cliente", "estoque", "fornecedor", 
               "funcionario", "produto", "venda"]


def limpa_tela():
    system("clear") or None


def criaArquivo():

    for x in lst_classes:
        if not path.exists(x + ".csv"):
            with open(x + ".csv", "w") as arq:
                arq.write("")


def menu(opcao, *args):

    limpa_tela()
    mnu = "MENU PRINCIPAL" if opcao == 0 else lst_classes[opcao - 1]

    print("-" * 40)
    print(f"{mnu.upper().center(40, ' ')}")
    print("-" * 40)
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
        print("[ 9 ] Para Retornar")

    print()


def pausar(texto):
    print("\n" + texto)
    sleep(1.5)


if __name__ == "__main__":

    while True:
        # m = int(input("Qual menu? [0-9] "))
        # if m == 7:
        #     menu(m, "Relatório Geral", "Vendas por data")
        # else:
        #     menu(m)
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
                    menu(1, "Mostrar categorias cadastradas")
                    try:
                        op_1 = int(input("Informe a sua opção: "))

                        if op_1 == 9:
                            break

                        if op_1 == 1:
                            cat_nome = input("\nInforme o nome da categoria que deseja cadastrar: ").strip().upper()
                            if len(cat_nome) > 0:
                                retorno = cat.cadastrar_categoria(cat_nome)
                                if retorno == 0:
                                    pausar("Categoria já existe, tente novamente.")
                                elif retorno == 1:
                                    pausar("Categoria cadastrada com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível salvar a categoria.")
                                else:
                                    pass
                            else:
                                pausar("O nome não foi informado!")
                            
                        elif op_1 == 2:
                            cat_nome = input("\nInforme o nome da categoria que deseja alterar: ").strip().upper()
                            cat_novonome = input("\nInforme o novo nome da categoria: ").strip().upper()
                            if len(cat_nome) > 0 and len(cat_novonome) > 0:
                                retorno = cat.alterar_categoria(cat_nome, cat_novonome)
                                if retorno == 0:
                                    pausar("Categoria não existe no cadastro, tente novamente.")
                                elif retorno == 1:
                                    pausar("Categoria alterada com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível alterar a categoria.")
                                else:
                                    pass
                            else:
                                pausar("O 'nome' ou o 'novo nome' não foi informado!")

                        elif op_1 == 3:
                            cat_nome = input("\nInforme o nome da categoria que deseja remover: ").strip().upper()
                            if len(cat_nome) > 0:
                                retorno = cat.remover_categoria(cat_nome)
                                if retorno == 0:
                                    pausar("Categoria não existe no cadastro, tente novamente.")
                                elif retorno == 1:
                                    pausar("Categoria removida com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível remover a categoria.")
                                else:
                                    pass
                            else:
                                pausar("O nome não foi informado!")

                        elif op_1 == 4:
                            limpa_tela()
                            cat.listar_categorias()
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
                            break

                        if op_2 == 1:
                            print("\nInforme os dados do cliente que deseja cadastrar")
                            cli_nome = input("\nNome: ").strip().upper()
                            cli_doc = input("CPF/CNPJ: ").strip().upper()
                            cli_tel = input("Telefone: ").strip().upper()
                            cli_email = input("E-mail: ").strip().upper()
                            cli_end = input("Endereço: ").strip().upper()
                            if len(cli_nome) == 0:
                                pausar("O nome não foi informado!")
                            elif (len(cli_doc) < 11) or (len(cli_doc) > 14) or (len(cli_doc) == 12) or (len(cli_doc) == 13):
                                pausar("CPF/CNPJ inválido!")
                            elif len(cli_tel) < 10:
                                pausar("Telefone inválido!")
                            elif len(cli_email) == 0 or ('@' not in cli_email):
                                pausar("E-mail inválido ou não informado!")
                            elif len(cli_end) == 0:
                                pausar("O endereço não foi informado!")
                            else:
                                retorno = cli.cadastrar_cliente(cli_nome, cli_doc, cli_tel, cli_email, cli_end)
                                if retorno == 0:
                                    pausar("Cliente já existe, tente novamente.")
                                elif retorno == 1:
                                    pausar("Cliente cadastrado com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível salvar o cliente.")

                            
                        elif op_2 == 2:
                            # nome, cpf_cnpj, telefone, email, endereco
                            cli_nome = input("\nInforme o nome do cliente que deseja alterar: ").strip().upper()
                            if len(cli_nome) > 0 :
                                atributos = ["nome", "cpf/cnpj", "telefone", "e-mail", "endereço"]
                                print("\nDeixe em branco o que não deseja alterar\n")
                                alterar = [input(f"Novo {i}: ").strip().upper() for i in atributos]
                                retorno = cli.alterar_cliente(cli_nome, alterar)
                                if retorno == 0:
                                    pausar("Cliente não existe no cadastro, tente novamente.")
                                elif retorno == 1:
                                    pausar("Cliente alterado com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível alterar os dados do cliente.")
                            else:
                                pausar("O nome não foi informado!")

                        elif op_2 == 3:
                            cli_nome = input("\nInforme o nome do cliente que deseja remover: ").strip().upper()
                            if len(cli_nome) > 0:
                                retorno = cli.remover_cliente(cli_nome)
                                if retorno == 0:
                                    pausar("Cliente não existe no cadastro, tente novamente.")
                                elif retorno == 1:
                                    pausar("Cliente removido com sucesso.")
                                elif retorno == 2:
                                    pausar("Ocorreu um erro, não foi possível remover o cliente.")
                                else:
                                    pass
                            else:
                                pausar("O nome não foi informado!")

                        elif op_2 == 4:
                            limpa_tela()
                            cli.listar_clientes()
                            input("\nTecle <Enter> para continuar ... ")
                        else:
                            pausar("Opção inválida, tente novamente.")
                    except ValueError:
                        pausar("Opção inválida!")


        except ValueError:
            pausar("Opção inválida!")


