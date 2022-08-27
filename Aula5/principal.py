import contatos_utils

try:
    with open('contatos.csv') as arquivo_contatos:

        """conteudo = arquivo_contatos.readlines()
        
        for linha in conteudo:
            print(linha, end='')"""

        """for linha in arquivo_contatos:
            print(linha, end='')"""

        #contatos = contatos_utils.csv_para_contatos('contatos.csv', 'utf-8')
        #contatos_utils.contatos_para_pickles(contatos, 'contatos.pickle')

        #contatos = contatos_utils.pickle_para_contatos('contatos.pickle')
        #contatos_utils.contatos_para_json(contatos, 'contatos.json')

        contatos = contatos_utils.json_para_contatos('contatos.json')

        for contato in contatos:
            print(f'{contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
finally:
    arquivo_contatos.close()
    print('arquivo fechado..')