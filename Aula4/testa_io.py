arquivo = open('contatos-escrita.csv', mode='a+')

print(type(arquivo.buffer))


texto_em_bytes = bytes('esse é um texto em bytes', 'utf-8')

#print(texto_em_bytes)
#print(type(texto_em_bytes))

contato = bytes('15,verônica,veronica@veronica.com.br\n','utf-8')
arquivo.buffer.write(contato)

arquivo.close()