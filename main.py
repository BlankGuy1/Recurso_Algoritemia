from listas.edita_lista import cria_lista, acrescenta_elemento, insere_elemento, remove_de_indice, remove_elemento
from listas.operacoes_lista import posicao_maximo,maximo, soma, media, pesquisa
from listas.transforma_lista import ordena
from listas.pesquisa import pesquisa_binaria, pesquisa_binaria_recursiva
from listas.ordena import ordena_selecao, ordena_bolha

from dicionarios.edita_dicionario import cria_dicionario, insere_elemento_dic, remove_elemento_dic
from dicionarios.transforma_dicionario import apresenta_ordenado, soma_valores, media_valores, maximo_valor

from listas_encadeadas import listas_encadeadas as le


while True:
    print("1 - Criar lista "
          "\n 2 - Criar dicionario"
          "\n 3 - Criar lista encadeada"
          "\n 4 - Sair")

    opcao = int(input("Selecione: "))
    if opcao == 1:
        lista = cria_lista()
        print(" 1 - Acrescentar elemento"
                "\n 2 - Insere elemento"
                "\n 3 - remover do indice"
                "\n 4 - remover elemento"
                "\n 5 - ordenar lista"
                "\n 6 - maximo da lista"
                "\n 7 - posição do maior numero da lista"
                "\n 8 - soma da lista"
                "\n 9 - media da lista"
                "\n 10 - pesquisa sequencial"
                "\n 11 - pesquisa binaria"
                "\n 12 - pesquisa binaria recursiva"
                "\n 13 - ordena seleção"
                "\n 14 - ordena bolha"
                "\n 15 - sair")
        while True:
            opcao = int(input("Selecionar: "))
            if opcao == 1:
                acrescenta_elemento(lista)
            if opcao == 2:
                insere_elemento(lista)
            if opcao == 3:
                remove_de_indice(lista)
            if opcao == 4:
                remove_elemento((lista))
            if opcao == 5:
                ordena(lista)
            if opcao == 6:
                maximo(lista)
            if opcao == 7:
                posicao_maximo(lista)
            if opcao == 8:
                soma(lista)
            if opcao == 9:
                media(lista)
            if opcao == 10:
                item = int(input("item: "))
                pesquisa(lista, item)
            if opcao == 11:
                item = int(input("item: "))
                pesquisa_binaria(lista, item)
            if opcao == 12:
                item = int(input("item: "))
                pesquisa_binaria_recursiva(lista, item)
            if opcao == 13:
                ordena_selecao(lista)
            if opcao == 14:
                ordena_bolha(lista)
            if opcao == 15:
                break

    if opcao == 2:
        dicionario = cria_dicionario()
        print("1 - Inserir elemento"
              "\n 2 - Remover elemento"
              "\n 3 - Apresentar dicionado ordenado"
              "\n 4 - Soma dos valores"
              "\n 5 - Media dos valores"
              "\n 6 - Maximo dos valores"
              "\n 7 - Sair")
        while True:
            opcao = int(input("Selecione: "))
            if opcao == 1:
                insere_elemento_dic(dicionario)
            if opcao == 2:
                remove_elemento_dic(dicionario)
            if opcao == 3:
                apresenta_ordenado(dicionario)
            if opcao == 4:
                soma_valores(dicionario)
            if opcao == 5:
                media_valores(dicionario)
            if opcao == 6:
                maximo_valor(dicionario)
            if opcao == 7:
                break

    if opcao == 3:
        lista1 = le.ListaEncadeada()
        print("1 - Inserir no inicio"
              "\n 2 - Inserir no fim"
              "\n 3 - Remover ultimo"
              "\n 4 - Contar nós"
              "\n 5 - Buscar item"
              "\n 6 - Obter N-ésimo nó"
              "\n 7 - Inserir em posição"
              "\n 8 - Apagar lista"
              "\n 9- Concatenar duas listas"
              "\n 10 - Sair")
        while True:
            opcao = int(input("Selecione: "))
            if opcao == 1:
                numero = int(input("Item a inserir: "))
                lista1.inserir_inicio(numero)
                lista1.imprimir()
            if opcao == 2:
                numero = int(input("Item a inserir: "))
                lista1.inserir_fim(numero)
                lista1.imprimir()
            if opcao == 3:
                lista1.remover_ultimo()
                lista1.imprimir()
            if opcao == 4:
                lista1.contar_nos()
            if opcao == 5:
                numero = int(input("Item que pretende encontrar: "))
                lista1.buscar(numero)
            if opcao == 6:
                numero = int(input("Introduza o indice: "))
                lista1.obter_n(numero)
            if opcao == 7:
                pos = int(input("Introduza a posição: "))
                numero = int(input("Introduza o item: "))
                lista1.insere_em_posicao(numero, pos)
            if opcao == 8:
                lista1.apagar_lista()
                lista1.imprimir()
            if opcao == 9:
                lista2 = le.ListaEncadeada()
                lista2.inserir_inicio(2)
                lista2.inserir_inicio(4)
                print("Lista 2")
                lista2.imprimir()
                print("Lista 1")
                lista1.imprimir()

                lista1.concatenar(lista2)
                print("Lista concatenada")
                lista1.imprimir()
            if opcao == 10:
                break
    if opcao == 4:
        break
    else:
        print("Erro o numero que digitou não e valido")