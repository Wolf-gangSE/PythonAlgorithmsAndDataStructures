class Fila:
    def __init__(self):
        self.itens = []

    def inserir(self, item):
        self.itens.append(item)
    
    def remover(self):
        self.itens.pop(0)
    
    def estaVazia(self):
        return self.itens == []

    def medir(self):
        return len(self.itens)

    def olhar(self, posicao):
        if posicao <= len(self.itens):
            return self.itens[posicao-1]
        else:
            return 'Erro: A posição definida está fora do alcance da pilha.'
    def cabeca(self):
        return self.itens[0]
