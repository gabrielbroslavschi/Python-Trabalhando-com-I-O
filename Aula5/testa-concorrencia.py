
contato_carol = '11,Carol,Carol@carol.com.br\n'
contato_andrezza = '12,Andrezza,Andreza@andrezza.com.br\n'

with open('contatos-escrita.csv', encoding='latin_1', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open('contatos-escrita.csv', encoding='latin_1', mode='a') as arquivo2:
    arquivo2.write(contato_andrezza)
