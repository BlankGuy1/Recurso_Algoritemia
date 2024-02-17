class No:
    def __init__(self, item=None):
        self.item = item
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir_inicio(self, item):
        novo_no = No(item)
        novo_no.prox = self.primeiro
        self.primeiro = novo_no
        if self.ultimo is None:
            self.ultimo = novo_no

    def inserir_fim(self, item):
        novo_no = No(item)
        novo_no.prox = None
        if self.ultimo is not None:
            self.ultimo.prox = novo_no
        self.ultimo = novo_no
        if self.primeiro is None:
            self.primeiro = novo_no

    def remover_ultimo(self):
        n = self.primeiro
        if n is None:
            return
        elif n is not None:
            while n.prox != self.ultimo:
                n = n.prox
            del(n.prox)
            n.prox = None
            self.ultimo = n
            return

    def imprimir(self):
        n = self.primeiro
        while n is not None:
            print(n.item)
            n = n.prox

    def contar_nos(self):
        Count = 0
        n = self.primeiro
        while n is not None:
            Count = Count + 1
            n = n.prox
        return

    def buscar(self, item):
        n = self.primeiro
        while n is not None:
            if n.item == item:
                return True
            n = n.prox
        return False

    def obter_n(self, indice):
        if indice < 0:
            return None
        n = self.primeiro
        Count = 0
        while n is not None:
            if n == indice:
                return n
            Count = Count + 1
            n = n.prox
        return None

    def insere_em_posicao(self, item, posicao):
        if posicao < 0:
            print(f"Erro {posicao} e menor que 0")
            return
        novo_no = No(item)
        if posicao == 0:
            novo_no.prox = self.primeiro
            self.primeiro = novo_no
            if self.ultimo is None:
                self.ultimo = novo_no
            return
        antes = self.obter_n(posicao - 1)
        if antes is None:
            print(f"Erro {posicao} esta fora dos limites")
            return
        novo_no.prox = antes.prox
        antes.prox = novo_no
        if antes == self.ultimo:
            self.ultimo = novo_no

    def concatenar(self, outra_lista):
        if outra_lista.primeiro is not None:
            if self.ultimo is not None:
                self.ultimo.prox = outra_lista.primeiro
                self.ultimo = outra_lista.ultimo
            else:
                self.primeiro = outra_lista.primeiro
                self.ultimo = outra_lista.ultimo
    def apagar_lista(self):
        n = self.primeiro
        while n is not None:
            proximo = n.prox
            del n
            atual = proximo
        self.primeiro = None
        self.ultimo = None

        class No:
            def __init__(self, item=None):
                self.item = item
                self.prox = None

        class ListaEncadeada:
            def __init__(self):
                self.primeiro = None
                self.ultimo = None

            def inserir_inicio(self, item):
                novo_no = No(item)
                novo_no.prox = self.primeiro
                self.primeiro = novo_no
                if self.ultimo is None:
                    self.ultimo = novo_no

            def inserir_fim(self, item):
                novo_no = No(item)
                novo_no.prox = None
                if self.ultimo is not None:
                    self.ultimo.prox = novo_no
                self.ultimo = novo_no
                if self.primeiro is None:
                    self.primeiro = novo_no

            def remover_ultimo(self):
                n = self.primeiro
                if n is None:
                    return
                while n.prox != self.ultimo:
                    n = n.prox
                del(n.prox)
                n.prox = None
                self.ultimo = n
                return

            def contar_nos(self):
                contador = 0
                atual = self.primeiro
                while atual is not None:
                    contador += 1
                    atual = atual.prox
                return contador

            def buscar(self, item):
                atual = self.primeiro
                while atual is not None:
                    if atual.item == item:
                        return True
                    atual = atual.prox
                return False

            def contar_ocorrencias(self, item):
                contador = 0
                atual = self.primeiro
                while atual is not None:
                    if atual.item == item:
                        contador += 1
                    atual = atual.prox
                return contador

            def obter_no(self, indice):
                if indice < 0:
                    return None

                atual = self.primeiro
                contador = 0

                while atual is not None:
                    if contador == indice:
                        return atual
                    contador += 1
                    atual = atual.prox

                return None

            def insere_em_posicao(self, item, posicao):
                if posicao < 0:
                    print("Posição inválida. Insira uma posição não negativa.")
                    return

                novo_no = No(item)

                if posicao == 0:
                    novo_no.prox = self.primeiro
                    self.primeiro = novo_no
                    if self.ultimo is None:
                        self.ultimo = novo_no
                    return

                anterior = self.obter_no(posicao - 1)

                if anterior is None:
                    print(f"Posição {posicao} está fora dos limites. O elemento não foi inserido.")
                    return

                novo_no.prox = anterior.prox
                anterior.prox = novo_no

                if anterior == self.ultimo:
                    self.ultimo = novo_no

            def apagar_lista(self):
                atual = self.primeiro
                while atual is not None:
                    proximo = atual.prox
                    del atual
                    atual = proximo

                self.primeiro = None
                self.ultimo = None


