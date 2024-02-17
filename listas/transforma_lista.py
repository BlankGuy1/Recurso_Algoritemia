def ordena(lista):
    print("1 - Ordenar de forma crescente \n 2 - Ordenar de forma decrescente")
    opcao = int(input("Escolha a opeção: "))
    if opcao == 1:
        lista.sort()
        print(f"Nova lista {lista}")
        return lista
    if opcao == 2:
        lista = sorted(lista, reverse=True)
        print(f"Nova lista {lista}")
        return lista
    else:
        return print("Erro opeção não encontrada")
