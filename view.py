import controller
import os.path


def criaArquivo():
    arquivos = ["categoria.csv", "cliente.csv", "estoque.csv",
                "fornecedor.csv", "funcionario.csv", "produto.csv",
                "venda.csv"]
    for x in arquivos:
        if not os.path.exists(x):
            with open(x, "w") as arq:
                arq.write("")


def menu():
    print("-" * 40)
    print("\tMENU PRINCIPAL")
    print("-" * 40)
    print("""
        [ 1 ] Para Categoria
        [ 2 ] Para Cliente
        [ 3 ] Para Estoque
        [ 4 ] Para Fornecedor
        [ 5 ] Para Funcionário
        [ 6 ] Para Produto
        [ 7 ] Para Venda
        [ 9 ] Para Sair
        """)


if __name__ == "__main__":

    while True:
        menu()
        opcao = int(input("Informe a sua opção: "))

        if opcao == 9:
            break
