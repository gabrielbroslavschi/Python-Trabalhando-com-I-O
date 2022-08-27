import csv, pickle, json
from Contato import Contato


def csv_para_contatos(caminho, encodign):
    contatos = []
    with open(caminho, encoding=encodign) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            id, nome, email = linha

            contato = Contato(id, nome, email)
            contatos.append(contato)
    return contatos


def contatos_para_pickles(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)


def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivos:
        contatos = pickle.load(arquivos)
        return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)

def _contato_para_json(contato):
    return contato.__dict__

def json_para_contatos(caminho):
    contatos = []

    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:


            #Das 2 formas, é possível realizar
            #c = Contato(id=contato['id'], nome=contato['nome'], email=contato['email'])
            c = Contato(**contato)


            contatos.append(c)

    return contatos