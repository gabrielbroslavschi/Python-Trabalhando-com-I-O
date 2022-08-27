arquivo_contatos = open('contatos-escrita.csv', encoding='latin_1', mode='w+')


contatos = ['11,Carol,Carol@carol.com.br\n',
           '12,Gabiel,Gabiel@cGabiel.com.br\n',
           '13,Joao,Joao@Joao.com.br\n',
           '14,Antonio,Antonio@Antonio.com.br\n',
           '15,Maria,Maria@Maria.com.br\n']

for contato in contatos:
    arquivo_contatos.write((contato))

#Esse metodo escre no arquivo e fecha o programa
#arquivo_contatos.close()

#Esse metodo escreve no arquivo com o programa rodando
arquivo_contatos.flush()

arquivo_contatos.seek(29)
arquivo_contatos.write('12,Gabiel,Gabiel@cGabiel.com.br'.upper())
arquivo_contatos.flush()
arquivo_contatos.seek(0)

#Se utilizarmos isso com a leitura do arquivo no modo "w", não iremos conseguir, pois é somente para escrita
#Para que escreva e leia, precisamos colocar "w+", mas ele começa a ler dps da inserção (começa a ler depois do 15)
#Para que ele leia tudo, tem que usar o metodo utilizado acima (.seek(0))
for linha in arquivo_contatos:
    print(linha, end='')
