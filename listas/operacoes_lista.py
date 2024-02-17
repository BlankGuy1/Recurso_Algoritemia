def maximo(lista):
    max = 0
    for i in lista:
        if i >= max:
            max = i
    print(f"O maior valor da lista: {max}")
    return

def posicao_maximo(lista):
    max = 0
    pos = 0
    for i in range(len(lista)):
        if lista[i] >= max:
            max = lista[i]
            pos = i
    print(f"A posição do maior valor e {pos}")
    return

def soma(lista):
    print(f"A soma da lista e {sum(lista)}")
    return
def media(lista):
    print(f"A media e {sum(lista)/len(lista)}")

def pesquisa(lista, item):
    encontrado = False
    for elemento in lista:
        if elemento == item:
            encontrado = True
            break
    return  encontrado