from No import No

class ListaLigada:
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def adicionar(self, elemento):
        #adiciona elementos ao fim da lista
        if self.primeiro:
            ponteiro = self.primeiro
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(elemento)
        else:
            self.primeiro = No(elemento)
        self.tamanho = self.tamanho +1
    
    def medir(self):
        #retorna o tamanho da lista
        return self.tamanho

    def getno(self, indice):
        ponteiro = self.primeiro
        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError('list index out of range')
        return ponteiro

    def olhar(self, posicao):
        #retorna um elemento a partir de sua posição
        ponteiro = self.primeiro
        i = 1
        while(ponteiro):
            if i == (posicao):
                return ponteiro.dado
            else:
                ponteiro = ponteiro.proximo
                i = i + 1
        return 'Erro: A posição está fora do alcance da lista!'

    def procurar(self, elemento):
        #retorna a posição do elemento indicado
        ponteiro = self.primeiro
        i = 1
        while(ponteiro):
            if ponteiro.dado == elemento:
                return i
            else:
                ponteiro = ponteiro.proximo
                i = i + 1
        return 'Erro: O elemento não está na lista!'

    def inserir(self, posicao, elemento):
        #insere um elemento na posição indicada, movendo os outros (caso preciso)
        no = No(elemento)
        if posicao == 1:
            no.proximo = self.primeiro
            self.primeiro = no
        else:
            ponteiro = self.getno(posicao-2)
            no.proximo = ponteiro.proximo
            ponteiro.proximo = no
        self.tamanho = self.tamanho + 1

    def estaVazia(self):
        return self.primeiro == None

    def remover(self, elemento):
        #remove um elemento
        if self.primeiro == None:
            return print('Erro: O elemento não está na lista, pois ela é vazia!')
        elif self.primeiro.dado == elemento:
            self.primeiro = self.primeiro.proximo
            self.tamanho = self.tamanho - 1
            return True
        else:
            antecessor = self.primeiro
            ponteiro = self.primeiro.proximo
            while(ponteiro):
                if ponteiro.dado == elemento:
                    antecessor.proximo = ponteiro.proximo
                    ponteiro.proximo = None
                antecessor = ponteiro
                ponteiro = ponteiro.proximo
            self.tamanho = self.tamanho - 1
            return True
        return print('Erro: O elemento não está na lista!')
    
    def __repr__(self):
        #representação dos elementos da lista
        r="| "
        ponteiro = self.primeiro
        while(ponteiro):
            r = r + str(ponteiro.dado) + " | "
            ponteiro = ponteiro.proximo
        return r

    def __str__(self):
        return self.__repr__()

lista = ListaLigada()
print(lista.estaVazia())
lista.remover(22)
lista.adicionar(7)
lista.adicionar(80)
lista.adicionar(56)
lista.adicionar(32)
lista.adicionar(17)
lista.inserir(1, 22)
lista.inserir(3, 888)
print(lista.procurar(888))
print(lista.procurar(535322))
print(lista.olhar(5))
print(lista)
lista.remover(888)
print(lista.olhar(2))
print(lista)
print(lista.estaVazia())
print(lista.medir())