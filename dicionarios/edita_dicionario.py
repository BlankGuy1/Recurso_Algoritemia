def cria_dicionario():
    Dic_entr = input("Escreva pares chave-valor separados por vírgula e ':' (ex: Filipe:14, Antonio:23): ")

    virgula = [i.strip() for i in Dic_entr.split(', ')]
    dicionario = {}

    for par in virgula:
        chave, valor = par.split(':')
        dicionario[chave] = int(valor)
    print(f"Novo dicionario: {dicionario}")
    return dicionario

def insere_elemento_dic(dicionario):
    Dic_entr = input("Novo pare chave-valor separado por ':' : ")

    chave, valor = Dic_entr.split(':')
    dicionario[chave] = valor
    print(f"Novo dicionario: {dicionario}")
    return dicionario

def remove_elemento_dic(dicionario):
    nome = input("Nome que quer remover: ")
    dicionario.pop(nome)
    print(f"Novo dicionario: {dicionario}")
    return dicionario
