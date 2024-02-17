def ordena_selecao(lista):
    for i in range(0,len(lista)):
        j_min = i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[j_min]:
                j_min = j
        if j_min != i:
            lista[i], lista[j_min] = lista[j_min], lista[i]

    return lista

def ordena_bolha(lista):
    n = len(lista)

    for i in range(n):
        for j in range(i, n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista