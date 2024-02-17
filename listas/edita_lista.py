
def cria_lista():
    lista_squencia = input("Escreva uma sequencia de numeros separada por espaço: ")
    lista_squencia = lista_squencia.split()
    lista = [int(i) for i in lista_squencia]
    print(f"Lista criada: {lista}")
    return lista

def acrescenta_elemento(lista):
    new = int(input("Novo numero: "))
    lista.append(new)
    print(f"Nova lista: {lista}")
    return lista

def insere_elemento(lista):
    print(lista)
    posicao = int(input("numero da posiçao: "))
    numero = int(input("novo numero: "))
    if posicao <= len(lista):
        lista.insert(posicao, numero)
        print(f"Nova lista: {lista}")
        return lista
    else:
        return print("Erro posicao nao existe na lista")

def remove_de_indice(lista):
    print(lista)
    posicao = int(input("\n qual a posicao que pretende remover?: "))
    if posicao <= len(lista):
        lista.pop(posicao)
        print(f"Nova lista: {lista}")
        return lista
    else:
        return print("Erro posicao nao existe na lista")

def remove_elemento(lista):
    print(lista)
    numero = int(input("\n qual o numero que pretende remover?: "))
    for i in lista:
        if i not in lista:
            return print("Erro numero não esta na lista")
        else:
            lista.remove(numero)
            print(f"Nova lista {lista}")
            return lista

