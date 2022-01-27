def proximo_id(tabela):

		with open(tabela, "r") as arq:
			lista = arq.readlines()
			
		return 1 if len(lista) == 0 else int(lista[-1].split('|')[0]) + 1
