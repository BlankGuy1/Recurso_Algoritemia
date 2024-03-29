def pesquisa_binaria(lista, item):
    primeiro = 0
    ultimo = len(lista) -1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == item:
            return True
        else:
            if item < lista[meio]:
                ultimo = meio-1
            else:
                primeiro = meio+1
        return False

def pesquisa_binaria_recursiva(lista, item):
    if len(lista) == 0:
        return False
    else:
        meio = len(lista)//2
        if lista[meio]==item:
            return True
        else:
            if item<lista[meio]:
                return pesquisa_binaria(lista[:meio], item)
            else:
                return pesquisa_binaria(lista[meio+1:], item)