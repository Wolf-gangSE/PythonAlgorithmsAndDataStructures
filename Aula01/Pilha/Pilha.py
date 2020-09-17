class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        self.itens.pop()

    def estaVazia(self):
        return self.itens == []

    def medir(self):
        return len(self.itens)

    def olhar(self, posicao):
        if posicao <= len(self.itens):
            return self.itens[posicao-1]
        else:
            return 'Erro: A posição definida está fora do alcance da pilha.'
    def topo(self):
        return self.itens[len(self.itens)-1]
