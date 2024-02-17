def apresenta_ordenado(dicionario):
    Or_Chaves = sorted(dicionario.keys())

    for chave in Or_Chaves:
        valor = dicionario[chave]
        print(f'{chave}: {valor}')
    return

def soma_valores(dicionario):
    soma = sum(dicionario.values())
    print(f"Soma do dicionario: {soma}")
    return

def media_valores(dicionario):
    media = sum(dicionario.values())/len(dicionario.values())
    print(f"Media do dicionario: {media}")
    return

def maximo_valor(dicionario):
    max = 0
    for i in dicionario.values():
        if i >= max:
            max = i
    print(f"Maior valor do dicionario: {max}")

