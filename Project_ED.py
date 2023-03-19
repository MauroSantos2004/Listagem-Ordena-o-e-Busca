class Node:
    def __init__(self, dados):
        self.anterior = None
        self.dados = dados
        self.proximo = None

class lista_duplamente_encadeada:
    def __init__(self):
        self.cabeca_da_lista = None

    def adicionar(self, dados):
        novo_nó = Node(dados)
        if self.cabeca_da_lista is None:
            self.cabeca_da_lista = novo_nó
            return
        atual = self.cabeca_da_lista
        while atual.proximo:
            atual = atual.proximo
            atual.proximo = novo_nó
            novo_nó.anterior = atual


    def ordenador(self, dados):
        novo_nó = Node(dados)
        if self.cabeca_da_lista is None:
            self.cabeca_da_lista = novo_nó
            return
        if dados < self.cabeca_da_lista.dados:
            novo_nó.proximo = self.cabeca_da_lista
            self.cabeca_da_lista.anterior = novo_nó
            self.cabeca_da_lista = novo_nó
            return
        atual = self.cabeca_da_lista
        while atual.proximo and atual.proximo.dados < dados:
            atual = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = novo_nó
        novo_nó.proximo = atual.proximo
        atual.proximo = novo_nó
        novo_nó.anterior = atual


    def remover(self, dados):
        atual = self.cabeca_da_lista
        while atual:
            if atual.dados == dados:
                if atual.anterior is None:
                    self.cabeca_da_lista = atual.proximo
                    if atual.proximo:
                        atual.proximo.anterior = None
                elif atual.proximo is None:
                    atual.anterior.proximo = None
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior
                return
            atual = atual.proximo


    def enumeração(self):
        atual = self.cabeca_da_lista
        i = 1
        while atual:
            print(f"{i}°. {atual.dados}")
            atual = atual.proximo
            i += 1


    def add_pessoa(self, names):
        for name in names:
            self.ordenador(name)

    def mostrar_lista(self):
        atual = self.cabeca_da_lista
        while atual:
            print(atual.dados)
            atual = atual.proximo

    def busca_linear(self, item):
        atual = self.cabeca_da_lista
        i = 0
        while atual:
            if atual.dados == item:
                return i
            atual = atual.proximo
            i += 1
        return -1
        


lista = lista_duplamente_encadeada()
print("Lista atual:")
lista.enumeração()

print("\nAdicionando uma nova pessoa...")
lista.add_pessoa(["Sophia", "Ethan", "Aria", "Noah", "Isabella", "Liam", "Ava", "Mason", "Mia", "Jackson", "Amelia", "Logan", "Harper", "Lucas", "Charlotte", "Oliver", "Emily", "Elijah", "Abigail", "Alexander", "Madison", "Benjamin", "Elizabeth", "Caleb", "Sofia", "Gabriel", "Scarlett", "Daniel", "Chloe", "William", "Victoria", "Samuel", "Grace", "Matthew", "Riley", "Owen", "Zoey", "Henry", "Natalie", "Julian", "Ellie", "Sebastian", "Lily", "David", "Lila", "Levi", "Stella", "Aaron", "Maya", "Anthony"])
lista.enumeração()
lista.remover('Aaron')
lista.enumeração()

pessoa_preocurada = ('William')
indice = lista.busca_linear(pessoa_preocurada)
if indice != -1:
    print(f"{pessoa_preocurada} está na lista! Sua posição é {indice+1}!")
else:
    print(f"{pessoa_preocurada} não se encontra na lista")