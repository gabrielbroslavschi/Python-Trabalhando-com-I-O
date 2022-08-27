try:
    with open('contatos.csv') as arquivo_contatos:

        """conteudo = arquivo_contatos.readlines()
        
        for linha in conteudo:
            print(linha, end='')"""

        for linha in arquivo_contatos:
            print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
finally:
    arquivo_contatos.close()
    print('arquivo fechado..')